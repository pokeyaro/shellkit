"""
engine/builtins/pwd.py

Implements the `pwd` shell command.
Prints the current working directory to standard output.
"""

from shellkit.i18n import t
from shellkit.libc import eprintln, println
from shellkit.shell.environs.accessors import get_pwd
from shellkit.shell.state.exit_code import EXIT_FAILURE, EXIT_SUCCESS, EXIT_USAGE_ERROR, ExitCode


def pwd_builtin(args: list[str]) -> ExitCode:
    """
    Implements the `pwd` built-in command.

    Prints the absolute path of the current working directory.
    Does not accept any arguments.

    Args:
        args: Command-line arguments passed to `pwd`.

    Returns:
        ExitCode:
            - EXIT_SUCCESS (0): Successfully printed working directory
            - EXIT_FAILURE (1): Failed to retrieve working directory
            - EXIT_USAGE_ERROR (2): Unexpected arguments were provided
    """
    # Reject extra arguments
    if args:
        println(t("shell.engine.builtin.pwd.unexpected_args"))
        println(t("shell.engine.builtin.pwd.usage"))
        return EXIT_USAGE_ERROR

    try:
        # Get current working directory and home path (ignored here)
        current, _ = get_pwd()

        # Validate retrieved path
        if not current:
            println(t("shell.engine.builtin.pwd.empty"))
            return EXIT_FAILURE

        # Output result
        println(current)
        return EXIT_SUCCESS

    except Exception as e:
        eprintln(t("shell.engine.builtin.pwd.error"), str(e))
        return EXIT_FAILURE
