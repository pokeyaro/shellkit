"""
state/context.py

Manages core shell runtime state (e.g. exit code, process ID, login status).
"""

import os
from typing import Optional

from .detection import is_login_shell
from .exit_code import EXIT_SUCCESS, ExitCode


class ShellState:
    """
    Global runtime state for the shell.
    """

    def __init__(self) -> None:
        # Detect if shell is a login shell
        self._is_login = is_login_shell()

        self.last_exit_status = EXIT_SUCCESS
        self.process_id = os.getpid()

        # Set program name based on login shell status
        if self._is_login:
            self.program_name = "-pysh"
        else:
            self.program_name = "pysh"

    @property
    def is_login_shell(self) -> bool:
        return self._is_login

    def set_success(self) -> None:
        self.last_exit_status = EXIT_SUCCESS

    def set_exit_status(self, status: int | ExitCode) -> None:
        """Set the exit status of the last executed command."""
        self.last_exit_status = status  # type: ignore[assignment]

    def exit_status(self) -> int | ExitCode:
        """Get the exit status of the last executed command."""
        return self.last_exit_status

    def special_var(self, name: str) -> Optional[str]:
        """Return the value of special shell variables like $?, $$, $0."""
        if name == "?":
            return str(self.last_exit_status)
        elif name == "$":
            return str(self.process_id)
        elif name == "0":
            return self.program_name
        return None


# Global shell state instance
_shell_state = ShellState()


def get_context() -> ShellState:
    """Return the global shell state instance."""
    return _shell_state
