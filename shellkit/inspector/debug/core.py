"""
inspector.debug.core

Core utilities and shared state for debug tracing and counter control.
"""

from typing import Any, Callable, TypeVar


F = TypeVar('F', bound=Callable[..., Any])

# Private module state
_debug_enabled = False  # Whether debug mode is enabled
_debug_counter = 0      # Debug print message counter
_startup_silent = True  # Silent phase during startup


def enable_debug() -> None:
    """
    Enables debug mode (silent during startup).
    """
    global _debug_enabled, _startup_silent
    _debug_enabled = True
    _startup_silent = True


def disable_debug() -> None:
    """
    Disables debug mode.
    """
    global _debug_enabled
    _debug_enabled = False


def end_startup_phase() -> None:
    """
    Ends startup phase and enables full debug output.
    """
    global _startup_silent
    _startup_silent = False


def is_debug_enabled() -> bool:
    """
    Returns True if debug mode is active.
    """
    return _debug_enabled


def reset_counter() -> None:
    """
    Resets the debug output counter.
    """
    global _debug_counter
    _debug_counter = 0


def get_counter() -> int:
    """
    Returns the current debug counter value.
    """
    return _debug_counter


def _get_next_counter() -> int:
    """
    Increments and returns the next debug counter value.
    """
    global _debug_counter
    _debug_counter += 1
    return _debug_counter


def _debug_print(emoji: str, prefix: str, message: str, *args: Any) -> None:
    """
    Prints a formatted debug message if debugging is enabled.
    """
    if not _debug_enabled:
        return
    if _startup_silent and prefix not in ("Startup", "Libc"):
        return

    counter = _get_next_counter()
    formatted_msg = message % args if args else message
    print(f"\033[37m[{counter:2d}] {emoji} {prefix}: {formatted_msg}\033[0m")


def reset_counter_after(func: F) -> F:
    """
    Decorator: resets debug counter after the function call.
    """
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return func(*args, **kwargs)
        finally:
            reset_counter()
    return wrapper  # type: ignore[return-value]
