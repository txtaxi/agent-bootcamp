import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from days.day20.config import load_settings, validate_settings
from days.day20.logging_setup import setup_logging


def test_load_settings_defaults():
    settings = load_settings({})
    assert settings["app_env"] == "dev"
    assert settings["log_level"] == "INFO"
    assert settings["default_thread_id"] == "default-thread"


def test_load_settings_custom():
    settings = load_settings(
        {
            "APP_ENV": "prod",
            "LOG_LEVEL": "ERROR",
            "DEFAULT_THREAD_ID": "thread-001",
        }
    )
    assert settings["app_env"] == "prod"
    assert settings["log_level"] == "ERROR"
    assert settings["default_thread_id"] == "thread-001"


def test_validate_settings_invalid_env():
    try:
        validate_settings(
            {
                "app_env": "local",
                "log_level": "INFO",
                "default_thread_id": "x",
            }
        )
        assert False
    except ValueError:
        assert True


def test_validate_settings_invalid_log_level():
    try:
        validate_settings(
            {
                "app_env": "dev",
                "log_level": "TRACE",
                "default_thread_id": "x",
            }
        )
        assert False
    except ValueError:
        assert True


def test_setup_logging():
    result = setup_logging("debug")
    assert result["logger_name"] == "agent_bootcamp"
    assert result["log_level"] == "DEBUG"
    assert result["handler_count"] == 1
