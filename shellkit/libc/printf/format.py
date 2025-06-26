"""
libc.printf.format

Formats a string with C-style specifiers and returns the final result.
"""

from typing import Any

from shellkit.inspector.trace import trace_call

from .parser import _parse_format_spec
from .renderer import _handle_format
from .specmeta import FORMAT_START
from .utils import check_argument_count


@trace_call("libc.printf.format")
def format_string(fmt: str, *args: Any, strict: bool = False) -> str:
    """
    A high-performance formatter for a subset of C-style specifiers:
    %s, %d, %x, %X, %f, %c, %b, %o, and %% (escaped percent sign).

    Supported Features:
        - '#' flag for base-prefixed output (e.g., %#x → 0x1f)
        - Precision control for floats (e.g., %.2f → 3.14)

    Limitations:
        - Width, alignment, and named arguments are not supported.

    Error Handling:
        - Default: falls back to a literal representation of invalid specifiers.
        - strict=True: raises ValueError on unknown or unsupported formats.

    Example:
        >>> format_string("pi = %.2f", 3.14159)
        'pi = 3.14'
    """
    parts: list[str] = []
    i = 0
    arg_index = 0

    while i < len(fmt):
        if fmt[i] == FORMAT_START:
            spec_info, i = _parse_format_spec(fmt, i + 1)

            if spec_info.valid:
                parts.append(
                    _handle_format(
                        spec_info.spec, args, arg_index, spec_info.flags, spec_info.precision
                    )
                )
                if spec_info.consume:
                    arg_index += 1
            else:
                if strict:
                    raise ValueError(f"Invalid format spec: {spec_info.fallback}")
                fallback = spec_info.fallback or ""
                parts.append(fallback)
        else:
            parts.append(fmt[i])
            i += 1

    if strict:
        check_argument_count(arg_index, len(args))

    return "".join(parts)
