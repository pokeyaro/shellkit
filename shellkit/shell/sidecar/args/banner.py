"""
sidecar/args/banner.py

Handles the --no-banner flag to suppress startup banner display.
"""

from shellkit.shell.environs.accessors import set_banner_disabled


def apply_no_banner_args() -> None:
    """
    Disables the startup banner in the environment config.
    """
    set_banner_disabled()
