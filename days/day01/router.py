"""Day01: 关键词路由器（中文注释版）。"""


def normalize_text(text: str) -> str:
    """规范化输入文本，保证后续意图识别稳定。

    步骤：
    1. 校验输入类型
    2. 去掉首尾空格
    3. 转为小写
    4. 拒绝空字符串
    """
    # 保护：只接受字符串输入。
    if not isinstance(text, str):
        raise ValueError("text must be string")

    # 清理空白并统一大小写。
    cleaned = text.strip().lower()

    # 保护：清理后为空，判定为非法输入。
    if not cleaned:
        raise ValueError("text is empty")

    return cleaned


def detect_intent(text: str) -> str:
    """根据文本识别意图。

    返回值只会是：weather、math、unknown。
    """
    normalized = normalize_text(text)

    # 天气相关关键词。
    if any(k in normalized for k in ["weather", "temperature", "forecast"]):
        return "weather"

    # 数学相关关键词或运算符。
    if any(k in normalized for k in ["+", "-", "*", "/", "math", "calc"]):
        return "math"

    # 兜底分类。
    return "unknown"


def route(text: str) -> dict:
    """对外入口函数。

    统一返回字典结构，便于后续迁移到状态机/图框架。
    """
    return {"intent": detect_intent(text)}
