"""
environs/accessors/ps1.py

Accessors for reading and writing the PS1 shell prompt string.
"""

from ..constants import DEFAULT_PS1, ENV_KEY_PS1
from ..store import get_env, set_env


def get_ps1() -> str:
    """
    Returns the current PS1 prompt string from the environment.
    """
    result = get_env(ENV_KEY_PS1, DEFAULT_PS1)
    return str(result)


def set_ps1(value: str) -> None:
    """
    Sets the PS1 prompt string in the environment.
    """
    set_env(ENV_KEY_PS1, value)
