from copy import deepcopy
from decimal import localcontext
from fractions import Fraction as F
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT / "scripts"), str(ROOT / "validation")]
from benchmark import money, path_pay, reference
from independent_oracle import score_case
from scoring import score
from score_responses import evaluate

CASES = [json.loads(line) for line in (ROOT / "data/cases.jsonl").read_text().splitlines()]
BY_ID = {case["id"]: case for case in CASES}


class ContractTests(unittest.TestCase):
    def test_every_exact_answer_matches_independent_oracle(self):
        with localcontext() as context:
            context.prec = 60
            for case in CASES:
                with self.subTest(case=case["id"]):
                    independent = score_case(case)
                    self.assertFalse(independent["gold_disagreements"])
                    self.assertEqual(independent["independent_choice"], case["gold"]["choice"])
                    self.assertEqual(reference(case), case["gold"])

    def test_threshold_boundary_changes_bonus(self):
        contract = deepcopy(BY_ID["G1-19"]["contract"])
        outcome = [{"gross_profit": "50", "cost": "0", "benchmark_profit": "0"}]
        self.assertEqual(path_pay(contract, outcome)[0], 30)
        contract["hurdle_inclusive"] = False
        self.assertEqual(path_pay(contract, outcome)[0], 20)
        contract["bonus_type"] = "hard_hurdle"
        self.assertEqual(path_pay(contract, outcome)[0], 20)

    def test_floor_applies_before_averaging(self):
        case = BY_ID["G2-06"]
        self.assertEqual(case["gold"]["expected_pay"]["B"], "41.00")
        self.assertEqual(case["gold"]["choice"], "B")
        self.assertEqual([r["manager_pay"] for r in case["gold"]["ledgers"]["B"]], ["62", "20"])

    def test_per_period_cap_is_not_whole_plan_cap(self):
        case = deepcopy(BY_ID["G2-16"])
        periods = case["options"][0]["outcomes"][0]["periods"]
        self.assertEqual(path_pay(case["contract"], periods)[0], 36)
        case["contract"]["limit_scope"] = "whole_plan"
        self.assertEqual(path_pay(case["contract"], periods)[0], 28)

    def test_half_cent_rounding(self):
        self.assertEqual(money("25.425"), "25.43")

    def test_correct_choices_and_wrong_payments_are_separate(self):
        case = CASES[0]
        answer = {"choice": case["gold"]["choice"], "expected_pay": {k: 0 for k in case["gold"]["expected_pay"]}}
        result = score(case, answer, "direct")
        self.assertTrue(result["choice_correct"])
        self.assertFalse(result["payments_correct"])

    def test_all_gold_responses_score_correctly(self):
        for case in CASES:
            answer = {"choice": case["gold"]["choice"], "expected_pay": case["gold"]["expected_pay"]}
            direct = score(case, answer, "direct")
            self.assertTrue(direct["choice_correct"] and direct["payments_correct"])
            interpretation = score(case, case["contract"], "interpretation")
            self.assertTrue(interpretation["interpretation_correct"])
            self.assertTrue(interpretation["executor_choice_correct"])

    def test_duplicate_predictions_are_rejected(self):
        answer = {"case_id": CASES[0]["id"], "answer": {"choice": "A", "expected_pay": {"A": 0}}}
        with self.assertRaises(ValueError):
            evaluate(CASES, [answer, answer], "direct")

    def test_incomplete_answers_are_not_correct(self):
        result = evaluate(CASES, [{"case_id": CASES[0]["id"], "status": "incomplete"}], "direct")
        self.assertEqual(result["summary"]["completed"], 0)
        self.assertEqual(result["summary"]["choice_correct"], 0)

    def test_all_order_variants_preserve_outcomes(self):
        variants = [json.loads(line) for line in (ROOT / "data/order-controls.jsonl").read_text().splitlines()]
        for variant in variants:
            source = BY_ID[variant["base_case_id"]]
            for old, new in variant["old_to_new_labels"].items():
                self.assertEqual(source["gold"]["ledgers"][old], variant["gold"]["ledgers"][new])


if __name__ == "__main__":
    unittest.main()
