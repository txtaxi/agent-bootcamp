"""Day19: 最小版评测器与报告（中文注释版）。"""

from __future__ import annotations

import time


def run_case(case: dict, runner_func) -> dict:
    """执行单条评测用例，并记录延迟。"""
    if not isinstance(case, dict):
        raise ValueError("case must be dict")

    required_keys = ["name", "input", "expected"]
    for key in required_keys:
        if key not in case:
            raise ValueError(f"case missing key: {key}")

    if not callable(runner_func):
        raise ValueError("runner_func must be callable")

    start_time = time.perf_counter()
    actual = runner_func(case["input"])
    latency_ms = (time.perf_counter() - start_time) * 1000

    return {
        "name": case["name"],
        "input": case["input"],
        "expected": case["expected"],
        "actual": actual,
        "latency_ms": latency_ms,
    }


def score_case(run_result: dict) -> dict:
    """给单条执行结果打分。"""
    if not isinstance(run_result, dict):
        raise ValueError("run_result must be dict")

    required_keys = ["name", "expected", "actual", "latency_ms"]
    for key in required_keys:
        if key not in run_result:
            raise ValueError(f"run_result missing key: {key}")

    success = run_result["expected"] == run_result["actual"]

    return {
        "name": run_result["name"],
        "success": success,
        "latency_ms": run_result["latency_ms"],
        "expected": run_result["expected"],
        "actual": run_result["actual"],
    }


def summarize_report(scored_results: list[dict]) -> dict:
    """汇总基线报告。"""
    if not isinstance(scored_results, list):
        raise ValueError("scored_results must be list")

    if not scored_results:
        raise ValueError("scored_results is empty")

    total = len(scored_results)
    success_count = sum(1 for result in scored_results if result["success"])
    average_latency_ms = sum(result["latency_ms"] for result in scored_results) / total

    return {
        "total": total,
        "success_count": success_count,
        "success_rate": success_count / total,
        "average_latency_ms": average_latency_ms,
    }
