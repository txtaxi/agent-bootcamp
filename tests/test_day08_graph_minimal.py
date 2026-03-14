import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from days.day08.graph_minimal import build_graph, echo_node


def test_echo_node():
    result = echo_node({"user_input": "hello", "reply": ""})
    assert result["reply"] == "Echo: hello"


def test_build_graph_invoke():
    graph = build_graph()
    result = graph.invoke({"user_input": "langgraph", "reply": ""})
    assert result["user_input"] == "langgraph"
    assert result["reply"] == "Echo: langgraph"


def test_echo_node_invalid_input():
    try:
        echo_node({"user_input": "   ", "reply": ""})
        assert False
    except ValueError:
        assert True
