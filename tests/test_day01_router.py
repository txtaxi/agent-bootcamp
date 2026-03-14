# sys: 访问 Python 运行时信息（包括导入路径）
import sys
# pathlib: 更安全地处理路径
from pathlib import Path

# 项目根目录 = tests 的上一级目录
ROOT = Path(__file__).resolve().parents[1]
# 把项目根目录放到搜索路径最前面，确保可导入 day01 包
sys.path.insert(0, str(ROOT))

from days.day01.router import route, normalize_text


def test_weather():
    # 天气输入应识别为 weather
    assert route("weather in beijing")["intent"] == "weather"


def test_math():
    # 数学输入应识别为 math
    assert route("1 + 2")["intent"] == "math"


def test_unknown():
    # 普通文本应识别为 unknown
    assert route("hello")["intent"] == "unknown"


def test_empty_raises():
    # 空白输入应抛出 ValueError
    try:
        normalize_text("   ")
        assert False
    except ValueError:
        assert True

