"""
engine/dispatcher.py

Dispatches shell input through history, alias, builtin, and fallback layers.
"""

from shellkit.i18n import t
from shellkit.inspector.debug import debug_shell
from shellkit.shell.state import get_context

from .exclamation import expand_history_shortcut
from .fallback import run_fallback
from .parser import parse_line
from .register import execute_builtin
from .resolver import resolve_alias


def handle_line(line: str) -> None:
    """
    Dispatches a user command line through several processing stages:
    - Expands history shortcuts (e.g. !N)
    - Applies alias resolution
    - Executes built-in commands first
    - Falls back to system commands if necessary
    """
    debug_shell(t("shell.engine.dispatcher.input_received", line=line))

    # Expand history shortcut, e.g. "!1" → command from history
    expanded = expand_history_shortcut(line)
    if expanded:
        debug_shell(t("shell.engine.dispatcher.history_expanded", original=line, expanded=expanded))
        line = expanded

    # Parse command and arguments: "ls -l" → ("ls", ["-l"])
    cmd, args = parse_line(line)
    debug_shell(t("shell.engine.dispatcher.parsed", cmd=cmd, args=args))

    # Skip if input is empty or just whitespace
    if not cmd:
        debug_shell(t("shell.engine.dispatcher.empty_skipped"))
        return

    # Resolve aliases: "ll" → ("ls", ["-l", "-h"])
    cmd, args = resolve_alias(cmd, args)

    # Try to execute a built-in command (e.g. cd, echo)
    debug_shell(t("shell.engine.dispatcher.check_builtin", cmd=cmd))
    if execute_builtin(cmd, args):
        return

    # Fall back to executing the system command
    debug_shell(t("shell.engine.dispatcher.fallback", cmd=cmd))
    status_code = run_fallback(cmd, args)

    debug_shell(t("shell.engine.dispatcher.fallback_done", cmd=cmd, code=status_code))
    get_context().set_exit_status(status_code)
