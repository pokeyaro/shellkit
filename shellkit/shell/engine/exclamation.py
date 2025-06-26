"""
engine/exclamation.py

Handles history-based command shortcuts such as !!, !N, and !prefix.
"""

import readline

from shellkit.i18n import t
from shellkit.libc import println


def expand_history_shortcut(line: str) -> str | None:
    """
    Supports history expansion shortcuts:
      !!         → Previous command
      !3         → Command number 3 in history (1-based)
      !ls        → Most recent command starting with 'ls'
    """
    if not line.startswith("!"):
        return None

    hist_len = readline.get_current_history_length()

    # Case: !! → Expand to the previous command (skip !! itself)
    if line == "!!":
        if hist_len <= 1:
            println("\033[33m[warn]\033[0m %s", t("shell.engine.exclamation.no_prev"))
            return None
        # Search backward for the last valid command before !!
        for i in range(hist_len - 1, 0, -1):
            cmd = readline.get_history_item(i)
            if cmd != "!!":
                println("↪ %s", cmd)
                return cmd
        println("\033[33m[warn]\033[0m %s", t("shell.engine.exclamation.no_valid"))
        return None

    # Case: !N → Fetch the Nth command from history (1-based index)
    if line[1:].isdigit():
        idx = int(line[1:])
        if idx <= 0 or idx > hist_len:
            println("\033[31m[error]\033[0m %s", t("shell.engine.exclamation.out_of_range", idx=idx))
            return None
        cmd = readline.get_history_item(idx)
        println("↪ %s", cmd)
        # Recursively expand again in case it also starts with !
        return expand_history_shortcut(cmd) or cmd

    # Case: !prefix → Find the most recent command starting with given prefix
    prefix = line[1:]
    for i in range(hist_len, 0, -1):
        cmd = readline.get_history_item(i)
        if cmd and cmd.startswith(prefix):
            println("↪ %s", cmd)
            return cmd

    println("\033[33m[warn]\033[0m %s", t("shell.engine.exclamation.no_match", prefix=prefix))
    return None
