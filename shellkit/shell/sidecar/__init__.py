"""
shell.sidecar

Parses and applies CLI arguments during shell startup.
"""

from .handler import handle_args
from .parser import parse_args


__all__ = ["handle_args", "parse_args"]
