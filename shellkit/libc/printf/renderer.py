"""
libc.printf.renderer

Handles rendering of a FormatSpec with its corresponding argument into a final string.

Supports:
- '#' flag for base-prefixed formatting (%#x, %#b, %#o)
- Precision control for floating-point values (e.g., %.2f)
"""

from typing import Any

from .types import FormatFlag, FormatSpecKind


def _handle_format(
    spec: FormatSpecKind,
    args: tuple[Any, ...],
    index: int,
    flags: set[FormatFlag],
    precision: int | None = None,
) -> str:
    """
    Renders a formatted fragment based on the spec and argument.

    Args:
        spec: Parsed format specifier (e.g., %s, %d)
        args: Tuple of arguments
        index: Index of the current argument to consume
        flags: Set of modifier flags (e.g., FormatFlag.HASH)
        precision: Precision value for float formatting (if applicable)

    Returns:
        Rendered string fragment
    """
    val = args[index] if spec != FormatSpecKind.PERCENT else None

    # noinspection PyUnreachableCode
    match spec:
        case FormatSpecKind.S:
            return str(val)
        case FormatSpecKind.D:
            return str(int(val))  # type: ignore[arg-type]
        case FormatSpecKind.X:
            v = hex(int(val))  # type: ignore[arg-type]
            return v if "#" in flags else v[2:]
        case FormatSpecKind.XX:
            v = hex(int(val))[2:].upper()  # type: ignore[arg-type]
            return "0X" + v if "#" in flags else v
        case FormatSpecKind.F:
            p = precision if precision is not None else 6
            return f"{float(val):.{p}f}"  # type: ignore[arg-type]
        case FormatSpecKind.C:
            return chr(int(val))  # type: ignore[arg-type]
        case FormatSpecKind.B:
            v = bin(int(val))  # type: ignore[arg-type]
            return v if "#" in flags else v[2:]
        case FormatSpecKind.O:
            v = oct(int(val))  # type: ignore[arg-type]
            return v if "#" in flags else v[2:]
        case FormatSpecKind.PERCENT:
            return "%"
        case _:
            spec_str = str(spec.value) if spec.value is not None else "?"
            return "%" + spec_str
