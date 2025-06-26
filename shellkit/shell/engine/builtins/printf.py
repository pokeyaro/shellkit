"""
engine/builtins/printf.py

Implements the `printf` shell command.
Provides formatted output with variable expansion and escape sequence support.
"""

from shellkit.i18n import t
from shellkit.inspector.trace import tracing
from shellkit.libc import eprintln, printf, println
from shellkit.shell.state.exit_code import EXIT_FAILURE, EXIT_SUCCESS, EXIT_USAGE_ERROR, ExitCode

from ..text_processing import process_shell_text


def printf_builtin(args: list[str]) -> ExitCode:
    """
    Implements the `printf` built-in command.

    Usage:
        printf FORMAT [ARGUMENTS...]

    Features:
        - Supports format specifiers like %s, %d, %f
        - Expands shell variables like $USER, $HOME
        - Interprets escape sequences like \n, \t
        - Does **not** append newline automatically (unlike `echo`)

    Args:
        args: A list where the first element is the format string,
              followed by optional arguments.

    Returns:
        ExitCode:
            - EXIT_SUCCESS (0): Output completed successfully
            - EXIT_FAILURE (1): Format error or runtime output error
            - EXIT_USAGE_ERROR (2): Missing format string
    """
    # Argument validation
    if not args:
        println(t("shell.engine.builtin.printf.missing_format"))
        println(t("shell.engine.builtin.printf.usage"))
        println(t("shell.engine.builtin.printf.help_hint"))
        return EXIT_USAGE_ERROR

    try:
        fmt, *values = args

        # Preprocess the format string: shell variable expansion + escape interpretation
        processed_fmt = process_shell_text(fmt)

        # Preprocess each argument the same way
        processed_values = [process_shell_text(val) for val in values]

        # Simple check: count format specifiers
        # (this won't catch complex cases like %*.*f, but good enough)
        expected_count = processed_fmt.count('%') - 2 * processed_fmt.count('%%')
        if len(processed_values) < expected_count:
            eprintln(t("shell.engine.builtin.printf.too_few_arguments"))
            return EXIT_FAILURE

        # Execute formatted output with tracing enabled
        with tracing():
            printf(processed_fmt, *processed_values)

        return EXIT_SUCCESS

    except TypeError as e:
        eprintln(t("shell.engine.builtin.printf.error_format"), str(e))
        return EXIT_FAILURE

    except ValueError as e:
        eprintln(t("shell.engine.builtin.printf.error_value"), str(e))
        return EXIT_FAILURE

    except Exception as e:
        eprintln(t("shell.engine.builtin.printf.unexpected_error"), str(e))
        return EXIT_FAILURE
