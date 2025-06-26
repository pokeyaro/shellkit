"""
sidecar/parser.py

Parses CLI arguments and startup options for PySH.
"""

import argparse
from typing import Union

from shellkit.i18n import t


class SpacedRawTextHelpFormatter(argparse.RawTextHelpFormatter):
    """
    Custom help formatter that adds spacing before each argument block.
    Improves readability of grouped CLI help messages.
    """
    def _format_action(self, action: argparse.Action) -> str:
        return "\n" + super()._format_action(action)


def validate_history_size(value: Union[str, int]) -> int:
    """
    Validates the --history-size argument to ensure it falls within a safe range.

    Raises:
        argparse.ArgumentTypeError: if the value is not a number or out of bounds.
    """
    try:
        size = int(value)
        min_history_size = 10
        max_history_size = 10000

        # Ensure value is within the allowed range
        if not min_history_size <= size <= max_history_size:
            raise argparse.ArgumentTypeError(
                t("shell.sidecar.parser.history_size.out_of_range", min=min_history_size, max=max_history_size)
            )
        return size
    except ValueError:
        raise argparse.ArgumentTypeError(t("shell.sidecar.parser.history_size.not_a_number"))


def parse_args() -> argparse.Namespace:
    """
    Parses and returns all CLI arguments for PySH.
    """
    # Create an ArgumentParser with custom help formatter
    parser = argparse.ArgumentParser(
        prog="pysh",
        usage=f"%(prog)s {t('shell.sidecar.parser.usage')}",
        description=f"🐚 ShellKit · {t('shell.sidecar.parser.description')}",
        add_help=False,
        formatter_class=SpacedRawTextHelpFormatter,
    )

    # === Main options ===

    # Run a single command and exit
    parser.add_argument(
        "-c", "--command",
        metavar="CMD",
        help=t("shell.sidecar.parser.command.help")
    )

    # Prompt color configuration
    parser.add_argument(
        "--prompt-color",
        metavar="COLOR",
        choices=["red", "green", "yellow", "blue", "magenta", "cyan", "white", "gray", "black"],
        default="blue",
        help=t("shell.sidecar.parser.prompt_color.help")
    )

    # Prompt path style configuration
    parser.add_argument(
        "--prompt-path",
        metavar="STYLE",
        choices=["none", "short", "full"],
        default="short",
        help=t("shell.sidecar.parser.prompt_path.help")
    )

    # Set shell history size (validated)
    parser.add_argument(
        "--history-size",
        type=validate_history_size,
        metavar="N",
        default=1000,
        help=t("shell.sidecar.parser.history_size.help")
    )

    # Toggle banner visibility
    parser.add_argument(
        "--no-banner",
        action="store_true",
        help=t("shell.sidecar.parser.no_banner.help")
    )

    # Toggle reminder visibility
    parser.add_argument(
        "--no-reminder",
        action="store_true",
        help=t("shell.sidecar.parser.no_reminder.help")
    )

    # === Mode switches ===

    # Switch quiet mode
    parser.add_argument(
        "-q", "--quiet",
        action="store_true",
        help=t("shell.sidecar.parser.quiet.help")
    )

    # Switch safe mode
    parser.add_argument(
        "-s", "--safe",
        action="store_true",
        help=t("shell.sidecar.parser.safe.help")
    )

    # === Debugging ===

    # Enable command parsing & shell-level debug logging
    parser.add_argument(
        "-d", "--debug",
        action="store_true",
        help=t("shell.sidecar.parser.debug.help")
    )

    # Trace function calls inside echo/printf implementation
    parser.add_argument(
        "--trace-echo",
        action="store_true",
        help=t("shell.sidecar.parser.trace_echo.help")
    )

    # Shortcut for enabling both debug + trace-echo
    parser.add_argument(
        "--thinking",
        action="store_true",
        help=t("shell.sidecar.parser.thinking.help")
    )

    # Experimental: trace libc/native/syscall across layers
    parser.add_argument(
        "--deep-thinking",
        action="store_true",
        help=t("shell.sidecar.parser.deep_thinking.help")
    )

    # === Meta ===

    # Display help and exit
    parser.add_argument(
        "-h", "--help",
        action="help",
        help=t("shell.sidecar.parser.help.help")
    )

    # Print version metadata and exit
    parser.add_argument(
        "-V", "--version",
        action="store_true",
        help=t("shell.sidecar.parser.version.help")
    )

    # Parse arguments
    args = parser.parse_args()

    # --thinking implies --debug + --trace-echo
    if args.thinking:
        args.debug = True
        args.trace_echo = True

    return args
