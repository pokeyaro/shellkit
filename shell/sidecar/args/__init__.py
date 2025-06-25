"""
shell.sidecar.args

Aggregates CLI option handlers for prompt, execution, modes, and debugging.
"""

from .command import apply_command_args
from .version import apply_version_args
from .history import apply_history_size_args
from .banner import apply_no_banner_args
from .reminder import apply_no_reminder_args
from .quiet import apply_quiet_mode_args
from .safe import apply_safe_mode_args
from .debug import apply_debug_args
from .trace_echo import apply_trace_echo_args
from .prompt import (
    apply_prompt_args,
    apply_prompt_color_args,
    apply_prompt_path_args
)


__all__ = [
    "apply_command_args",
    "apply_version_args",
    "apply_history_size_args",
    "apply_no_banner_args",
    "apply_no_reminder_args",
    "apply_quiet_mode_args",
    "apply_safe_mode_args",
    "apply_debug_args",
    "apply_trace_echo_args",
    "apply_prompt_args",
    "apply_prompt_color_args",
    "apply_prompt_path_args",
]
