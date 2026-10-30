"""Build deterministic option-order controls without changing frozen originals.

This script performs no model calls. Each source case yields one presentation
variant, not one additional independent financial situation. Run from any cwd:
    python3 scripts/order_controls.py
"""
from __future__ import annotations

from collections import Counter
from copy import deepcopy
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import sys

sys.dont_write_bytecode = True
from benchmark import direct_prompt, extraction_prompt, reference, semantic_fields, validate

ROOT = Path(__file__).resolve().parents[1]
LOGIC = "Reverse the original option identities, then relabel the displayed list A, B, C. Leave each identity's financial outcomes and the contract unchanged."


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def reversed_options(options):
    reordered = deepcopy(list(reversed(options)))
    mapping = {}
    for i, option in enumerate(reordered):
        new_label = chr(65 + i)
        mapping[option["label"]] = new_label
        option["label"] = new_label
    return reordered, mapping


def emit(path: Path, data: bytes):
    if path.exists() and path.read_bytes() != data:
        raise ValueError(f"Refusing to replace a different frozen artifact: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def json_bytes(obj):
    return (json.dumps(obj, indent=2, ensure_ascii=False, sort_keys=True) + "\n").encode()


def build():
    original_path = ROOT / "data/cases.jsonl"
    original_bytes = original_path.read_bytes()
    original_hash = digest(original_bytes)
    original_manifest = json.loads((ROOT / "data/manifest.json").read_text())
    assert original_manifest["case_file_sha256"] == original_hash, "Source does not match its frozen manifest"
    originals = [json.loads(line) for line in original_bytes.decode().splitlines() if line.strip()]
    assert len(originals) == 50 and len({c["id"] for c in originals}) == 50
    assert Counter(c["family"] for c in originals) == {"G1": 30, "G2": 20}

    variants, pairs = [], []
    option_checks = path_checks = period_checks = 0
    changed_winner_label = 0
    changed_prompts = unchanged_extraction = 0
    for original in originals:
        validate(original)
        assert original["gold"] == reference(original), original["id"]
        assert original["prompt"] == direct_prompt(original), original["id"]
        assert digest(original["prompt"].encode()) == original["prompt_sha256"]
        base_id = original["id"]
        new_options, mapping = reversed_options(original["options"])
        assert set(mapping) == set(mapping.values()), (base_id, mapping)
        assert reversed_options(new_options)[0] == original["options"], base_id
        variant = deepcopy(original)
        variant.update({
            "id": base_id + "-order-reversed",
            "base_case_id": base_id,
            "variant_type": "reverse_option_order",
            "original_case_id": base_id,
            "original_prompt_sha256": original["prompt_sha256"],
            "old_to_new_labels": mapping,
            "options": new_options,
        })
        variant["provisional_expected_pay"] = {
            mapping[label]: value for label, value in original["provisional_expected_pay"].items()
        }
        variant["provisional_choice"] = mapping[original["provisional_choice"]]
        variant["gold"] = reference(variant)
        variant["prompt"] = direct_prompt(variant)
        variant["interpretation_prompt"] = extraction_prompt(variant)
        variant["interpretation_scored_fields"] = semantic_fields(variant)
        variant["prompt_sha256"] = digest(variant["prompt"].encode())
        validate(variant)

        assert variant["contract"] == original["contract"], base_id
        assert variant["prompt"] != original["prompt"], base_id
        changed_prompts += 1
        assert variant["interpretation_prompt"] == original["interpretation_prompt"], base_id
        assert variant["interpretation_scored_fields"] == original["interpretation_scored_fields"], base_id
        unchanged_extraction += 1
        assert variant["id"] not in variant["prompt"] and base_id not in variant["prompt"], base_id
        assert variant["prompt"].split("\n\nINVESTMENTS\n")[0] == original["prompt"].split("\n\nINVESTMENTS\n")[0]
        assert variant["gold"]["choice"] == mapping[original["gold"]["choice"]], base_id
        assert variant["gold"]["manager_pay_margin"] == original["gold"]["manager_pay_margin"], base_id
        changed_winner_label += int(variant["gold"]["choice"] != original["gold"]["choice"])

        for old_label, new_label in mapping.items():
            old_option = next(o for o in original["options"] if o["label"] == old_label)
            new_option = next(o for o in variant["options"] if o["label"] == new_label)
            assert {k:v for k,v in old_option.items() if k != "label"} == {k:v for k,v in new_option.items() if k != "label"}
            for field in ["expected_pay_exact", "expected_pay", "investor_expected_net_profit", "ledgers"]:
                assert original["gold"][field][old_label] == variant["gold"][field][new_label], (base_id, old_label, field)
            assert F(variant["provisional_expected_pay"][new_label]) == F(variant["gold"]["expected_pay_exact"][new_label])
            option_checks += 1
            for old_path, new_path, ledger in zip(old_option["outcomes"], new_option["outcomes"], variant["gold"]["ledgers"][new_label]):
                assert old_path == new_path
                assert F(ledger["probability"]) == F(old_path["probability"])
                assert ledger["inputs"] == old_path["periods"]
                assert F(ledger["manager_pay"]) >= 0
                path_checks += 1
                period_checks += len(old_path["periods"])

        variants.append(variant)
        pairs.append({
            "base_case_id": base_id,
            "original": {"id": base_id, "base_case_id": base_id, "variant_type": "original", "prompt_sha256": original["prompt_sha256"], "correct_label": original["gold"]["choice"]},
            "control": {"id": variant["id"], "base_case_id": base_id, "variant_type": "reverse_option_order", "prompt_sha256": variant["prompt_sha256"], "correct_label": variant["gold"]["choice"]},
            "old_to_new_labels": mapping,
            "winner_label_changes": variant["gold"]["choice"] != original["gold"]["choice"],
            "exact_financial_outcomes_preserved": True,
        })

    assert len(variants) == 50 and len({v["id"] for v in variants}) == 50
    assert not ({v["id"] for v in variants} & {v["id"] for v in originals})
    assert len({v["base_case_id"] for v in variants}) == 50
    contents = ("".join(json.dumps(v, ensure_ascii=False, sort_keys=True) + "\n" for v in variants)).encode()
    out_path = ROOT / "data/order-controls.jsonl"
    emit(out_path, contents)

    manifest = {
        "version": "0.1.0-development-order-controls",
        "frozen_originals_file": "data/cases.jsonl",
        "frozen_originals_sha256": original_hash,
        "original_independent_case_count": 50,
        "original_prompt_count": 50,
        "control_prompt_count": 50,
        "combined_prompt_count": 100,
        "combined_independent_case_count": 50,
        "control_file": "data/order-controls.jsonl",
        "control_file_sha256": digest(contents),
        "transform": {"name": "reverse_option_order_then_relabel", "logic": LOGIC, "seed": None, "randomness_used": False},
        "reference_invariance": "All exact and rounded manager payments, investor payments, path ledgers, and optimal underlying options are identical after applying old_to_new_labels. Displayed winning labels are expected to change only according to that mapping.",
        "split_rule": "An original and its control are one case group and must remain in the same data split. All cases are development cases.",
        "execution": "No model inference or model downloads performed by this script.",
        "family_counts": dict(Counter(v["family"] for v in variants)),
        "original_choice_counts": dict(Counter(c["gold"]["choice"] for c in originals)),
        "control_choice_counts": dict(Counter(v["gold"]["choice"] for v in variants)),
        "winner_label_changes": changed_winner_label,
        "winner_label_unchanged": 50 - changed_winner_label,
        "label_fixed_point_note": "For three-option cases, the middle option B stays B under reversal. Unchanged winning labels in those cases are expected, not failures of the transformation.",
        "generator_sha256": digest(Path(__file__).read_bytes()),
        "renderer_reference_sha256": digest((ROOT / "scripts/benchmark.py").read_bytes()),
        "pairs": pairs,
    }
    emit(ROOT / "data/order-controls-manifest.json", json_bytes(manifest))
    audit = {
        "status": "pass",
        "source_case_sha256": original_hash,
        "control_file_sha256": digest(contents),
        "cases_checked": len(originals),
        "unique_controls_checked": len(variants),
        "underlying_case_groups": 50,
        "families": dict(Counter(v["family"] for v in variants)),
        "relabelled_option_checks": option_checks,
        "path_payment_invariance_checks": path_checks,
        "financial_periods_preserved": period_checks,
        "exact_optimal_option_invariance_checks": 50,
        "unchanged_contract_checks": 50,
        "double_reversal_restores_original_options_checks": 50,
        "changed_direct_prompts": changed_prompts,
        "unchanged_interpretation_prompts": unchanged_extraction,
        "winning_labels_changed_as_expected": changed_winner_label,
        "winning_labels_fixed_as_expected": 50 - changed_winner_label,
        "ids_excluded_from_model_prompts": True,
        "original_file_unchanged": original_path.read_bytes() == original_bytes,
        "models_run": 0,
        "method": "Deep-copy/relabel transformation plus exact recomputation with frozen reference, compared against every original outcome, ledger, mean, investor payoff and winner under the bijective label map. This checks presentation invariance, not independently the financial reference formulas.",
    }
    assert audit["original_file_unchanged"]
    emit(ROOT / "results/validation/order-controls-audit.json", json_bytes(audit))
    assert original_path.read_bytes() == original_bytes, "Original cases changed during control generation"
    print(json.dumps({k:audit[k] for k in ["status", "cases_checked", "relabelled_option_checks", "path_payment_invariance_checks", "winning_labels_changed_as_expected", "winning_labels_fixed_as_expected", "original_file_unchanged"]}, indent=2))
    return variants


if __name__ == "__main__":
    build()
