"""
sidecar/args/history.py

Handles the --history-size option to set shell history capacity.
"""

from shellkit.shell.environs.accessors import set_history_size


def apply_history_size_args(size: int) -> None:
    """
    Sets the maximum number of shell history entries.
    """
    set_history_size(size)
