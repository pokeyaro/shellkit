"""
engine/builtins/tree.py

Implements the `tree` shell command.
Delegates to the system's `tree` binary if available, with fallback instructions if not installed.
Includes logic to ignore common development directories automatically.
"""

import shutil
import subprocess

from shellkit.i18n import t
from shellkit.libc import eprintln, println
from shellkit.shell.state.exit_code import EXIT_FAILURE, EXIT_SUCCESS, EXIT_USAGE_ERROR, ExitCode


def tree_builtin(args: list[str]) -> ExitCode:
    """
    Implements the `tree` built-in command.

    Attempts to invoke the system `tree` command to display directory structures.
    If the `tree` binary is not available, it prints a helpful installation message.

    Args:
        args: Command-line arguments passed to `tree`.

    Returns:
        ExitCode:
            - EXIT_SUCCESS (0): Tree displayed successfully
            - EXIT_FAILURE (1): Tree binary not found or execution failed
            - EXIT_USAGE_ERROR (2): Improper arguments (reserved for future)
    """
    # Check if system 'tree' command exists
    if shutil.which("tree"):
        return _run_system_tree(args)
    else:
        println("\033[31m[error]\033[0m %s", t("shell.engine.builtin.tree.not_found"))
        println(t("shell.engine.builtin.tree.install_tip"))
        return EXIT_FAILURE


def _run_system_tree(args: list[str]) -> ExitCode:
    """
    Helper function to run the system `tree` command with enhanced arguments.

    Automatically filters out known clutter directories (e.g., .git, node_modules).
    Adds user-specified `-I` exclusion rules if provided.
    Passes all other arguments through to the system command.

    Args:
        args: Command-line arguments passed to `tree`.

    Returns:
        ExitCode:
            - EXIT_SUCCESS (0): Tree executed with code 0
            - EXIT_FAILURE (1/2): Tree failed or encountered runtime error
            - EXIT_USAGE_ERROR (2): Malformed input (e.g. missing value for -I)
    """
    try:
        # Check if verbose mode is enabled
        verbose = "-v" in args

        # Default flags: show hidden files if verbose, otherwise suppress summary report
        default_args = ["-a"] if verbose else ["--noreport"]

        # Common development directories to ignore by default
        ignored_dirs = {
            ".git", ".hg", ".svn",
            ".idea", ".vscode", ".DS_Store",
            "__pycache__", ".mypy_cache", ".ruff_cache", ".pytest_cache", ".tox",
            ".coverage", "htmlcov", "coverage.xml",
            ".venv", "venv", "env",
            "node_modules",
            ".trash", "Thumbs.db", "desktop.ini",
        }

        # Extract user-defined -I excludes
        user_excludes = set()
        it = iter(args)
        for arg in it:
            if arg == "-I":
                try:
                    val = next(it)
                    user_excludes.add(val)
                except StopIteration:
                    eprintln(t("shell.engine.builtin.tree.missing_I_value"))
                    return EXIT_USAGE_ERROR

        # Merge default excludes with user-defined ones
        exclude_args = []
        for d in ignored_dirs:
            if d not in user_excludes:
                exclude_args += ["-I", d]

        # Final command to execute
        cmd = ["tree"] + default_args + exclude_args + args

        # Execute tree command, inherit stdio
        result = subprocess.run(cmd, stdin=None, stdout=None, stderr=None)

        # Tree return codes:
        #   0 - success
        #   1 - partial success (e.g., permission errors)
        #   2 - fatal error
        return EXIT_SUCCESS if result.returncode == 0 else EXIT_FAILURE

    except PermissionError:
        eprintln("\033[31m[error]\033[0m %s", t("shell.engine.builtin.tree.error.permission_denied"))
        return EXIT_FAILURE

    except Exception as e:
        eprintln("\033[31m[error]\033[0m %s: %s", t("shell.engine.builtin.tree.error.unexpected"), str(e))
        return EXIT_FAILURE
