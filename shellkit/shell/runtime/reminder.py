"""
runtime/reminder.py

Periodically reminds the user to take breaks while using the shell.
"""

import random
import threading
import time

from shellkit.i18n import t
from shellkit.libc import eprintln, println
from shellkit.shell.docs import get_reminder_texts
from shellkit.shell.docs.texts import INFO_CRITICAL, INFO_NORMAL
from shellkit.shell.environs.accessors import is_quiet_mode, is_reminder_disabled


# Reminder config (in seconds)
REMIND_INTERVAL = 30 * 60     # 30 minutes
BREAK_THRESHOLD = 90          # Escalate after 90 minutes


def _format_time(minutes: int) -> str:
    """
    Convert elapsed time (in minutes) to localized human-friendly string.
    """
    if minutes < 60:
        return t("shell.runtime.reminder.minutes", minutes)
    elif minutes % 60 == 0:
        hours = minutes // 60
        return t("shell.runtime.reminder.hours", hours)
    else:
        hours = minutes // 60
        remaining = minutes % 60
        decimal = remaining // 6  # Approximate to 0.1 units
        return t("shell.runtime.reminder.partial_hours", hours, decimal)


def _remind_loop() -> None:
    """
    Background loop that prints wellness reminders periodically.
    """
    count = 0

    while True:
        try:
            time.sleep(REMIND_INTERVAL)
            count += 1
            elapsed = count * 30  # in minutes

            label = t("shell.runtime.reminder.prefix")
            time_str = _format_time(elapsed)

            # Dynamically reload based on current locale
            normal_messages = get_reminder_texts(INFO_NORMAL)
            critical_messages = get_reminder_texts(INFO_CRITICAL)

            if elapsed >= BREAK_THRESHOLD and critical_messages:
                msg = random.choice(critical_messages).format(time=time_str)
                println("\n\033[31m🐚 %s \033[0m %s", label, msg)
            elif normal_messages:
                msg = random.choice(normal_messages)
                full = t("shell.runtime.reminder.worked_for") % (elapsed, msg)
                println("\n\033[36m🐚 %s \033[0m %s", label, full)

        except Exception as e:
            eprintln("\n\033[91m💥 Reminder thread crashed!\033[0m")
            eprintln("Exception: %s", str(e))
            eprintln("Context: count=%d, elapsed=%d minutes", count, elapsed)


def start_reminder() -> None:
    """
    Launches the background reminder thread if enabled.
    """
    # Check if reminders are disabled or suppressed in quiet mode
    if is_reminder_disabled() or is_quiet_mode():
        return

    thread = threading.Thread(target=_remind_loop, daemon=True)
    thread.start()
