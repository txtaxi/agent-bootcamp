import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from days.day04.http_client import fetch_json, should_retry


def test_fetch_json_success():
    def fake_request(url: str) -> dict:
        return {"status_code": 200, "json": {"city": "beijing"}, "error": None}

    result = fetch_json("https://example.com/weather", fake_request)
    assert result["ok"] is True
    assert result["data"] == {"city": "beijing"}
    assert result["error"] is None
    assert result["status_code"] == 200
    assert result["attempts"] == 1


def test_fetch_json_timeout_retry_success():
    calls = {"count": 0}

    def fake_request(url: str) -> dict:
        calls["count"] += 1
        if calls["count"] == 1:
            raise TimeoutError()
        return {"status_code": 200, "json": {"value": 42}, "error": None}

    result = fetch_json("https://example.com/retry", fake_request, max_retries=2)
    assert result["ok"] is True
    assert result["data"] == {"value": 42}
    assert result["attempts"] == 2


def test_fetch_json_4xx_no_retry():
    calls = {"count": 0}

    def fake_request(url: str) -> dict:
        calls["count"] += 1
        return {"status_code": 404, "json": None, "error": "not found"}

    result = fetch_json("https://example.com/missing", fake_request, max_retries=2)
    assert result["ok"] is False
    assert result["error"] == "not found"
    assert result["status_code"] == 404
    assert result["attempts"] == 1
    assert calls["count"] == 1


def test_fetch_json_5xx_retry_then_fail():
    calls = {"count": 0}

    def fake_request(url: str) -> dict:
        calls["count"] += 1
        return {"status_code": 503, "json": None, "error": "service unavailable"}

    result = fetch_json("https://example.com/bad-gateway", fake_request, max_retries=2)
    assert result["ok"] is False
    assert result["error"] == "service unavailable"
    assert result["status_code"] == 503
    assert result["attempts"] == 3
    assert calls["count"] == 3


def test_should_retry():
    assert should_retry(status_code=503) is True
    assert should_retry(status_code=404) is False
    assert should_retry(error_type="timeout") is True
