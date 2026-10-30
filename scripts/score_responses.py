"""Grade saved predictions without starting a model or accessing the network."""
import argparse
from collections import Counter
import json
from pathlib import Path

from benchmark import ROOT
from scoring import score


def evaluate(cases, records, task):
    lookup = {case["id"]: case for case in cases}
    rows = []
    seen = set()
    for record in records:
        case_id = record["case_id"]
        if case_id not in lookup or case_id in seen:
            raise ValueError("Unknown or repeated case_id: " + case_id)
        seen.add(case_id)
        row = {"case_id": case_id, "family": lookup[case_id]["family"]}
        if record.get("status") in {"incomplete", "resource_stop", "error"}:
            row.update(status=record["status"], error=record.get("error"))
        else:
            try:
                answer = record.get("answer", record.get("parsed"))
                if answer is None:
                    answer = json.loads(record["response"]["message"]["content"])
                row.update(status="complete", scores=score(lookup[case_id], answer, task))
            except (KeyError, ValueError, TypeError, AssertionError) as error:
                row.update(status="invalid", error=str(error))
        rows.append(row)
    summary = {
        "task": task,
        "available_cases": len(cases),
        "attempted": len(rows),
        "completed": sum(row["status"] == "complete" for row in rows),
        "status_counts": dict(Counter(row["status"] for row in rows)),
    }
    fields = ["choice_correct", "payments_correct"] if task == "direct" else [
        "interpretation_correct", "extracted_rule_ledger_correct", "executor_choice_correct"
    ]
    for field in fields:
        summary[field] = sum(row.get("scores", {}).get(field, False) for row in rows)
    return {"summary": summary, "cases": rows}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("predictions", type=Path)
    parser.add_argument("--task", choices=["direct", "interpretation"], default="direct")
    parser.add_argument("--cases", type=Path, default=ROOT / "data/cases.jsonl")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    cases = [json.loads(line) for line in args.cases.read_text().splitlines() if line.strip()]
    predictions = [json.loads(line) for line in args.predictions.read_text().splitlines() if line.strip()]
    result = evaluate(cases, predictions, args.task)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result["summary"], indent=2))


if __name__ == "__main__":
    main()
