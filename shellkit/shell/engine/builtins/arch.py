"""
engine/builtins/arch.py

Implements the `arch` shell command.
Supports retrieving system architecture information via system utilities or environment introspection.
"""

import subprocess

from shellkit.i18n import t
from shellkit.libc import eprintln, println
from shellkit.shell.environs.accessors import get_sysinfo
from shellkit.shell.environs.constants import ENV_KEY_SYSINFO_ARCH
from shellkit.shell.state.exit_code import EXIT_FAILURE, EXIT_SUCCESS, ExitCode


def arch_builtin(args: list[str]) -> ExitCode:
    """
    Implements the `arch` built-in command.

    Outputs the current system architecture.

    - By default, uses environment-based system info (portable and consistent).
    - If `--raw` is passed, invokes the native `arch` command directly.

    Args:
        args: Command-line arguments passed to the arch command.

    Returns:
        ExitCode:
            - EXIT_SUCCESS (0) on success.
            - EXIT_FAILURE (1) on failure (e.g., `arch` command not found).
    """
    if args and args[0] == "--raw":
        try:
            result = subprocess.check_output(["arch"], text=True).strip()
            println("\033[1m%s\033[0m %s", t("shell.engine.builtin.arch.label_raw"), result)
            return EXIT_SUCCESS

        except subprocess.CalledProcessError as e:
            eprintln("\033[31m[error]\033[0m " + t("shell.engine.builtin.arch.raw_failed_code"), e.returncode)
            return EXIT_FAILURE

        except FileNotFoundError:
            eprintln("\033[31m[error]\033[0m " + t("shell.engine.builtin.arch.not_found"))
            return EXIT_FAILURE

        except Exception as e:
            eprintln("\033[31m[error]\033[0m " + t("shell.engine.builtin.arch.raw_unexpected"), str(e))
            return EXIT_FAILURE
    else:
        try:
            arch = get_sysinfo().get(ENV_KEY_SYSINFO_ARCH)
            if arch is None:
                println("\033[31m[error]\033[0m " + t("shell.engine.builtin.arch.not_available"))
                return EXIT_FAILURE

            println("\033[1m%s\033[0m %s", t("shell.engine.builtin.arch.label"), arch)
            return EXIT_SUCCESS

        except Exception as e:
            eprintln("\033[31m[error]\033[0m " + t("shell.engine.builtin.arch.info_unexpected"), str(e))
            return EXIT_FAILURE
