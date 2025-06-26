"""
inspector.trace.format

Formats function arguments and return values for trace logs.
"""

from typing import Any


def format_args(args: tuple[Any, ...], kwargs: dict[str, Any]) -> str:
    """
    Format function arguments into a compact string for trace display.

    Args:
        args (tuple): Positional arguments passed to the function.
        kwargs (dict): Keyword arguments passed to the function.

    Returns:
        str: A concise formatted string of args and kwargs.
    """
    arg_strs = []

    # Handle first 3 positional args (avoid overflowing trace lines)
    for arg in args[:3]:
        if isinstance(arg, str):
            truncated = repr(arg)[:30]  # Shorten long strings
            if len(repr(arg)) > 30:
                truncated = truncated[:-1] + "...'"
            arg_strs.append(truncated)
        elif isinstance(arg, (int, float, bool)):
            arg_strs.append(str(arg))
        else:
            arg_strs.append(f"<{type(arg).__name__}>")  # Fallback for complex types

    if len(args) > 3:
        arg_strs.append("...")  # Indicate truncated args

    # Handle up to 2 keyword args
    for k, v in list(kwargs.items())[:2]:
        if isinstance(v, str):
            truncated = repr(v)[:20]  # Shorten long strings
            if len(repr(v)) > 20:
                truncated = truncated[:-1] + "...'"
            arg_strs.append(f"{k}={truncated}")
        else:
            arg_strs.append(f"{k}={v}")

    if len(kwargs) > 2:
        arg_strs.append("...")  # Indicate truncated kwargs

    return ", ".join(arg_strs)


def format_result(result: Any) -> str:
    """
    Format a function return value into a readable string for trace output.

    Args:
        result (Any): The return value from the traced function.

    Returns:
        str: A human-readable summary of the result.
    """
    if result is None:
        return "None"  # Explicitly mark None

    elif isinstance(result, int) and 0 < result < 10000:
        return f"{result} bytes"  # Small integers shown as byte size

    elif isinstance(result, str):
        # Truncate long strings to avoid log overflow
        truncated = repr(result)[:30]
        if len(repr(result)) > 30:
            truncated = truncated[:-1] + "...'"
        return truncated

    elif isinstance(result, bool):
        return str(result)  # Print True/False as-is

    else:
        # Fallback: show type name for complex/unprintable objects
        return f"<{type(result).__name__}>"
