"""
shell.docs

Provides user-facing documentation, including manuals and help messages.
"""

from .manuals import (
    get_manual,
    has_manual,
    list_manuals,
    get_manual_path,
)
from .texts import (
    get_help_text,
    get_reminder_texts,
)


__all__ = [
    "get_manual",
    "has_manual",
    "list_manuals",
    "get_manual_path",
    "get_help_text",
    "get_reminder_texts",
]
