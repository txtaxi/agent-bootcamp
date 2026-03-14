"""Day07: 第一周统一入口（中文注释版）。"""

from __future__ import annotations

from days.day06.agent_loop import run_turn


def parse_args(args: list[str]) -> dict:
    """解析最小命令行参数。"""
    if not isinstance(args, list):
        raise ValueError("args must be list")
    if not args:
        raise ValueError("args is empty")

    user_input = args[0]
    if not isinstance(user_input, str) or not user_input.strip():
        raise ValueError("user_input is invalid")

    thread_id = "cli-thread"
    if len(args) > 1:
        if not isinstance(args[1], str) or not args[1].strip():
            raise ValueError("thread_id is invalid")
        thread_id = args[1].strip()

    return {"user_input": user_input.strip(), "thread_id": thread_id}


def main(args: list[str]) -> dict:
    """第一周统一入口。"""
    parsed_args = parse_args(args)
    state = run_turn(parsed_args["user_input"], thread_id=parsed_args["thread_id"])
    return {
        "thread_id": state["thread_id"],
        "intent": state["intent"],
        "reply": state["messages"][-1]["content"],
        "error": state["error"],
    }
