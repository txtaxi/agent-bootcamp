"""Day06: 最小版 Agent 主循环（中文注释版）。"""

from __future__ import annotations

from days.day01.router import detect_intent
from days.day02.state import append_message, create_state, set_error, set_intent, set_result
from days.day03.memory import save_state
from days.day05.tools import dispatch_tool


def run_turn(user_input: str, thread_id: str = "default-thread") -> dict:
    """执行一轮最小 Agent 流程。"""
    state = create_state(user_input, thread_id=thread_id)
    append_message(state, "user", state["user_input"])

    intent = detect_intent(state["user_input"])
    set_intent(state, intent)

    if intent == "weather":
        tool_result = dispatch_tool("weather", "beijing")
        set_result(state, str(tool_result["result"]))
    elif intent == "math":
        tool_result = dispatch_tool("calc", state["user_input"])
        set_result(state, str(tool_result["result"]))
    else:
        set_error(state, "unknown intent")

    reply = build_reply(state)
    append_message(state, "assistant", reply)
    save_state(state)
    return state


def build_reply(state: dict) -> str:
    """根据当前 state 生成用户可读回复。"""
    _validate_state_for_reply(state)

    if state["error"]:
        return f"Error: {state['error']}"

    if state["intent"] == "weather":
        return f"Weather reply: {state['result']}"

    if state["intent"] == "math":
        return f"Math reply: {state['result']}"

    return "Unknown reply"


def run_cli() -> None:
    """最小命令行入口。"""
    print("Agent CLI started. Type 'exit' to quit.")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Agent stopped.")
            break

        state = run_turn(user_input)
        print(f"Agent: {build_reply(state)}")


def _validate_state_for_reply(state: dict) -> None:
    """校验 build_reply 需要的最小结构。"""
    if not isinstance(state, dict):
        raise ValueError("state must be dict")

    required_keys = ["intent", "result", "error"]
    for key in required_keys:
        if key not in state:
            raise ValueError(f"state missing key: {key}")
