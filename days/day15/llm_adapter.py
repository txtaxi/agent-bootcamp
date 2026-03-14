"""Day15: 最小版 LLM 适配层（中文注释版）。"""

from __future__ import annotations


def build_messages(user_input: str, system_prompt: str = "You are a helpful assistant.") -> list[dict]:
    """构造最小消息列表。"""
    cleaned_system_prompt = _validate_non_empty_string(system_prompt, "system_prompt")
    cleaned_user_input = _validate_non_empty_string(user_input, "user_input")

    return [
        {"role": "system", "content": cleaned_system_prompt},
        {"role": "user", "content": cleaned_user_input},
    ]


def parse_response(response: dict) -> str:
    """从模型响应中提取文本内容。"""
    if not isinstance(response, dict):
        raise ValueError("response must be dict")

    if "content" not in response:
        raise ValueError("response missing key: content")

    content = response["content"]
    if not isinstance(content, str):
        raise ValueError("response content must be string")

    cleaned_content = content.strip()
    if not cleaned_content:
        raise ValueError("response content is empty")

    return cleaned_content


def generate(model_func, user_input: str, system_prompt: str = "You are a helpful assistant.") -> dict:
    """通过适配层调用模型，统一输入输出结构。"""
    if not callable(model_func):
        raise ValueError("model_func must be callable")

    messages = build_messages(user_input, system_prompt=system_prompt)
    raw_response = model_func(messages)
    content = parse_response(raw_response)

    return {
        "ok": True,
        "messages": messages,
        "content": content,
        "error": None,
    }


def _validate_non_empty_string(value: str, field_name: str) -> str:
    """校验通用字符串字段。"""
    if not isinstance(value, str):
        raise ValueError(f"{field_name} must be string")

    cleaned_value = value.strip()
    if not cleaned_value:
        raise ValueError(f"{field_name} is empty")

    return cleaned_value
