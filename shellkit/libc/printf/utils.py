"""
libc.printf.utils

Utility functions for parsing format specs, generating fallback strings,
and validating argument counts in formatted output.
"""

from .specmeta import CONSUME_SPECS, FORMAT_START, PRECISION_DOT
from .types import FormatFlag, FormatSpecKind


def spec_consumes_argument(spec: FormatSpecKind) -> bool:
    """
    Returns whether the given format specifier consumes one argument.

    Used for determining how many arguments are expected by a format string.
    """
    return spec in CONSUME_SPECS


def build_format_fallback(flags: set[FormatFlag], precision_digits: list[str], spec: str) -> str:
    """
    Constructs a fallback string for invalid or unsupported format specifiers.

    This is used when parsing fails due to unknown specifiers or invalid flag-spec combinations.
    The fallback preserves the original formatting intent in literal form.

    Example:
        flags = {'#'}, precision_digits = ['2'], spec = 'f'
        → "%#.2f"

    Args:
        flags: Set of FormatFlag (e.g., {FormatFlag.HASH})
        precision_digits: List of digit characters representing the precision (e.g., ['2'])
        spec: Final specifier character (e.g., 'f' or an unsupported one like 'q')

    Returns:
        A literal format string fallback starting with '%', such as "%#f" or "%q"
    """
    flag_str = "".join(sorted(flag.value for flag in flags))
    precision_str = PRECISION_DOT + "".join(precision_digits) if precision_digits else ""
    return FORMAT_START + flag_str + precision_str + spec


def check_argument_count(expected: int, actual: int) -> None:
    """
    Validates that the number of arguments matches the number of expected specifiers.

    Should be used in strict mode to enforce correctness of format usage.

    Args:
        expected: Number of arguments required by the format string.
        actual: Number of arguments actually provided.

    Raises:
        ValueError: If too many or too few arguments are passed.
    """
    if expected < actual:
        raise ValueError(f"Too many arguments: expected {expected}, got {actual}")
    elif expected > actual:
        raise ValueError(f"Too few arguments: expected {expected}, got {actual}")
