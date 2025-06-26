"""
libc.exit.internal

Wraps raw syscall_exit and provides flush_all() for stdout/stderr.
"""

from shellkit.libc.write import STDERR, STDOUT, flush
from shellkit.syscall import _get_lib


def _exit(code: int = 0) -> None:
    """
    Performs raw system-level exit without flushing or running hooks.

    Args:
        code: Exit code to return to the OS
    """
    lib = _get_lib()
    lib.syscall_exit(code)


def flush_all() -> None:
    """
    Flushes both STDOUT and STDERR buffers.

    This is typically used before exiting to ensure buffered output is written.
    """
    for fd in (STDOUT, STDERR):
        flush(fd)
