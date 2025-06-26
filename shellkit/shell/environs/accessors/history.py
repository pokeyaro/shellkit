"""
environs/accessors/history.py

Accessors for reading and writing the command history size.
"""

from ..constants import DEFAULT_HISTORY_SIZE, ENV_KEY_HISTORY_SIZE
from ..store import get_env, set_env


def get_history_size() -> int:
    """
    Returns the configured command history size.
    """
    result = get_env(ENV_KEY_HISTORY_SIZE, DEFAULT_HISTORY_SIZE)
    try:
        return int(result)  # type: ignore[arg-type]
    except (ValueError, TypeError):
        return DEFAULT_HISTORY_SIZE


def set_history_size(size: int) -> None:
    """
    Sets the command history size in the environment.
    """
    set_env(ENV_KEY_HISTORY_SIZE, size)
