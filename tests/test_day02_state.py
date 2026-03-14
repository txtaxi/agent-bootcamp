import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from days.day02.state import append_message, create_state, set_error, set_intent, set_result


def test_create_state():
    state = create_state("hello", thread_id="t-001")
    assert state["thread_id"] == "t-001"
    assert state["user_input"] == "hello"
    assert state["messages"] == []
    assert state["intent"] is None
    assert state["result"] is None
    assert state["error"] is None


def test_update_state():
    state = create_state("weather in beijing")
    append_message(state, "user", "weather in beijing")
    set_intent(state, "weather")
    set_result(state, "today is sunny")
    set_error(state, "temporary warning")
    assert state["messages"] == [{"role": "user", "content": "weather in beijing"}]
    assert state["intent"] == "weather"
    assert state["result"] == "today is sunny"
    assert state["error"] == "temporary warning"


def test_create_state_invalid_input():
    try:
        create_state("   ")
        assert False
    except ValueError:
        assert True


def test_append_message_invalid_state():
    try:
        append_message({}, "user", "hello")
        assert False
    except ValueError:
        assert True
