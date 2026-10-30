"""Parse every final direct/extraction contract and direct option list independently.

This deliberately does not import the benchmark renderer or exact solver. A
Decimal credit/debit oracle then checks answers implied by the displayed prose.
"""
from __future__ import annotations

from collections import Counter
from decimal import Decimal, ROUND_HALF_UP, localcontext
import hashlib
import json
from pathlib import Path
import re

from independent_oracle import D, score_case

ROOT = Path(__file__).resolve().parents[1]
NUM = r"(-?\d+(?:\.\d+)?)"


def match(pattern, text):
    result = re.search(pattern, text)
    if result is None:
        raise AssertionError("Missing/ambiguous prose pattern: " + pattern)
    return result


def contract_from_prose(text):
    base = match(r"fixed payment of USD " + NUM + " once for the complete plan", text).group(1)
    if "profit measure used for the bonus is investment profit before the listed costs" in text:
        basis = "gross"
    elif "profit measure used for the bonus is investment profit after subtracting the listed costs" in text:
        basis = "net"
    else:
        raise AssertionError("Bonus profit/cost basis missing")
    rate = D(match(r"bonus is " + NUM + r"% of", text).group(1)) / 100
    hurdle, inclusive = "0", False
    if "positive difference between that profit measure and the stated reference-portfolio dollar profit" in text:
        kind = "benchmark"
        assert "Each mandate has its own stated reference portfolio on the same notional dollar basis" in text
        assert "There is no additional positive-fund-profit condition" in text
        assert "A bonus is allowed when both amounts are negative" in text
    elif "of the amount by which that profit measure exceeds" in text:
        kind = "hard_hurdle"
        hurdle = match(r"profit measure exceeds USD " + NUM, text).group(1)
        assert "no bonus when the measure is at or below" in text
    elif "If that profit measure is" in text:
        kind = "soft_hurdle"
        trigger = match(r"If that profit measure is (at least|strictly greater than) USD " + NUM, text)
        inclusive, hurdle = trigger.group(1) == "at least", trigger.group(2)
        assert "of its entire positive amount, including the portion below" in text
    else:
        kind = "gain"
        assert "positive part of that profit measure" in text
        assert "zero if that measure is zero or negative" in text
    loss = re.search(r"Separately, deduct " + NUM + r"% of the loss when investment profit (before|after) listed costs is negative", text)
    loss_rate = str(D(loss.group(1)) / 100) if loss else "0"
    loss_basis = ("gross" if loss.group(2) == "before" else "net") if loss else "gross"
    if loss:
        assert "explicitly hypothetical deduction from the manager's compensation" in text
    else:
        assert "There is no separate loss deduction" in text
    bc = re.search(r"Cap (each period's bonus|the total bonus for the complete plan) at USD " + NUM, text)
    lc = re.search(r"Cap (each period's loss deduction|the total loss deduction for the complete plan) at USD " + NUM, text)
    bonus_cap, loss_cap = (bc.group(2) if bc else None), (lc.group(2) if lc else None)
    if bc:
        assert "fixed payment is excluded from this bonus cap" in text
    else:
        assert "There is no bonus cap" in text
    scopes = ["per_period" if "each period" in m.group(1) else "whole_plan" for m in (bc, lc) if m]
    assert len(set(scopes)) <= 1, "Mixed cap scopes require a richer schema"
    scope = scopes[0] if scopes else "whole_plan"
    floor = re.search(r"raise the final TOTAL compensation to USD " + NUM, text)
    if floor:
        assert "After adding the fixed payment and bonuses and subtracting any applicable loss deductions" in text
        assert "Apply this floor once at final settlement" in text
    else:
        assert "There is no additional floor on final total compensation" in text
    assert "All compensation is settled separately at the end" in text
    assert "There is no discounting" in text
    return dict(base=base, rate=str(rate), profit_basis=basis, bonus_type=kind,
                hurdle=hurdle, hurdle_inclusive=inclusive, bonus_cap=bonus_cap,
                loss_rate=loss_rate, loss_basis=loss_basis, loss_cap=loss_cap,
                pay_floor=floor.group(1) if floor else None, limit_scope=scope)


