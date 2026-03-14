import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from days.day06.agent_loop import run_turn
from days.day10.graph_agent import build_agent_graph, final_node, tool_node


def _initial_state(user_input: str) -> dict:
    return {"user_input": user_input, "intent": "", "result": None, "error": None, "reply": ""}


def test_tool_node_weather():
    result = tool_node(_initial_state("weather in beijing") | {"intent": "weather"})
    assert result["result"] == "beijing is sunny"
    assert result["error"] is None


def test_final_node_math():
    result = final_node(_initial_state("1 + 2") | {"intent": "math", "result": "3"})
    assert result["reply"] == "Math reply: 3"


def test_graph_matches_day06_weather():
    graph = build_agent_graph()
    graph_result = graph.invoke(_initial_state("weather in beijing"))
    loop_result = run_turn("weather in beijing", thread_id="day10-weather")
    assert graph_result["intent"] == loop_result["intent"]
    assert graph_result["reply"] == loop_result["messages"][-1]["content"]


def test_graph_matches_day06_math():
    graph = build_agent_graph()
    graph_result = graph.invoke(_initial_state("1 + 2 * 3"))
    loop_result = run_turn("1 + 2 * 3", thread_id="day10-math")
    assert graph_result["intent"] == loop_result["intent"]
    assert graph_result["reply"] == loop_result["messages"][-1]["content"]


def test_graph_matches_day06_unknown():
    graph = build_agent_graph()
    graph_result = graph.invoke(_initial_state("hello"))
    loop_result = run_turn("hello", thread_id="day10-unknown")
    assert graph_result["intent"] == loop_result["intent"]
    assert graph_result["reply"] == loop_result["messages"][-1]["content"]
    assert graph_result["error"] == loop_result["error"]
