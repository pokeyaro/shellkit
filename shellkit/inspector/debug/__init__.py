"""
inspector.debug

Shell-layer debugging hooks for interactive CLI diagnostics, designed to trace
internal control flow such as command parsing, alias resolution, and builtin dispatching.

Design Notes:
- core.py:       Tracks global debug state, manages counter, and prints emoji-tagged messages
- command.py:    Provides user-facing debug command handlers (used internally by CLI)
- layers.py:     Defines fine-grained debug entrypoints for each shell subsystem

This module is only active when pysh is launched with `--debug`.
Not intended for use outside the shell entrypoint.
"""

# core
from .core import (
    enable_debug, disable_debug, end_startup_phase,
    get_counter, is_debug_enabled,
    reset_counter, reset_counter_after,
)

# command
from .command import (
    debug_command,
    debug_reset, debug_status, debug_off, debug_help,
)

# layers
from .layers import (
    debug_startup, debug_argv, debug_alias,
    debug_shell, debug_env, debug_builtin,
    debug_repl, debug_docs, debug_exit,
    debug_libc,
)


__all__ = [
    # core
    "enable_debug", "disable_debug", "end_startup_phase",
    "get_counter", "is_debug_enabled",
    "reset_counter", "reset_counter_after",

    # command
    "debug_command",
    "debug_reset", "debug_status", "debug_off", "debug_help",

    # layers
    "debug_startup", "debug_argv", "debug_alias",
    "debug_shell", "debug_env", "debug_builtin",
    "debug_repl", "debug_docs", "debug_exit",
    "debug_libc",
]
