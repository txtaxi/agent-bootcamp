"""Day18: 最小版多工具流水线（中文注释版）。"""

from __future__ import annotations


def retrieve_step(query: str) -> dict:
    """模拟检索步骤，返回结构化检索结果。"""
    cleaned_query = _validate_non_empty_string(query, "query")

    return {
        "query": cleaned_query,
        "retrieved_text": "price is 5",
        "error": None,
    }


def calculate_step(retrieval_result: dict) -> dict:
    """根据检索结果做一个最小计算。"""
    if not isinstance(retrieval_result, dict):
        raise ValueError("retrieval_result must be dict")

    if "retrieved_text" not in retrieval_result:
        raise ValueError("retrieval_result missing key: retrieved_text")

    retrieved_text = retrieval_result["retrieved_text"]
    if not isinstance(retrieved_text, str):
        raise ValueError("retrieved_text must be string")

    if "5" not in retrieved_text:
        raise ValueError("retrieved_text does not contain expected number")

    value = 5
    total = value * 2

    return {
        "retrieved_text": retrieved_text,
        "calculated_value": total,
        "error": None,
    }


def summarize_step(calculation_result: dict) -> dict:
    """把中间结果整理成最终摘要。"""
    if not isinstance(calculation_result, dict):
        raise ValueError("calculation_result must be dict")

    if "retrieved_text" not in calculation_result:
        raise ValueError("calculation_result missing key: retrieved_text")

    if "calculated_value" not in calculation_result:
        raise ValueError("calculation_result missing key: calculated_value")

    retrieved_text = calculation_result["retrieved_text"]
    calculated_value = calculation_result["calculated_value"]

    if not isinstance(retrieved_text, str):
        raise ValueError("retrieved_text must be string")
    if not isinstance(calculated_value, int):
        raise ValueError("calculated_value must be int")

    return {
        "summary": f"Retrieved '{retrieved_text}', calculated total is {calculated_value}.",
        "error": None,
    }


def _validate_non_empty_string(value: str, field_name: str) -> str:
    """校验通用字符串字段。"""
    if not isinstance(value, str):
        raise ValueError(f"{field_name} must be string")

    cleaned_value = value.strip()
    if not cleaned_value:
        raise ValueError(f"{field_name} is empty")

    return cleaned_value
