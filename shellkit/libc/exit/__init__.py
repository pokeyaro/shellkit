"""
libc.exit

A unified exit control module for system-level programs, wrapping standard exit behaviors
with support for atexit-style hook registration, buffer flushing, and graceful shutdown flows.

Function overview:
- exit(code):            Graceful exit — runs registered hooks, flushes buffers, then calls _exit
- _exit(code):           Raw exit — directly invokes syscall_exit without flushing or hooks
- atexit(func):          Registers a user-defined exit hook (LIFO order)
- graceful_exit(...):    High-level wrapper for structured exits with optional hooks and messages

Design Notes:
- hooks.py:     Manages a stack of user-defined exit hooks and provides hook execution logic
- internal.py:  Wraps low-level syscall_exit and implements flush_all()
- __init__.py:  Acts as the public interface, orchestrating graceful and raw exits

Examples:
    atexit(lambda: println("Goodbye"))      → Registers a hook to run before exit
    graceful_exit(1, message="Exiting...")  → Prints message and exits with code 1
    exit(0)                                 → Executes all hooks, flushes, and exits
"""

from collections.abc import Callable
from typing import Optional

from shellkit.libc.printf import println

from .hooks import register_exit_hook, run_exit_hooks
from .internal import _exit, flush_all


__all__ = [
    "_exit",
    "exit", "atexit",
    "graceful_exit",
]


def exit(code: int = 0) -> None:
    """
    Performs a graceful exit: runs registered hooks, flushes buffers, then exits.

    Args:
        code: Exit code (default: 0)
    """
    run_exit_hooks()
    flush_all()
    _exit(code)


def atexit(func: Callable[[], None]) -> None:
    """
    Registers a function to be called on program exit (LIFO order).

    Args:
        func: Callable with no arguments, executed during exit
    """
    register_exit_hook(func)


def graceful_exit(
    code: int = 0,
    *,
    flush: bool = True,
    exit_hooks: Optional[list[Callable[[], None]]] = None,
    message: str | None = None,
) -> None:
    """
    High-level exit routine with optional hooks, flushing, and message display.

    Args:
        code: Exit code to return (default: 0)
        flush: Whether to flush stdout/stderr before exit
        exit_hooks: Optional list of hook functions to register before exit
        message: Optional message to display before exiting

    Returns:
        None
    """
    _hooks = list(exit_hooks or [])

    # If message is provided, append a hook that prints it
    if message:
        _hooks.append(lambda: println(message) or None)  # type: ignore[arg-type]

    # Register all provided exit_hooks
    for h in _hooks:
        atexit(h)

    # Optionally flush stdout/stderr
    if flush:
        flush_all()

    # Perform graceful exit (runs hooks, flushes again, calls _exit)
    exit(code)
