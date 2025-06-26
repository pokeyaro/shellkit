"""
environs/store.py

Stores and manages shell environment variables in memory.
"""

from typing import Any, Optional, Union

from shellkit.i18n import t
from shellkit.inspector.debug import debug_env


# Supported value types in environment: primitives, dicts, and lists
JSONPrimitive = Union[str, int, float, bool, None]
JSONValue = Union[JSONPrimitive, dict[str, Any], list[Any]]


# In-memory environment map: str key → JSON-compatible value
_env: dict[str, JSONValue] = {}


def get_env(key: str, default: Optional[JSONValue] = None) -> Optional[JSONValue]:
    """
    Retrieves the value of an environment variable by key.
    Handles special shell variables like $? and $0.
    """
    # Check for runtime-bound special variables first
    if (special := _get_special_var_from_state(key)) is not None:
        debug_env(t("shell.environs.get_env.special_value", key, special))
        return special

    result = _env.get(key, default)

    # Skip debug output for internal or high-frequency variables
    if not key.startswith("_ENV__") and key not in ["PS1", "HISTORY_SIZE", "PWD", "HOME", "SYSINFO"]:
        debug_env(t("shell.environs.get_env.normal_value", key, result))

    return result


def set_env(key: str, value: JSONValue, force: bool = True) -> None:
    """
    Sets or updates the value of an environment variable.
    Skips setting if force=False and key already exists.
    """
    if not key.startswith("_ENV__"):
        debug_env(t("shell.environs.set_env.set_value", key, value))

    if force or key not in _env:
        _env[key] = value
    else:
        if not key.startswith("_ENV__"):
            debug_env(t("shell.environs.set_env.skip_existing", key))


def del_env(key: str) -> bool:
    """
    Deletes an environment variable by key.
    Returns True if deletion succeeded, False otherwise.
    """
    if not key.startswith("_ENV__"):
        debug_env(t("shell.environs.del_env.start", key))

    if key in _env:
        del _env[key]
        if not key.startswith("_ENV__"):
            debug_env(t("shell.environs.del_env.success", key))
        return True

    if not key.startswith("_ENV__"):
        debug_env(t("shell.environs.del_env.failed", key))

    return False


def all_env() -> dict[str, JSONValue]:
    """
    Returns a shallow copy of all current environment variables.
    """
    debug_env(t("shell.environs.all_env.dump"))
    return dict(_env)


def _get_special_var_from_state(name: str) -> Optional[str]:
    """
    Returns runtime-bound shell variables like $?, $$, $0.
    """
    from shellkit.shell.state import get_context
    return get_context().special_var(name)
