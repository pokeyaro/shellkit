"""
engine/resolver.py

Resolves user input commands through the alias mapping table.
If an alias is matched, expands it to the real command and prepends predefined arguments.
"""

from shellkit.i18n import t
from shellkit.inspector.debug import debug_alias

from .tables import ALIAS_TABLE


def resolve_alias(cmd: str, args: list[str]) -> tuple[str, list[str]]:
    """
    If `cmd` is an alias, resolve it to its real command and arguments;
    otherwise, return the original command and arguments as-is.

    - Any extra arguments provided by the user will be appended after the alias-defined args.
    """
    if cmd in ALIAS_TABLE:
        real_cmd, alias_args = ALIAS_TABLE[cmd]
        target = f"{real_cmd} {' '.join(alias_args)}".strip()
        debug_alias(t("shell.engine.resolver.alias_expansion", alias=cmd, target=target))
        return real_cmd, alias_args + args
    return cmd, args
