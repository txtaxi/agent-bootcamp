"""Day21: 最小版毕业项目 Agent（中文注释版）。"""

from __future__ import annotations

import json
from pathlib import Path

from days.day19.eval_runner import run_case, score_case, summarize_report
from days.day10.graph_agent import build_agent_graph


def _initial_state(user_input: str) -> dict:
    return {
        "user_input": user_input,
        "intent": "",
        "result": None,
        "error": None,
        "reply": "",
    }


def build_capstone_graph():
    """构建毕业项目使用的最小图。"""
    return build_agent_graph()


def run_demo(user_input: str) -> dict:
    """运行一次最小 demo。"""
    if not isinstance(user_input, str) or not user_input.strip():
        raise ValueError("user_input is invalid")

    graph = build_capstone_graph()
    result = graph.invoke(_initial_state(user_input.strip()))

    return {
        "intent": result["intent"],
        "reply": result["reply"],
        "error": result["error"],
    }


def run_batch_eval(cases_path: str | None = None) -> dict:
    """批量运行毕业项目评测。"""
    resolved_path = cases_path or str(
        Path(__file__).resolve().parents[1] / "day19" / "eval_cases.json"
    )
    path = Path(resolved_path)
    if not path.exists():
        raise ValueError("cases_path does not exist")

    cases = json.loads(path.read_text(encoding="utf-8"))

    def runner(user_input: str) -> str:
        return run_demo(user_input)["reply"]

    run_results = [run_case(case, runner) for case in cases]
    scored_results = [score_case(result) for result in run_results]
    report = summarize_report(scored_results)

    return {
        "report": report,
        "results": scored_results,
    }
