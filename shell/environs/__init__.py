"""
shell.environs

Initializes and manages in-memory environment variables for the shell.
"""

from .initialize import init_environs
from .store import get_env, set_env, del_env, all_env


__all__ = [
    "init_environs",
    "get_env", "set_env", "del_env", "all_env",
]
