"""
runtime/launcher.py

Bootstraps the shell by showing the banner, starting reminders, and entering REPL.
"""

from shellkit.i18n import t
from shellkit.libc import atexit, println

from .banner import show_banner
from .repl import start_repl
from .reminder import start_reminder


def on_exit() -> None:
    """
    Prints a farewell message on shell exit.
    """
    println(t("shell.runtime.launcher.exit_farewell"))


def launch() -> None:
    """
    Launches the shell: show banner, register exit hook, start reminder and REPL.
    """
    show_banner()
    atexit(on_exit)
    start_reminder()
    start_repl()
