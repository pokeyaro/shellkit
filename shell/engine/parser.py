"""
engine/parser.py

Parses user input into command name and argument list.
Supports special syntax like parentheses for selected built-ins
and escape aliases for debugging.
"""

import shlex


# Built-in commands that allow Python-style parentheses calls (e.g., exit())
BUILTINS_ALLOW_PARENS = {"help", "exit", "quit", "copyright", "license"}

# Special escape aliases for debugging commands (used as-is without parsing)
DEBUG_ESCAPE_ALIASES = [r"\q", r"\d", r"\dr", r"\ds", r"\doff", r"\d?"]


def parse_line(line: str) -> tuple[str, list[str]]:
    r"""
    Parses a line of user input into a command name and argument list.

    Examples:
        - Normal command:     "echo hello" → ("echo", ["hello"])
        - Parentheses form:   "exit()" or "exit ()" → ("exit", [])
        - Debug aliases:      "\d" → ("\d", [])
        - Comments:           "# comment" → ("", [])

    Args:
        line: Raw input string from the shell.

    Returns:
        A tuple of (command_name, argument_list). If parsing fails or empty,
        returns ("", []).
    """
    # Strip whitespace and check for comments
    line_stripped = line.strip()

    # If line is empty or starts with #, treat as comment/empty
    if not line_stripped or line_stripped.startswith('#'):
        return "", []

    # Handle escape aliases like \d or \q
    if line_stripped in DEBUG_ESCAPE_ALIASES:
        return line_stripped, []

    try:
        parts = shlex.split(line)
    except ValueError:
        return "", []

    if not parts:
        return "", []

    cmd = parts[0]
    args = parts[1:]

    # Case 1: Single token like "exit()"
    if len(parts) == 1 and cmd.endswith("()"):
        base = cmd[:-2]
        if base in BUILTINS_ALLOW_PARENS:
            cmd = base

    # Case 2: Split tokens like "exit ()"
    if len(parts) == 2 and parts[1] == "()" and parts[0] in BUILTINS_ALLOW_PARENS:
        args = []

    return cmd, args
