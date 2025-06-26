"""
libc.write

A unified output backend for low-level write operations, serving as the syscall layer
beneath higher-level modules like `libc.printf`.

Function overview:
- write(fd, msg, buffered=False):    Write a string to the given file descriptor (e.g. STDOUT)
- flush(fd):                         Flush the buffered output (relevant only if buffering is enabled)
- write_bytes(fd, data):             Write raw bytes directly to a file descriptor
- write_cstr(fd, ptr):               Write a C-style null-terminated string from a ctypes pointer

Design Notes:
- Wraps native syscall-level `write` functions from the underlying system
- Supports both unbuffered and buffered execution paths
- Uses `strlen()` internally for handling C-style strings (via syslib)

Internal helpers:
- _write(), _bwrite(), _bflush(): syscall logic separated by buffering strategy
- _encode(): UTF-8 string to (bytes, len) tuple for transmission

Examples:
    write(1, "Hello, world!")              → Writes to STDOUT (fd=1)
    flush(1)                               → Flushes buffer for STDOUT
    write_bytes(2, b"ERR\\n")              → Writes directly to STDERR
    write_cstr(1, ctypes.c_char_p(b"ok"))  → Writes null-terminated C string
"""

import ctypes

from shellkit.inspector.trace import trace_call
from shellkit.syscall import _get_lib

from .constants import STDERR, STDIN, STDOUT
from .internal import _bflush, _bwrite, _write
from .utils import strlen


__all__ = [
    # Standard file descriptors
    "STDIN", "STDOUT", "STDERR",

    # Core write and flush interfaces
    "write", "flush",

    # Raw bytes and C-style string writers
    "write_bytes", "write_cstr",
]


@trace_call("libc.write.__init__")
def write(fd: int, message: str, buffered: bool = False) -> int:
    """
    write(fd, message, buffered=False)
    - High-level wrapper for writing string output.
    - If buffered is True, the output is written through an internal buffer.
    """
    lib = _get_lib()
    return _bwrite(lib, fd, message) if buffered else _write(lib, fd, message)


def flush(fd: int) -> None:
    """
    flush(fd)
    - Flushes the output buffer for the specified file descriptor.
    - Has no effect if the output was not buffered.
    """
    lib = _get_lib()
    _bflush(lib, fd)


def write_bytes(fd: int, data: bytes, buffered: bool = False) -> int:
    """
    write_bytes(fd, data, buffered=False)
    - Low-level interface to write raw bytes.
    - Accepts a bytes object without performing any encoding.
    """
    lib = _get_lib()
    data_len = len(data)
    c_data = ctypes.c_char_p(data)
    return int(
        lib.buffered_syscall_write(fd, c_data, data_len)
        if buffered
        else lib.syscall_write(fd, c_data, data_len)
    )


def write_cstr(fd: int, c_str: ctypes.c_char_p) -> int:
    """
    write_cstr(fd, c_str)
    - Writes a C-style null-terminated string (char*) to the given file descriptor.
    - Uses strlen(c_str) to determine the length. Output is truncated at the first null byte.

    Example:
        c_str = ctypes.c_char_p(b"hello\\0world")
        write_cstr(1, c_str)  # Output: hello

    Note:
        The built-in len() function does not work on c_char_p in Python.
    """
    lib = _get_lib()
    data_len = strlen(c_str)
    return lib.syscall_write(fd, c_str, data_len)
