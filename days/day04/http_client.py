"""Day04: 最小版 HTTP 调用封装（中文注释版）。"""


def should_retry(status_code: int | None = None, error_type: str | None = None) -> bool:
    """判断这次失败是否应该重试。"""
    if status_code is not None:
        if not isinstance(status_code, int):
            raise ValueError("status_code must be int")

        # 5xx 表示服务端错误，通常可以尝试重试。
        if 500 <= status_code <= 599:
            return True

        # 4xx 通常是请求本身有问题，重试意义不大。
        return False

    if error_type is not None:
        if not isinstance(error_type, str):
            raise ValueError("error_type must be string")

        cleaned_error_type = error_type.strip().lower()
        if not cleaned_error_type:
            raise ValueError("error_type is empty")

        # 超时、连接错误可以认为是临时故障。
        return cleaned_error_type in ["timeout", "connection"]

    raise ValueError("status_code or error_type is required")


def fetch_json(url: str, request_func, max_retries: int = 2) -> dict:
    """调用请求函数，统一返回成功或失败结构。"""
    if not isinstance(url, str):
        raise ValueError("url must be string")

    cleaned_url = url.strip()
    if not cleaned_url:
        raise ValueError("url is empty")

    if not callable(request_func):
        raise ValueError("request_func must be callable")

    if not isinstance(max_retries, int):
        raise ValueError("max_retries must be int")

    if max_retries < 0:
        raise ValueError("max_retries must be >= 0")

    attempt = 0
    last_error = None

    while attempt <= max_retries:
        try:
            response = request_func(cleaned_url)
        except TimeoutError:
            last_error = "request timeout"
            if attempt == max_retries or not should_retry(error_type="timeout"):
                return {
                    "ok": False,
                    "data": None,
                    "error": last_error,
                    "status_code": None,
                    "attempts": attempt + 1,
                }
            attempt += 1
            continue
        except ConnectionError:
            last_error = "connection failed"
            if attempt == max_retries or not should_retry(error_type="connection"):
                return {
                    "ok": False,
                    "data": None,
                    "error": last_error,
                    "status_code": None,
                    "attempts": attempt + 1,
                }
            attempt += 1
            continue

        checked_response = _validate_response(response)
        status_code = checked_response["status_code"]

        if 200 <= status_code <= 299:
            return {
                "ok": True,
                "data": checked_response["json"],
                "error": None,
                "status_code": status_code,
                "attempts": attempt + 1,
            }

        last_error = checked_response["error"]

        if attempt == max_retries or not should_retry(status_code=status_code):
            return {
                "ok": False,
                "data": None,
                "error": last_error,
                "status_code": status_code,
                "attempts": attempt + 1,
            }

        attempt += 1

    return {
        "ok": False,
        "data": None,
        "error": last_error,
        "status_code": None,
        "attempts": attempt + 1,
    }


def _validate_response(response: dict) -> dict:
    """校验请求函数返回的最小结构。"""
    if not isinstance(response, dict):
        raise ValueError("response must be dict")

    required_keys = ["status_code", "json", "error"]
    for key in required_keys:
        if key not in response:
            raise ValueError(f"response missing key: {key}")

    if not isinstance(response["status_code"], int):
        raise ValueError("response status_code must be int")

    return response
