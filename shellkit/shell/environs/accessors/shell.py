"""
environs/accessors/shell.py

Accessors for reading and writing the shell path.
"""

from ..constants import DEFAULT_SHELL, ENV_KEY_SHELL
from ..store import get_env, set_env


def get_shell() -> str:
    """
    Returns the configured shell path.
    """
    result = get_env(ENV_KEY_SHELL, DEFAULT_SHELL)
    return str(result)


def set_shell(value: str) -> None:
    """
    Sets the shell path in the environment.
    """
    set_env(ENV_KEY_SHELL, value)
