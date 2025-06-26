"""
inspector.trace.context

Provides the `tracing()` context manager to enable fine-grained trace logging.
"""

import contextvars
import inspect
from contextlib import contextmanager
from typing import Iterator

from .core import enter_function, flush_trace_log


# A context-local flag to indicate whether tracing is currently enabled
_trace_flag = contextvars.ContextVar("_trace_flag", default=False)


def is_call_trace_allowed() -> bool:
    """
    Check if tracing is currently allowed in this context.

    Returns:
        bool: True if tracing is active (inside `with tracing():`)
    """
    return _trace_flag.get()


@contextmanager
def tracing() -> Iterator[None]:
    """
    Enable tracing within this context block.

    Use this to activate @trace_call decorators for temporary sections of code.

    Example:
        with tracing():
            printf("hello")  # Will be traced
    """
    module, func = _find_user_function()
    enter_function(module, func, args=(), kwargs={})

    token = _trace_flag.set(True)
    try:
        yield
    finally:
        _trace_flag.reset(token)
        flush_trace_log()


def _find_user_function() -> tuple[str, str]:
    """
    Heuristically find the first non-internal function in the call stack.

    Returns:
        tuple[str, str]: (module_name, function_name) of the user-level call.
    """
    for frame_info in inspect.stack():
        module = frame_info.frame.f_globals.get("__name__", "")
        # Skip internal utility modules
        if not module.startswith("contextlib") and not module.startswith("inspect"):
            func = frame_info.function
            return module, func
    return "<unknown>", "<unknown>"
