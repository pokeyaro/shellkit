"""
environs/constants.py

Defines environment variable keys, default values, hidden flags, and protected key list.
"""

from pathlib import Path

# Path to the default environment template file
TEMPLATE_PATH = Path(__file__).parent / "template.json"


# Standard environment variable keys
ENV_KEY_USER = "USER"
ENV_KEY_HOME = "HOME"
ENV_KEY_SHELL = "SHELL"
ENV_KEY_PWD = "PWD"
ENV_KEY_PS1 = "PS1"
ENV_KEY_LANG = "LANG"
ENV_KEY_SYSINFO = "SYSINFO"
ENV_KEY_HISTORY_SIZE = "HISTORY_SIZE"


# Subkeys
ENV_KEY_PWD_CUR = "current"
ENV_KEY_PWD_PREV = "previous"

ENV_KEY_SYSINFO_ARCH = "arch"
ENV_KEY_SYSINFO_UNAME = "uname"
ENV_KEY_SYSINFO_KERNEL_VERSION = "kernel_version"
ENV_KEY_SYSINFO_OS_RELEASE = "os_release"
ENV_KEY_SYSINFO_CPU = "cpu"
ENV_KEY_SYSINFO_CORES = "cores"
ENV_KEY_SYSINFO_LOGICAL_CORES = "logical_cores"
ENV_KEY_SYSINFO_HYPERTHREADING = "hyperthreading"
ENV_KEY_SYSINFO_MEMORY_TOTAL = "mem_total"
ENV_KEY_SYSINFO_DISK_TOTAL = "disk_total"
ENV_KEY_SYSINFO_PRODUCT_NAME = "product_name"
ENV_KEY_SYSINFO_SERIAL_NUMBER = "serial_number"


# Default values (used for fallback when data is missing)
DEFAULT_USER = "anonymous"
DEFAULT_HOME = "/home/anonymous"
DEFAULT_SHELL = "/bin/pysh"
DEFAULT_PWD = {
    ENV_KEY_PWD_CUR: "~",
    ENV_KEY_PWD_PREV: ""
}
DEFAULT_PS1 = "pysh ➜  "
DEFAULT_LANG = "en"
DEFAULT_SYSINFO = {
    ENV_KEY_SYSINFO_ARCH: "unknown",
    ENV_KEY_SYSINFO_UNAME: "unknown",
    ENV_KEY_SYSINFO_KERNEL_VERSION: "x.y.z",
    ENV_KEY_SYSINFO_OS_RELEASE: "unknown",
    ENV_KEY_SYSINFO_CPU: "unknown",
    ENV_KEY_SYSINFO_CORES: 0,
    ENV_KEY_SYSINFO_LOGICAL_CORES: 0,
    ENV_KEY_SYSINFO_HYPERTHREADING: False,
    ENV_KEY_SYSINFO_MEMORY_TOTAL: "0GB",
    ENV_KEY_SYSINFO_DISK_TOTAL: "0GB",
    ENV_KEY_SYSINFO_PRODUCT_NAME: "unknown",
    ENV_KEY_SYSINFO_SERIAL_NUMBER: "unknown",
}
DEFAULT_HISTORY_SIZE = 1000


# Hidden internal control variables (set by CLI args or runtime logic)
ENV_HIDDEN_BANNER_DISABLED = "_ENV__BANNER_DISABLED"
ENV_HIDDEN_REMINDER_DISABLED = "_ENV__REMINDER_DISABLED"
ENV_HIDDEN_QUIET_MODE = "_ENV__QUIET_MODE"
ENV_HIDDEN_SAFE_MODE = "_ENV__SAFE_MODE"
ENV_HIDDEN_PROMPT_FLAG = "_ENV__PROMPT_OVERRIDDEN"
ENV_HIDDEN_PROMPT_COLOR = "_ENV__PROMPT_STYLE_COLOR"
ENV_HIDDEN_PROMPT_PATH = "_ENV__PROMPT_STYLE_PATH"


# Protected keys (not allowed to be changed via `export`)
PROTECTED_ENV_KEYS = {
    # Read-only identity
    ENV_KEY_USER,
    ENV_KEY_HOME,
    ENV_KEY_SHELL,
    ENV_KEY_LANG,

    # Runtime state
    ENV_KEY_PWD,
    ENV_KEY_SYSINFO,

    # Config settings
    ENV_KEY_HISTORY_SIZE,
}
