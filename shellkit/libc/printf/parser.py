"""
libc.printf.parser

Parses formatting directives from format strings, including flags, precision, and specifier.
Builds a FormatSpec structure that describes each component.
"""

from .specmeta import ALLOWED_FLAGS, ALLOWED_FLAG_HASH, PRECISION_DOT
from .types import FormatFlag, FormatSpec, FormatSpecKind
from .utils import build_format_fallback, spec_consumes_argument


def _parse_format_spec(fmt: str, i: int) -> tuple[FormatSpec, int]:
    """
    Parses a format specifier starting at fmt[i] (after the initial '%').

    Returns a FormatSpec and the new position in the format string.

    Examples:
        %#x      → flags={'#'}, spec='x'
        %.2f     → precision=2, spec='f'
        %#.3X    → flags={'#'}, precision=3, spec='X'

    Unsupported:
        Width, alignment, or named fields are not yet supported.

    Args:
        fmt: The full format string to parse.
        i: The current parsing index (just after '%').

    Returns:
        A tuple of:
            - FormatSpec: The parsed spec object.
            - int: The next position to resume parsing.
    """
    start_i = i
    n = len(fmt)
    flags = set()

    # Parse flags (currently only '#' is supported; future expansion possible)
    while i < n and fmt[i] in {f.value for f in ALLOWED_FLAGS}:
        try:
            flags.add(FormatFlag(fmt[i]))
        except ValueError:
            # Should not occur due to prior filtering
            break
        i += 1

    # Parse precision, e.g., %.2f → precision = 2
    precision = None
    precision_digits = []
    if i < n and fmt[i] == PRECISION_DOT:
        i += 1
        while i < n and fmt[i].isdigit():
            precision_digits.append(fmt[i])
            i += 1
        # "%.f" = precision 0
        precision = int("".join(precision_digits)) if precision_digits else 0

    # Reached end with incomplete specifier (e.g., "%." or "%#")
    if i >= n:
        fallback = fmt[start_i - 1 :]
        return FormatSpec(False, flags, precision, FormatSpecKind.UNKNOWN, False, fallback), n

    # Try to interpret current character as a format specifier (e.g., 's', 'd', etc.)
    try:
        spec = FormatSpecKind(fmt[i])
    except ValueError:
        # Invalid specifier → fallback like "%!x"
        fallback = build_format_fallback(flags, precision_digits, fmt[i])
        return FormatSpec(False, flags, precision, FormatSpecKind.UNKNOWN, False, fallback), i + 1

    # Valid specifier, but with an unsupported flag combination (e.g., %#s is invalid)
    if FormatFlag.HASH in flags and spec not in ALLOWED_FLAG_HASH:
        fallback = build_format_fallback(flags, precision_digits, spec.value)
        return FormatSpec(False, flags, precision, spec, False, fallback), i + 1

    # Valid format spec, construct and return FormatSpec
    consume = spec_consumes_argument(spec)
    return FormatSpec(True, flags, precision, spec, consume, None), i + 1
