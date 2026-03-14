"""Day11: 最小版 InMemory Checkpointer 图（中文注释版）。"""

from __future__ import annotations

from typing import TypedDict

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph


class MemoryState(TypedDict, total=False):
    """Day11 图中使用的状态结构。"""

    user_input: str
    reply: str
    turn_count: int


def memory_node(state: MemoryState) -> dict:
    """根据当前 state 生成 reply，并累计轮次。"""
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

    previous_turn_count = state.get("turn_count", 0)
    if not isinstance(previous_turn_count, int):
        raise ValueError("turn_count must be int")

    new_turn_count = previous_turn_count + 1
    return {
        "reply": f"Turn {new_turn_count}: {cleaned_input}",
        "turn_count": new_turn_count,
    }


def build_graph_with_inmem():
    """构建带 InMemory checkpointer 的最小图。"""
    graph_builder = StateGraph(MemoryState)
    graph_builder.add_node("memory", memory_node)
    graph_builder.add_edge(START, "memory")
    graph_builder.add_edge("memory", END)
    return graph_builder.compile(checkpointer=InMemorySaver())


def invoke_with_thread(graph, user_input: str, thread_id: str) -> dict:
    """按 thread_id 调用图，观察同线程状态延续。"""
    if not isinstance(user_input, str):
        raise ValueError("user_input must be string")

    cleaned_input = user_input.strip()
    if not cleaned_input:
        raise ValueError("user_input is empty")

    if not isinstance(thread_id, str):
        raise ValueError("thread_id must be string")

    cleaned_thread_id = thread_id.strip()
    if not cleaned_thread_id:
        raise ValueError("thread_id is empty")

    return graph.invoke(
        {"user_input": cleaned_input},
        config={"configurable": {"thread_id": cleaned_thread_id}},
    )
