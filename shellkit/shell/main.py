"""
main.py

Entry point for the PySH shell.

This file delegates execution to the core shell runner defined in `shell.app`.
When invoked as a script, it initializes the shell runtime, sets up the environment,
and launches the REPL (Read-Eval-Print Loop) loop.
"""

from shellkit.shell.app import run_pysh


def main() -> None:
    run_pysh()


if __name__ == "__main__":
    main()
