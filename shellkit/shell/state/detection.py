"""
state/detection.py

Provides logic to detect whether the current shell is a login shell.
"""

import os
import platform
import subprocess
import sys


def is_login_shell() -> bool:
    """
    Determines if the current shell is a login shell (lightweight check without psutil).
    """

    # Non-interactive input means it's not a login shell
    if not sys.stdin.isatty():
        return False

    # Check parent process name
    try:
        parent_name = _get_parent_process_name()
        if parent_name:
            parent_name = parent_name.lower()

            # If parent is another shell, it's likely non-login
            shell_names = {"bash", "zsh", "sh", "fish", "dash", "tcsh", "csh"}
            if any(shell in parent_name for shell in shell_names):
                return False

            # If parent is terminal or login service, it's likely a login shell
            login_names = {
                "terminal",
                "iterm",
                "gnome-terminal",
                "konsole",
                "xterm",
                "alacritty",
                "kitty",
                "wezterm",
                "sshd",
                "login",
                "getty",
            }
            if any(name in parent_name for name in login_names):
                return True

    except (OSError, subprocess.SubprocessError, ValueError):
        pass

    # Check for SSH-related environment variables
    if any(var in os.environ for var in ["SSH_CLIENT", "SSH_CONNECTION", "SSH_TTY"]):
        return True

    # Fallback: assume login shell by default
    return True


def _get_parent_process_name() -> str:
    """
    Returns the name of the parent process (cross-platform).
    """
    system = platform.system().lower()
    parent_pid = os.getppid()

    try:
        if system == "darwin":  # macOS
            # Use `ps` command to get parent process name
            result = subprocess.run(
                ["ps", "-p", str(parent_pid), "-o", "comm="],
                capture_output=True,
                text=True,
                timeout=2,
            )
            if result.returncode == 0:
                return result.stdout.strip()

        elif system == "linux":  # Linux
            # Read from /proc filesystem
            try:
                with open(f"/proc/{parent_pid}/comm", "r") as f:
                    return f.read().strip()
            except (FileNotFoundError, PermissionError):
                pass

            # Use `ps` command as fallback
            result = subprocess.run(
                ["ps", "-p", str(parent_pid), "-o", "comm="],
                capture_output=True,
                text=True,
                timeout=2,
            )
            if result.returncode == 0:
                return result.stdout.strip()

        else:  # Windows or unknown system
            # Fallback: attempt to use generic `ps` command
            result = subprocess.run(
                ["ps", "-p", str(parent_pid), "-o", "comm="],
                capture_output=True,
                text=True,
                timeout=2,
            )
            if result.returncode == 0:
                return result.stdout.strip()

    except (subprocess.TimeoutExpired, subprocess.SubprocessError, OSError):
        pass

    return ""
