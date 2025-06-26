"""
engine/fallback.py

Executes non-builtin commands by falling back to the host system.
Handles command lookup, safety restrictions, and quiet/debug modes.
"""

import shutil
import subprocess

from shellkit.i18n import t
from shellkit.libc import eprintln, println
from shellkit.shell.environs.accessors import is_quiet_mode, is_safe_mode
from shellkit.shell.state.exit_code import EXIT_COMMAND_NOT_FOUND, EXIT_FAILURE, EXIT_PERMISSION_DENIED

from .tables import UNSAFE_TABLE


def run_fallback(cmd: str, args: list[str]) -> int:
    """
    Executes an external command by falling back to the system shell.
    - Always returns a proper exit code (0 for success, non-zero for errors).
    """

    # Check if the command exists in PATH
    if shutil.which(cmd) is None:
        println(t("shell.engine.fallback.not_found", cmd=cmd))
        return EXIT_COMMAND_NOT_FOUND

    # If safe mode is enabled, disallow execution of dangerous commands
    if is_safe_mode() and cmd in UNSAFE_TABLE:
        safe_tag = t("shell.engine.fallback.forbidden")
        println("%s: \033[1;31m%s\033[0m", safe_tag, cmd)
        return EXIT_PERMISSION_DENIED

    # Show fallback execution notice unless in quiet mode
    if not is_quiet_mode():
        label = t("shell.engine.fallback.fallback_tag")
        fallback_tag = f"\033[1;33m{label}: \033[0m"
        cmd_text = "\033[90m" + " ".join([cmd] + args) + "\033[0m"
        println("%s%s", fallback_tag, cmd_text)

    # Try executing the external command via subprocess
    try:
        result = subprocess.run([cmd] + args)
        return result.returncode

    except Exception as e:
        eprintln("Error running command: %s", str(e))
        return EXIT_FAILURE
