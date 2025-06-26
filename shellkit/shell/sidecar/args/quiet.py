"""
sidecar/args/quiet.py

Handles the -q / --quiet flag to suppress output and banner.
"""

from shellkit.shell.environs.accessors import set_quiet_mode, set_banner_disabled


def apply_quiet_mode_args() -> None:
    """
    Enables quiet mode and disables the startup banner.
    """
    set_quiet_mode()
    set_banner_disabled()
