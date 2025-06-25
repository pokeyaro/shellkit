"""
shell.environs.accessors

Unified access interface for environment variables and internal runtime flags.
"""

from .user import get_user, set_user
from .home import get_home, set_home
from .shell import get_shell, set_shell
from .pwd import get_pwd, set_pwd
from .ps1 import get_ps1, set_ps1
from .lang import get_lang, set_lang
from .sysinfo import get_sysinfo, set_sysinfo
from .history import get_history_size, set_history_size
from .internal import (
    is_banner_disabled, set_banner_disabled,
    is_reminder_disabled, set_reminder_disabled,
    is_quiet_mode, set_quiet_mode,
    is_safe_mode, set_safe_mode,
    is_prompt_overridden, set_prompt_overridden,
    get_prompt_color_style, set_prompt_color_style,
    get_prompt_path_style, set_prompt_path_style,
)


__all__ = [
    "get_user", "set_user",
    "get_home", "set_home",
    "get_shell", "set_shell",
    "get_pwd", "set_pwd",
    "get_ps1", "set_ps1",
    "get_lang", "set_lang",
    "get_sysinfo", "set_sysinfo",
    "get_history_size", "set_history_size",
    "is_banner_disabled", "set_banner_disabled",
    "is_reminder_disabled", "set_reminder_disabled",
    "is_quiet_mode", "set_quiet_mode",
    "is_safe_mode", "set_safe_mode",
    "is_prompt_overridden", "set_prompt_overridden",
    "get_prompt_color_style", "set_prompt_color_style",
    "get_prompt_path_style", "set_prompt_path_style",
]
