"""Day17: 最小版人在回路流程（中文注释版）。"""

from __future__ import annotations


def needs_approval(action: str) -> dict:
    """判断当前动作是否需要人工批准。"""
    cleaned_action = _validate_non_empty_string(action, "action").lower()

    high_risk_keywords = ["delete", "pay", "transfer", "shutdown"]
    requires_approval = any(keyword in cleaned_action for keyword in high_risk_keywords)

    return {
        "action": cleaned_action,
        "requires_approval": requires_approval,
        "status": "waiting_approval" if requires_approval else "approved",
    }


def wait_for_approval(action: str, approved: bool) -> dict:
    """模拟等待人工批准后的状态结果。"""
    checked = needs_approval(action)

    if checked["requires_approval"] is False:
        return {
            "action": checked["action"],
            "approved": True,
            "status": "approved",
        }

    if not isinstance(approved, bool):
        raise ValueError("approved must be bool")

    return {
        "action": checked["action"],
        "approved": approved,
        "status": "approved" if approved else "rejected",
    }


def resume_after_approval(action: str, approved: bool) -> dict:
    """根据批准结果恢复后续流程。"""
    approval_result = wait_for_approval(action, approved)

    if approval_result["approved"]:
        return {
            "ok": True,
            "action": approval_result["action"],
            "message": f"Action executed: {approval_result['action']}",
            "status": approval_result["status"],
        }

    return {
        "ok": False,
        "action": approval_result["action"],
        "message": f"Action rejected: {approval_result['action']}",
        "status": approval_result["status"],
    }


def _validate_non_empty_string(value: str, field_name: str) -> str:
    """校验通用字符串字段。"""
    if not isinstance(value, str):
        raise ValueError(f"{field_name} must be string")

    cleaned_value = value.strip()
    if not cleaned_value:
        raise ValueError(f"{field_name} is empty")

    return cleaned_value
