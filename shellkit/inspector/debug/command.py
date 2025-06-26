"""
inspector.debug.command

Command handlers for shell-level debug control (reset, status, off, help).
"""

from shellkit.i18n import t
from shellkit.libc import println

from .core import disable_debug, get_counter, is_debug_enabled, reset_counter


def debug_command(cmd: str) -> None:
    """
    Dispatches internal debug subcommands.
    """
    if not is_debug_enabled():
        return

    cmd = cmd.strip().lower()

    if cmd == "reset":
        println("\033[33m[DEBUG] %s\033[0m", t("inspector.debug.command.reset_done"))
        reset_counter()

    elif cmd == "status":
        prefix = t("inspector.debug.command.status_prefix")
        counter_label = t("inspector.debug.command.counter")
        status = t("inspector.debug.command.status_enabled") if is_debug_enabled() else t("inspector.debug.command.status_disabled")
        counter_val = get_counter()
        println("\033[33m[DEBUG] %s: %s, %s = %d\033[0m", prefix, status, counter_label, counter_val)

    elif cmd == "off":
        disable_debug()
        println("\033[33m[DEBUG] %s\033[0m", t("inspector.debug.command.disabled"))

    elif cmd in ("help", "?"):
        println("\033[33m[DEBUG] %s\033[0m", t("inspector.debug.command.help_title"))
        println("  reset  - " + t("inspector.debug.command.help_reset"))
        println("  status - " + t("inspector.debug.command.help_status"))
        println("  off    - " + t("inspector.debug.command.help_off"))
        println("  help   - " + t("inspector.debug.command.help_help"))

    else:
        println("\033[33m[DEBUG] %s: %s (%s)\033[0m",
                t("inspector.debug.command.unknown_cmd"),
                cmd,
                t("inspector.debug.command.help_suggestion"))


def debug_reset() -> None:
    """
    Resets the debug counter.
    """
    debug_command("reset")


def debug_status() -> None:
    """
    Prints the current debug status.
    """
    debug_command("status")


def debug_off() -> None:
    """
    Disables debug mode.
    """
    debug_command("off")


def debug_help() -> None:
    """
    Shows help for debug subcommands.
    """
    debug_command("help")
