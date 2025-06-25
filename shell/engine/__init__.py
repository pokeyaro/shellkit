"""
shell.engine

Main interface for handling shell input.
Provides `handle_line()` to coordinate parsing, alias resolution, and command dispatching.
"""

from .dispatcher import handle_line


__all__ = ["handle_line"]
