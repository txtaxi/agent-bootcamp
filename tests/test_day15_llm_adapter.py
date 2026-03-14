import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from days.day15.llm_adapter import build_messages, generate, parse_response


def test_build_messages():
    messages = build_messages("hello")
    assert messages[0]["role"] == "system"
    assert messages[1]["role"] == "user"
    assert messages[1]["content"] == "hello"


def test_parse_response():
    assert parse_response({"content": "hi there"}) == "hi there"


def test_generate():
    def fake_model(messages: list[dict]) -> dict:
        assert messages[1]["content"] == "hello"
        return {"content": "mock reply"}

    result = generate(fake_model, "hello")
    assert result["ok"] is True
    assert result["content"] == "mock reply"
    assert result["error"] is None
    assert result["messages"][1]["content"] == "hello"


def test_generate_invalid_response():
    def bad_model(messages: list[dict]) -> dict:
        return {"text": "missing content"}

    try:
        generate(bad_model, "hello")
        assert False
    except ValueError:
        assert True
