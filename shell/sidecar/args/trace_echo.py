"""
sidecar/args/trace_echo.py

Handles the --trace-echo flag to enable libc-level call tracing.
"""

from i18n import t
from inspector.trace import enable_trace
from inspector.debug import debug_startup


def apply_trace_echo_args() -> None:
    """
    Enables internal function call tracing for echo/printf.
    """
    enable_trace()
    debug_startup(t("shell.sidecar.args.trace_echo.trace_enabled"))
