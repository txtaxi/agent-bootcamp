import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from days.day09.graph_router import build_graph, math_node, route_key, router_node, unknown_node, weather_node


def test_router_node():
    result = router_node({"user_input": "weather in beijing", "intent": "", "reply": ""})
    assert result["intent"] == "weather"


def test_route_key():
    assert route_key({"user_input": "x", "intent": "weather", "reply": ""}) == "weather"
    assert route_key({"user_input": "x", "intent": "math", "reply": ""}) == "math"
    assert route_key({"user_input": "x", "intent": "unknown", "reply": ""}) == "unknown"


def test_branch_nodes():
    assert weather_node({"user_input": "x", "intent": "weather", "reply": ""})["reply"] == "Weather branch"
    assert math_node({"user_input": "x", "intent": "math", "reply": ""})["reply"] == "Math branch"
    assert unknown_node({"user_input": "x", "intent": "unknown", "reply": ""})["reply"] == "Unknown branch"


def test_build_graph_weather():
    graph = build_graph()
    result = graph.invoke({"user_input": "weather in beijing", "intent": "", "reply": ""})
    assert result["intent"] == "weather"
    assert result["reply"] == "Weather branch"


def test_build_graph_math():
    graph = build_graph()
    result = graph.invoke({"user_input": "1 + 2", "intent": "", "reply": ""})
    assert result["intent"] == "math"
    assert result["reply"] == "Math branch"


def test_build_graph_unknown():
    graph = build_graph()
    result = graph.invoke({"user_input": "hello", "intent": "", "reply": ""})
    assert result["intent"] == "unknown"
    assert result["reply"] == "Unknown branch"
