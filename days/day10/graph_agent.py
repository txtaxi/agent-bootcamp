"""Day10: 用 LangGraph 复刻手写 Agent（中文注释版）。"""

from __future__ import annotations

from typing import TypedDict

from langgraph.graph import END, START, StateGraph

from days.day01.router import detect_intent
from days.day05.tools import dispatch_tool


class AgentState(TypedDict):
    """Day10 图中的最小状态结构。"""

    user_input: str
    intent: str
    result: str | None
    error: str | None
    reply: str


def router_node(state: AgentState) -> dict:
    """先识别当前输入的意图。"""
    user_input = _validate_user_input(state)
    return {"intent": detect_intent(user_input)}


def route_key(state: AgentState) -> str:
    """根据 intent 选择下一条边。"""
    _validate_intent(state)
    if state["intent"] in {"weather", "math"}:
        return "tool"
    return "final"


def tool_node(state: AgentState) -> dict:
    """根据意图调用工具，并写回 result 或 error。"""
    _validate_intent(state)
    user_input = _validate_user_input(state)

    if state["intent"] == "weather":
        tool_result = dispatch_tool("weather", "beijing")
        return {"result": str(tool_result["result"]), "error": None}

    if state["intent"] == "math":
        tool_result = dispatch_tool("calc", user_input)
        return {"result": str(tool_result["result"]), "error": None}

    return {"result": None, "error": "unknown intent"}


def final_node(state: AgentState) -> dict:
    """根据当前 state 生成最终回复。"""
    _validate_intent(state)
    if state.get("error"):
        return {"reply": f"Error: {state['error']}"}
    if state["intent"] == "weather":
        return {"reply": f"Weather reply: {state['result']}"}
    if state["intent"] == "math":
        return {"reply": f"Math reply: {state['result']}"}
    return {"reply": "Error: unknown intent", "error": "unknown intent"}


def build_agent_graph():
    """构建并编译 LangGraph 版最小 Agent。"""
    graph_builder = StateGraph(AgentState)
    graph_builder.add_node("router", router_node)
    graph_builder.add_node("tool", tool_node)
    graph_builder.add_node("final", final_node)
    graph_builder.add_edge(START, "router")
    graph_builder.add_conditional_edges("router", route_key, {"tool": "tool", "final": "final"})
    graph_builder.add_edge("tool", "final")
    graph_builder.add_edge("final", END)
    return graph_builder.compile()


def _validate_user_input(state: AgentState) -> str:
    """校验 user_input 字段。"""
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


def _validate_intent(state: AgentState) -> None:
    """校验 intent 字段。"""
    if not isinstance(state, dict):
        raise ValueError("state must be dict")
    if "intent" not in state:
        raise ValueError("state missing key: intent")
    if not isinstance(state["intent"], str):
        raise ValueError("intent must be string")
