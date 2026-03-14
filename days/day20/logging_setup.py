"""Day20: 最小版日志初始化（中文注释版）。"""

from __future__ import annotations

import logging


def setup_logging(log_level: str = "INFO") -> dict:
    """初始化最小日志配置。"""
    if not isinstance(log_level, str):
        raise ValueError("log_level must be string")

    cleaned_level = log_level.strip().upper()
    if cleaned_level not in {"DEBUG", "INFO", "WARNING", "ERROR"}:
        raise ValueError("log_level is invalid")

    logger = logging.getLogger("agent_bootcamp")
    logger.handlers.clear()
    logger.setLevel(cleaned_level)

    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(levelname)s | %(name)s | %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return {
        "logger_name": logger.name,
        "log_level": cleaned_level,
        "handler_count": len(logger.handlers),
    }
