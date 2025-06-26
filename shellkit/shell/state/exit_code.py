"""
state/exit_code.py

Defines standard exit codes used across PySH, based on the POSIX shell convention.
"""

from enum import IntEnum


class ExitCode(IntEnum):
    """
    Shell exit codes based on POSIX standards.
    """

    # Program exited normally without any error.
    SUCCESS = 0

    # General error (unspecified failure). Indicates failure without a clear reason.
    FAILURE = 1

    # Misuse of shell builtins, such as invalid arguments or incorrect syntax.
    USAGE_ERROR = 2

    # Command found but not executable (e.g., permission denied).
    PERMISSION_DENIED = 126

    # Command not found (non-existent or incorrect path).
    COMMAND_NOT_FOUND = 127

    # Invalid or semantically incorrect argument supplied.
    INVALID_ARGUMENT = 128

    # Interrupted by Ctrl+C (SIGINT). The process did not complete normally.
    SIGINT = 130

    # Terminated by Ctrl+\ (SIGQUIT), often with a core dump.
    SIGQUIT = 131

    # Pipe write failure (e.g., broken pipe due to early close like `head`).
    PIPEFAIL = 141

    # Internal shell error or uncaught exception. Indicates serious failure (e.g., crash, illegal call).
    INTERNAL_ERROR = 255


# Backward compatibility: preserve legacy constant names
EXIT_SUCCESS = ExitCode.SUCCESS
EXIT_FAILURE = ExitCode.FAILURE
EXIT_USAGE_ERROR = ExitCode.USAGE_ERROR
EXIT_PERMISSION_DENIED = ExitCode.PERMISSION_DENIED
EXIT_COMMAND_NOT_FOUND = ExitCode.COMMAND_NOT_FOUND
EXIT_INVALID_ARGUMENT = ExitCode.INVALID_ARGUMENT
EXIT_SIGINT = ExitCode.SIGINT
EXIT_SIGQUIT = ExitCode.SIGQUIT
EXIT_PIPEFAIL = ExitCode.PIPEFAIL
EXIT_INTERNAL_ERROR = ExitCode.INTERNAL_ERROR
