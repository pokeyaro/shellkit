"""
syscall module: native syscall bridge layer for Python.

Bridges Python to native .so system calls such as:
- syscall_write()
- buffered_syscall_write()
- syscall_exit()

Note:
This module does not expose public APIs directly.
Use higher-level wrappers from the `libc/` package.
"""

from .bindings import _get_lib


__all__ = ["_get_lib"]
