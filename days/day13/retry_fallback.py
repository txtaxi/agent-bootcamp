"""Day13: 最小版错误恢复与兜底（中文注释版）。"""

from __future__ import annotations


def safe_call_tool(tool_func, tool_input: str) -> dict:
    """安全调用工具，确保异常不会直接冒泡到用户层。"""
    if not callable(tool_func):
        raise ValueError("tool_func must be callable")

    cleaned_input = _validate_non_empty_string(tool_input, "tool_input")

    try:
        result = tool_func(cleaned_input)
    except Exception as exc:
        return {
            "ok": False,
            "result": None,
            "error": str(exc) or "tool call failed",
        }

    return {
        "ok": True,
        "result": result,
        "error": None,
    }


def fallback_reply(error: str) -> str:
    """把错误信息转成用户可读回复。"""
    cleaned_error = _validate_non_empty_string(error, "error")
    return f"Sorry, something went wrong: {cleaned_error}"


def with_retry(tool_func, tool_input: str, max_retries: int = 2) -> dict:
    """带重试地调用工具，失败后返回统一错误结构。"""
    if not callable(tool_func):
        raise ValueError("tool_func must be callable")

    cleaned_input = _validate_non_empty_string(tool_input, "tool_input")

    if not isinstance(max_retries, int):
        raise ValueError("max_retries must be int")

    if max_retries < 0:
        raise ValueError("max_retries must be >= 0")

    attempts = 0
    last_error = None

    while attempts <= max_retries:
        attempts += 1
        result = safe_call_tool(tool_func, cleaned_input)
        if result["ok"]:
            return {
                "ok": True,
                "result": result["result"],
                "error": None,
                "attempts": attempts,
            }

        last_error = result["error"]

    return {
        "ok": False,
        "result": None,
        "error": fallback_reply(last_error or "tool call failed"),
        "attempts": attempts,
    }


def _validate_non_empty_string(value: str, field_name: str) -> str:
    """校验通用字符串字段。"""
    if not isinstance(value, str):
        raise ValueError(f"{field_name} must be string")

    cleaned_value = value.strip()
    if not cleaned_value:
        raise ValueError(f"{field_name} is empty")

    return cleaned_value
