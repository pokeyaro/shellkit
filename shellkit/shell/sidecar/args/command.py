"""
sidecar/args/command.py

Handles the -c / --command argument for executing one or more inline commands.
"""

from shellkit.i18n import t
from shellkit.inspector.debug import debug_argv, debug_startup, end_startup_phase
from shellkit.libc import exit
from shellkit.shell.environs import init_environs


def apply_command_args(command: str) -> None:
    """
    Executes the given command string and exits immediately.

    Supports multiple commands separated by semicolons.
    """
    # Delay import to avoid circular dependency
    from shellkit.shell.engine import handle_line

    # Initialize environment variables
    init_environs()

    end_startup_phase()
    debug_startup(t("shell.sidecar.args.command.init_environs"))

    # Split command string by semicolons
    commands = command.split(";")
    if len(commands) > 1:
        debug_argv(t("shell.sidecar.args.command.split_semicolon", {"n": len(commands)}))

    for cmd in commands:
        cmd = cmd.strip()
        if cmd:  # Skip empty segments
            handle_line(cmd)

    debug_argv(t("shell.sidecar.args.command.done"))
    exit()
