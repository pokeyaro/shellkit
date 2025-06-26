"""
engine/builtins/alias.py

Implements the `alias` shell command.
Supports listing all aliases, adding new ones, and querying specific alias mappings.
"""

from shellkit.i18n import t
from shellkit.libc import println
from shellkit.shell.state.exit_code import EXIT_SUCCESS, EXIT_USAGE_ERROR, ExitCode


def alias_builtin(args: list[str]) -> ExitCode:
    """
    Implements the `alias` built-in command.

    This command supports the following behaviors:
      - No arguments: list all defined aliases.
      - NAME=VALUE format: define a new alias.
      - NAME only: display the expanded form of a specific alias.

    Args:
        args: List of command-line arguments passed to `alias`.

    Returns:
        ExitCode:
            - EXIT_SUCCESS (0) on success.
            - EXIT_USAGE_ERROR (2) on invalid usage or query failure.
    """
    # Runtime import to avoid circular dependencies
    from ..tables import ALIAS_TABLE

    if not args:
        _print_all_aliases(ALIAS_TABLE)
        return EXIT_SUCCESS

    for arg in args:
        # Add a new alias
        if "=" in arg:
            name, value = arg.split("=", 1)
            name = name.strip()
            value = value.strip().strip("'\"")  # Remove surrounding quotes

            tokens = value.split()
            if not tokens:
                println(t("shell.engine.builtin.alias.invalid_value", name=name))
                return EXIT_USAGE_ERROR

            real_cmd = tokens[0]
            real_args = tokens[1:]

            ALIAS_TABLE[name] = (real_cmd, real_args)
        else:
            # Query existing alias
            if arg in ALIAS_TABLE:
                real_cmd, args = ALIAS_TABLE[arg]
                short_opts = "".join(x[1] for x in args if x.startswith("-") and len(x) == 2)
                long_args = [x for x in args if not (x.startswith("-") and len(x) == 2)]
                full = " ".join([real_cmd] + ([f"-{short_opts}"] if short_opts else []) + long_args)
                println("%s='%s'", arg, full)
            else:
                println(t("shell.engine.builtin.alias.not_found", name=arg))
                return EXIT_USAGE_ERROR

    return EXIT_SUCCESS


def _print_all_aliases(alias_table: dict[str, tuple[str, list[str]]]) -> None:
    """
    Prints all alias mappings in a human-readable format.

    Each alias is displayed as: name='real_cmd -opts args'

    Args:
        alias_table: A dictionary mapping alias names to a tuple of:
                     (real command, list of arguments)
    """
    from shellkit.libc import println

    for name, (real_cmd, args) in alias_table.items():
        short_opts = ""
        new_args = []

        for arg in args:
            if arg.startswith("-") and not arg.startswith("--") and len(arg) == 2:
                short_opts += arg[1]
            else:
                new_args.append(arg)

        parts = [real_cmd]
        if short_opts:
            parts.append(f"-{short_opts}")
        parts.extend(new_args)

        full_cmd = " ".join(parts)
        println("%s='%s'", name, full_cmd)
