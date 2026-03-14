import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from days.day11.graph_memory_inmem import invoke_with_thread
from days.day12.graph_memory_sqlite import build_graph_with_sqlite, init_sqlite_path


def test_init_sqlite_path():
    path = init_sqlite_path("test_day12_path.sqlite")
    assert path.endswith("test_day12_path.sqlite")


def test_sqlite_checkpoint_survives_rebuild():
    sqlite_path = init_sqlite_path("test_day12_survive.sqlite")
    sqlite_file = Path(sqlite_path)
    if sqlite_file.exists():
        sqlite_file.unlink()

    graph_one = build_graph_with_sqlite(sqlite_path)
    first = invoke_with_thread(graph_one, "hello", "thread-sqlite")
    graph_one.sqlite_conn.close()

    graph_two = build_graph_with_sqlite(sqlite_path)
    second = invoke_with_thread(graph_two, "again", "thread-sqlite")
    graph_two.sqlite_conn.close()

    assert first["turn_count"] == 1
    assert first["reply"] == "Turn 1: hello"
    assert second["turn_count"] == 2
    assert second["reply"] == "Turn 2: again"


def test_sqlite_checkpoint_thread_isolation():
    sqlite_path = init_sqlite_path("test_day12_isolation.sqlite")
    sqlite_file = Path(sqlite_path)
    if sqlite_file.exists():
        sqlite_file.unlink()

    graph = build_graph_with_sqlite(sqlite_path)
    first_a = invoke_with_thread(graph, "hello", "thread-a")
    first_b = invoke_with_thread(graph, "world", "thread-b")
    graph.sqlite_conn.close()

    assert first_a["turn_count"] == 1
    assert first_b["turn_count"] == 1
    assert first_a["reply"] == "Turn 1: hello"
    assert first_b["reply"] == "Turn 1: world"
