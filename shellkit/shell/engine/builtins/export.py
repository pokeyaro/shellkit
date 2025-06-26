"""
engine/builtins/export.py

Implements the `export` shell command.
Supports setting environment variables, protecting system keys, and ANSI-aware prompt updates.
"""

import re

from shellkit.i18n import t
from shellkit.libc import eprintln, println
from shellkit.shell.environs import get_env, set_env
from shellkit.shell.environs.accessors import set_prompt_overridden
from shellkit.shell.environs.constants import ENV_KEY_PS1, PROTECTED_ENV_KEYS
from shellkit.shell.state.exit_code import EXIT_FAILURE, EXIT_SUCCESS, EXIT_USAGE_ERROR, ExitCode


EXPORT_PATTERN = re.compile(r"^[\w\u4e00-\u9fff][\w\u4e00-\u9fff\d_]*=.+$")


def export_builtin(args: list[str]) -> ExitCode:
    """
    Implements the `export` built-in command.

    Sets environment variables in the current shell session. Supports:
        - Assigning multiple variables at once.
        - Protecting system and read-only variables.
        - Special handling for PS1 with ANSI escape parsing.

    Behavior:
        - Valid keys must start with a Unicode letter or underscore and consist of alphanumerics, underscores, or CJK characters.
        - The format must be VAR=value or ['VAR', '=', 'value'] (auto-merged).
        - System-reserved keys (in PROTECTED_ENV_KEYS) are immutable.
        - Hidden internal keys starting with _ENV__ can only be set once.
        - Setting ENV_KEY_PS1 triggers ANSI interpretation and prompt override.

    Args:
        args: List of strings in the format VAR=value (or a tokenized equivalent like ['VAR', '=', 'value']).

    Returns:
        ExitCode:
            - EXIT_SUCCESS (0) if all variables are set successfully.
            - EXIT_FAILURE (1) if any variable fails to set.
            - EXIT_USAGE_ERROR (2) if no arguments are provided.
    """
    # No arguments provided
    if not args:
        println(t("shell.engine.builtin.export.missing_args"))
        println(t("shell.engine.builtin.export.usage"))
        println(t("shell.engine.builtin.export.tip_more_info"))
        return EXIT_USAGE_ERROR

    try:
        # Merge ['VAR', '=', 'value'] into ['VAR=value']
        args = _normalize_export_args(args)

        success_count = 0
        error_count = 0

        # Process each key=value pair
        for raw in args:
            # Reject invalid format
            if not EXPORT_PATTERN.match(raw):
                println(t("shell.engine.builtin.export.invalid_format", arg=raw))
                println(t("shell.engine.builtin.export.expected_format"))
                error_count += 1
                continue

            try:
                key, val = raw.split("=", 1)
            except ValueError:
                println("export: invalid format: %s", raw)
                error_count += 1
                continue

            # Block protected system keys
            if key in PROTECTED_ENV_KEYS:
                println("\033[33m[warn]\033[0m " + t("shell.engine.builtin.export.protected_key", **{"key": key}))
                error_count += 1
                continue

            # Block rewrites to special internal keys
            if key.startswith("_ENV__") and get_env(key) is not None:
                println("\033[33m[warn]\033[0m " + t("shell.engine.builtin.export.internal_key_once", **{"key": key}))
                error_count += 1
                continue

            try:
                # Special case: PS1 with ANSI escape sequence support
                if key == ENV_KEY_PS1:
                    val = _interpret_ansi(val)
                    set_prompt_overridden()

                set_env(key, val)
                success_count += 1

            except Exception as e:
                eprintln(t("shell.engine.builtin.export.error_set", **{"key": key}, error=str(e)))
                error_count += 1

        # Determine return code
        if error_count > 0:
            if success_count > 0:
                # Partial success
                return EXIT_FAILURE
            else:
                # Total failure
                return EXIT_FAILURE
        else:
            # All success
            return EXIT_SUCCESS

    except Exception as e:
        eprintln(t("shell.engine.builtin.export.unexpected_error", str(e)))
        return EXIT_FAILURE


def _normalize_export_args(args: list[str]) -> list[str]:
    """
    Merges tokenized triplets like ['FOO', '=', 'bar'] into ['FOO=bar'].
    Enables tolerant input parsing.

    Example:
    Input:  ['FOO', '=', 'bar', 'BAZ=qux']
    Output: ['FOO=bar', 'BAZ=qux']
    """
    fixed = []
    i = 0
    while i < len(args):
        if i + 2 < len(args) and args[i + 1] == "=":
            fixed.append(f"{args[i]}={args[i+2]}")
            i += 3
        else:
            fixed.append(args[i])
            i += 1
    return fixed


def _interpret_ansi(s: str) -> str:
    """
    Converts escaped ANSI code (\033) into actual escape characters.

    Used for custom PS1 prompt formatting.
    """
    return s.replace(r"\033", "\033")
