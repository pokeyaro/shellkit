"""
sidecar/args/safe.py

Handles the -s / --safe flag to enable protection against dangerous commands.
"""

from shellkit.shell.environs.accessors import set_safe_mode


def apply_safe_mode_args() -> None:
    """
    Enables safe mode to block potentially destructive commands.
    """
    set_safe_mode()
