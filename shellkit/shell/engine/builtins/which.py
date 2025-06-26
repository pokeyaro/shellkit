"""
engine/builtins/which.py

Implements the `which` shell command.
Searches for the source of a command: shell built-in, alias, or external executable.
"""

import shutil

from shellkit.i18n import t
from shellkit.libc import eprintln, println
from shellkit.shell.state.exit_code import EXIT_FAILURE, EXIT_SUCCESS, EXIT_USAGE_ERROR, ExitCode


def which_builtin(args: list[str]) -> ExitCode:
    """
    Built-in implementation of the `which` command.

    Checks each argument to see whether it is a built-in command, a defined alias,
    or an external executable found in the system's PATH. Prints the source location.

    Args:
        args: List of command names to check.

    Returns:
        ExitCode:
            - EXIT_SUCCESS (0): All commands were found
            - EXIT_FAILURE (1): One or more commands not found
            - EXIT_USAGE_ERROR (2): No arguments provided
    """
    # No arguments provided
    if not args:
        println(t("shell.engine.builtin.which.missing_args"))
        println(t("shell.engine.builtin.which.usage"))
        println(t("shell.engine.builtin.which.more_info"))
        return EXIT_USAGE_ERROR

    try:
        # Lazy import to avoid circular dependency at runtime
        from ..tables import BUILTIN_TABLE, ALIAS_TABLE

        found_count = 0
        not_found_count = 0

        for name in args:
            # Validate command name syntax to prevent injection or garbage input
            if not name or not name.replace("-", "").replace("_", "").replace(".", "").isalnum():
                println(t("shell.engine.builtin.which.invalid_name"), name)
                not_found_count += 1
                continue

            # Check if it's a shell built-in
            if name in BUILTIN_TABLE:
                println(t("shell.engine.builtin.which.builtin"), name)
                found_count += 1

            # Check if it's an alias
            elif name in ALIAS_TABLE:
                target, alias_args = ALIAS_TABLE[name]
                if alias_args:
                    println(t("shell.engine.builtin.which.alias_with_args"), name, target, " ".join(alias_args))
                else:
                    println(t("shell.engine.builtin.which.alias"), name, target)
                found_count += 1

            # Otherwise, check for external executable using PATH
            else:
                try:
                    path = shutil.which(name)
                    if path:
                        println("%s", path)
                        found_count += 1
                    else:
                        println(t("shell.engine.builtin.which.not_found"), name)
                        not_found_count += 1

                except Exception as e:
                    eprintln(t("shell.engine.builtin.which.error_searching"), name, str(e))
                    not_found_count += 1

        # Determine return status: success only if all commands are found
        if not_found_count > 0:
            return EXIT_FAILURE
        else:
            return EXIT_SUCCESS

    except Exception as e:
        eprintln(t("shell.engine.builtin.which.unexpected_error"), str(e))
        return EXIT_FAILURE