def options_from_prose(text, contract):
    options, current = [], None
    for line in text.splitlines():
        op = re.fullmatch(r"Option ([ABC]):", line)
        if op:
            current = {"label": op.group(1), "outcomes": []}
            options.append(current)
        outcome = re.match(r"\s*Outcome (\d+), probability " + NUM + r"%: (.+)\.", line)
        if outcome:
            assert current is not None
            assert int(outcome.group(1)) == len(current["outcomes"]) + 1
            probability = D(outcome.group(2)) / 100
            periods = []
            for part in outcome.group(3).split("; "):
                record = match(r"gross investment profit USD " + NUM + r", costs USD " + NUM, part)
                reference = re.search(r"associated reference-portfolio profit USD " + NUM, part)
                if contract["bonus_type"] == "benchmark":
                    assert reference is not None
                periods.append(dict(gross_profit=record.group(1), cost=record.group(2),
                                    benchmark_profit=reference.group(1) if reference else "0"))
            current["outcomes"].append({"probability": str(probability), "periods": periods})
    assert options
    return options


def same_value(a, b):
    if isinstance(a, bool) or isinstance(b, bool):
        return a is b
    if a is None or b is None:
        return a is b
    try:
        return abs(D(a) - D(b)) < Decimal("1e-40")
    except Exception:
        return a == b


def review():
    path = ROOT / "data/cases.jsonl"
    raw = path.read_bytes()
    cases = [json.loads(line) for line in raw.decode().splitlines() if line]
    md = (ROOT / "questions.md").read_text()
    results, defects = [], []
    with localcontext() as ctx:
        ctx.prec = 60
        for case in cases:
            cid = case["id"]
            try:
                p = case["prompt"]
                assert cid not in p and case["title"] not in p and case["rationale"] not in p
                assert "## " + cid + ": " + case["title"] in md and p in md
                assert hashlib.sha256(p.encode()).hexdigest() == case["prompt_sha256"]
                assert "exact half-cent values rounded upward" in p
                assert "Choose using the unrounded averages" in p
                body = p.split("\n\nCONTRACT\n", 1)[1].split("\n\nINVESTMENTS\n", 1)[0]
                parsed = contract_from_prose(body)
                extracted = contract_from_prose(case["interpretation_prompt"].split("\n\nCONTRACT\n", 1)[1])
                assert parsed == extracted, "Direct/extraction contract mismatch"
                for key, expected in case["contract"].items():
                    assert same_value(parsed[key], expected), ("Rendered contract field mismatch", key, parsed[key], expected)
                parsed_options = options_from_prose(p, parsed)
                assert len(parsed_options) == len(case["options"])
                for a, b in zip(parsed_options, case["options"]):
                    assert a["label"] == b["label"] and len(a["outcomes"]) == len(b["outcomes"])
                    for x, y in zip(a["outcomes"], b["outcomes"]):
                        assert same_value(x["probability"], y["probability"])
                        assert len(x["periods"]) == len(y["periods"])
                        for xp, yp in zip(x["periods"], y["periods"]):
                            assert all(same_value(xp[k], yp[k]) for k in xp), ("Displayed investment mismatch", a["label"])
                if any(len(o["periods"]) > 1 for op in parsed_options for o in op["outcomes"]):
                    assert "Do not multiply these path probabilities by additional round probabilities" in p
                    assert "add those period bonuses without offsetting" in body
                    assert "There is no high-water-mark rule or clawback" in body
                independent = score_case({**case, "contract": parsed, "options": parsed_options})
                assert not independent["gold_disagreements"], independent["gold_disagreements"]
                assert independent["independent_choice"] == case["gold"]["choice"]
                for label, value in independent["independent_expected_pay"].items():
                    assert same_value(value, case["gold"]["expected_pay_exact"][label])
                    rounded = D(value).quantize(Decimal(".01"), rounding=ROUND_HALF_UP)
                    assert same_value(rounded, case["gold"]["expected_pay"][label])
                results.append({"id": cid, "status": "pass", "expected_pay": independent["independent_expected_pay"],
                                "choice": independent["independent_choice"], "rendered_contract_fields_checked": 12,
                                "paths_checked": independent["path_count"]})
            except Exception as exc:
                defects.append({"id": cid, "error": f"{type(exc).__name__}: {exc}"})
    out = {"case_file_sha256": hashlib.sha256(raw).hexdigest(), "case_count": len(cases),
           "pass_count": len(results), "defects": defects,
           "method": "Independent regex reconstruction of every displayed contract and investment, then Decimal credit/debit oracle; no root renderer or solver imported.",
           "scoped_approval": "Ready for development inference if no defects; not a claim of external financial expert validation.",
           "cases": results}
    (ROOT / "results/validation").mkdir(parents=True, exist_ok=True)
    (ROOT / "results/validation/final-prose-audit.json").write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({k: out[k] for k in ("case_file_sha256", "case_count", "pass_count", "defects")}, indent=2))
    return out


if __name__ == "__main__":
    review()
