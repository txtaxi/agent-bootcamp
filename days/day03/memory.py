"""Day03: 用 JSON 保存和恢复 state（中文注释版）。"""

from __future__ import annotations

import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1] / "data" / "threads"


def get_state_path(thread_id: str) -> str:
    """根据 thread_id 生成状态文件路径。"""
    cleaned_thread_id = _validate_thread_id(thread_id)
    file_path = BASE_DIR / f"{cleaned_thread_id}.json"
    return str(file_path)


def save_state(state: dict) -> dict:
    """把 state 保存到对应的 JSON 文件。"""
    checked_state = _validate_state(state)
    file_path = Path(get_state_path(checked_state["thread_id"]))

    # 确保目录存在，这样第一次保存也不会失败。
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with file_path.open("w", encoding="utf-8") as file:
        json.dump(checked_state, file, ensure_ascii=False, indent=2)

    return {
        "thread_id": checked_state["thread_id"],
        "path": str(file_path),
        "saved": True,
    }


def load_state(thread_id: str) -> dict:
    """根据 thread_id 读取 JSON 文件中的 state。"""
    file_path = Path(get_state_path(thread_id))

    if not file_path.exists():
        raise ValueError("state file does not exist")

    with file_path.open("r", encoding="utf-8") as file:
        loaded_state = json.load(file)

    return _validate_state(loaded_state)


def list_threads() -> dict:
    """列出已经保存过的 thread_id。"""
    if not BASE_DIR.exists():
        return {"threads": []}

    thread_ids = sorted(file.stem for file in BASE_DIR.glob("*.json"))
    return {"threads": thread_ids}


def _validate_thread_id(thread_id: str) -> str:
    """thread_id 必须是非空字符串，且不能包含路径分隔符。"""
    if not isinstance(thread_id, str):
        raise ValueError("thread_id must be string")

    cleaned_thread_id = thread_id.strip()
    if not cleaned_thread_id:
        raise ValueError("thread_id is empty")

    invalid_chars = ["\\", "/", ":"]
    if any(char in cleaned_thread_id for char in invalid_chars):
        raise ValueError("thread_id contains invalid character")

    return cleaned_thread_id


def _validate_state(state: dict) -> dict:
    """校验 state 至少具备 Day02 约定的固定结构。"""
    if not isinstance(state, dict):
        raise ValueError("state must be dict")

    required_keys = ["thread_id", "user_input", "messages", "intent", "result", "error"]
    for key in required_keys:
        if key not in state:
            raise ValueError(f"state missing key: {key}")

    _validate_thread_id(state["thread_id"])

    if not isinstance(state["user_input"], str) or not state["user_input"].strip():
        raise ValueError("user_input is invalid")

    if not isinstance(state["messages"], list):
        raise ValueError("messages must be list")

    return state
