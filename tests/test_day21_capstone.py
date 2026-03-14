import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from days.day21.capstone_agent import build_capstone_graph, run_batch_eval, run_demo


def test_run_demo_weather():
    result = run_demo("weather in beijing")
    assert result["intent"] == "weather"
    assert result["reply"] == "Weather reply: beijing is sunny"
    assert result["error"] is None


def test_run_demo_math():
    result = run_demo("1 + 2 * 3")
    assert result["intent"] == "math"
    assert result["reply"] == "Math reply: 7"
    assert result["error"] is None


def test_build_capstone_graph():
    graph = build_capstone_graph()
    result = graph.invoke(
        {
            "user_input": "hello",
            "intent": "",
            "result": None,
            "error": None,
            "reply": "",
        }
    )
    assert result["intent"] == "unknown"
    assert result["reply"] == "Error: unknown intent"


def test_run_batch_eval():
    report = run_batch_eval()
    assert report["report"]["total"] == 3
    assert report["report"]["success_rate"] == 1.0
