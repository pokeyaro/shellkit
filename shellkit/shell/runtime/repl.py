"""
runtime/repl.py

Implements the main interactive REPL loop for PySH.
"""

from shellkit.i18n import t
from shellkit.inspector.debug import debug_repl
from shellkit.shell.engine import handle_line

from .input import read_user_input


def start_repl() -> None:
    """
    Main interactive loop.
    Reads and executes user commands line by line, skipping empty input.
    """
    debug_repl(t("shell.runtime.repl.loop_start"))
    command_count = 0

    while True:
        cmd = read_user_input()

        if not cmd.strip():
            continue

        command_count += 1
        debug_repl(t("shell.runtime.repl.command_received", {"n": command_count, "cmd": cmd.strip()}))

        handle_line(cmd)
