"""
sidecar/args/debug.py

Handles the -d / --debug flag to enable shell-level debugging.
"""

from i18n import t
from inspector.debug import enable_debug, debug_startup


def apply_debug_args() -> None:
    """
    Enable shell debugging mode (parsing, dispatch, and flow tracing).
    """
    enable_debug()
    debug_startup(t("shell.sidecar.args.debug.startup"))
