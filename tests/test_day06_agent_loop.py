import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from days.day06.agent_loop import build_reply, run_turn


def test_run_turn_weather():
    state = run_turn("weather in beijing", thread_id="day06-weather")
    assert state["intent"] == "weather"
    assert state["result"] == "beijing is sunny"
    assert state["error"] is None
    assert state["messages"][0]["role"] == "user"
    assert state["messages"][1]["role"] == "assistant"


def test_run_turn_math():
    state = run_turn("1 + 2 * 3", thread_id="day06-math")
    assert state["intent"] == "math"
    assert state["result"] == "7"
    assert state["error"] is None
    assert "Math reply" in state["messages"][1]["content"]


def test_run_turn_unknown():
    state = run_turn("hello world", thread_id="day06-unknown")
    assert state["intent"] == "unknown"
    assert state["result"] is None
    assert state["error"] == "unknown intent"
    assert state["messages"][1]["content"] == "Error: unknown intent"


def test_build_reply():
    state = {"intent": "weather", "result": "beijing is sunny", "error": None}
    assert build_reply(state) == "Weather reply: beijing is sunny"
