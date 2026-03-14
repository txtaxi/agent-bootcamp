import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from days.day07.main import main
from days.day19.eval_runner import run_case, score_case, summarize_report


def _runner(user_input: str) -> str:
    result = main([user_input, "day19-thread"])
    return result["reply"]


def test_run_case():
    case = {
        "name": "weather_case",
        "input": "weather in beijing",
        "expected": "Weather reply: beijing is sunny",
    }
    result = run_case(case, _runner)
    assert result["name"] == "weather_case"
    assert result["actual"] == "Weather reply: beijing is sunny"
    assert result["latency_ms"] >= 0


def test_score_case():
    scored = score_case(
        {
            "name": "math_case",
            "expected": "Math reply: 7",
            "actual": "Math reply: 7",
            "latency_ms": 1.0,
        }
    )
    assert scored["success"] is True
    assert scored["latency_ms"] == 1.0


def test_summarize_report():
    report = summarize_report(
        [
            {"name": "a", "success": True, "latency_ms": 10.0, "expected": "x", "actual": "x"},
            {"name": "b", "success": False, "latency_ms": 30.0, "expected": "y", "actual": "z"},
        ]
    )
    assert report["total"] == 2
    assert report["success_count"] == 1
    assert report["success_rate"] == 0.5
    assert report["average_latency_ms"] == 20.0


def test_eval_cases_file():
    cases_path = ROOT / "days" / "day19" / "eval_cases.json"
    cases = json.loads(cases_path.read_text(encoding="utf-8"))
    run_results = [run_case(case, _runner) for case in cases]
    scored_results = [score_case(result) for result in run_results]
    report = summarize_report(scored_results)
    assert report["total"] == 3
    assert report["success_count"] == 3
    assert report["success_rate"] == 1.0
