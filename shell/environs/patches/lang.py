"""
environs/patches/lang.py

Updates the LANG environment variable using system locale detection.
"""

from ..accessors import set_lang
from i18n import get_language


def patch_lang() -> None:
    """
    Injects LANG into the environment from PYSH_LANG or LANG, even if unsupported.
    This does not affect actual i18n behavior.
    """
    set_lang(get_language())
