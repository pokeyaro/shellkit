"""
shell.engine.builtins

Aggregates all built-in shell command handlers into a single module.
Exposes functions like `cd_builtin`, `echo_builtin`, `exit_builtin`, etc.
"""

from .alias import alias_builtin
from .arch import arch_builtin
from .cd import cd_builtin
from .clear import clear_builtin
from .copyright import copyright_builtin
from .date import date_builtin
from .debug import debug_builtin
from .echo import echo_builtin
from .env import env_builtin
from .exit import exit_builtin
from .export import export_builtin
from .help import help_builtin
from .history import history_builtin
from .license import license_builtin
from .locale import locale_builtin
from .machinfo import machinfo_builtin
from .printf import printf_builtin
from .pwd import pwd_builtin
from .sleep import sleep_builtin
from .tree import tree_builtin
from .uname import uname_builtin
from .which import which_builtin
from .whoami import whoami_builtin


__all__ = [
    "alias_builtin",
    "arch_builtin",
    "cd_builtin",
    "clear_builtin",
    "copyright_builtin",
    "date_builtin",
    "debug_builtin",
    "echo_builtin",
    "env_builtin",
    "exit_builtin",
    "export_builtin",
    "help_builtin",
    "history_builtin",
    "license_builtin",
    "locale_builtin",
    "machinfo_builtin",
    "printf_builtin",
    "pwd_builtin",
    "sleep_builtin",
    "tree_builtin",
    "uname_builtin",
    "which_builtin",
    "whoami_builtin",
]
