"""
inspector.debug.layers

High-level debug entrypoints for shell-layer components (e.g. argv, alias, env).
"""

import random

from .core import _debug_print


def debug_startup(message: str) -> None:
    """
    Debug messages during shell startup phase.
    """
    _debug_print("🚀", "Startup", message)


def debug_argv(message: str) -> None:
    """
    Debug command-line args parsing.
    """
    _debug_print("💻", "Argv", message)


def debug_alias(message: str) -> None:
    """
    Debug alias resolution and expansion.
    """
    _debug_print("📎", "Alias", message)


def debug_shell(message: str) -> None:
    """
    Debug shell execution flow (main loop, input, eval).
    """
    _debug_print("🤔", "Shell", message)


def debug_env(message: str) -> None:
    """
    Debug shell environment variable access.
    """
    _debug_print("🌐", "Env", message)


def debug_builtin(message: str) -> None:
    """
    Debug builtin command execution.
    """
    _debug_print("🏠", "Builtin", message)


def debug_repl(message: str) -> None:
    """
    Debug REPL loop lifecycle (input/output).
    """
    _debug_print("🔄", "REPL", message)


def debug_docs(message: str, *, doc_type: str = "read") -> None:
    """
    Debug documentation access and fallback.
    """
    if doc_type == "index":
        emoji = "📚"  # index overview
    elif doc_type == "read":
        books = ["📓", "📔", "📒", "📕", "📗", "📘", "📙"]
        emoji = random.choice(books)  # reading a doc
    elif doc_type == "notfound":
        emoji = "❓"  # missing doc
    else:
        emoji = "📄"  # fallback
    _debug_print(emoji, "Docs", message)


def debug_exit(message: str) -> None:
    """
    Debug graceful exit or final cleanup.
    """
    _debug_print("🎉", "Exit", message)


def debug_libc(message: str) -> None:
    """
    Debug libc-level calls (used by --trace-echo).
    """
    _debug_print("🧬", "Libc", message)
