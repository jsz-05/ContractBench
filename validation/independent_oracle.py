"""Independent Decimal oracle for the G1/G2 development release.

Does not import the benchmark builder, its solver, or model outputs. Arithmetic
is organized as per-period credits/debits followed by contractual settlement.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from decimal import Decimal, localcontext
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
ZERO = Decimal(0)
FIELDS = {"base", "rate", "profit_basis", "bonus_type", "hurdle",
          "hurdle_inclusive", "bonus_cap", "loss_rate", "loss_basis",
          "loss_cap", "pay_floor", "limit_scope"}


def D(value):
    if isinstance(value, bool):
        raise ValueError("Boolean used as money or probability")
    value = str(value)
    if "/" in value:
        n, d = value.split("/")
        return Decimal(n) / Decimal(d)
    result = Decimal(value)
    if not result.is_finite():
        raise ValueError("Nonfinite monetary/probability value")
    return result


def positive(x):
    return x if x > ZERO else ZERO


def ceiling(value, cap):
    return value if cap is None else min(value, D(cap))


def path_ledger(contract, periods):
    credits, debits, history = [], [], []
    for period in periods:
        gross = D(period["gross_profit"])
        cost = D(period["cost"])
        assert cost >= ZERO, "Negative cost"
        net = gross - cost
        basis = gross if contract["profit_basis"] == "gross" else net
        kind = contract["bonus_type"]
        if kind == "gain":
            eligible = positive(basis)
        elif kind == "hard_hurdle":
            eligible = positive(basis - D(contract["hurdle"]))
        elif kind == "soft_hurdle":
            hurdle = D(contract["hurdle"])
            passed = basis >= hurdle if contract["hurdle_inclusive"] else basis > hurdle
            eligible = positive(basis) if passed else ZERO
        elif kind == "benchmark":
            eligible = positive(basis - D(period["benchmark_profit"]))
        else:
            raise ValueError("Unknown bonus type: " + str(kind))
        credit = eligible * D(contract["rate"])
        loss_base = gross if contract["loss_basis"] == "gross" else net
        debit = positive(-loss_base) * D(contract["loss_rate"])
        if contract["limit_scope"] == "per_period":
            credit = ceiling(credit, contract["bonus_cap"])
            debit = ceiling(debit, contract["loss_cap"])
        credits.append(credit)
        debits.append(debit)
        history.append({"basis": str(basis), "eligible_profit": str(eligible),
                        "credited_bonus": str(credit), "loss_deduction": str(debit),
                        "gross_profit": str(gross), "net_profit": str(net)})
    credit, debit = sum(credits, ZERO), sum(debits, ZERO)
    if contract["limit_scope"] == "whole_plan":
        credit = ceiling(credit, contract["bonus_cap"])
        debit = ceiling(debit, contract["loss_cap"])
    pre_floor = D(contract["base"]) + credit - debit
    total = pre_floor
    if contract["pay_floor"] is not None:
        total = max(total, D(contract["pay_floor"]))
    return total, {"periods": history, "total_bonus": str(credit),
                   "total_deduction": str(debit), "pay_before_floor": str(pre_floor),
                   "pay_after_floor": str(total)}


def score_case(case):
    c = case["contract"]
    assert set(c) == FIELDS, ("Contract fields differ", sorted(set(c) ^ FIELDS))
    assert c["profit_basis"] in {"gross", "net"}
    assert c["loss_basis"] in {"gross", "net"}
    assert c["bonus_type"] in {"gain", "hard_hurdle", "soft_hurdle", "benchmark"}
    assert c["limit_scope"] in {"per_period", "whole_plan"}
    assert isinstance(c["hurdle_inclusive"], bool)
    for key in ("base", "rate", "hurdle", "loss_rate"):
        assert D(c[key]) >= ZERO, ("Negative contract value", key)
    assert D(c["rate"]) <= 1 and D(c["loss_rate"]) <= 1, "Rate outside 0--1"
    for key in ("bonus_cap", "loss_cap", "pay_floor"):
        assert c[key] is None or D(c[key]) >= ZERO, ("Negative bound", key)
    if c["bonus_type"] != "soft_hurdle":
        assert c["hurdle_inclusive"] is False
    if case["family"] == "G1":
        assert all(c[k] is None for k in ("bonus_cap", "loss_cap", "pay_floor"))
        assert D(c["loss_rate"]) == 0
    labels = [o["label"] for o in case["options"]]
    assert labels == list("ABC"[:len(labels)]) and len(labels) in (2, 3)
    pay, gross_expected, net_expected, ledgers = {}, {}, {}, {}
    total_paths = 0
    for option in case["options"]:
        assert option["outcomes"], "Empty option"
        assert abs(sum((D(x["probability"]) for x in option["outcomes"]), ZERO) - 1) < Decimal("1e-45"), "Probabilities not normalized"
        value = gross = net = ZERO
        rows = []
        for outcome in option["outcomes"]:
            probability = D(outcome["probability"])
            assert probability > 0 and probability <= 1
            assert outcome["periods"], "Empty history"
            if case["family"] == "G1":
                assert len(outcome["periods"]) == 1
            amount, ledger = path_ledger(c, outcome["periods"])
            assert amount >= ZERO, "Negative realized compensation"
            value += probability * amount
            gross += probability * sum((D(p["gross_profit"]) for p in outcome["periods"]), ZERO)
            net += probability * sum((D(p["gross_profit"]) - D(p["cost"]) for p in outcome["periods"]), ZERO)
            rows.append({"probability": str(probability), "compensation": str(amount), **ledger})
            total_paths += 1
        label = option["label"]
        pay[label], gross_expected[label], net_expected[label] = value, gross, net
        ledgers[label] = rows
    ranked = sorted(pay.values(), reverse=True)
    assert ranked[0] > ranked[1], "Nonunique optimum"
    margin = ranked[0] - ranked[1]
    assert margin >= Decimal("0.10"), "Margin smaller than $0.10"
    choice = max(pay, key=pay.get)
    differences = {}
    for label, expected in case.get("provisional_expected_pay", {}).items():
        difference = abs(D(expected) - pay[label])
        if difference > Decimal("1e-20"):
            differences[label] = {"author": str(expected), "independent": str(pay[label]), "difference": str(difference)}
    if case.get("provisional_choice") not in (None, choice):
        differences["choice"] = {"author": case["provisional_choice"], "independent": choice}
    return {"id": case["id"], "family": case["family"], "subtype": case["subtype"],
            "independent_expected_pay": {k: str(v) for k, v in pay.items()},
            "independent_choice": choice, "margin": str(margin),
            "gold_disagreements": differences, "path_count": total_paths,
            "gross_profit_optima": [k for k,v in gross_expected.items() if v == max(gross_expected.values())],
            "net_profit_optima": [k for k,v in net_expected.items() if v == max(net_expected.values())],
            "ledgers": ledgers}


def run(paths, output):
    cases, file_hashes = [], {}
    for path in paths:
        path = path.resolve()
        raw = path.read_bytes()
        file_hashes[str(path.relative_to(ROOT))] = hashlib.sha256(raw).hexdigest()
        if path.suffix == ".jsonl":
            loaded = [json.loads(line) for line in raw.decode().splitlines() if line.strip()]
        else:
            loaded = json.loads(raw)
        if isinstance(loaded, dict):
            loaded = loaded.get("cases", loaded.get("questions"))
        assert isinstance(loaded, list)
        cases.extend(loaded)
    duplicates, seen, rows, failures = [], {}, [], []
    ids = [x["id"] for x in cases]
    if len(set(ids)) != len(ids):
        failures.append({"id": "dataset", "error": "Duplicate case IDs"})
    with localcontext() as ctx:
        ctx.prec = 60
        for case in cases:
            try:
                rows.append(score_case(case))
            except Exception as exc:
                failures.append({"id": case.get("id"), "error": f"{type(exc).__name__}: {exc}"})
            opportunities = [o["outcomes"] for o in case["options"]]
            signature = json.dumps(sorted(opportunities, key=lambda x: json.dumps(x, sort_keys=True)), sort_keys=True)
            if signature in seen:
                duplicates.append([seen[signature], case["id"]])
            else:
                seen[signature] = case["id"]
    source_counts = Counter(x["family"] for x in cases)
    subtype_counts = Counter((x["family"] + ":" + x["subtype"]) for x in cases)
    report = {"independence": "Decimal per-period credit/debit oracle; imports no benchmark solver",
              "file_sha256": file_hashes, "case_count": len(cases), "family_counts": dict(source_counts),
              "subtype_counts": dict(subtype_counts), "case_ids": ids,
              "successfully_checked": len(rows), "path_payments_checked": sum(r["path_count"] for r in rows),
              "failures": failures, "exact_duplicate_opportunities": duplicates,
              "author_disagreements": {r["id"]: r["gold_disagreements"] for r in rows if r["gold_disagreements"]},
              "winning_label_counts": dict(Counter(r["independent_choice"] for r in rows)),
              "cases_where_manager_optimum_not_gross_profit_optimum": [r["id"] for r in rows if r["independent_choice"] not in r["gross_profit_optima"]],
              "cases_where_manager_optimum_not_net_profit_optimum": [r["id"] for r in rows if r["independent_choice"] not in r["net_profit_optima"]],
              "cases": rows,
              "limits": ["Arithmetic agreement is not financial expert validation.",
                         "Formal source specification review does not by itself validate rendered question wording.",
                         "These are exposed development cases, not a held-out test set."]}
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2) + "\n")
    summary = {k: report[k] for k in ["case_count", "family_counts", "successfully_checked", "path_payments_checked", "failures", "exact_duplicate_opportunities", "author_disagreements", "winning_label_counts"]}
    print(json.dumps(summary, indent=2))
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", type=Path)
    parser.add_argument("--output", type=Path, default=ROOT / "results/validation/independent-audit.json")
    args = parser.parse_args()
    paths = args.paths or [ROOT / "data/authored-group1.json", ROOT / "data/authored-group2.json"]
    run(paths, args.output)
