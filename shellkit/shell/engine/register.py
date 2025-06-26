"""
engine/register.py

Registers and executes built-in shell commands by name,
setting exit status after execution.
"""

from collections.abc import Callable
from typing import Optional

from shellkit.i18n import t
from shellkit.inspector.debug import debug_builtin, debug_libc
from shellkit.shell.state import get_context

from .tables import BUILTIN_TABLE


def find_shell_builtin(cmd: str) -> Optional[Callable[[list[str]], int]]:
    """
    Look up a built-in command by name. Returns None if not found.

    Returns:
        The function corresponding to the command, which takes a list of arguments
        and returns an integer exit code.
    """
    entry = BUILTIN_TABLE.get(cmd)

    if entry:
        debug_builtin(t("shell.engine.register.found", cmd=cmd))
        return entry[0]

    debug_builtin(t("shell.engine.register.not_found", cmd=cmd))
    return None


def execute_builtin(cmd: str, args: list[str]) -> bool:
    """
    Execute the built-in command specified by `cmd`, with arguments `args`.

    Returns:
        True if the command was a built-in and was executed successfully;
        False otherwise.

    Side Effects:
        Sets the shell's exit status after execution.
    """
    func = find_shell_builtin(cmd)
    if func:
        debug_builtin(t("shell.engine.register.exec_start", cmd=cmd, args=args))

        if cmd in ("echo", "printf"):
            debug_libc(t("shell.engine.register.call_libc_trace", cmd=cmd))

        exit_code = func(args)  # Run the built-in and capture its exit code

        if cmd != "debug":
            debug_builtin(t("shell.engine.register.exec_done", cmd=cmd, code=exit_code))

        get_context().set_exit_status(int(exit_code))
        return True
    return False
