import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from days.day11.graph_memory_inmem import build_graph_with_inmem, invoke_with_thread


def test_same_thread_keeps_turn_count():
    graph = build_graph_with_inmem()
    first = invoke_with_thread(graph, "hello", "thread-a")
    second = invoke_with_thread(graph, "again", "thread-a")
    assert first["turn_count"] == 1
    assert first["reply"] == "Turn 1: hello"
    assert second["turn_count"] == 2
    assert second["reply"] == "Turn 2: again"


def test_different_threads_are_isolated():
    graph = build_graph_with_inmem()
    first_a = invoke_with_thread(graph, "hello", "thread-a")
    first_b = invoke_with_thread(graph, "world", "thread-b")
    assert first_a["turn_count"] == 1
    assert first_b["turn_count"] == 1
    assert first_a["reply"] == "Turn 1: hello"
    assert first_b["reply"] == "Turn 1: world"


def test_invoke_with_thread_invalid_input():
    graph = build_graph_with_inmem()
    try:
        invoke_with_thread(graph, "   ", "thread-a")
        assert False
    except ValueError:
        assert True
