"""
libc.printf

A collection of printf-style functions that emulate output behaviors found in C, Go, Rust, and Python.

Supports basic formatting syntax (%s, %d, %f, etc.), base notation flags (%#x), precision control (%.2f), and more.

Function overview:
- sprintf(fmt, ...):     Format only (C/Go-style), no output
- format(fmt, ...):      Format only (Python-style), no output
- printf(fmt, ...):      Write formatted string to STDOUT, no newline (C/Go-style)
- println(fmt, ...):     Write formatted string to STDOUT with newline (Rust-style)
- bprintf(fmt, ...):     Buffered write to STDOUT, no newline
- bprintln(fmt, ...):    Buffered write to STDOUT with newline
- eprintf(fmt, ...):     Write to STDERR, no newline
- eprintln(fmt, ...):    Write to STDERR with newline
- print(...):            Python-like print with sep / end / buffered / flush support
- fmt_println(...):      Go-style print with space-separated arguments and newline
- Println(...):          Alias for fmt_println

Design Notes:
- Implements a unified formatting backend to simulate low-level output across languages
- Supports both buffered and unbuffered writes via libc.write
- Internal helpers _formatted_str(), _formatted_write(), and _formatted_line()
  unify formatting and output dispatch logic
- Allows consistent system-call-based emulation of common output APIs

Examples:
    printf("Hello %s", "world")        → Hello world
    println("pi = %.2f", 3.14159)      → pi = 3.14\n
    bprintln("loading %d%%", 42)       → buffered write (requires manual flush)
    eprintln("error: %d", 404)         → error: 404\n (to stderr)
    print("a", "b", sep="-", end="!")  → a-b!
"""

from typing import Any

from shellkit.inspector.trace import trace_call
from shellkit.libc.write import STDERR, STDOUT

from .internal import _formatted_line, _formatted_str, _formatted_write


__all__ = [
    # Formatting-only functions
    "sprintf", "format",

    # Standard output
    "printf", "println",

    # Buffered standard output
    "bprintf", "bprintln",

    # Standard error output
    "eprintf", "eprintln",

    # Python-style print
    "print",

    # Go-style aliases
    "fmt_println", "Println",
]


# ===== Formatting-only =====


def sprintf(fmt: str, *args: Any) -> str:
    """
    sprintf(fmt, *args)

    Args:
        fmt: Format string (e.g., "name: %s")
        *args: Arguments to be formatted

    Returns:
        Formatted string (not printed or written)
    """
    return _formatted_str(fmt, *args, strict=False)


def format(fmt: str, *args: Any, strict: bool = False) -> str:
    """
    format(fmt, *args, strict=False)

    Args:
        fmt: Format string (supports %s, %d, %f, etc.)
        *args: Substitution arguments
        strict: If True, raises error on argument mismatch

    Returns:
        Formatted string
    """
    return _formatted_str(fmt, *args, strict=strict)


# ===== Standard output =====


@trace_call("libc.printf.__init__")
def printf(fmt: str, *args: Any) -> int:
    """
    printf(fmt, *args)

    Args:
        fmt: Format string
        *args: Substitution arguments

    Returns:
        Number of bytes written to STDOUT (no newline)
    """
    return _formatted_write(STDOUT, fmt, args, newline=False)


def println(fmt: str, *args: Any) -> int:
    """
    println(fmt, *args)

    Args:
        fmt: Format string
        *args: Substitution arguments

    Returns:
        Number of bytes written to STDOUT (with newline)
    """
    return _formatted_write(STDOUT, fmt, args, newline=True)


# ===== Buffered standard output =====


def bprintf(fmt: str, *args: Any) -> int:
    """
    bprintf(fmt, *args)

    Args:
        fmt: Format string
        *args: Substitution arguments

    Returns:
        Number of bytes written to STDOUT (buffered, no newline)
    """
    return _formatted_write(STDOUT, fmt, args, newline=False, buffered=True)


def bprintln(fmt: str, *args: Any) -> int:
    """
    bprintln(fmt, *args)

    Args:
        fmt: Format string
        *args: Substitution arguments

    Returns:
        Number of bytes written to STDOUT (buffered, with newline)
    """
    return _formatted_write(STDOUT, fmt, args, newline=True, buffered=True)


# ===== Standard error output =====


def eprintf(fmt: str, *args: Any) -> int:
    """
    eprintf(fmt, *args)

    Args:
        fmt: Format string
        *args: Substitution arguments

    Returns:
        Number of bytes written to STDERR (no newline)
    """
    return _formatted_write(STDERR, fmt, args, newline=False)


def eprintln(fmt: str, *args: Any) -> int:
    """
    eprintln(fmt, *args)

    Args:
        fmt: Format string
        *args: Substitution arguments

    Returns:
        Number of bytes written to STDERR (with newline)
    """
    return _formatted_write(STDERR, fmt, args, newline=True)


# ===== Python-style output =====


@trace_call("libc.printf.__init__")
def print(
    *args: Any,
    sep: str = " ",
    end: str = "\n",
    buffered: bool = False,
    flush: bool = False
) -> int:
    """
    print(*args, sep=" ", end="\\n", buffered=False, flush=False)

    Args:
        *args: Items to print
        sep: Separator inserted between items
        end: String appended after the last item
        buffered: If True, enables buffered write
        flush: If True, flushes after writing

    Returns:
        Number of bytes written to STDOUT
    """
    s = sep.join(str(arg) for arg in args) + end
    return _formatted_line(STDOUT, s, auto_wrap=False, buffered=buffered, flush=flush)


# ===== Go-style output =====


def fmt_println(*args: str) -> int:
    """
    fmt_println(*args)

    Args:
        *args: Strings to join with space and print

    Returns:
        Number of bytes written to STDOUT (with newline)
    """
    s = " ".join(args)
    return _formatted_line(STDOUT, s, auto_wrap=True)


# Alias for Go-style println
Println = fmt_println
