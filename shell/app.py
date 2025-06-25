"""
app.py

Launches the PySH shell by initializing args, environment, prompt, and REPL.
"""

from shell.runtime import launch
from shell.environs import init_environs
from shell.sidecar import parse_args, handle_args
from shell.sidecar.args import apply_prompt_args

from i18n import t
from inspector.debug import debug_startup, debug_argv, end_startup_phase


def run_pysh() -> None:
    # Parse and handle CLI arguments
    args = parse_args()
    if handle_args(args):
        end_startup_phase()
        debug_argv(t("shell.app.cli_handled"))
        return

    # Initialize environment system
    debug_startup(t("shell.app.init_environs"))
    init_environs()

    # Apply prompt configuration
    debug_startup(t("shell.app.apply_prompt"))
    apply_prompt_args(
        color=args.prompt_color,
        path_style=args.prompt_path,
    )

    # Launch REPL (Read-Eval-Print Loop)
    debug_startup(t("shell.app.launching"))
    launch()
