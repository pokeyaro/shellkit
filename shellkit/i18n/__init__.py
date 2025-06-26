"""
i18n module: internationalization support for pysh shell.

Provides mechanisms for detecting user language and returning localized messages
based on a centralized message dictionary (`LANG_MAP`).

Includes the following components:
- lang: defines supported language codes and their associated message dictionaries
- core: implements language detection logic and translation dispatch via the `t()` function

Design Notes:
- Language detection priority: PYSH_LANG > LANG > fallback (default: "en")
- Not all message keys are guaranteed to exist in all locales; fallback warns with `"[!! missing i18n: key !!]"`
- Language can be switched at runtime using `set_language()`, allowing for dynamic language overrides
"""

from .core import (
    t,
    get_language,
    set_language,
    supported_languages,

    I18N_DEFAULT,
    I18N_EN,
    I18N_ZH,
    I18N_JA,
    I18N_KO,
)


__all__ = [
    "t", "get_language", "set_language", "supported_languages",
    "I18N_DEFAULT", "I18N_EN", "I18N_ZH", "I18N_JA", "I18N_KO"
]
