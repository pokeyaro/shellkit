"""
sidecar/handler.py

Processes parsed CLI arguments and applies side effects (e.g., prompt settings, execution flags).
"""

from argparse import Namespace
from typing import Callable, Literal

from .args import (
    apply_command_args,
    apply_version_args,
    apply_prompt_color_args,
    apply_prompt_path_args,
    apply_history_size_args,
    apply_no_banner_args,
    apply_no_reminder_args,
    apply_quiet_mode_args,
    apply_safe_mode_args,
    apply_debug_args,
    apply_trace_echo_args,
)


HandlerTuple = tuple[Callable[[], None], bool, Literal["conditional", "always"]]


def handle_args(args: Namespace) -> bool:
    """
    Applies side effects based on parsed CLI arguments.

    Returns:
        True if the program should exit early after handling an argument (e.g., --version or -c),
        False to proceed with normal shell launch.
    """
    # Pre-handle --debug flag to enable early debugging
    if getattr(args, "debug", False):
        apply_debug_args()

    handlers: dict[str, HandlerTuple] = {
        # Conditional handlers: run only if explicitly specified by user
        "command": (lambda: apply_command_args(args.command), True, "conditional"),
        "version": (apply_version_args, True, "conditional"),
        "no_banner": (apply_no_banner_args, False, "conditional"),
        "no_reminder": (apply_no_reminder_args, False, "conditional"),
        "quiet": (apply_quiet_mode_args, False, "conditional"),
        "safe": (apply_safe_mode_args, False, "conditional"),
        "trace_echo": (apply_trace_echo_args, False, "conditional"),

        # Always-run handlers: apply regardless of user input
        "prompt_color": (lambda: apply_prompt_color_args(args.prompt_color), False, "always"),
        "prompt_path": (lambda: apply_prompt_path_args(args.prompt_path), False, "always"),
        "history_size": (lambda: apply_history_size_args(args.history_size), False, "always"),
    }

    for attr, (handler, should_exit, execution_type) in handlers.items():
        if execution_type == "conditional":
            # Only execute if user explicitly passed this flag
            if getattr(args, attr):
                handler()
                if should_exit:
                    return True
        elif execution_type == "always":
            # Always execute regardless of CLI input
            handler()
            if should_exit:
                return True

    return False
