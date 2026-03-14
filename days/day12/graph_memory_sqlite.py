"""Day12: 最小版 SQLite Checkpointer 图（中文注释版）。"""

from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import TypedDict

from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph import END, START, StateGraph


class SqliteMemoryState(TypedDict, total=False):
    """Day12 图中使用的状态结构。"""

    user_input: str
    reply: str
    turn_count: int


def init_sqlite_path(filename: str = "day12_checkpoint.sqlite") -> str:
    """初始化 SQLite 文件路径。"""
    if not isinstance(filename, str):
        raise ValueError("filename must be string")

    cleaned_filename = filename.strip()
    if not cleaned_filename:
        raise ValueError("filename is empty")

    if not cleaned_filename.endswith(".sqlite"):
        raise ValueError("filename must end with .sqlite")

    base_dir = Path(__file__).resolve().parents[1] / "data" / "checkpoints"
    base_dir.mkdir(parents=True, exist_ok=True)
    return str(base_dir / cleaned_filename)


def memory_node(state: SqliteMemoryState) -> dict:
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


def build_graph_with_sqlite(sqlite_path: str | None = None):
    """构建带 SQLite checkpointer 的最小图。"""
    resolved_path = sqlite_path or init_sqlite_path()
    if not isinstance(resolved_path, str):
        raise ValueError("sqlite_path must be string")

    cleaned_path = resolved_path.strip()
    if not cleaned_path:
        raise ValueError("sqlite_path is empty")

    graph_builder = StateGraph(SqliteMemoryState)
    graph_builder.add_node("memory", memory_node)
    graph_builder.add_edge(START, "memory")
    graph_builder.add_edge("memory", END)

    conn = sqlite3.connect(cleaned_path, check_same_thread=False)
    graph = graph_builder.compile(checkpointer=SqliteSaver(conn))

    # 挂在图对象上，方便测试或调用方显式关闭连接。
    graph.sqlite_conn = conn
    graph.sqlite_path = cleaned_path
    return graph
