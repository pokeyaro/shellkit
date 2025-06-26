"""
engine/builtins/whoami.py

Implements the `whoami` shell command.
Prints the current username from environment or session context.
"""

from shellkit.i18n import t
from shellkit.libc import eprintln, println
from shellkit.shell.environs.accessors.user import get_user
from shellkit.shell.state.exit_code import EXIT_FAILURE, EXIT_SUCCESS, EXIT_USAGE_ERROR, ExitCode


def whoami_builtin(args: list[str]) -> ExitCode:
    """
    Built-in implementation of the `whoami` command.

    Prints the current username based on the shell environment context.
    Does not accept any arguments.

    Args:
        args: Command-line arguments passed to `whoami`.

    Returns:
        ExitCode:
            - EXIT_SUCCESS (0): Username displayed successfully
            - EXIT_FAILURE (1): Failed to retrieve username
            - EXIT_USAGE_ERROR (2): Arguments were incorrectly passed
    """
    # Reject unexpected arguments
    if args:
        println(t("shell.engine.builtin.whoami.usage_error"))
        println(t("shell.engine.builtin.whoami.usage_hint"))
        return EXIT_USAGE_ERROR

    try:
        # Attempt to fetch the current user
        user = get_user()

        if not user:
            println(t("shell.engine.builtin.whoami.error_retrieval"))
            return EXIT_FAILURE

        # Print resolved username
        println(user)
        return EXIT_SUCCESS

    except Exception as e:
        eprintln(t("shell.engine.builtin.whoami.unexpected_error"), str(e))
        return EXIT_FAILURE
