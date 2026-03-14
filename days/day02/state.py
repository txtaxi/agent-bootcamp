"""Day02: 统一状态对象（中文注释版）。"""


def create_state(user_input: str, thread_id: str = "default-thread") -> dict:
    """创建统一状态。

    这个函数的目标很简单：
    1. 把外部输入收进一个统一字典
    2. 给后续节点预留固定字段
    3. 保证后面所有函数都围绕同一个 state 工作
    """
    # 保护：用户输入必须是字符串。
    if not isinstance(user_input, str):
        raise ValueError("user_input must be string")

    # 保护：去掉空白后不能为空。
    cleaned_input = user_input.strip()
    if not cleaned_input:
        raise ValueError("user_input is empty")

    # 保护：thread_id 也必须是非空字符串。
    if not isinstance(thread_id, str):
        raise ValueError("thread_id must be string")

    cleaned_thread_id = thread_id.strip()
    if not cleaned_thread_id:
        raise ValueError("thread_id is empty")

    # 统一状态结构。
    return {
        "thread_id": cleaned_thread_id,
        "user_input": cleaned_input,
        "messages": [],
        "intent": None,
        "result": None,
        "error": None,
    }


def append_message(state: dict, role: str, content: str) -> dict:
    """向消息列表追加一条消息。"""
    checked_state = _validate_state(state)

    # role 表示消息身份，例如 user / assistant / system。
    if not isinstance(role, str):
        raise ValueError("role must be string")
    cleaned_role = role.strip()
    if not cleaned_role:
        raise ValueError("role is empty")

    # content 表示消息正文。
    if not isinstance(content, str):
        raise ValueError("content must be string")
    cleaned_content = content.strip()
    if not cleaned_content:
        raise ValueError("content is empty")

    checked_state["messages"].append(
        {"role": cleaned_role, "content": cleaned_content}
    )
    return checked_state


def set_intent(state: dict, intent: str) -> dict:
    """写入当前识别到的意图。"""
    checked_state = _validate_state(state)
    checked_state["intent"] = _validate_non_empty_string(intent, "intent")
    return checked_state


def set_result(state: dict, result: str) -> dict:
    """写入处理结果。"""
    checked_state = _validate_state(state)
    checked_state["result"] = _validate_non_empty_string(result, "result")
    return checked_state


def set_error(state: dict, error: str) -> dict:
    """写入用户可读错误信息。"""
    checked_state = _validate_state(state)
    checked_state["error"] = _validate_non_empty_string(error, "error")
    return checked_state


def _validate_state(state: dict) -> dict:
    """校验 state 是否是可用的统一结构。"""
    if not isinstance(state, dict):
        raise ValueError("state must be dict")

    required_keys = ["thread_id", "user_input", "messages", "intent", "result", "error"]
    for key in required_keys:
        if key not in state:
            raise ValueError(f"state missing key: {key}")

    if not isinstance(state["messages"], list):
        raise ValueError("state messages must be list")

    return state


def _validate_non_empty_string(value: str, field_name: str) -> str:
    """校验通用字符串字段。"""
    if not isinstance(value, str):
        raise ValueError(f"{field_name} must be string")

    cleaned_value = value.strip()
    if not cleaned_value:
        raise ValueError(f"{field_name} is empty")

    return cleaned_value
