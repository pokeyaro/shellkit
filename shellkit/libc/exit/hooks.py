"""
libc.exit.hooks

Implements atexit-style behavior with reverse-order (LIFO) execution.
"""

from collections.abc import Callable

from shellkit.libc.printf import eprintln


_hooks: list[Callable[[], None]] = []


def register_exit_hook(func: Callable[[], None]) -> None:
    """
    Registers a function to be called at program exit.

    Args:
        func: A callable with no arguments, executed during exit
    """
    _hooks.append(func)


def run_exit_hooks() -> None:
    """
    Executes all registered exit hooks in reverse (LIFO) order.

    Any exceptions raised by hooks are caught and printed to STDERR.
    """
    for f in reversed(_hooks):
        try:
            f()
        except Exception as e:
            eprintln("exit hook error: %s", str(e))
