"""Sequential Ollama client. Requires an existing server; never downloads models."""
import argparse
import datetime as dt
import hashlib
import json
import platform
import re
import subprocess
import threading
import time
import urllib.parse
import urllib.request
from pathlib import Path

from benchmark import ROOT
from scoring import schema, score


def memory():
    if platform.system() == "Darwin":
        pressure = subprocess.run(
            ["/usr/sbin/sysctl", "-n", "kern.memorystatus_vm_pressure_level"],
            capture_output=True, text=True, check=True, timeout=5,
        )
        free = subprocess.run(
            ["/usr/bin/memory_pressure", "-Q"],
            capture_output=True, text=True, check=True, timeout=5,
        )
        match = re.search(r"memory free percentage:\s*(\d+)%", free.stdout)
        if match is None:
            raise RuntimeError("Cannot verify memory headroom")
        level = int(pressure.stdout.strip())
        return {"normal": level == 1, "pressure_level": level, "free_percent": int(match.group(1))}
    if platform.system() == "Linux":
        fields = {}
        for line in Path("/proc/meminfo").read_text().splitlines():
            key, value = line.split(":", 1)
            fields[key] = int(value.strip().split()[0])
        return {"normal": True, "pressure_level": 1, "free_percent": 100 * fields["MemAvailable"] // fields["MemTotal"]}
    raise RuntimeError("Memory guards currently support macOS and Linux")


def ensure_memory(initial=False):
    current = memory()
    # Yellow pressure alone is not a failure; critical pressure still stops the run.
    if current["pressure_level"] >= 4 or current["free_percent"] < (20 if initial else 10):
        raise RuntimeError("Memory safety stop: " + json.dumps(current))
    return current


def run(args):
    parsed_url = urllib.parse.urlsplit(args.url)
    if parsed_url.scheme != "http" or parsed_url.hostname not in {"127.0.0.1", "localhost", "::1"}:
        raise ValueError("This runner accepts only a local Ollama server")
    if not 1 <= args.num_ctx <= 4096 or not 1 <= args.num_predict <= 2048:
        raise ValueError("Context limit 4096; output limit 2048")
    if args.max_model_gib <= 0:
        raise ValueError("Model package limit must be positive")
    if args.limit is not None and args.limit < 1:
        raise ValueError("Case limit must be positive")
    metadata_path = args.output.with_suffix(".metadata.json")
    if args.output.exists() or metadata_path.exists():
        raise FileExistsError("Choose a new output filename; previous runs are preserved")

    def request(path, payload=None, timeout=15):
        body = None if payload is None else json.dumps(payload).encode()
        req = urllib.request.Request(args.url.rstrip("/") + path, data=body,
                                     headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return json.load(response)

    ensure_memory(initial=True)
    if request("/api/ps").get("models"):
        raise RuntimeError("Another model is loaded; leave it untouched and stop")
    installed = next((m for m in request("/api/tags")["models"] if m["name"] == args.model), None)
    if installed is None:
        raise RuntimeError("Model is not installed; this script never downloads weights")
    if installed["size"] > args.max_model_gib * 1024**3:
        raise RuntimeError("Model package exceeds configured RAM-conservative size limit")
    info = request("/api/show", {"model": args.model})
    total = info.get("model_info", {}).get("general.parameter_count")
    if total is None or total > 8_000_000_000:
        raise RuntimeError("Cannot verify that total model size is at most 8B parameters")
    if args.think and "thinking" not in info.get("capabilities", []):
        raise RuntimeError("This model does not advertise thinking support")
    raw = args.cases.read_bytes()
    cases = [json.loads(line) for line in raw.decode().splitlines() if line.strip()]
    if args.limit:
        cases = cases[:args.limit]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    options = {"temperature": 0, "seed": 97, "num_ctx": args.num_ctx, "num_predict": args.num_predict}
    metadata = {
        "model": args.model, "model_digest": installed["digest"], "total_parameters": total,
        "task": args.task, "think": args.think, "options": options,
        "dataset_sha256": hashlib.sha256(raw).hexdigest(),
        "started_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "runner_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "runtime": request("/api/version"),
    }
    metadata_path.write_text(json.dumps(metadata, indent=2) + "\n")
    finished, unsafe = threading.Event(), threading.Event()

    def watchdog():
        while not finished.wait(1):
            try:
                ensure_memory()
            except Exception:
                unsafe.set()
                # Cancel this model's load/generation; the existing server remains user-owned.
                try:
                    request("/api/generate", {"model": args.model, "keep_alive": 0}, timeout=5)
                except Exception:
                    pass
                return

    thread = threading.Thread(target=watchdog, daemon=True)
    thread.start()
    started_model_request = False
    try:
        with args.output.open("x") as destination:
            for case in cases:
                ensure_memory()
                if unsafe.is_set():
                    raise RuntimeError("Memory watchdog stopped the run")
                prompt = case["prompt"] if args.task == "direct" else case["interpretation_prompt"]
                payload = {
                    "model": args.model, "messages": [{"role": "user", "content": prompt}],
                    "stream": True, "think": args.think, "format": schema(case, args.task),
                    "keep_alive": "30s", "options": options,
                }
                row = {"case_id": case["id"], "family": case["family"], "task": args.task, "request": payload}
                begin = time.monotonic()
                content, thinking, last = [], [], {}
                try:
                    started_model_request = True
                    req = urllib.request.Request(args.url.rstrip("/") + "/api/chat",
                        data=json.dumps(payload).encode(), headers={"Content-Type": "application/json"})
                    with urllib.request.urlopen(req, timeout=60) as response:
                        for line in response:
                            if not line.strip():
                                continue
                            last = json.loads(line)
                            if "error" in last:
                                raise RuntimeError(last["error"])
                            content.append(last.get("message", {}).get("content", ""))
                            thinking.append(last.get("message", {}).get("thinking", ""))
                            if unsafe.is_set() or time.monotonic() - begin > 90:
                                raise RuntimeError("Resource or wall-time stop")
                            if last.get("done"):
                                break
                    row["response"] = {**last, "message": {"content": "".join(content), "thinking": "".join(thinking)}}
                    if last.get("done_reason") != "stop":
                        row["status"] = "incomplete"
                    else:
                        row["answer"] = json.loads("".join(content))
                        row["scores"] = score(case, row["answer"], args.task)
                        row["status"] = "complete"
                except Exception as error:
                    row.update(status="resource_stop" if unsafe.is_set() else "error", error=str(error))
                row["seconds"] = round(time.monotonic() - begin, 3)
                destination.write(json.dumps(row) + "\n")
                destination.flush()
                print(case["id"], row["status"], flush=True)
                if unsafe.is_set():
                    break
    finally:
        finished.set()
        thread.join(timeout=6)
        if started_model_request:
            try:
                request("/api/generate", {"model": args.model, "keep_alive": 0})
            except Exception:
                pass
        metadata["finished_utc"] = dt.datetime.now(dt.timezone.utc).isoformat()
        metadata["stopped_for_memory"] = unsafe.is_set()
        metadata_path.write_text(json.dumps(metadata, indent=2) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", required=True)
    parser.add_argument("--task", choices=["direct", "interpretation"], default="direct")
    parser.add_argument("--cases", type=Path, default=ROOT / "data/cases.jsonl")
    parser.add_argument("--output", type=Path, default=ROOT / "results/local.jsonl")
    parser.add_argument("--url", default="http://127.0.0.1:11434")
    parser.add_argument("--num-ctx", type=int, default=4096)
    parser.add_argument("--num-predict", type=int, default=768)
    parser.add_argument("--max-model-gib", type=float, default=2)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--think", action="store_true")
    run(parser.parse_args())


if __name__ == "__main__":
    main()
