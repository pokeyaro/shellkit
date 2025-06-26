"""
environs/accessors/internal.py

Internal accessors for PySH's hidden environment variables.
These variables are set via CLI arguments, used to control runtime behavior,
and are not meant to be modified by users via `export`.
"""

from ..constants import (
    ENV_HIDDEN_BANNER_DISABLED,
    ENV_HIDDEN_REMINDER_DISABLED,
    ENV_HIDDEN_QUIET_MODE,
    ENV_HIDDEN_SAFE_MODE,
    ENV_HIDDEN_PROMPT_FLAG,
    ENV_HIDDEN_PROMPT_COLOR,
    ENV_HIDDEN_PROMPT_PATH,
)
from ..store import get_env, set_env


# ---- Banner Control ----


def is_banner_disabled() -> bool:
    """
    Returns True if the startup banner is disabled.
    By default, the banner is shown unless explicitly disabled.
    """
    return bool(get_env(ENV_HIDDEN_BANNER_DISABLED, False))


def set_banner_disabled() -> None:
    """
    Disables the startup banner.
    """
    set_env(ENV_HIDDEN_BANNER_DISABLED, True)


# ---- Reminder Control ----


def is_reminder_disabled() -> bool:
    """
    Returns True if runtime reminders are disabled.
    Useful in education or minimal display modes.
    """
    return bool(get_env(ENV_HIDDEN_REMINDER_DISABLED, False))


def set_reminder_disabled() -> None:
    """
    Disables runtime reminder messages.
    """
    set_env(ENV_HIDDEN_REMINDER_DISABLED, True)


# ---- Quiet Mode Control ----


def is_quiet_mode() -> bool:
    """
    Returns True if the shell is running in quiet mode.
    Quiet mode suppresses most output.
    """
    return bool(get_env(ENV_HIDDEN_QUIET_MODE, False))


def set_quiet_mode() -> None:
    """
    Enables quiet mode.
    """
    set_env(ENV_HIDDEN_QUIET_MODE, True)


# ---- Safe Mode Control ----


def is_safe_mode() -> bool:
    """
    Returns True if safe mode is enabled.
    Safe mode restricts potentially dangerous commands.
    """
    return bool(get_env(ENV_HIDDEN_SAFE_MODE, False))


def set_safe_mode() -> None:
    """
    Enables safe mode.
    """
    set_env(ENV_HIDDEN_SAFE_MODE, True)


# ---- Prompt Override Flag ----


def is_prompt_overridden() -> bool:
    """
    Returns True if the prompt string (PS1) has been manually overridden by the user.
    When overridden, automatic patching of PS1 is skipped.
    """
    return bool(get_env(ENV_HIDDEN_PROMPT_FLAG))


def set_prompt_overridden() -> None:
    """
    Marks the prompt string as overridden by user.
    This disables auto-patching from system logic.
    """
    set_env(ENV_HIDDEN_PROMPT_FLAG, True)


# ---- Prompt Style: Color ----


def get_prompt_color_style() -> str:
    """
    Returns the current prompt color style (e.g., "blue", "green").
    Default is "blue" if not explicitly set.
    """
    result = get_env(ENV_HIDDEN_PROMPT_COLOR, "blue")
    return str(result)


def set_prompt_color_style(color: str = "") -> None:
    """
    Sets the prompt color style.
    Injected via CLI argument like --prompt-color=green.
    """
    set_env(ENV_HIDDEN_PROMPT_COLOR, color)


# ---- Prompt Style: Path ----


def get_prompt_path_style() -> str:
    """
    Returns the current path display style in prompt.
    Options may include "short", "full", or "none".
    Default is "short".
    """
    result = get_env(ENV_HIDDEN_PROMPT_PATH, "short")
    return str(result)


def set_prompt_path_style(style: str = "") -> None:
    """
    Sets the prompt path display style.
    """
    set_env(ENV_HIDDEN_PROMPT_PATH, style)
