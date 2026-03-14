import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from days.day02.state import append_message, create_state, set_intent, set_result
from days.day03.memory import get_state_path, list_threads, load_state, save_state


def test_save_and_load_state():
    state = create_state("weather in beijing", thread_id="thread-save-load")
    append_message(state, "user", "weather in beijing")
    set_intent(state, "weather")
    set_result(state, "today is sunny")

    save_result = save_state(state)
    loaded_state = load_state("thread-save-load")

    assert save_result["saved"] is True
    assert save_result["thread_id"] == "thread-save-load"
    assert loaded_state["thread_id"] == "thread-save-load"
    assert loaded_state["user_input"] == "weather in beijing"
    assert loaded_state["intent"] == "weather"
    assert loaded_state["result"] == "today is sunny"
    assert loaded_state["messages"] == [{"role": "user", "content": "weather in beijing"}]


def test_get_state_path():
    path = get_state_path("thread-path-check")
    assert path.endswith("thread-path-check.json")


def test_load_state_missing_file():
    try:
        load_state("thread-not-exist")
        assert False
    except ValueError:
        assert True


def test_list_threads():
    state = create_state("hello", thread_id="thread-list-check")
    save_state(state)
    result = list_threads()
    assert "thread-list-check" in result["threads"]
