"""
engine/builtins/clear.py

Implements the `clear` shell command.
Sends ANSI escape sequences to clear the terminal screen.
"""

from shellkit.i18n import t
from shellkit.libc import println, STDOUT, write
from shellkit.shell.state.exit_code import EXIT_SUCCESS, EXIT_USAGE_ERROR, ExitCode


def clear_builtin(args: list[str]) -> ExitCode:
    """
    Implements the `clear` built-in command.

    Clears the terminal screen using ANSI escape sequences.
    This command does not accept any arguments.

    Args:
        args: Command-line arguments (should be empty).

    Returns:
        ExitCode:
            - EXIT_SUCCESS (0) on success.
            - EXIT_USAGE_ERROR (2) if arguments are provided.
    """
    if args:
        println(t("shell.engine.builtin.clear.unexpected_args"))
        return EXIT_USAGE_ERROR

    # Clear screen and move cursor to top-left
    write(STDOUT, "\033[2J\033[H")
    return EXIT_SUCCESS
