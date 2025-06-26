"""
engine/builtins/license.py

Implements the `license` shell command.
Displays the full content of the project's LICENSE file.
"""

from importlib.metadata import PackageNotFoundError, distribution
from pathlib import Path

from shellkit.i18n import t
from shellkit.libc import println
from shellkit.shell.state.exit_code import EXIT_FAILURE, EXIT_SUCCESS, EXIT_USAGE_ERROR, ExitCode


def license_builtin(args: list[str]) -> ExitCode:
    """
    Implements the `license` built-in command.

    Displays the full content of the project's LICENSE file.

    Behavior:
        - Reads the LICENSE file (UTF-8 encoded).
        - Trims leading/trailing whitespace before printing.
        - Does not accept any arguments.

    Args:
        args: Command-line arguments passed to `license`.

    Returns:
        ExitCode:
            - EXIT_SUCCESS (0) on successful output.
            - EXIT_FAILURE (1) on I/O or content errors.
            - EXIT_USAGE_ERROR (2) if any arguments are provided.
    """
    if args:
        println(t("shell.engine.builtin.license.unexpected_args"))
        return EXIT_USAGE_ERROR

    candidates: list[Path] = []

    # Try to find LICENSE from installed package
    try:
        dist = distribution("ShellKit")
        if dist.files:
            for file_path in dist.files:
                if file_path.name.upper() == "LICENSE":
                    candidates.append(Path(file_path.locate()))
                    break
    except PackageNotFoundError:
        pass

    # Try source code path - go up 3 levels to root
    current_file = Path(__file__).resolve()
    candidates.append(current_file.parents[4] / "LICENSE")

    # Try to read the first found file
    for path in candidates:
        if path.exists() and path.is_file():
            try:
                content = path.read_text(encoding="utf-8").strip()
                if content:
                    println(content)
                    return EXIT_SUCCESS
            except (UnicodeDecodeError, PermissionError, Exception):
                continue

    println(t("shell.engine.builtin.license.error_not_found"))
    return EXIT_FAILURE
