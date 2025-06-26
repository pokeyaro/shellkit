"""
inspector.trace.decorator

Provides the @trace_call decorator to log function entry/exit during debugging.
"""

import functools
from typing import Any, Callable, Optional, TypeVar

from .context import is_call_trace_allowed
from .core import enter_function, exit_function, is_trace_enabled


F = TypeVar('F', bound=Callable[..., Any])


def trace_call(module_name: Optional[str] = None) -> Callable[[F], F]:
    """
    Decorator to trace function entry and exit for debugging purposes.

    Args:
        module_name (str, optional): Override for module name in trace output.
                                     Defaults to the function's __module__.

    Returns:
        Callable: A wrapped function with trace logging enabled (if tracing active).
    """
    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Skip tracing if globally disabled or not inside `with tracing():`
            if not is_trace_enabled() or not is_call_trace_allowed():
                return func(*args, **kwargs)

            # Determine which module name to display
            mod_name = module_name or str(getattr(func, "__module__", "unknown"))
            func_name = func.__name__

            # Log entry
            enter_function(mod_name, func_name, args, kwargs)

            try:
                result = func(*args, **kwargs)
                exit_function(result)  # Log exit with return value
                return result
            except Exception as e:
                exit_function(None, exception=e)  # Log exit with exception
                raise

        return wrapper  # type: ignore[return-value]

    return decorator
