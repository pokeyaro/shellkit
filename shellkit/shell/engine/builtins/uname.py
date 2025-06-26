"""
engine/builtins/uname.py

Implements the `uname` shell command.
Displays system information fields, based on SYSINFO.
Supports flags for OS name, architecture, kernel version, and more.
"""

from shellkit.i18n import t
from shellkit.libc import bprintf, eprintln, flush, println, STDOUT
from shellkit.shell.environs.accessors import get_sysinfo
from shellkit.shell.state.exit_code import EXIT_FAILURE, EXIT_SUCCESS, EXIT_USAGE_ERROR, ExitCode


def uname_builtin(args: list[str]) -> ExitCode:
    """
    Built-in implementation of the `uname` command.

    Supports displaying various system information fields such as OS name, architecture,
    kernel version, and more. Uses the internal SYSINFO accessor for data retrieval.

    Args:
        args: List of option flags (e.g. -a, -s, -r, -m)

    Returns:
        ExitCode:
            - EXIT_SUCCESS (0): Successful execution
            - EXIT_FAILURE (1): Retrieval failure or partial output
            - EXIT_USAGE_ERROR (2): Invalid command-line options
    """
    try:
        # Retrieve system information from shell SYSINFO accessor
        info = get_sysinfo()

        if not info:
            println(t("shell.engine.builtin.uname.error_retrieval"))
            return EXIT_FAILURE

        flags = set(args)

        # Validate flags
        valid_options = {
            "-a",
            "--all",
            "-m",
            "--machine",
            "-r",
            "--kernel-version",
            "-s",
            "--kernel-name",
        }
        invalid_options = flags - valid_options

        if invalid_options:
            for invalid in invalid_options:
                println(t("shell.engine.builtin.uname.invalid_option"), invalid)
            println(t("shell.engine.builtin.uname.valid_options"))
            return EXIT_USAGE_ERROR

        # Default behavior: no flags → display OS name only
        if not flags:
            if name := info.get("uname"):
                println(name)
                return EXIT_SUCCESS
            else:
                println(t("shell.engine.builtin.uname.missing_os_name"))
                return EXIT_FAILURE

        # Combined output for --all or -a
        if "-a" in flags or "--all" in flags:
            try:
                bprintf("%s; ", t("shell.engine.builtin.uname.label_uname", info.get("uname", "?")))
                bprintf("%s; ", t("shell.engine.builtin.uname.label_arch", info.get("arch", "?")))
                bprintf("%s; ", t("shell.engine.builtin.uname.label_kernel", info.get("kernel_version", "?")))
                bprintf("%s\n", t("shell.engine.builtin.uname.label_release", info.get("os_release", "?")))
                flush(STDOUT)
                return EXIT_SUCCESS

            except Exception as e:
                eprintln(t("shell.engine.builtin.uname.error_output"), str(e))
                return EXIT_FAILURE

        # Handle individual flags
        output_count = 0
        for flag in flags:
            match flag:
                case "-m" | "--machine":
                    if val := info.get("arch"):
                        println(val)
                        output_count += 1
                    else:
                        println(t("shell.engine.builtin.uname.missing_arch"))
                        return EXIT_FAILURE

                case "-r" | "--kernel-version":
                    if val := info.get("kernel_version"):
                        println(val)
                        output_count += 1
                    else:
                        println(t("shell.engine.builtin.uname.missing_kernel"))
                        return EXIT_FAILURE

                case "-s" | "--kernel-name":
                    if val := info.get("uname"):
                        println(val)
                        output_count += 1
                    else:
                        println(t("shell.engine.builtin.uname.missing_uname"))
                        return EXIT_FAILURE

        # Ensure at least one field was printed
        if output_count == 0:
            println(t("shell.engine.builtin.uname.empty_result"))
            return EXIT_FAILURE

        return EXIT_SUCCESS

    except Exception as e:
        eprintln(t("shell.engine.builtin.uname.unexpected_error"), str(e))
        return EXIT_FAILURE
