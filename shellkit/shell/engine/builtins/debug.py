"""
engine/builtins/debug.py

Implements the `debug` shell command.
Provides an interface to control the shell’s internal debugging system.
"""

from shellkit.i18n import t
from shellkit.inspector.debug import debug_command, get_counter, is_debug_enabled
from shellkit.libc import println
from shellkit.shell.state.exit_code import EXIT_SUCCESS, EXIT_USAGE_ERROR, ExitCode


def debug_builtin(args: list[str]) -> ExitCode:
    """
    Implements the `debug` built-in command.

    Provides controls for the internal debug system, including counter reset,
    status querying, and toggling debug mode on/off.

    Usage:
        - debug reset   → Reset the internal debug counter.
        - debug status  → Show current debug mode and counter value.
        - debug off     → Disable debug mode.
        - debug help    → Display help message.
        - (no args)     → Show current debug mode and counter status.

    Args:
        args: Command-line arguments passed to `debug`.

    Returns:
        ExitCode:
            - EXIT_SUCCESS (0) on success.
            - EXIT_USAGE_ERROR (2) if incorrect arguments are provided.
    """
    if not args:
        # No arguments → show current debug status
        if is_debug_enabled():
            println(t("shell.engine.builtin.debug.enabled", counter=get_counter()))
        else:
            println(t("shell.engine.builtin.debug.disabled"))
        return EXIT_SUCCESS

    if len(args) != 1:
        # Too many arguments → show usage error
        println(t("shell.engine.builtin.debug.invalid_args"))
        println(t("shell.engine.builtin.debug.usage"))
        return EXIT_USAGE_ERROR

    cmd = args[0].lower()

    # Dispatch debug subcommand to internal handler
    debug_command(cmd)

    return EXIT_SUCCESS
