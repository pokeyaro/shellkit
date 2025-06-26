"""
sidecar/args/reminder.py

Handles the --no-reminder flag to disable break reminders.
"""

from shellkit.shell.environs.accessors import set_reminder_disabled


def apply_no_reminder_args() -> None:
    """
    Disables the periodic break reminder system.
    """
    set_reminder_disabled()
