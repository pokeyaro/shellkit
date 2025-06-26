"""
engine/builtins/locale.py

Implements the `locale` shell command.
Supports querying and changing the current language (LANG) used for translation.
"""

from shellkit.i18n import get_language, set_language, supported_languages, t
from shellkit.libc import println
from shellkit.shell.environs.accessors import set_lang
from shellkit.shell.state.exit_code import EXIT_FAILURE, EXIT_SUCCESS, EXIT_USAGE_ERROR, ExitCode


def locale_builtin(args: list[str]) -> ExitCode:
    """
    Implements the `locale` built-in command.

    Args:
        args: Command-line arguments passed to `locale`.

    Returns:
        ExitCode:
            - EXIT_SUCCESS (0) on success.
            - EXIT_FAILURE (1) if an unsupported language code is provided.
            - EXIT_USAGE_ERROR (2) if too many or invalid arguments are given.
    """
    if not args:
        println(t("shell.engine.builtin.locale.current_lang"), get_language())
        return EXIT_SUCCESS

    if args[0] in ("-l", "--list"):
        println(t("shell.engine.builtin.locale.supported"))
        for code in supported_languages():
            println("  - %s", code)
        return EXIT_SUCCESS

    if len(args) > 1:
        println(t("shell.engine.builtin.locale.too_many_args"))
        println(t("shell.engine.builtin.locale.usage"))
        return EXIT_USAGE_ERROR

    lang_code = args[0].lower()
    if lang_code not in supported_languages():
        println(t("shell.engine.builtin.locale.unsupported_lang"), lang_code)
        println(t("shell.engine.builtin.locale.suggestion"))
        return EXIT_FAILURE

    set_lang(lang_code)
    set_language(lang_code)
    println(t("shell.engine.builtin.locale.lang_set"), lang_code)
    return EXIT_SUCCESS
