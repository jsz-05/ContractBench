# ContractBench

WIP. 50 synthetic development cases about investment-manager compensation:
30 fee-base and hurdle cases, plus 20 cap, floor, and loss-limit cases.

- `questions.md`, `answers.md`, `solutions.md`: questions and reference solutions.
- `data/`: structured cases, exact answers, and 50 option-order controls.
- `scripts/`: case formatting, reference calculations, local evaluation, and scoring.
- `validation/`, `tests/`: independent calculation and question checks.

Python 3.10+, standard library only:

```sh
python3 scripts/check_cases.py
python3 -m unittest discover -s tests
python3 scripts/run_local.py --help
python3 scripts/score_responses.py --help
```

Local evaluation requires an existing Ollama server. The runner never downloads
models and uses memory guards and an 8B total-parameter ceiling. Local outputs
go in `results/` and are ignored by Git. These are development cases, not a held-out evaluation set.

Text-only llama.cpp GPU settings are in `configs/llamacpp-gpu.json`.
