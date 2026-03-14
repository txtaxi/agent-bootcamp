"""Day20: 最小版配置加载与校验（中文注释版）。"""

from __future__ import annotations

import os


def load_settings(env: dict | None = None) -> dict:
    """从环境变量中读取最小配置。"""
    source = env if env is not None else os.environ
    if not isinstance(source, dict):
        raise ValueError("env must be dict")

    settings = {
        "app_env": source.get("APP_ENV", "dev"),
        "log_level": source.get("LOG_LEVEL", "INFO"),
        "default_thread_id": source.get("DEFAULT_THREAD_ID", "default-thread"),
    }
    validate_settings(settings)
    return settings


def validate_settings(settings: dict) -> dict:
    """校验配置是否合法。"""
    if not isinstance(settings, dict):
        raise ValueError("settings must be dict")

    required_keys = ["app_env", "log_level", "default_thread_id"]
    for key in required_keys:
        if key not in settings:
            raise ValueError(f"settings missing key: {key}")

    if settings["app_env"] not in {"dev", "test", "prod"}:
        raise ValueError("app_env must be one of dev/test/prod")

    if settings["log_level"] not in {"DEBUG", "INFO", "WARNING", "ERROR"}:
        raise ValueError("log_level is invalid")

    thread_id = settings["default_thread_id"]
    if not isinstance(thread_id, str) or not thread_id.strip():
        raise ValueError("default_thread_id is invalid")

    return settings
