"""
sidecar/args/version.py

Handles the -V / --version flag to print shell version information.
"""

from shellkit.i18n import t
from shellkit.libc import println


def apply_version_args() -> None:
    """
    Prints the shell name and version to stdout.
    """
    # Delay import to avoid circular dependency
    from shellkit.shell.runtime import get_metadata

    name, version, _ = get_metadata()
    println(t("shell.sidecar.args.version.version_format"), name, version)
