"""
engine/text_processing.py

Shell text processing module:
Provides variable expansion, escape sequence processing, and unified shell-style formatting support.
"""

import re
from typing import Callable, Optional

from shellkit.shell.environs import get_env


# Variable expansion pattern
VAR_PATTERN = re.compile(
    r"""
    (?<!\\)\$                    # $ is not escaped
    (
        [a-zA-Z_]\w*             # normal variable names: USER, HOME, etc.
        |                        # or
        [?$#0-9@*!]              # special symbols: ?, $, #, digits, @, *, !
    )
    |                            # or
    (?<!\\)\$\{([^}]+)\}         # ${VAR} format
""",
    re.VERBOSE,
)


def expand_variables(text: str, get_env_func: Callable[[str], Optional[str]]) -> str:
    """
    Expands variables in a string, while preserving escaped ones.

    Args:
        text: The input string to process.
        get_env_func: A callable that retrieves environment variable values.

    Returns:
        The text after expanding all variables.
    """
    def replacer(match: re.Match[str]) -> str:
        var_name = match.group(1) or match.group(2)
        val = get_env_func(var_name)
        return str(val) if val is not None else ""

    return VAR_PATTERN.sub(replacer, text)


def unescape_variables(text: str) -> str:
    r"""
    Restores escaped variables for correct visual display.
    \$VAR → $VAR
    \${VAR} → ${VAR}
    """
    return text.replace(r"\$", "$").replace(r"\${", "${")


def process_escapes(s: str) -> str:
    r"""
    Processes escape sequences in a string.
    \n → newline, \t → tab, etc.
    """
    # Handle \\ first to avoid re-processing escaped backslashes
    s = s.replace("\\\\", "\x00")  # temporary placeholder

    escape_map = {
        "\\n": "\n",  # newline
        "\\t": "\t",  # tab
        "\\r": "\r",  # carriage return
        "\\b": "\b",  # backspace
        "\\f": "\f",  # form feed
        "\\v": "\v",  # vertical tab
        "\\a": "\a",  # bell
        "\\0": "\0",  # null byte
        '\\"': '"',   # double quote
        "\\'": "'",   # single quote
        "\\?": "?",   # literal question mark
    }

    for escape, char in escape_map.items():
        s = s.replace(escape, char)

    # Handle octal escape: \ooo → char
    def replace_octal(match: re.Match[str]) -> str:
        octal_str = match.group(1)
        try:
            code = int(octal_str, 8)
            if code <= 255:
                return chr(code)
        except (ValueError, OverflowError):
            pass
        return match.group(0)

    s = re.sub(r"\\([0-7]{1,3})", replace_octal, s)

    # Handle hex escape: \xhh → char
    def replace_hex(match: re.Match[str]) -> str:
        hex_str = match.group(1)
        try:
            code = int(hex_str, 16)
            if code <= 255:
                return chr(code)
        except (ValueError, OverflowError):
            pass
        return match.group(0)

    s = re.sub(r"\\x([0-9a-fA-F]{1,2})", replace_hex, s)

    # Handle unicode escape: \uxxxx → char
    def replace_unicode4(match: re.Match[str]) -> str:
        hex_str = match.group(1)
        try:
            code = int(hex_str, 16)
            return chr(code)
        except (ValueError, OverflowError):
            pass
        return match.group(0)

    s = re.sub(r"\\u([0-9a-fA-F]{4})", replace_unicode4, s)

    # Handle extended unicode escape: \Uxxxxxxxx
    def replace_unicode8(match: re.Match[str]) -> str:
        hex_str = match.group(1)
        try:
            code = int(hex_str, 16)
            if code <= 0x10FFFF:  # Unicode 最大值
                return chr(code)
        except (ValueError, OverflowError):
            pass
        return match.group(0)

    s = re.sub(r"\\U([0-9a-fA-F]{8})", replace_unicode8, s)

    # Restore actual backslashes
    s = s.replace("\x00", "\\")

    return s


def default_env_adapter(var_name: str) -> Optional[str]:
    """
    Default environment adapter for variable resolution.
    """
    result = get_env(var_name)
    if result is None:
        return None
    return str(result)


def process_shell_text(
    text: str,
    get_env_func: Optional[Callable[[str], Optional[str]]] = None,
    expand_vars: bool = True,
    process_escape: bool = True,
) -> str:
    """
    Composite processing function for shell text:
    performs variable expansion and escape sequence resolution.

    Args:
        text: The raw input text.
        get_env_func: Optional environment variable fetcher.
        expand_vars: Whether to expand variables.
        process_escape: Whether to handle escape sequences.

    Returns:
        The processed string.
    """
    if get_env_func is None:
        get_env_func = default_env_adapter

    result = text

    if expand_vars:
        result = expand_variables(result, get_env_func)
        result = unescape_variables(result)

    if process_escape:
        result = process_escapes(result)

    return result
