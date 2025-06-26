"""
environs/accessors/home.py

Accessors for reading and writing the HOME directory.
"""

from ..constants import DEFAULT_HOME, ENV_KEY_HOME
from ..store import get_env, set_env


def get_home() -> str:
    """
    Returns the HOME directory from the environment.
    """
    result = get_env(ENV_KEY_HOME, DEFAULT_HOME)
    return str(result)


def set_home(value: str) -> None:
    """
    Sets the HOME directory in the environment.
    """
    set_env(ENV_KEY_HOME, value)
