"""
engine/builtins/exit.py

Implements the `exit` shell command.
Parses optional exit code and terminates the shell process cleanly.
"""

from shellkit.i18n import t
from shellkit.inspector.debug import debug_exit
from shellkit.libc import eprintln, exit, println
from shellkit.shell.state.exit_code import EXIT_SUCCESS, EXIT_USAGE_ERROR, ExitCode


def exit_builtin(args: list[str]) -> ExitCode:
    """
    Implements the `exit` built-in command.

    Terminates the shell process, optionally with a user-defined exit code.

    Behavior:
        - Accepts an optional integer argument between 0 and 255.
        - Defaults to 0 if no argument is provided.
        - Performs validation and exits the process immediately.
        - Triggers debug_exit() for logging purposes before exit().

    Args:
        args: A list containing at most one string argument (the exit code).

    Returns:
        ExitCode:
            - EXIT_USAGE_ERROR (2) if input is invalid.
            - EXIT_SUCCESS (0) only for type checker; never actually reached.
    """
    # Validate number of arguments
    if len(args) > 1:
        println(t("shell.engine.builtin.exit.too_many_args"))
        println(t("shell.engine.builtin.exit.usage"))
        return EXIT_USAGE_ERROR

    # Parse exit code
    if args:
        try:
            code = int(args[0])

            # Validate range (0–255)
            if code < 0 or code > 255:
                println(t("shell.engine.builtin.exit.invalid_range"))
                return EXIT_USAGE_ERROR

        except ValueError:
            eprintln(t("shell.engine.builtin.exit.invalid_int", arg=args[0]))
            eprintln(t("shell.engine.builtin.exit.usage"))
            return EXIT_USAGE_ERROR
    else:
        code = 0  # Default exit code

    debug_exit(t("shell.engine.builtin.exit.session_end"))

    # Terminate the shell
    exit(code)

    # Never reached, added for static type checkers
    return EXIT_SUCCESS  # pragma: no cover
