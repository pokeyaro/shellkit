"""
engine/tables.py

Built-in command registry and alias mappings for the shell.
Defines supported commands, their handlers, alias shortcuts,
unsafe command warnings, and common completions.
"""

from collections.abc import Callable

from shellkit.shell.state.exit_code import ExitCode

from .builtins import (
    alias_builtin,
    arch_builtin,
    cd_builtin,
    clear_builtin,
    copyright_builtin,
    date_builtin,
    debug_builtin,
    echo_builtin,
    env_builtin,
    exit_builtin,
    export_builtin,
    help_builtin,
    history_builtin,
    license_builtin,
    locale_builtin,
    machinfo_builtin,
    printf_builtin,
    pwd_builtin,
    sleep_builtin,
    tree_builtin,
    uname_builtin,
    which_builtin,
    whoami_builtin,
)


# Built-in command table: maps command name to (handler function, brief description)
BUILTIN_TABLE: dict[str, tuple[Callable[[list[str]], ExitCode], str]] = {
    "alias":     (alias_builtin, "Display all built-in command aliases"),
    "arch":      (arch_builtin, "Print machine architecture using system arch"),
    "cd":        (cd_builtin, "Change current directory"),
    "clear":     (clear_builtin, "Clear the screen"),
    "copyright": (copyright_builtin, "Show copyright info"),
    "date":      (date_builtin, "Print current system time"),
    "debug":     (debug_builtin, "Control debug system (reset counter, show status)"),
    "echo":      (echo_builtin, "Print arguments to stdout"),
    "env":       (env_builtin, "Print current shell variables"),
    "exit":      (exit_builtin, "Exit the shell"),
    "export":    (export_builtin, "Set a shell variable"),
    "help":      (help_builtin, "Show available commands"),
    "history":   (history_builtin, "Show command history of the current session"),
    "license":   (license_builtin, "Show license text"),
    "locale":    (locale_builtin, "Get or set the current language (PYSH_LANG)"),
    "machinfo":  (machinfo_builtin, "Show detailed system information"),
    "printf":    (printf_builtin, "Formatted output (like C)"),
    "pwd":       (pwd_builtin, "Print current working directory"),
    "quit":      (exit_builtin, "Alias for exit"),
    "sleep":     (sleep_builtin, "Pause execution for N seconds"),
    "tree":      (tree_builtin, "List directory structure as a tree view"),
    "uname":     (uname_builtin, "Show system info (like 'uname')"),
    "which":     (which_builtin, "Locate a command and show its source"),
    "whoami":    (whoami_builtin, "Show current user name"),
}


# Alias mapping table: shared by both parser and `alias` command
ALIAS_TABLE: dict[str, tuple[str, list[str]]] = {
    # Navigation shortcuts
    "..": ("cd", [".."]),
    ".": ("cd", ["."]),
    "cls": ("clear", []),

    # Common operations
    "?": ("help", []),
    "md": ("mkdir", ["-p"]),
    "cp": ("cp", ["-a"]),

    # Shell exit shortcuts
    r"\q": ("quit", []),

    # Debug-related aliases
    r"\d": ("debug", []),
    r"\dr": ("debug", ["reset"]),
    r"\ds": ("debug", ["status"]),
    r"\doff": ("debug", ["off"]),
    r"\d?": ("debug", ["help"]),

    # File and directory listings
    "ll": ("ls", ["--color=auto", "-l", "-h"]),
    "l":  ("ls", ["--color=auto", "-l", "-A"]),
    "dir": ("ls", ["-l", "-h"]),

    # System info
    "df": ("df", ["-h"]),
    "ipa": ("ip", ["address"]),
}


# High-risk (potentially dangerous) command list
UNSAFE_TABLE: list[str] = [
    "dd",
    "kill",
    "rm",
    "rmdir",
    "reboot",
    "shutdown",
    "su",
    "sudo",
    "chmod",
    "chown",
    "mount",
    "umount"
]


# Common command suggestions for auto-completion
COMMON_COMMANDS = sorted(set(
    list(BUILTIN_TABLE.keys()) +
    UNSAFE_TABLE + [
        "?",
        "basename",
        "bash",
        "cat",
        "cls",
        "df",
        "dir",
        "du",
        "file",
        "groups",
        "head",
        "id",
        "last",
        "less",
        "ll",
        "ls",
        "man",
        "mkdir",
        "more",
        "mv",
        "ps",
        "stat",
        "tail",
        "tar",
        "top",
        "touch",
        "vim",
        "w",
        "who"
    ]
))
