# Agent Bootcamp

21-day agent learning project built as small, testable Python exercises.

This repository is structured as a learning record:

- `days/`: daily implementations from routing and state handling to LangGraph memory, evaluation, config, and a small capstone.
- `tests/`: automated tests for each day.
- `study_notes/`: reading notes and guided summaries.
- `ARCHITECTURE_GUIDE.md`: high-level architecture notes.
- `FINAL_REVIEW_21_DAYS.md`: final learning review.

## Highlights

- Incremental progression from simple rule-based routing to graph-based agents
- Memory persistence with JSON and SQLite
- Retry, fallback, human-in-the-loop, and evaluation exercises
- End-to-end capstone in `days/day21`

## Run Locally

Create a virtual environment, install the project dependencies you use during the exercises, then run:

```bash
pytest tests -q
```

In the current workspace, the test suite passes:

```text
86 passed
```

## Suggested GitHub Upload Scope

Recommended to keep:

- `days/`
- `tests/`
- `study_notes/`
- `ARCHITECTURE_GUIDE.md`
- `FINAL_REVIEW_21_DAYS.md`
- `week1_review.md`
- `week2_review.md`
- `.env.example`

Recommended not to upload:

- `.venv/`
- `.pytest_cache/`
- `__pycache__/`
- `logs/`
- generated `*.sqlite`
- generated runtime JSON under `data/` or `days/data/`

## Notes

- This repo currently contains generated runtime data under both `data/` and `days/data/`. The code references `days/data/`; the root `data/` directory looks redundant and can be removed if you do not want to keep run artifacts.
- Some source files contain Chinese comments that may display with mojibake in terminals using a different encoding. That does not affect the Python logic, but you may want to normalize encoding before publishing if presentation matters.
