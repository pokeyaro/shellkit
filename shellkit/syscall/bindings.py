"""
syscall.bindings

ctypes bridge to syslib.so
"""

import ctypes
import importlib.resources
from pathlib import Path


# Global: CDLL instance cache
_lib = None


# Load and bind native functions
def _get_lib() -> ctypes.CDLL:
    """
    Load and bind native functions from syslib.so.

    Exposed native symbols:
        - syscall_write(int fd, const char *buf, size_t count) -> ssize_t
        - buffered_syscall_write(int fd, const char *buf, size_t count) -> ssize_t
        - buffered_syscall_flush(int fd) -> void
        - syscall_exit(int code) -> void
        - strlen(const char *s) -> size_t
    """
    global _lib

    if _lib is None:
        # Dynamically locate the .so file
        so_path = _find_syslib_path()
        _lib = ctypes.CDLL(str(so_path))

        # ssize_t syscall_write(int fd, const char *buf, size_t count);
        _lib.syscall_write.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_size_t]
        _lib.syscall_write.restype = ctypes.c_ssize_t

        # ssize_t buffered_syscall_write(int fd, const char *buf, size_t count);
        _lib.buffered_syscall_write.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_size_t]
        _lib.buffered_syscall_write.restype = ctypes.c_ssize_t

        # void buffered_syscall_flush(int fd);
        _lib.buffered_syscall_flush.argtypes = [ctypes.c_int]
        _lib.buffered_syscall_flush.restype = None

        # void syscall_exit(int code);
        _lib.syscall_exit.argtypes = [ctypes.c_int]
        _lib.syscall_exit.restype = None

        # size_t strlen(const char* s);
        _lib.strlen.argtypes = [ctypes.c_char_p]
        _lib.strlen.restype = ctypes.c_size_t

    return _lib


def _find_syslib_path() -> Path:
    """
    Dynamically locate the syslib shared library file.
    """
    # Get the path to the syscall package
    with importlib.resources.path("shellkit.syscall", "__init__.py") as init_path:
        syscall_dir = init_path.parent

    # Try multiple possible filename patterns
    patterns = [
        "syslib.so",                        # Simple name
        "syslib.*.so",                      # Wildcard match
        "syslib.cpython-*-*-linux-gnu.so",  # Linux
        "syslib.cpython-*-*-darwin.so",     # macOS
    ]

    for pattern in patterns:
        matches = list(syscall_dir.glob(pattern))
        if matches:
            return matches[0]

    raise FileNotFoundError(f"Could not find syslib shared library in {syscall_dir}")
