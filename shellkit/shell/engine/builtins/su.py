"""
engine/builtins/su.py

Implements the `su` shell command.
Launches a root login shell using the current pysh binary as the login shell.
Supports both Linux (`su ... -s <pysh>`) and macOS (`sudo <pysh>`).
"""

import os
import platform
import shutil
import sys
from pathlib import Path

from shellkit.i18n import t
from shellkit.libc import eprintln, println
from shellkit.shell.environs.accessors import get_user
from shellkit.shell.state.exit_code import EXIT_FAILURE, EXIT_USAGE_ERROR, ExitCode


def su_builtin(args: list[str]) -> ExitCode:
    """
    Launches a root login shell with pysh as the shell.

    Behavior:
        - Detects the current pysh executable path.
        - On Linux: executes `su [args...] -s <pysh_path>`
        - On macOS: only allows no args, executes `sudo <pysh_path>`
        - Replaces current process via os.execvp()

    Args:
        args: Command-line arguments passed to `su`.

    Returns:
        ExitCode:
            - EXIT_SUCCESS (0) if execvp succeeds (never returns).
            - EXIT_USAGE_ERROR (2) if args passed on macOS.
            - EXIT_FAILURE (1) on error.
    """
    system = platform.system().lower()
    pysh_path = shutil.which("pysh") or sys.argv[0]
    pysh_path = str(Path(pysh_path).resolve())

    if not pysh_path or not os.path.exists(pysh_path):
        println(t("shell.engine.builtin.su.cannot_detect_pysh"))
        return EXIT_FAILURE

    if system == "linux":
        target_user = args[0] if args else "root"
        println(t("shell.engine.builtin.su.switching_user", user=target_user))

        # Allow arg passthrough, and append -s <pysh_path> at the end
        cmd = ["su"] + args + ["-s", pysh_path]
    elif system == "darwin":
        if args:
            println(t("shell.engine.builtin.su.macos_args_not_allowed"))
            return EXIT_USAGE_ERROR
        println(t("shell.engine.builtin.su.switching_user", user=get_user()))
        cmd = ["sudo", pysh_path]
    else:
        println(t("shell.engine.builtin.su.unsupported_platform", platform=system))
        return EXIT_FAILURE

    try:
        os.execvp(cmd[0], cmd)
    except Exception as e:
        eprintln(t("shell.engine.builtin.su.unexpected_error"), str(e))
        return EXIT_FAILURE
