"""
engine/builtins/echo.py

Implements the `echo` shell command.
Supports string output with variable substitution, escape sequence parsing,
and optional newline suppression via the -n flag.
"""

from shellkit.i18n import t
from shellkit.inspector.trace import tracing
from shellkit.libc import eprintln, print, println
from shellkit.shell.state.exit_code import EXIT_FAILURE, EXIT_SUCCESS, EXIT_USAGE_ERROR, ExitCode

from ..text_processing import process_shell_text


def echo_builtin(args: list[str]) -> ExitCode:
    r"""
    Implements the `echo` built-in command.

    Outputs the provided text to standard output, supporting environment variable
    expansion and escape sequence interpretation.

    Features:
        - Supports `-n` flag to suppress the trailing newline.
        - Enables escape sequences such as `\n`, `\t`, `\\`, etc.
        - Performs variable substitution: `$VAR` or `${VAR}`, but ignores `\$VAR`.

    Args:
        args: Command-line arguments passed to `echo`. The first argument may be `-n`.

    Returns:
        ExitCode:
            - EXIT_SUCCESS (0) on successful output.
            - EXIT_FAILURE (1) on runtime errors (rare).
            - EXIT_USAGE_ERROR (2) if invalid options are provided.
    """
    # Check for -n flag (suppress newline)
    newline = True
    text_args = args[:]

    if args and args[0] == "-n":
        newline = False
        text_args = args[1:]
    elif args and args[0].startswith("-") and args[0] != "-n":
        # Invalid option handling
        println(t("shell.engine.builtin.echo.invalid_option", opt=args[0]))
        println(t("shell.engine.builtin.echo.usage"))
        return EXIT_USAGE_ERROR

    try:
        # Handle empty echo
        if not text_args:
            print()
            return EXIT_SUCCESS

        # Merge and process shell-like text (with escapes and variable substitution)
        raw = " ".join(text_args)
        output = process_shell_text(raw)

        with tracing():
            print(output, end="" if not newline else "\n")

        return EXIT_SUCCESS

    except Exception as e:
        eprintln(t("shell.engine.builtin.echo.error", msg=str(e)))
        return EXIT_FAILURE
