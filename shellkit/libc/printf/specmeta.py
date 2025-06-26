"""
libc.printf.specmeta

Defines static rules for format specifiers, including which flags are allowed,
which specifiers consume arguments, and other format metadata.
"""

from .types import FormatFlag, FormatSpecKind


# Allowed flags (currently only '#')
ALLOWED_FLAGS = {FormatFlag.HASH}

# Specifiers that support the '#' flag
ALLOWED_FLAG_HASH = {
    FormatSpecKind.X,
    FormatSpecKind.XX,
    FormatSpecKind.B,
    FormatSpecKind.O,
}

# Specifiers that consume an argument during formatting
CONSUME_SPECS = {
    FormatSpecKind.S,
    FormatSpecKind.D,
    FormatSpecKind.X,
    FormatSpecKind.XX,
    FormatSpecKind.F,
    FormatSpecKind.C,
    FormatSpecKind.B,
    FormatSpecKind.O,
}

# Format directive start character
FORMAT_START = "%"

# Precision control indicator (e.g., %.2f)
PRECISION_DOT = "."
