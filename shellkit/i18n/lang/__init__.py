"""
i18n.lang

Loads supported language message dictionaries from JSON files.
Each file (e.g. en.json, zh.json) contains a flat key-value mapping.

This module dynamically constructs:
- LANG_MAP: { "en": {...}, "zh": {...}, ... }
- SUPPORTED_LANGS: { "en", "zh", ... }

Usage:
    from i18n.lang import LANG_MAP, SUPPORTED_LANGS
"""

import json
from pathlib import Path

from shellkit.libc import eprintln


# Directory containing this __init__.py
_LANG_DIR = Path(__file__).parent

# Supported language codes (corresponding to JSON filenames)
_SUPPORTED_CODES = ["en", "zh", "ja", "ko"]

# Final mapping: lang_code → dict of message key-values
LANG_MAP = {}
for code in _SUPPORTED_CODES:
    path = _LANG_DIR / f"{code}.json"
    try:
        with open(path, encoding="utf-8") as f:
            LANG_MAP[code] = json.load(f)

    except Exception as e:
        LANG_MAP[code] = {}
        eprintln(f"[i18n] Failed to load language file: {path.name} — {e}")

SUPPORTED_LANGS = set(LANG_MAP.keys())
