import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from days.day07.main import main, parse_args


def test_parse_args():
    result = parse_args(["weather in beijing", "day07-thread"])
    assert result["user_input"] == "weather in beijing"
    assert result["thread_id"] == "day07-thread"


def test_main_weather():
    result = main(["weather in beijing", "day07-weather"])
    assert result["thread_id"] == "day07-weather"
    assert result["intent"] == "weather"
    assert "Weather reply" in result["reply"]
    assert result["error"] is None


def test_main_math():
    result = main(["1 + 2 * 3", "day07-math"])
    assert result["intent"] == "math"
    assert result["reply"] == "Math reply: 7"
    assert result["error"] is None


def test_main_unknown():
    result = main(["hello", "day07-unknown"])
    assert result["intent"] == "unknown"
    assert result["reply"] == "Error: unknown intent"
    assert result["error"] == "unknown intent"
