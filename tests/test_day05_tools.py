import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from days.day05.tools import dispatch_tool, tool_calc, tool_time, tool_weather


def test_tool_weather():
    result = tool_weather("beijing")
    assert result["ok"] is True
    assert result["tool"] == "weather"
    assert result["result"] == "beijing is sunny"


def test_tool_calc():
    result = tool_calc("1 + 2 * 3")
    assert result["ok"] is True
    assert result["tool"] == "calc"
    assert result["result"] == 7


def test_tool_time():
    result = tool_time("+08:00")
    assert result["ok"] is True
    assert result["tool"] == "time"
    assert isinstance(result["result"], str)
    assert len(result["result"]) == 19


def test_dispatch_tool():
    weather_result = dispatch_tool("weather", "shanghai")
    calc_result = dispatch_tool("calc", "8 / 2")
    time_result = dispatch_tool("time", "+08:00")
    assert weather_result["tool"] == "weather"
    assert weather_result["result"] == "shanghai is sunny"
    assert calc_result["tool"] == "calc"
    assert calc_result["result"] == 4.0
    assert time_result["tool"] == "time"


def test_dispatch_tool_unknown():
    try:
        dispatch_tool("stock", "tsla")
        assert False
    except ValueError:
        assert True
