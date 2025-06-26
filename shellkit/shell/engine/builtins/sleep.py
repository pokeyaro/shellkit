"""
engine/builtins/sleep.py

Implements the `sleep` shell command.
Pauses execution for a specified number of seconds with optional countdown display.
"""

import time

from shellkit.i18n import t
from shellkit.libc import eprintln, print, println
from shellkit.shell.state.exit_code import EXIT_FAILURE, EXIT_SUCCESS, EXIT_USAGE_ERROR, ExitCode


def sleep_builtin(args: list[str]) -> ExitCode:
    """
    Implements the `sleep` built-in command.

    Pauses shell execution for a specified number of seconds.
    Supports optional countdown messages, quiet mode, and custom done messages.

    Usage:
        sleep SECONDS [--quiet] [--countdown=TEXT] [--done=TEXT]

    Args:
        args: Command-line arguments passed to `sleep`.

    Supported options:
        - SECONDS: Positive float or integer, required
        - --quiet: Suppress countdown display
        - --countdown=TEXT: Customize countdown display with `{i}` placeholder
        - --done=TEXT: Message to print after sleep completes

    Returns:
        ExitCode:
            - EXIT_SUCCESS (0): Sleep completed successfully
            - EXIT_FAILURE (1): Interrupted or failed
            - EXIT_USAGE_ERROR (2): Invalid input or option
    """
    # Argument validation
    if not args:
        println(t("shell.engine.builtin.sleep.missing_args"))
        println(t("shell.engine.builtin.sleep.usage"))
        println(t("shell.engine.builtin.sleep.help_hint"))
        return EXIT_USAGE_ERROR

    # Default configuration
    countdown_fmt = t("shell.engine.builtin.sleep.default_countdown")
    done_msg = t("shell.engine.builtin.sleep.default_done")
    quiet = False
    parsed_args = []

    # Parse options
    for arg in args:
        if arg == "--quiet":
            quiet = True
        elif arg.startswith("--countdown="):
            countdown_fmt = arg.split("=", 1)[1]

            # Ensure the countdown format includes the {i} placeholder
            if "{i}" not in countdown_fmt:
                println(t("shell.engine.builtin.sleep.invalid_template"))
                return EXIT_USAGE_ERROR
        elif arg.startswith("--done="):
            done_msg = arg.split("=", 1)[1]
        elif arg.startswith("--"):
            # Unrecognized long option
            println(t("shell.engine.builtin.sleep.invalid_option"), arg)
            println(t("shell.engine.builtin.sleep.valid_options"))
            return EXIT_USAGE_ERROR
        else:
            parsed_args.append(arg)

    # Check if SECONDS argument is missing
    if not parsed_args:
        println(t("shell.engine.builtin.sleep.missing_seconds"))
        return EXIT_USAGE_ERROR

    # Ensure only one positional argument is passed
    if len(parsed_args) > 1:
        println(t("shell.engine.builtin.sleep.too_many_args"))
        return EXIT_USAGE_ERROR

    # Parse the sleep duration
    try:
        seconds = float(parsed_args[0])
        if seconds < 0:
            println(t("shell.engine.builtin.sleep.invalid_interval"), parsed_args[0])
            return EXIT_USAGE_ERROR
        elif seconds == 0:
            return EXIT_SUCCESS

    except ValueError:
        eprintln(t("shell.engine.builtin.sleep.invalid_interval"), parsed_args[0])
        eprintln(t("shell.engine.builtin.sleep.expected_number"))
        return EXIT_USAGE_ERROR

    # Perform the sleep
    try:
        if quiet:
            # Silent sleep
            time.sleep(seconds)
        else:
            if seconds < 1:
                # For short sleeps < 1s, skip countdown
                time.sleep(seconds)
            else:
                # Show countdown for integer part
                int_seconds = int(seconds)
                remaining_fraction = seconds - int_seconds

                for i in range(int_seconds, 0, -1):
                    text = countdown_fmt.replace("{i}", str(i))
                    print(f"\r{text} ", end="", flush=True)
                    time.sleep(1)

                # Sleep for fractional remainder
                if remaining_fraction > 0:
                    time.sleep(remaining_fraction)

            # Print done message if defined
            if done_msg:
                println(f"\r\033[K\033[32m{done_msg}\033[0m")

        return EXIT_SUCCESS

    except KeyboardInterrupt:
        # Handle Ctrl+C interrupt
        eprintln(t("shell.engine.builtin.sleep.interrupted"))
        return EXIT_FAILURE

    except Exception as e:
        eprintln(t("shell.engine.builtin.sleep.unexpected_error"), str(e))
        return EXIT_FAILURE
