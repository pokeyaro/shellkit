"""
shell.sidecar

Parses and applies CLI arguments during shell startup.
"""

from .parser import parse_args
from .handler import handle_args


__all__ = ["parse_args", "handle_args"]
