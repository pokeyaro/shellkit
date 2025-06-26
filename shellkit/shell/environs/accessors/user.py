"""
environs/accessors/user.py

Accessors for reading and writing the current shell user.
"""

from ..constants import DEFAULT_USER, ENV_KEY_USER
from ..store import get_env, set_env


def get_user() -> str:
    """
    Returns the current user name from the environment.
    """
    result = get_env(ENV_KEY_USER, DEFAULT_USER)
    return str(result)


def set_user(value: str) -> None:
    """
    Sets the current user name in the environment.
    """
    set_env(ENV_KEY_USER, value)
