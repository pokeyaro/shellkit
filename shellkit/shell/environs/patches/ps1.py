"""
environs/patches/ps1.py

Updates the PS1 shell prompt with emoji and color styling; skips if overridden by CLI.
"""

from ..accessors import set_ps1


def patch_ps1() -> None:
    """
    Injects a styled PS1 prompt:
    - Uses an emoji + ANSI black (30) color;
    - Skips if user has manually overridden PS1 via CLI.
    """
    ps1 = "🤖 \033[1;30mpysh ➜\033[0m "
    set_ps1(ps1)
