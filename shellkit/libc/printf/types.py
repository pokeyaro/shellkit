"""
libc.printf.types

Type definitions for format specifiers, flags, and parsed format metadata.
"""

from enum import Enum
from typing import NamedTuple, Optional, Set


# ruff: noqa: E741
class FormatSpecKind(str, Enum):
    """
    Enumeration of supported format specifiers.

    Includes common C-style specifiers: %s, %d, %x, etc.
    """
    S = "s"
    D = "d"
    X = "x"
    XX = "X"
    F = "f"
    C = "c"
    B = "b"
    O = "o"
    PERCENT = "%"
    UNKNOWN = "<?>"  # Placeholder for invalid or unrecognized format specifier


class FormatFlag(str, Enum):
    """
    Enumeration of supported format flags.

    Currently only supports '#' for base-prefixed formatting.
    """
    HASH = "#"
    # TODO: More flags can be added in the future
    # ZERO = "0"
    # PLUS = "+"
    # MINUS = "-"
    # SPACE = " "


class FormatSpec(NamedTuple):
    """
    Represents a parsed format specifier and associated metadata.

    Fields:
        valid: Whether the spec is valid
        flags: Set of FormatFlag (e.g., {'#'})
        precision: Optional precision value (for floats)
        spec: FormatSpecKind enum member
        consume: Whether this specifier consumes a value from argument list
        fallback: If invalid, literal fallback string to use
    """
    valid: bool
    flags: Set[FormatFlag]
    precision: Optional[int]
    spec: FormatSpecKind
    consume: bool
    fallback: Optional[str] = None
