"""Day16: 最小版 LLM + Tool Calling 闭环（中文注释版）。"""

from __future__ import annotations

from days.day05.tools import dispatch_tool
from days.day15.llm_adapter import generate


def decide_tool_call(model_func, user_input: str) -> dict:
    """让模型先决定是否要调用工具。"""
    result = generate(model_func, user_input, system_prompt="Decide whether a tool is needed.")
    content = result["content"].strip()

    if content.startswith("TOOL:"):
        parts = [part.strip() for part in content.split(":", 2)]
        if len(parts) != 3:
            raise ValueError("tool decision format is invalid")
        return {
            "use_tool": True,
            "tool_name": parts[1].lower(),
            "tool_input": parts[2],
            "raw_decision": content,
        }

    return {"use_tool": False, "tool_name": None, "tool_input": None, "raw_decision": content}


def execute_tool_call(decision: dict) -> dict:
    """按模型决策执行工具调用。"""
    if not isinstance(decision, dict):
        raise ValueError("decision must be dict")
    if "use_tool" not in decision:
        raise ValueError("decision missing key: use_tool")

    if decision["use_tool"] is False:
        return {"ok": True, "tool_used": False, "tool_result": None, "error": None}

    tool_name = decision.get("tool_name")
    tool_input = decision.get("tool_input")
    if not isinstance(tool_name, str) or not tool_name.strip():
        raise ValueError("tool_name is invalid")
    if not isinstance(tool_input, str) or not tool_input.strip():
        raise ValueError("tool_input is invalid")

    tool_result = dispatch_tool(tool_name.strip(), tool_input.strip())
    return {
        "ok": True,
        "tool_used": True,
        "tool_result": tool_result["result"],
        "error": None,
    }


def finalize_answer(model_func, user_input: str, tool_execution: dict) -> dict:
    """根据是否调过工具，生成最终回答。"""
    if not callable(model_func):
        raise ValueError("model_func must be callable")
    if not isinstance(tool_execution, dict):
        raise ValueError("tool_execution must be dict")

    if tool_execution.get("tool_used"):
        prompt = f"User asked: {user_input}\nTool result: {tool_execution['tool_result']}"
    else:
        prompt = user_input

    result = generate(model_func, prompt, system_prompt="Provide the final answer.")
    return {
        "ok": True,
        "answer": result["content"],
        "used_tool": bool(tool_execution.get("tool_used")),
        "error": None,
    }
