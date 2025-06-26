"""
shell.environs.patches

Patches default environment variables with real-time system values at runtime.
"""

from .user import patch_user
from .home import patch_home
from .pwd import patch_pwd
from .ps1 import patch_ps1
from .lang import patch_lang
from .sysinfo import patch_sysinfo


__all__ = [
    "patch_user",
    "patch_home",
    "patch_pwd",
    "patch_ps1",
    "patch_lang",
    "patch_sysinfo",
]
