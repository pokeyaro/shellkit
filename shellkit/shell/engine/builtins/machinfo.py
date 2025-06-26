"""
engine/builtins/machinfo.py

Implements the `machinfo` shell command.
Displays detailed system information, with optional JSON or short output modes.
"""

import json

from shellkit.i18n import t
from shellkit.libc import eprintln, println
from shellkit.shell.environs.accessors import get_sysinfo
from shellkit.shell.state.exit_code import EXIT_FAILURE, EXIT_SUCCESS, EXIT_USAGE_ERROR, ExitCode


def machinfo_builtin(args: list[str]) -> ExitCode:
    """
    Implements the `machinfo` built-in command.

    Shows detailed hardware and OS information about the host machine.

    Supported options:
        --json     Output info in JSON format
        --short    Output compact summary line
        (default)  Verbose ANSI-decorated format

    Args:
        args: Command-line arguments passed to `machinfo`.

    Returns:
        ExitCode:
            - EXIT_SUCCESS (0) if info was printed successfully.
            - EXIT_FAILURE (1) if system info could not be retrieved.
            - EXIT_USAGE_ERROR (2) if invalid or conflicting options were passed.
    """
    # Validate arguments against allowed options
    valid_options = {"--json", "--short"}
    invalid_args = [arg for arg in args if arg not in valid_options]

    if invalid_args:
        println(t("shell.engine.builtin.machinfo.invalid_option"), invalid_args[0])
        println(t("shell.engine.builtin.machinfo.valid_options"))
        return EXIT_USAGE_ERROR

    # Disallow combining --json and --short
    if "--json" in args and "--short" in args:
        println(t("shell.engine.builtin.machinfo.conflict_options"))
        return EXIT_USAGE_ERROR

    # Prevent duplicate arguments
    if len(args) != len(set(args)):
        println(t("shell.engine.builtin.machinfo.duplicate_option"))
        return EXIT_USAGE_ERROR

    try:
        # Query system information using the accessor function
        info = get_sysinfo()

        if not info:
            println(t("shell.engine.builtin.machinfo.no_info"))
            return EXIT_FAILURE

        # If --json flag is passed, pretty-print raw data
        if "--json" in args:
            println(json.dumps(info, indent=2))
            return EXIT_SUCCESS

        # If --short flag is passed, show one-line summary
        if "--short" in args:
            short = f"{info.get('arch', '?')} / {info.get('uname', '?')} / {info.get('kernel_version', '?')} / {info.get('cpu', '?')}"
            println(short)
            return EXIT_SUCCESS

        # Default: verbose human-readable output with categories
        println("\033[1mMachine Info:\033[0m")

        # 🪪 Product section
        println("")
        println("  \033[1m🪪 Product\033[0m")
        println("     Product Name    : %s", info.get("product_name", "?"))
        println("     Serial#         : %s", info.get("serial_number", "?"))

        # 📦 Platform section
        println("")
        println("  \033[1m📦 Platform\033[0m")
        println("     OS              : %s", info.get("uname", "?"))
        println("     Release         : %s", info.get("os_release", "?"))
        println("     Kernel          : %s", info.get("kernel_version", "?"))
        println("     Arch            : %s", info.get("arch", "?"))

        # 🧠 CPU section
        println("")
        println("  \033[1m🧠 CPU\033[0m")
        println("     Model           : %s", info.get("cpu", "?"))
        println("     Cores           : %s physical / %s logical", info.get("cores", "?"),
                info.get("logical_cores", "?"))
        println("     Hyperthread     : %s", "Enabled" if info.get("hyperthreading") else "Disabled")

        # 💾 Hardware section
        println("")
        println("  \033[1m💾 Hardware\033[0m")
        println("     Memory          : %s", info.get("mem_total", "?"))
        println("     Disk            : %s", info.get("disk_total", "?"))

        # 📺 GPU section (if present)
        gpus = info.get("gpu", [])
        if gpus:
            println("")
            println("  \033[1m📺 GPU\033[0m")
            for gpu in gpus:
                name = gpu.get("name", "?")
                vram = gpu.get("vram", None)
                gpu_type = gpu.get("type", None)

                println("     · %s", name)
                if vram:
                    println("     VRAM            : %s", vram)
                if gpu_type:
                    println("     Type            : %s", gpu_type)

        return EXIT_SUCCESS

    except Exception as e:
        eprintln(t("shell.engine.builtin.machinfo.error_retrieval") + ": %s", str(e))
        return EXIT_FAILURE
