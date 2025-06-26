"""
engine/builtins/copyright.py

Implements the `copyright` shell command.
Displays the 3rd line from the LICENSE file with "All Rights Reserved.".
"""

from importlib.metadata import PackageNotFoundError, distribution
from pathlib import Path

from shellkit.i18n import t
from shellkit.libc import println
from shellkit.shell.state.exit_code import EXIT_FAILURE, EXIT_SUCCESS, EXIT_USAGE_ERROR, ExitCode


def copyright_builtin(args: list[str]) -> ExitCode:
    """
    Implements the `copyright` built-in command.

    Displays copyright information from the third line of the project's LICENSE file,
    followed by the line "All Rights Reserved.".

    Behavior:
        - Reads the 3rd line from the LICENSE file (UTF-8 encoded).
        - Appends "All Rights Reserved." as a footer.
        - Does not accept any arguments.

    Args:
        args: Command-line arguments passed to `copyright`.

    Returns:
        ExitCode:
            - EXIT_SUCCESS (0) on successful output.
            - EXIT_FAILURE (1) on I/O or format errors.
            - EXIT_USAGE_ERROR (2) if any arguments are provided.
    """
    if args:
        println(t("shell.engine.builtin.copyright.unexpected_args"))
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
    for license_path in candidates:
        if license_path.exists() and license_path.is_file():
            try:
                lines = license_path.read_text(encoding="utf-8").splitlines()

                if len(lines) < 3:
                    continue  # Try next file

                println(lines[2])
                println("All Rights Reserved.")
                return EXIT_SUCCESS

            except (UnicodeDecodeError, PermissionError, Exception):
                continue

    println(t("shell.engine.builtin.copyright.error_not_found"))
    return EXIT_FAILURE
