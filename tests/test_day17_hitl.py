import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from days.day17.hitl_flow import needs_approval, resume_after_approval, wait_for_approval


def test_needs_approval():
    result = needs_approval("delete user account")
    assert result["requires_approval"] is True
    assert result["status"] == "waiting_approval"


def test_no_approval_needed():
    result = needs_approval("show weather")
    assert result["requires_approval"] is False
    assert result["status"] == "approved"


def test_wait_for_approval_approved():
    result = wait_for_approval("delete file", True)
    assert result["approved"] is True
    assert result["status"] == "approved"


def test_resume_after_approval_approved():
    result = resume_after_approval("transfer money", True)
    assert result["ok"] is True
    assert result["status"] == "approved"
    assert result["message"] == "Action executed: transfer money"


def test_resume_after_approval_rejected():
    result = resume_after_approval("transfer money", False)
    assert result["ok"] is False
    assert result["status"] == "rejected"
    assert result["message"] == "Action rejected: transfer money"
