"""
runtime/readline.py

Adds readline-based input enhancements, including history and tab completion.
"""

import os
import readline
from functools import lru_cache
from typing import Optional

from shellkit.shell.engine.tables import COMMON_COMMANDS
from shellkit.shell.environs.accessors import get_history_size


# Use a more precise caching mechanism
_completion_cache = []       # Cache of current completion candidates
_last_line_buffer = ""       # The last full line buffer during completion
_last_completion_begin = -1  # The last completion start index (from readline)


# Original tab-completion logic refined with help from Claude Opus 4
def completer(text: str, state: int) -> Optional[str]:
    """
    Provides command and file path completion (case-insensitive).

    Args:
        text (str): The current token being completed.
        state (int): The index of the completion attempt, as requested by readline.

    Returns:
        Optional[str]: A matching completion string for the given state, or None if no more matches.
    """
    global _completion_cache, _last_line_buffer, _last_completion_begin

    # Get current input line and cursor positions (for completion boundaries)
    current_line = readline.get_line_buffer()
    current_begin = readline.get_begidx()

    # Recompute completions if this is a new session or the line context has changed
    if (
        state == 0
        or current_line != _last_line_buffer
        or current_begin != _last_completion_begin
    ):
        _last_line_buffer = current_line
        _last_completion_begin = current_begin

        if current_begin == 0:
            # If cursor is at the start of the line, complete command names
            _completion_cache = [
                cmd for cmd in COMMON_COMMANDS if cmd.startswith(text)
            ]
        else:
            # Otherwise, complete as a file path

            # Split the input line into two tokens: command + remainder
            tokens = current_line.split(None, 1)
            path_part = tokens[1] if len(tokens) > 1 else ""
            target = path_part

            # Determine directory and file prefix
            if target.endswith("/"):
                # User is completing inside a directory
                dirname = target.rstrip("/")
                partial = ""
                prefix = target
            elif "/" in target:
                # User typed a partial path (e.g. ./foo/ba)
                dirname, partial = os.path.split(target)
                prefix = dirname + "/" if dirname else ""
            else:
                # No slash: complete from current directory
                dirname = "."
                partial = target
                prefix = ""

            try:
                # List files in the target directory
                entries = os.listdir(dirname)
                matches = []

                for entry in entries:
                    if entry.lower().startswith(partial.lower()):
                        # Decide how to return the matched entry depending on text and partial

                        if text == partial and partial:
                            # Case 1: Replace full token
                            result = entry
                        elif text and partial and partial.endswith(text):
                            # Case 2: text is a suffix of partial (e.g. text="c", partial="abc")
                            prefix_len = len(partial) - len(text)
                            if entry.startswith(partial[:prefix_len]):
                                result = entry[prefix_len:]
                            else:
                                result = entry
                        elif text == "" and partial:
                            # Case 3: Replace with suffix of entry
                            if entry.startswith(partial):
                                result = entry[len(partial):]
                            else:
                                result = entry
                        elif text == "" and prefix:
                            # Case 4: Cursor is right after a slash
                            result = entry
                        else:
                            # Case 5: Fallback to returning the full path
                            result = prefix + entry

                        # Append '/' if the entry is a directory
                        check_path = os.path.join(dirname, entry)
                        if os.path.isdir(check_path):
                            result += "/"

                        matches.append(result)

                _completion_cache = matches

            except Exception:
                # On failure (e.g., invalid path), clear cache
                _completion_cache = []

    # Return the cached result for the given state index
    if state < len(_completion_cache):
        return _completion_cache[state]
    else:
        return None


def is_libedit() -> bool:
    """
    Detects whether the platform uses libedit (macOS default).
    Checks for 'libedit' in `readline.__doc__`.
    """
    return "libedit" in str(readline.__doc__).lower()


@lru_cache(maxsize=1)
def init_readline_once() -> None:
    """
    Initializes readline functionality (run once only).
    - Detects GNU readline vs macOS libedit.
    - Sets up tab completion.
    - Sets command history length.
    - Can be extended with history file or keybindings in future.
    """
    # Register tab completion function
    readline.set_completer(completer)

    # Get history size from environment
    history_size = get_history_size()

    # Set maximum number of history entries
    readline.set_history_length(history_size)

    # Bind Tab key depending on backend
    if is_libedit():
        readline.parse_and_bind("bind ^I rl_complete")  # macOS
    else:
        readline.parse_and_bind("tab: complete")        # Linux / GNU
