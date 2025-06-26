"""
runtime/banner.py

Displays the shell startup banner, including version and system architecture.
"""

import platform

from shellkit.i18n import t
from shellkit.libc import println
from shellkit.shell.environs.accessors import is_banner_disabled, is_quiet_mode
from shellkit.shell.state import get_context

from .metadata import get_metadata


def show_banner() -> None:
    """
    Prints the PySH startup banner unless disabled by CLI options.
    Includes version, build time, system info, and login shell status.
    """
    # --no-banner or --quiet disables the banner
    if is_banner_disabled() or is_quiet_mode():
        return

    # Debug information: login shell vs interactive shell
    context = get_context()
    if context.is_login_shell:
        println(t("shell.runtime.banner.login_shell"))
    else:
        println(t("shell.runtime.banner.interactive_shell"))

    # Version metadata from pyproject.toml + syscall build timestamp
    name, version, build_time = get_metadata()

    system = platform.system().lower()    # e.g., darwin / linux / windows
    machine = platform.machine().lower()  # e.g., x86_64 / arm64 / aarch64 / amd64

    # Normalize common architecture names
    arch = {
        "amd64": "x86_64",
        "aarch64": "arm64"
    }.get(machine, machine)

    println(
        t("shell.runtime.banner.sysinfo"),
        name,
        version,
        build_time,
        system,
        arch,
    )
    println(t("shell.runtime.banner.tip"))
