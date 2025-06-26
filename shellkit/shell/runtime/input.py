"""
runtime/input.py

Handles user input with support for line editing, Ctrl+C, and Ctrl+D behavior.
"""

from typing import NoReturn

from shellkit.i18n import t
from shellkit.inspector.debug import debug_repl, end_startup_phase
from shellkit.libc import graceful_exit, print
from shellkit.shell.environs.accessors import get_ps1
from shellkit.shell.runtime.readline import init_readline_once
from shellkit.shell.state import get_context
from shellkit.shell.state.exit_code import EXIT_SIGINT, EXIT_SUCCESS


def _get_prompt() -> str:
    """
    Returns the current prompt string.

    Defaults to PS1. Can be extended to support PS2, PS3, etc.
    """
    return get_ps1()


def _ctrl_d() -> NoReturn:
    """
    Handles Ctrl+D (EOF) for graceful shell exit.

    Triggers graceful_exit() with a message indicating Ctrl+D.
    """
    graceful_exit(EXIT_SUCCESS, message=" " + t("shell.runtime.input.ctrl_d_exit"))
    raise SystemExit


def _ctrl_c() -> str:
    """
    Handles Ctrl+C (KeyboardInterrupt) during input.

    Prints a newline and cancels current input by returning an empty string.
    """
    print()
    get_context().set_exit_status(EXIT_SIGINT)
    return ""


def read_user_input() -> str:
    """
    Reads a line of user input and handles common interrupts.

    Features:
    - Line editing, history, and tab completion via readline.
    - Ctrl+C cancels current input.
    - Ctrl+D exits the shell gracefully.
    - Returns the entered command string, or "" if cancelled.
    """
    init_readline_once()
    end_startup_phase()

    try:
        prompt = _get_prompt()
        return input(prompt)
    except EOFError:
        debug_repl(t("shell.runtime.input.ctrl_d"))
        _ctrl_d()
    except KeyboardInterrupt:
        debug_repl(t("shell.runtime.input.ctrl_c"))
        return _ctrl_c()
