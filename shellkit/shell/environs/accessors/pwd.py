"""
environs/accessors/pwd.py

Accessors for reading and writing the current and previous working directories.
"""

from ..constants import (
    DEFAULT_PWD, ENV_KEY_PWD,
    ENV_KEY_PWD_CUR, ENV_KEY_PWD_PREV,
)
from ..store import get_env, set_env


def get_pwd() -> tuple[str, str]:
    """
    Returns a tuple (current, previous) representing the working directories.
    """
    pwd = get_env(ENV_KEY_PWD, DEFAULT_PWD)
    current = pwd.get(ENV_KEY_PWD_CUR)  # type: ignore[union-attr]
    previous = pwd.get(ENV_KEY_PWD_PREV)  # type: ignore[union-attr]
    return str(current), str(previous)


def set_pwd(cur: str, prev: str) -> None:
    """
    Sets both the current and previous working directories.
    """
    set_env(ENV_KEY_PWD, {ENV_KEY_PWD_CUR: cur, ENV_KEY_PWD_PREV: prev})
