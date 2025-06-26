"""
engine/builtins/date.py

Implements the `date` shell command.
Displays the current date and time with optional formatting flags.
"""

import datetime

from shellkit.i18n import t
from shellkit.libc import eprintln, println
from shellkit.shell.state.exit_code import EXIT_FAILURE, EXIT_SUCCESS, EXIT_USAGE_ERROR, ExitCode


def date_builtin(args: list[str]) -> ExitCode:
    """
    Implements the `date` built-in command.

    Displays the current date and time, supporting optional output formats.

    Behavior:
        - By default, prints local time in POSIX-style format: "Mon Jun 17 14:30:00 2025"
        - With `--iso`, prints ISO 8601 format: "2025-06-17 14:30:00"
        - With `--utc`, uses UTC time instead of local time.
        - With `--timestamp`, outputs a Unix timestamp (seconds since epoch).
        - `--iso` and `--timestamp` cannot be used together.
        - Any unsupported arguments will trigger a usage error.

    Args:
        args: Command-line arguments passed to `date`.

    Returns:
        ExitCode:
            - EXIT_SUCCESS (0) on successful output.
            - EXIT_FAILURE (1) on internal error or I/O failure.
            - EXIT_USAGE_ERROR (2) on invalid or conflicting arguments.
    """
    # Validate input arguments
    valid_options = {"--iso", "--utc", "--timestamp"}
    invalid_args = [arg for arg in args if arg not in valid_options]

    if invalid_args:
        # Reject unrecognized options
        println(t("shell.engine.builtin.date.invalid_option", opt=invalid_args[0]))
        return EXIT_USAGE_ERROR

    # Detect mutually exclusive option conflict
    if "--iso" in args and "--timestamp" in args:
        println(t("shell.engine.builtin.date.conflicting_options"))
        return EXIT_USAGE_ERROR

    try:
        # Fetch current time (UTC or local)
        if "--utc" in args:
            now = datetime.datetime.now(datetime.timezone.utc)
        else:
            now = datetime.datetime.now()

        # Format output based on selected option
        if "--iso" in args:
            # ISO 8601 format: "YYYY-MM-DD HH:MM:SS"
            println(now.isoformat(sep=" ", timespec="seconds"))
        elif "--timestamp" in args:
            # Unix timestamp (integer seconds since epoch)
            println("%d", int(now.timestamp()))
        else:
            # Default format
            fmt = "%a %b %d %H:%M:%S %Y"
            println(now.strftime(fmt))

        return EXIT_SUCCESS

    except Exception as e:
        eprintln("date: error getting current time: %s", str(e))
        return EXIT_FAILURE
