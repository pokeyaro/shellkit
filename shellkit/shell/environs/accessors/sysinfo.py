"""
environs/accessors/sysinfo.py

Accessors for reading and writing system information.
"""

from typing import Any

from ..constants import DEFAULT_SYSINFO, ENV_KEY_SYSINFO
from ..store import get_env, set_env


def get_sysinfo() -> dict[str, Any]:
    """
    Returns the system information dictionary.
    Falls back to defaults if the value is missing or malformed.
    """
    result = get_env(ENV_KEY_SYSINFO, DEFAULT_SYSINFO)
    if isinstance(result, dict):
        return result
    else:
        return DEFAULT_SYSINFO


def set_sysinfo(info: dict[str, Any]) -> None:
    """
    Sets the system information dictionary in the environment.
    """
    set_env(ENV_KEY_SYSINFO, info)
