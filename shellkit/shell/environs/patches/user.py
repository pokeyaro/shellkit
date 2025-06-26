"""
environs/patches/user.py

Updates the USER variable using the actual system username via getpass.
"""

import getpass

from ..accessors import set_user
from ..constants import DEFAULT_USER


def patch_user() -> None:
    """
    Updates the USER environment variable using the current system username.
    Falls back to DEFAULT_USER if unavailable.
    """
    whoami = getpass.getuser() or DEFAULT_USER
    set_user(whoami)
