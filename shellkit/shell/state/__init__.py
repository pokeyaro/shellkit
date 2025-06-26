"""
shell.state

Manages global runtime state and exit codes for the shell.
"""

from .context import get_context


__all__ = ["get_context"]
