"""
inspector.trace.core

Central control module for call tracing, managing stack depth and log buffering.
"""

from typing import Any, Optional

from .format import format_args, format_result
from .printer import tprint
from .tree import get_tree_prefix


_trace_enabled = False                  # Whether tracing is currently active
_call_stack: list[dict[str, Any]] = []  # Stack to track nested call depth
_trace_log_buffer: list[str] = []       # Buffered trace output lines


def enable_trace() -> None:
    """
    Activate tracing globally.
    """
    global _trace_enabled
    _trace_enabled = True


def disable_trace() -> None:
    """
    Disable tracing and clear trace state.
    """
    global _trace_enabled
    _trace_enabled = False
    reset_trace_state()


def is_trace_enabled() -> bool:
    """
    Check if tracing is currently enabled.

    Returns:
        bool: True if tracing is active.
    """
    return _trace_enabled


def tlog(msg: str) -> None:
    """
    Append a trace message to the log buffer if tracing is active.

    Args:
        msg (str): A single trace log line (with ANSI formatting).
    """
    if _trace_enabled:
        _trace_log_buffer.append(msg)


def enter_function(
    module_name: str,
    func_name: str,
    args: tuple[Any, ...],
    kwargs: dict[str, Any],
) -> None:
    """
    Log function entry, including module, name, and formatted args.

    Args:
        module_name (str): The name of the module.
        func_name (str): The name of the function.
        args (tuple): Positional arguments.
        kwargs (dict): Keyword arguments.
    """
    depth = len(_call_stack)
    prefix = get_tree_prefix(depth, is_entering=True)
    args_str = format_args(args, kwargs)
    tlog(f"\033[90m{prefix}{module_name}::{func_name}({args_str})\033[0m")

    _call_stack.append({
        "module": module_name,
        "function": func_name,
        "depth": depth
    })


def exit_function(result: Any = None, exception: Optional[Exception] = None) -> None:
    """
    Log function exit, including result or exception.

    Args:
        result (Any): Return value of the function.
        exception (Exception, optional): Exception if the function raised.
    """
    from shellkit.i18n import t

    if not _call_stack:
        return

    call_info = _call_stack.pop()
    depth = call_info["depth"]
    prefix = get_tree_prefix(depth, is_entering=False)

    if exception:
        tlog(f"\033[91m{prefix}Exception: {exception}\033[0m")
    else:
        tlog(f"\033[90m{prefix}{t('inspector.trace.core.return_tag')}: {format_result(result)}\033[0m")


def flush_trace_log() -> None:
    """
    Print the full trace buffer in order and reset state.
    """
    from shellkit.i18n import t

    if not _trace_enabled or not _trace_log_buffer:
        return

    for line in _trace_log_buffer:
        tprint(line)

    tprint(f"└─ {t('inspector.trace.core.return_tag')}: ExitCode")  # Final stub line for clarity

    reset_trace_state()


def reset_trace_state() -> None:
    """
    Clear all trace state: call stack and log buffer.
    """
    _call_stack.clear()
    _trace_log_buffer.clear()
