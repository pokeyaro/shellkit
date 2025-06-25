"""
shell.runtime

Handles shell startup, input loop, and user interaction.
"""

from .launcher import launch
from .metadata import get_metadata


__all__ = ["launch", "get_metadata"]
