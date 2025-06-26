"""
environs/initialize.py

Initializes shell environment variables from template and runtime patches.
"""

import json
from typing import Any

from .constants import TEMPLATE_PATH
from .patches import (
    patch_user,
    patch_home,
    patch_pwd,
    patch_ps1,
    patch_lang,
    patch_sysinfo,
)
from .store import set_env


def load_env_template() -> dict[str, Any]:
    """
    Loads the default environment variables from the JSON template file.
    """
    try:
        with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)  # type: ignore[no-any-return]
    except FileNotFoundError:
        raise RuntimeError("Missing template file.")


def inject_runtime_environs() -> None:
    """
    Injects real runtime environment values (overriding defaults in template):
    - USER   : retrieved via getpass
    - HOME   : resolved via os.path.expanduser("~")
    - PWD    : sets both current and previous working directories
    - PS1    : sets platform-specific prompt logo
    - LANG   : detected from PYSH_LANG > LANG > fallback (e.g., "zh", "en")
    - SYSINFO: collects and injects basic system info
    """
    for f in (
        patch_user,
        patch_home,
        patch_pwd,
        patch_ps1,
        patch_lang,
        patch_sysinfo,
    ):
        f()


def init_environs() -> None:
    """
    Initializes the in-memory shell environment.
    - Loads defaults from the template;
    - Preserves any pre-set hidden vars (e.g., from CLI args);
    - Applies runtime patches where needed.
    """
    template = load_env_template()

    # Write all template values into memory (skip if already present)
    for k, v in template.items():
        set_env(k, v, force=False)

    # Patch with real-time info
    inject_runtime_environs()
