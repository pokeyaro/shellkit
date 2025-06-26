"""
libc.write.internal

Low-level write backend module.
Directly calls native syscall_write and buffered_syscall_write functions.
"""

from typing import Any

from shellkit.inspector.trace import trace_call

from .utils import _encode


@trace_call("libc.write.internal")
def _write(lib: Any, fd: int, message: str) -> int:
    """
    Performs an unbuffered write using the raw syscall.

    Args:
        lib: Low-level syscall provider object
        fd: File descriptor to write to
        message: String message to write (will be encoded)

    Returns:
        Number of bytes written
    """
    encoded_data, data_len = _encode(message)
    return int(lib.syscall_write(fd, encoded_data, data_len))


def _bwrite(lib: Any, fd: int, message: str) -> int:
    """
    Performs a buffered write; content goes through an internal buffer.

    Args:
        lib: Low-level syscall provider object
        fd: File descriptor to write to
        message: String message to write (will be encoded)

    Returns:
        Number of bytes buffered for writing
    """
    encoded_data, data_len = _encode(message)
    return int(lib.buffered_syscall_write(fd, encoded_data, data_len))


def _bflush(lib: Any, fd: int) -> None:
    """
    Flushes the internal buffer for a given file descriptor.

    Args:
        lib: Low-level syscall provider object
        fd: File descriptor whose buffer should be flushed
    """
    lib.buffered_syscall_flush(fd)
