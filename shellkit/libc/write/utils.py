"""
libc.write.utils

Utility functions for encoding strings and working with C-style pointers.
"""

import ctypes

from shellkit.syscall import _get_lib


def _encode(s: str) -> tuple[bytes, int]:
    """
    Encodes a string to UTF-8 bytes.

    Args:
        s: The input string

    Returns:
        A tuple containing the encoded bytes and their length
    """
    b = s.encode("utf-8")
    return b, len(b)


def strlen(ptr: ctypes.c_char_p) -> int:
    """
    Computes the length of a null-terminated C string.

    Args:
        ptr: A ctypes.c_char_p pointer to the C string

    Returns:
        The number of bytes before the first null terminator
    """
    return _get_lib().strlen(ptr)
