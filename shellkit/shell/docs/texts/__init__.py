"""
shell.docs.texts

Contains localized user-facing messages like help texts, reminders.
"""

from shellkit.shell.environs.accessors import get_lang
from shellkit.shell.environs.constants import DEFAULT_LANG

from .help import HELP_TEXT
from .reminder import INFO_CRITICAL, INFO_NORMAL, REMINDER_TEXTS


__all__ = [
    "get_help_text",
    "get_reminder_texts",
    "INFO_NORMAL",
    "INFO_CRITICAL",
]


def get_help_text() -> str:
    """
    Returns the localized help command summary text.

    This function selects the appropriate language-specific help message
    based on the current shell environment's language setting. If the
    selected language is not available, it falls back to the default language.

    Returns:
        str: The localized help message text.
    """
    lang = get_lang()
    return HELP_TEXT.get(lang, HELP_TEXT[DEFAULT_LANG])


def get_reminder_texts(level: str = INFO_NORMAL) -> list[str]:
    """
    Returns a list of localized wellness reminder messages by urgency level.

    Chooses the appropriate message list from REMINDER_TEXTS based on
    current language and the given urgency level (e.g., "normal", "critical").
    Falls back to DEFAULT_LANG if no localized entry is found.

    Args:
        level (str): The urgency level of the reminder.
                     Should be INFO_NORMAL or INFO_CRITICAL.

    Returns:
        list[str]: A list of localized reminder messages.
    """
    lang = get_lang()
    lang_map = REMINDER_TEXTS.get(lang, REMINDER_TEXTS.get(DEFAULT_LANG, {}))
    return lang_map.get(level, [])
