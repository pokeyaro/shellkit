"""
libc.printf.internal

Low-level format-to-fd output utilities for printf.
"""

from typing import Any

from shellkit.inspector.trace import trace_call
from shellkit.libc.write import write, flush as flush_fd

from .format import format_string


def _formatted_str(fmt: str, *args: Any, strict: bool = False) -> str:
    """
    Formats a string using printf-style specifiers without writing it.

    Args:
        fmt: Format string (e.g., "value = %#x")
        *args: Positional arguments to format into the string
        strict: If True, enforces strict argument count checking

    Returns:
        Formatted string result
    """
    safe_args = args or ()
    return format_string(fmt, *safe_args, strict)


@trace_call("libc.printf.internal")
def _formatted_write(
    fd: int, fmt: str, args: tuple[Any, ...], newline: bool = False, buffered: bool = False
) -> int:
    """
    Formats a string and writes it to the specified file descriptor.

    Args:
        fd: Target file descriptor (e.g., 1 for STDOUT)
        fmt: Format string using C-style specifiers
        args: Arguments to format (passed as a tuple)
        newline: If True, appends a newline character
        buffered: If True, uses buffered output

    Returns:
        Number of bytes written to the descriptor
    """
    safe_args = args or ()
    s = format_string(fmt, *safe_args)
    if newline:
        s += "\n"
    return write(fd, s, buffered=buffered)


@trace_call("libc.printf.internal")
def _formatted_line(
    fd: int, s: str, auto_wrap: bool = False, buffered: bool = False, flush: bool = False
) -> int:
    """
    Writes a plain string to the given file descriptor using "%s" formatting.

    Args:
        fd: File descriptor to write to
        s: The string content
        auto_wrap: If True, appends a newline
        buffered: Whether to buffer the output
        flush: If True, flushes after writing

    Returns:
        Number of bytes written
    """
    written = _formatted_write(fd, "%s", (s,) or (), newline=auto_wrap, buffered=buffered)

    if flush:
        flush_fd(fd)

    return written
