"""
inspector.trace.printer

Provides colorized stderr output for trace logs, removing nested ANSI escapes for safety.
"""

import re
import sys


ANSI_ESCAPE = re.compile(r"\033\[[0-9;]*m")


def tprint(msg: str) -> None:
    """
    Print a trace message to stderr in purple, stripping conflicting ANSI escape sequences.

    Args:
        msg (str): The message to display (may contain color codes).
    """
    safe_msg = ANSI_ESCAPE.sub("", msg)  # Strip potential nested color codes
    sys.stderr.write(f"\033[35m{safe_msg}\033[0m\n")
