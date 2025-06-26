"""
environs/patches/pwd.py

Updates PWD while preserving the previous path.
"""

import os

from ..accessors import get_pwd, set_pwd


def patch_pwd() -> None:
    """
    Refreshes the current path using os.getcwd() and updates the
    environment variable:
    - Keeps the previous path intact;
    - Ensures consistent PWD tracking for shell navigation features.
    """
    cur_path = os.getcwd()
    _, prev_path = get_pwd()
    set_pwd(cur_path, prev_path)
