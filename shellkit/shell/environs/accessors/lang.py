"""
environs/accessors/lang.py

Accessors for reading and writing the shell language setting (LANG).
"""

from ..constants import DEFAULT_LANG, ENV_KEY_LANG
from ..store import get_env, set_env


def get_lang() -> str:
    """
    Returns the current language setting from the environment.
    Falls back to DEFAULT_LANG if unset.
    """
    result = get_env(ENV_KEY_LANG, DEFAULT_LANG)
    return str(result)


def set_lang(value: str) -> None:
    """
    Sets the shell language setting in the environment.
    """
    set_env(ENV_KEY_LANG, value)
