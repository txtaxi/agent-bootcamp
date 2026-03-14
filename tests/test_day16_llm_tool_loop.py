import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from days.day16.llm_tool_loop import decide_tool_call, execute_tool_call, finalize_answer


def test_decide_tool_call_use_tool():
    def decision_model(messages: list[dict]) -> dict:
        return {"content": "TOOL:weather:beijing"}

    result = decide_tool_call(decision_model, "weather in beijing")
    assert result["use_tool"] is True
    assert result["tool_name"] == "weather"
    assert result["tool_input"] == "beijing"


def test_execute_tool_call():
    decision = {
        "use_tool": True,
        "tool_name": "weather",
        "tool_input": "beijing",
        "raw_decision": "TOOL:weather:beijing",
    }
    result = execute_tool_call(decision)
    assert result["ok"] is True
    assert result["tool_used"] is True
    assert result["tool_result"] == "beijing is sunny"


def test_finalize_answer_with_tool():
    def final_model(messages: list[dict]) -> dict:
        assert "Tool result: beijing is sunny" in messages[1]["content"]
        return {"content": "It is sunny in beijing."}

    result = finalize_answer(
        final_model,
        "weather in beijing",
        {"tool_used": True, "tool_result": "beijing is sunny"},
    )
    assert result["ok"] is True
    assert result["used_tool"] is True
    assert result["answer"] == "It is sunny in beijing."


def test_finalize_answer_without_tool():
    def final_model(messages: list[dict]) -> dict:
        assert messages[1]["content"] == "hello"
        return {"content": "Hello there."}

    result = finalize_answer(final_model, "hello", {"tool_used": False, "tool_result": None})
    assert result["ok"] is True
    assert result["used_tool"] is False
    assert result["answer"] == "Hello there."


def test_no_tool_path():
    def decision_model(messages: list[dict]) -> dict:
        return {"content": "NO_TOOL"}

    decision = decide_tool_call(decision_model, "hello")
    execution = execute_tool_call(decision)
    assert decision["use_tool"] is False
    assert execution["tool_used"] is False
    assert execution["tool_result"] is None
