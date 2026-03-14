"""Day09: 最小版条件分支图（中文注释版）。"""

from __future__ import annotations

from typing import TypedDict

from langgraph.graph import END, START, StateGraph

from days.day01.router import detect_intent


class RouterState(TypedDict):
    """Day09 图中使用的最小状态结构。"""

    user_input: str
    intent: str
    reply: str


def router_node(state: RouterState) -> dict:
    """先根据输入写入 intent。"""
    user_input = _validate_user_input(state)
    return {"intent": detect_intent(user_input)}


def weather_node(state: RouterState) -> dict:
    """天气分支节点。"""
    _validate_intent(state)
    return {"reply": "Weather branch"}


def math_node(state: RouterState) -> dict:
    """数学分支节点。"""
    _validate_intent(state)
    return {"reply": "Math branch"}


def unknown_node(state: RouterState) -> dict:
    """未知分支节点。"""
    _validate_intent(state)
    return {"reply": "Unknown branch"}


def route_key(state: RouterState) -> str:
    """根据 intent 返回下一条边的 key。"""
    _validate_intent(state)
    if state["intent"] == "weather":
        return "weather"
    if state["intent"] == "math":
        return "math"
    return "unknown"


def build_graph():
    """构建带条件边的最小图。"""
    graph_builder = StateGraph(RouterState)
    graph_builder.add_node("router", router_node)
    graph_builder.add_node("weather", weather_node)
    graph_builder.add_node("math", math_node)
    graph_builder.add_node("unknown", unknown_node)
    graph_builder.add_edge(START, "router")
    graph_builder.add_conditional_edges(
        "router",
        route_key,
        {"weather": "weather", "math": "math", "unknown": "unknown"},
    )
    graph_builder.add_edge("weather", END)
    graph_builder.add_edge("math", END)
    graph_builder.add_edge("unknown", END)
    return graph_builder.compile()


def _validate_user_input(state: RouterState) -> str:
    """校验用户输入字段。"""
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
    return cleaned_input


def _validate_intent(state: RouterState) -> None:
    """校验 intent 字段存在且可用。"""
    if not isinstance(state, dict):
        raise ValueError("state must be dict")
    if "intent" not in state:
        raise ValueError("state missing key: intent")
    if not isinstance(state["intent"], str):
        raise ValueError("intent must be string")
