"""
engine/builtins/env.py

Implements the `env` shell command.
Supports printing all environment variables in either plain or colorized JSON format.
"""

import json
from typing import Any

from shellkit.i18n import t
from shellkit.libc import eprintln, println
from shellkit.shell.environs import all_env
from shellkit.shell.state.exit_code import EXIT_FAILURE, EXIT_SUCCESS, EXIT_USAGE_ERROR, ExitCode


def env_builtin(args: list[str]) -> ExitCode:
    """
    Implements the `env` built-in command.

    Prints all current environment variables.

    Features:
        - Outputs `KEY=VALUE` pairs by default.
        - Supports `--json` flag to print variables in a colorized JSON format.

    Args:
        args: Command-line arguments passed to `env`. Accepts at most one argument (`--json`).

    Returns:
        ExitCode:
            - EXIT_SUCCESS (0) on successful output.
            - EXIT_FAILURE (1) if variables could not be fetched.
            - EXIT_USAGE_ERROR (2) if invalid or excessive arguments are provided.
    """
    # Validate arguments
    if len(args) > 1:
        println(t("shell.engine.builtin.env.too_many_args"))
        println(t("shell.engine.builtin.env.usage"))
        return EXIT_USAGE_ERROR

    if args and args[0] not in ["--json"]:
        println(t("shell.engine.builtin.env.invalid_option", opt=args[0]))
        println(t("shell.engine.builtin.env.usage"))
        return EXIT_USAGE_ERROR

    try:
        # Fetch environment variables
        env = all_env()

        if not env:
            println(t("shell.engine.builtin.env.no_env"))
            return EXIT_FAILURE

        # Print in JSON or plain format
        if args and args[0] == "--json":
            println(colorize_json(env))
        else:
            for k, v in env.items():
                println("%s=%s", k, v)

        return EXIT_SUCCESS

    except Exception as e:
        eprintln(t("shell.engine.builtin.env.error_retrieval", msg=str(e)))
        return EXIT_FAILURE


def colorize_json(obj: dict[str, Any]) -> str:
    """
    Converts a dictionary into a colorized JSON string using ANSI escape sequences.

    Color mapping:
        - Brackets: Bold orange
        - Keys: Bold blue
        - Strings: Green
        - Numbers: Cyan
        - Booleans and null: Pink

    Args:
        obj: A dictionary representing key-value pairs.

    Returns:
        A string containing the JSON with ANSI color codes embedded.
    """
    # === ANSI color definitions ===
    RESET = "\033[0m"
    BRACKET = "\033[1;38;5;208m"  # Bright orange for {}, []
    KEY = "\033[1;38;5;39m"       # Bright blue for object keys
    STRING = "\033[38;5;82m"      # Bright green for string values
    NUMBER = "\033[96m"           # Cyan for numbers
    BOOL = "\033[38;5;201m"       # Pink for true, false, null

    # Serialize the object into a JSON string with indentation
    raw = json.dumps(obj, indent=2, ensure_ascii=False)

    def colorize_char_by_char(text: str) -> str:
        """
        Walks through the JSON string character by character,
        applying ANSI colors based on structure and content type.
        """
        result = []
        i = 0
        in_string = False  # Tracks whether we are inside a string

        while i < len(text):
            char = text[i]

            # --- Detect and handle strings (unescaped quote) ---
            if char == '"' and (i == 0 or text[i - 1] != "\\"):
                in_string = not in_string
                if in_string:
                    # Find the end of the full string (handles escape characters)
                    string_end = i + 1
                    while string_end < len(text):
                        if text[string_end] == '"' and text[string_end - 1] != "\\":
                            break
                        string_end += 1

                    full_string = text[i : string_end + 1]

                    # Determine if this is a key (followed by colon `:`)
                    next_non_space = string_end + 1
                    while next_non_space < len(text) and text[next_non_space] in " \t":
                        next_non_space += 1

                    if next_non_space < len(text) and text[next_non_space] == ":":
                        # key
                        result.append(KEY + full_string + RESET)
                    else:
                        # value
                        result.append(STRING + full_string + RESET)

                    i = string_end + 1
                    in_string = False
                    continue

            # If still inside a string, output as-is
            if in_string:
                result.append(char)
                i += 1
                continue

            # --- Highlight brackets ---
            if char in "{}[]":
                result.append(BRACKET + char + RESET)

            # --- Highlight numbers (supports negative and decimal) ---
            elif char.isdigit() or (char == "-" and i + 1 < len(text) and text[i + 1].isdigit()):
                num_start = i
                if char == "-":
                    i += 1
                while i < len(text) and (text[i].isdigit() or text[i] == "."):
                    i += 1
                number = text[num_start:i]
                result.append(NUMBER + number + RESET)
                continue

            # --- Highlight booleans and null ---
            elif char in "tfn":
                if text[i:].startswith("true"):
                    result.append(BOOL + "true" + RESET)
                    i += 4
                    continue
                elif text[i:].startswith("false"):
                    result.append(BOOL + "false" + RESET)
                    i += 5
                    continue
                elif text[i:].startswith("null"):
                    result.append(BOOL + "null" + RESET)
                    i += 4
                    continue
                else:
                    result.append(char)
            else:
                # Normal characters (colon, comma, space, newline, etc.)
                result.append(char)

            i += 1

        return "".join(result)

    return colorize_char_by_char(raw)
