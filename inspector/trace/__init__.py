"""
inspector.trace

Libc-layer tracing system for visualizing internal function call chains
(e.g., echo/printf → write → syscall) via decorators and context managers.

Design Notes:
- core.py:       Manages global trace state, call stack, and buffered output
- context.py:    Enables scoped tracing with `with tracing(): ...` blocks;
                 integrates with call stack for entrypoint tracking
- decorator.py:  Provides `@trace_call` for instrumenting target functions;
                 checks both global and context-local flags before tracing
- format.py:     Formats function arguments and return values for compact display
- printer.py:    Outputs buffered logs with ANSI styling to stderr
- tree.py:       Generates visual indentation and tree prefixes for nested calls

This module is enabled via the `--trace-echo` CLI flag.
Primarily used for inspecting echo/printf call paths from shell to libc.
Not intended for external use.
"""

from .core import (
    enable_trace,
    disable_trace,
    is_trace_enabled,
)
from .context import tracing
from .decorator import trace_call


__all__ = [
    "enable_trace", "disable_trace", "is_trace_enabled",
    "tracing",
    "trace_call",
]
