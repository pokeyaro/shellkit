"""
engine/builtins/help.py

Implements the `help` shell command.
Provides access to built-in command documentation and manual pages.
Supports fallback viewing via external tools (glow, bat, mdcat, less).
"""

import shutil
import platform
import subprocess

from shellkit.i18n import t
from shellkit.libc import println, eprintln
from shellkit.inspector.debug import debug_docs

from .sleep import sleep_builtin
from shellkit.shell.docs import (
    get_manual,
    has_manual,
    list_manuals,
    get_manual_path,
    get_help_text,
)
from shellkit.shell.state.exit_code import (
    EXIT_SUCCESS,
    EXIT_FAILURE,
    EXIT_USAGE_ERROR,
    ExitCode,
)


def help_builtin(args: list[str]) -> ExitCode:
    """
    Implements the `help` built-in command.

    Displays help documentation for shell commands in markdown format. If no arguments
    are given, it prints an overview of all built-in commands. Supports viewing a specific
    command's manual or listing all available help topics.

    Behavior:
        - No arguments: shows full command list with usage hints.
        - Argument is a command name: opens its markdown help page.
        - Argument is '-l' or '--list-docs': lists all available help topics.
        - Tries external viewers: glow > bat > mdcat > less.
        - If all viewers are unavailable, falls back to plain-text output.

    Args:
        args: Command-line arguments passed to `help`.

    Returns:
        ExitCode:
            - EXIT_SUCCESS (0) on successful display.
            - EXIT_FAILURE (1) if the help file was not found or viewer failed.
            - EXIT_USAGE_ERROR (2) for invalid usage (e.g. too many args).
    """
    # Validate argument count
    if len(args) > 1:
        println(t("shell.engine.builtin.help.too_many_args"))
        println(t("shell.engine.builtin.help.usage"))
        println(t("shell.engine.builtin.help.usage_list_docs"))
        return EXIT_USAGE_ERROR

    try:
        # List all available help topics
        if args and args[0] in ("-l", "--list-docs"):
            topics = list_manuals()
            println("\033[1m" + t("shell.engine.builtin.help.available_topics") + ":\033[0m\n")
            for doc in topics:
                println(f"  {doc}")
            println(f"\n{t('shell.engine.builtin.help.total_topics').format(count=len(topics))}")
            return EXIT_SUCCESS

        # Show general help overview (command list)
        if not args:
            debug_docs(t("shell.engine.builtin.help.show_index"), doc_type="index")
            println(get_help_text())
            return EXIT_SUCCESS

        # Show specific command help
        name = args[0]

        # Reject invalid command names (prevent path injection)
        if not name.replace("-", "").replace("_", "").isalnum():
            println(t("shell.engine.builtin.help.invalid_command"), name)
            return EXIT_USAGE_ERROR

        # Load markdown file and content
        doc_file = get_manual_path(name)
        doc_content = get_manual(name)

        if not has_manual(name):
            println(doc_content)
            return EXIT_FAILURE

        # Try using external markdown renderers
        for viewer in ["glow", "bat", "mdcat"]:
            if shutil.which(viewer):
                try:
                    result = subprocess.run([viewer, str(doc_file)], capture_output=False)
                    if result.returncode != 0:
                        return EXIT_FAILURE
                    return EXIT_SUCCESS
                except Exception as e:
                    eprintln(t("shell.engine.builtin.help.viewer_error"), viewer, str(e))
                    continue

        # No markdown renderer found → show hint and fallback
        _print_glow_hint()

        # Delay fallback using countdown
        sleep_builtin([
            "3",
            t("shell.engine.builtin.help.countdown"),
            "--done="
        ])

        # Try fallback pager: less
        if shutil.which("less"):
            try:
                result = subprocess.run(["less", str(doc_file)])
                if result.returncode != 0:
                    return EXIT_FAILURE
                return EXIT_SUCCESS
            except Exception as e:
                eprintln(t("shell.engine.builtin.help.less_error"), str(e))
                return EXIT_FAILURE
        else:
            println(t("shell.engine.builtin.help.less_unavailable"))
            println(t("shell.engine.builtin.help.fallback_path"), doc_file)
            return EXIT_FAILURE

    except Exception as e:
        eprintln(t("shell.engine.builtin.help.unexpected_error"), str(e))
        return EXIT_FAILURE


def _print_glow_hint() -> None:
    """
    Prints installation hints for markdown viewers when none are found.

    Based on the host platform, suggests:
        - Homebrew (macOS)
        - apt or yum (Linux)
        - GitHub page (other platforms)

    Intended as a fallback when 'glow', 'bat', and 'mdcat' are unavailable,
    helping the user improve their terminal help rendering experience.
    """

    println(t("shell.engine.builtin.help.no_viewer_found"))

    system = platform.system().lower()

    if system == "darwin":
        # macOS user hint
        println("\033[33m[hint]\033[0m " + t("shell.engine.builtin.help.hint.brew") + "\n")

    elif system == "linux":
        # Linux hint based on package manager
        if shutil.which("apt"):
            println("\033[33m[hint]\033[0m " + t("shell.engine.builtin.help.hint.apt") + "\n")
        elif shutil.which("yum"):
            println("\033[33m[hint]\033[0m " + t("shell.engine.builtin.help.hint.yum") + "\n")
        else:
            println("\033[33m[hint]\033[0m " + t("shell.engine.builtin.help.hint.url") + "\n")

    else:
        # Generic fallback for unsupported platforms
        println("\033[33m[hint]\033[0m " + t("shell.engine.builtin.help.hint.url") + "\n")
