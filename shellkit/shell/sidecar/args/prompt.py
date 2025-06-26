"""
sidecar/args/prompt.py

Handles CLI prompt customization via --prompt-color and --prompt-path arguments.
"""

import os
import platform

from shellkit.shell.environs.accessors import (
    get_home,
    set_ps1, get_pwd,
    get_prompt_color_style, get_prompt_path_style,
    set_prompt_color_style, set_prompt_path_style,
    is_prompt_overridden,
)


# ANSI color codes for prompt foreground styling
COLOR_CODES = {
    "red":     91,
    "green":   92,
    "yellow":  93,
    "blue":    34,
    "magenta": 95,
    "cyan":    36,
    "white":   97,
    "gray":    90,
    "black":   30,
}


def build_prompt_ps1(color: str, path_style: str) -> str:
    """
    Builds the PS1 string with color and path style applied.
    """
    # Select ANSI color code (default to blue: 34)
    code = COLOR_CODES.get(color, 34)

    # Choose logo based on system type
    system = platform.system().lower()
    logo = {
        "darwin": "\uf8ff",  # Apple logo ()
        "linux": "🐧"        # Linux penguin
    }.get(system, "🤖")      # Default: robot face

    # Build path segment based on selected style
    path = None
    cur_path, _ = get_pwd()
    home_path = get_home()
    match path_style:
        case "none":
            path = ""
        case "short":
            path = os.path.basename(cur_path) or "/"
        case "full":
            # If inside HOME, replace with ~
            if cur_path.startswith(home_path):
                path = cur_path.replace(home_path, "~", 1)
            else:
                path = cur_path

    # Assemble full PS1 string
    if path:
        return f"{logo} \033[1;{code}mpysh [{path}] ➜\033[0m  "
    else:
        return f"{logo} \033[1;{code}mpysh ➜\033[0m  "


def apply_prompt_args(
    *,
    color: str | None = None,
    path_style: str | None = None,
) -> None:
    """
    Applies CLI prompt settings and updates PS1 at startup.
    """
    # Normalize arguments (set defaults and lowercase)
    color = (color or "blue").lower()
    path_style = (path_style or "short").lower()

    # Inject hidden env vars for runtime access
    apply_prompt_color_args(color)
    apply_prompt_path_args(path_style)

    # Build and apply the PS1 string
    ps1 = build_prompt_ps1(color, path_style)
    set_ps1(ps1)


def apply_prompt_color_args(color_style: str | None = None) -> None:
    """
    Stores the selected prompt color style into the environment.
    """
    set_prompt_color_style(color_style)  # type: ignore[arg-type]


def apply_prompt_path_args(path_style: str | None = None) -> None:
    """
    Stores the selected prompt path style into the environment.
    """
    set_prompt_path_style(path_style)  # type: ignore[arg-type]


def update_ps1_from_env() -> None:
    """
    Rebuilds PS1 based on stored styles, unless overridden (e.g. during execution).
    """
    # Skip update if PS1 was manually overridden
    if is_prompt_overridden():
        return

    # Retrieve stored prompt styles from environment
    color = get_prompt_color_style()
    path_style = get_prompt_path_style()

    # Rebuild and apply the PS1 string
    ps1 = build_prompt_ps1(color, path_style)
    set_ps1(ps1)
