"""
engine/builtins/history.py

Implements the `history` shell command.
Displays the current session's interactive command history using `readline`.
"""

import readline

from shellkit.i18n import t
from shellkit.libc import eprintln, println
from shellkit.shell.state.exit_code import EXIT_FAILURE, EXIT_SUCCESS, EXIT_USAGE_ERROR, ExitCode


def history_builtin(args: list[str]) -> ExitCode:
    """
    Implements the `history` built-in command.

    Displays all commands entered in the current shell session.
    Requires the underlying `readline` module to access input history.

    Behavior:
        - Does not accept any arguments.
        - Prints each command with an auto-aligned index.
        - Handles internal safety checks for invalid entries.

    Args:
        args: Command-line arguments passed to `history`.

    Returns:
        ExitCode:
            - EXIT_SUCCESS (0) on success.
            - EXIT_FAILURE (1) on runtime error (e.g., readline failure).
            - EXIT_USAGE_ERROR (2) if arguments are provided.
    """
    if args:
        println(t("shell.engine.builtin.history.unexpected_args"))
        println(t("shell.engine.builtin.history.usage"))
        return EXIT_USAGE_ERROR

    try:
        # Get the total number of commands in history
        total = readline.get_current_history_length()

        # If no history is available, print a message
        if total == 0:
            println(t("shell.engine.builtin.history.empty"))
            return EXIT_SUCCESS

        # Calculate the width needed for right-aligned numbering
        width = len(str(total))

        # Iterate over all history entries and print them
        for i in range(1, total + 1):
            line = readline.get_history_item(i)
            if line:
                println(f"  {i:>{width}}  {line}")
            else:
                # Should not happen, but fallback in case of null entry
                println(f"  {i:>{width}}  (empty)")

        return EXIT_SUCCESS

    except Exception as e:
        eprintln(t("shell.engine.builtin.history.error_read") + ": %s", str(e))
        return EXIT_FAILURE
