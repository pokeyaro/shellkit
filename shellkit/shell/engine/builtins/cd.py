"""
engine/builtins/cd.py

Implements the `cd` shell command.
Supports changing the current working directory with various path shortcuts.
"""

import os

from shellkit.i18n import t
from shellkit.libc import eprintln
from shellkit.shell.environs.accessors import get_home, get_pwd, set_pwd
from shellkit.shell.sidecar.args.prompt import update_ps1_from_env
from shellkit.shell.state.exit_code import EXIT_FAILURE, EXIT_SUCCESS, ExitCode


def cd_builtin(args: list[str]) -> ExitCode:
    """
    Implements the `cd` built-in command.

    Changes the current working directory.
    Supports:
        - `cd` (go to home)
        - `cd -` (switch to previous directory)
        - `cd ~` (go to home directory)
        - `cd /some/path` (absolute or relative path)

    Args:
        args: Command-line arguments passed to the cd command.

    Returns:
        ExitCode:
            - EXIT_SUCCESS (0) on success.
            - EXIT_FAILURE (1) on error (e.g., invalid path or permissions).
    """
    cur, prev = get_pwd()

    # Determine target path
    if args:
        target = args[0]
        if target == "-":
            target = prev or cur
        elif target == "~":
            target = get_home()
        else:
            target = os.path.expanduser(target)  # Support for cd ~/foo
    else:
        target = get_home()

    # Attempt to change directory
    try:
        os.chdir(target)
        new_path = os.getcwd()
        set_pwd(new_path, cur)

        # Update PS1 based on new environment
        update_ps1_from_env()

        return EXIT_SUCCESS

    except FileNotFoundError:
        eprintln(t("shell.engine.builtin.cd.not_found", path=target))
        return EXIT_FAILURE

    except NotADirectoryError:
        eprintln(t("shell.engine.builtin.cd.not_a_directory", path=target))
        return EXIT_FAILURE

    except PermissionError:
        eprintln(t("shell.engine.builtin.cd.permission_denied", path=target))
        return EXIT_FAILURE

    except Exception as e:
        eprintln(t("shell.engine.builtin.cd.unexpected_error"), str(e))
        return EXIT_FAILURE
