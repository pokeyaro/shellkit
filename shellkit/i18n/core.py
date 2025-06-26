"""
i18n/core.py

Core logic for internationalization (i18n) support.
Handles language detection, message loading, and translation lookup via `t()`.

Priority: PYSH_LANG > LANG > fallback ("en").
Exposes functions for runtime language switching.
"""

import os
from typing import Any

from shellkit.i18n.lang import LANG_MAP, SUPPORTED_LANGS


# Language code constants
I18N_EN = "en"
I18N_ZH = "zh"
I18N_JA = "ja"
I18N_KO = "ko"

# Default fallback language (used when no match found)
I18N_DEFAULT = I18N_EN

# Internal state: currently selected language code
_current_lang = None

# Internal state: current language's message dictionary
_current_messages = {}


def _detect_lang() -> str:
    """
    Detect the preferred language code from environment variables.
    Priority order:
        1. PYSH_LANG (explicit override)
        2. LANG (system locale, e.g. "zh_CN.UTF-8")
        3. Fallback to default ("en")

    Returns:
        str: A valid language code (e.g. "en", "zh", "ja")
    """
    raw = (
        os.getenv("PYSH_LANG")
        or os.getenv("LANG", "").split(".")[0].split("_")[0]
        or I18N_DEFAULT
    )
    return raw if raw in SUPPORTED_LANGS else I18N_DEFAULT


def supported_languages() -> list[str]:
    """
    Returns a sorted list of supported language codes (e.g. ['en', 'ja', 'zh']).
    """
    return sorted(LANG_MAP.keys())


def set_language(lang_code: str) -> None:
    """
    Set the active language for translations.
    Invalid codes fallback to the default language.

    Args:
        lang_code (str): Language code to activate (e.g. "zh", "en").
    """
    global _current_lang, _current_messages
    if lang_code not in SUPPORTED_LANGS:
        lang_code = I18N_DEFAULT
    _current_lang = lang_code
    _current_messages = LANG_MAP[lang_code]


def get_language() -> str:
    """
    Get the currently active language code.

    Returns:
        str: Current language code (e.g. "en", "ja")
    """
    return _current_lang or I18N_DEFAULT


def t(key: str, *args: Any, **kwargs: Any) -> str:
    """
    Translate a given key with optional formatting.

    Supports both:
    - printf-style (%s) formatting with positional args
    - str.format-style formatting with keyword args

    Example:
        t("key.with.printf", "foo")
        t("key.with.format", {"name": "Alice"})   ← old style (via *args)
        t("key.with.format", name="Alice")        ← new style (via **kwargs)
    """
    msg: str = _current_messages.get(key, f"[!! missing i18n: {key} !!]")

    try:
        if kwargs:
            return msg.format(**kwargs)
        elif args:
            if isinstance(args[0], dict):  # legacy dict-style call
                return msg.format(**args[0])
            else:
                return msg % args
        else:
            return msg

    except Exception as e:
        return f"[!! i18n format error: {key} – {e} !!]"


# Auto-detect and initialize language at module load
set_language(_detect_lang())
