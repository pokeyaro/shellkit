"""
shell.docs.manuals

Handles help documentation lookup and listing for shell commands.
"""

from pathlib import Path

from shellkit.i18n import t
from shellkit.inspector.debug import debug_docs
from shellkit.shell.environs.accessors import get_lang
from shellkit.shell.environs.constants import DEFAULT_LANG


_MANUAL_DIR = Path(__file__).parent

__all__ = ["has_manual", "get_manual", "list_manuals", "get_manual_path"]


def get_manual_path(command: str) -> Path:
    """
    Returns the full path to the localized Markdown help file for a given command.
    Falls back to English if current language is missing.
    """
    lang = get_lang()
    lang_path = _MANUAL_DIR / lang / f"{command}.md"
    fallback_path = _MANUAL_DIR / DEFAULT_LANG / f"{command}.md"
    return lang_path if lang_path.exists() else fallback_path


def has_manual(command: str) -> bool:
    """
    Checks whether the help markdown file exists for a given command.
    """
    return get_manual_path(command).exists()


def get_manual(command: str) -> str:
    """
    Reads and returns the help text for the given command.

    If the help file exists, returns its contents as a UTF-8 string.
    Otherwise, returns a fallback 'not found' message.
    """
    path = get_manual_path(command)
    _target = "/".join(str(path).split("/")[-4:])

    if path.exists():
        debug_docs(t("shell.docs.manuals.init.opening_doc", target=_target), doc_type="read")
        return path.read_text(encoding="utf-8").strip()

    debug_docs(t("shell.docs.manuals.init.doc_not_found", target=_target), doc_type="notfound")
    return t("shell.docs.manuals.init.not_found_fallback", cmd=command)


def list_manuals() -> list[str]:
    """
    Lists all available command help files (without .md extension).
    """
    manual_dir = _MANUAL_DIR / DEFAULT_LANG
    return sorted(p.stem for p in manual_dir.glob("*.md"))
