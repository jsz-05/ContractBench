"""Validate released questions and exact references without running a model."""
from collections import Counter
from decimal import localcontext
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "validation"))
from benchmark import direct_prompt, reference, validate
from independent_oracle import score_case
from review_final_prose import review


def main():
    raw = (ROOT / "data/cases.jsonl").read_bytes()
    manifest = json.loads((ROOT / "data/manifest.json").read_text())
    assert hashlib.sha256(raw).hexdigest() == manifest["case_file_sha256"]
    cases = [json.loads(line) for line in raw.decode().splitlines()]
    assert len(cases) == 50 and len({case["id"] for case in cases}) == 50
    assert Counter(case["family"] for case in cases) == {"G1": 30, "G2": 20}
    paths = 0
    with localcontext() as context:
        context.prec = 60
        for case in cases:
            validate(case)
            assert case["gold"] == reference(case), case["id"]
            assert case["prompt"] == direct_prompt(case), case["id"]
            independent = score_case(case)
            assert not independent["gold_disagreements"], case["id"]
            assert independent["independent_choice"] == case["gold"]["choice"]
            for label, value in independent["independent_expected_pay"].items():
                assert abs(F(value) - F(case["gold"]["expected_pay_exact"][label])) < F("1e-40")
            paths += independent["path_count"]
    prose = review()
    assert not prose["defects"] and prose["pass_count"] == 50
    controls = [json.loads(line) for line in (ROOT / "data/order-controls.jsonl").read_text().splitlines()]
    assert len(controls) == 50
    by_id = {case["id"]: case for case in cases}
    for control in controls:
        source = by_id[control["base_case_id"]]
        mapping = control["old_to_new_labels"]
        assert control["gold"] == reference(control)
        assert control["prompt"] == direct_prompt(control)
        assert control["gold"]["choice"] == mapping[source["gold"]["choice"]]
        for old, new in mapping.items():
            assert source["gold"]["ledgers"][old] == control["gold"]["ledgers"][new]
    print(json.dumps({"cases": 50, "path_payments": paths, "order_controls": 50, "status": "pass"}))


if __name__ == "__main__":
    main()
