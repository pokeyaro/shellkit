"""
environs/patches/home.py

Updates the HOME variable using the current user's real home directory.
"""

import os

from ..accessors import set_home


def patch_home() -> None:
    """
    Updates the HOME variable with the actual user home path
    resolved via os.path.expanduser("~").
    """
    real_home = os.path.expanduser("~")
    set_home(real_home)
