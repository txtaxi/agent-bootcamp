"""Day05: 最小版工具系统与分发器（中文注释版）。"""

from __future__ import annotations

from datetime import datetime, timezone, timedelta


def tool_weather(city: str) -> dict:
    """模拟天气工具。"""
    cleaned_city = _validate_non_empty_string(city, "city")

    return {
        "ok": True,
        "tool": "weather",
        "result": f"{cleaned_city} is sunny",
        "error": None,
    }


def tool_calc(expression: str) -> dict:
    """最小版计算工具，只支持 + - * /。"""
    cleaned_expression = _validate_non_empty_string(expression, "expression")

    allowed_chars = set("0123456789+-*/(). ")
    if any(char not in allowed_chars for char in cleaned_expression):
        raise ValueError("expression contains invalid character")

    try:
        # 这里用空的 __builtins__，避免执行任意 Python 内置能力。
        value = eval(cleaned_expression, {"__builtins__": {}}, {})
    except Exception:
        raise ValueError("expression is invalid")

    return {
        "ok": True,
        "tool": "calc",
        "result": value,
        "error": None,
    }


def tool_time(utc_offset: str = "+08:00") -> dict:
    """返回指定 UTC 偏移下的当前时间。"""
    cleaned_offset = _validate_non_empty_string(utc_offset, "utc_offset")
    tzinfo = _parse_utc_offset(cleaned_offset)
    current_time = datetime.now(tzinfo).strftime("%Y-%m-%d %H:%M:%S")

    return {
        "ok": True,
        "tool": "time",
        "result": current_time,
        "error": None,
    }


def dispatch_tool(tool_name: str, tool_input: str | None = None) -> dict:
    """统一工具分发入口。"""
    cleaned_tool_name = _validate_non_empty_string(tool_name, "tool_name").lower()

    if cleaned_tool_name == "weather":
        return tool_weather(tool_input or "beijing")

    if cleaned_tool_name == "calc":
        if tool_input is None:
            raise ValueError("tool_input is required for calc")
        return tool_calc(tool_input)

    if cleaned_tool_name == "time":
        return tool_time(tool_input or "+08:00")

    raise ValueError("unknown tool")


def _validate_non_empty_string(value: str, field_name: str) -> str:
    """校验通用字符串字段。"""
    if not isinstance(value, str):
        raise ValueError(f"{field_name} must be string")

    cleaned_value = value.strip()
    if not cleaned_value:
        raise ValueError(f"{field_name} is empty")

    return cleaned_value


def _parse_utc_offset(utc_offset: str):
    """把 +08:00 这种字符串转成 timezone 对象。"""
    if len(utc_offset) != 6 or utc_offset[0] not in "+-" or utc_offset[3] != ":":
        raise ValueError("utc_offset format must be like +08:00")

    sign = 1 if utc_offset[0] == "+" else -1

    try:
        hours = int(utc_offset[1:3])
        minutes = int(utc_offset[4:6])
    except ValueError:
        raise ValueError("utc_offset format must be like +08:00")

    if hours > 23 or minutes > 59:
        raise ValueError("utc_offset is out of range")

    offset = timedelta(hours=hours * sign, minutes=minutes * sign)
    return timezone(offset)
