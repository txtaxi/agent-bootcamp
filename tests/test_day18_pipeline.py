import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from days.day18.multi_tool_pipeline import calculate_step, retrieve_step, summarize_step


def test_retrieve_step():
    result = retrieve_step("find price")
    assert result["query"] == "find price"
    assert result["retrieved_text"] == "price is 5"
    assert result["error"] is None


def test_calculate_step():
    retrieval = retrieve_step("find price")
    result = calculate_step(retrieval)
    assert result["retrieved_text"] == "price is 5"
    assert result["calculated_value"] == 10
    assert result["error"] is None


def test_summarize_step():
    retrieval = retrieve_step("find price")
    calculation = calculate_step(retrieval)
    result = summarize_step(calculation)
    assert result["summary"] == "Retrieved 'price is 5', calculated total is 10."
    assert result["error"] is None


def test_pipeline_state_passing():
    retrieval = retrieve_step("find price")
    calculation = calculate_step(retrieval)
    summary = summarize_step(calculation)
    assert retrieval["retrieved_text"] == calculation["retrieved_text"]
    assert "calculated total is 10" in summary["summary"]
