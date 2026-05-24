"""Compatibility layer — re-export dependency helpers from `deps.py`.
This keeps the API surface expected by some frameworks and docs.
"""
from .deps import get_current_user, admin_required, student_required, teacher_required

__all__ = ["get_current_user", "admin_required", "student_required", "teacher_required"]
