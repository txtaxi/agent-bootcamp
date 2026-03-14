"""Day08: 最小版 LangGraph 图（中文注释版）。"""

from __future__ import annotations

from typing import TypedDict

from langgraph.graph import END, START, StateGraph


class MinimalState(TypedDict):
    """最小图状态。"""

    user_input: str
    reply: str


def echo_node(state: MinimalState) -> dict:
    """把用户输入简单回显成 reply。"""
    if not isinstance(state, dict):
        raise ValueError("state must be dict")

    if "user_input" not in state:
        raise ValueError("state missing key: user_input")

    user_input = state["user_input"]
    if not isinstance(user_input, str):
        raise ValueError("user_input must be string")

    cleaned_input = user_input.strip()
    if not cleaned_input:
        raise ValueError("user_input is empty")

    return {"reply": f"Echo: {cleaned_input}"}


def build_graph():
    """构建并编译最小 StateGraph。"""
    graph_builder = StateGraph(MinimalState)
    graph_builder.add_node("echo", echo_node)
    graph_builder.add_edge(START, "echo")
    graph_builder.add_edge("echo", END)
    return graph_builder.compile()
