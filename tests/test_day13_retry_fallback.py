import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from days.day13.retry_fallback import fallback_reply, safe_call_tool, with_retry


def test_safe_call_tool_success():
    def ok_tool(user_input: str) -> str:
        return f"ok: {user_input}"

    result = safe_call_tool(ok_tool, "hello")
    assert result["ok"] is True
    assert result["result"] == "ok: hello"
    assert result["error"] is None


def test_safe_call_tool_error():
    def bad_tool(user_input: str) -> str:
        raise RuntimeError("network failed")

    result = safe_call_tool(bad_tool, "hello")
    assert result["ok"] is False
    assert result["result"] is None
    assert result["error"] == "network failed"


def test_fallback_reply():
    assert fallback_reply("network failed") == "Sorry, something went wrong: network failed"


def test_with_retry_success_after_retry():
    calls = {"count": 0}

    def flaky_tool(user_input: str) -> str:
        calls["count"] += 1
        if calls["count"] < 3:
            raise RuntimeError("temporary error")
        return f"ok: {user_input}"

    result = with_retry(flaky_tool, "hello", max_retries=2)
    assert result["ok"] is True
    assert result["result"] == "ok: hello"
    assert result["attempts"] == 3


def test_with_retry_fallback():
    def always_bad(user_input: str) -> str:
        raise RuntimeError("service unavailable")

    result = with_retry(always_bad, "hello", max_retries=1)
    assert result["ok"] is False
    assert result["result"] is None
    assert result["attempts"] == 2
    assert result["error"] == "Sorry, something went wrong: service unavailable"
