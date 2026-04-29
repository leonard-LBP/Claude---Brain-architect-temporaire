"""
Helper utilitaire pour la lecture des payloads Notion via MCP.

Piège connu : les noms de propriétés contenant une apostrophe arrivent en ASCII
(' U+0027) dans les payloads de `notion-query-database-view`, alors que la
définition du schéma (`notion-fetch`) les présente en typographique (' U+2019).

Usage :
    from scripts.lib.notion_keys import normalize_keys, get
    entry = normalize_keys(raw_entry)            # remplace ' par ' partout
    val = get(raw_entry, "Statut de l'objet")    # tente les 2 variantes
"""
from __future__ import annotations

TYPO_APOS = "’"  # '
ASCII_APOS = "'"       # U+0027

def _swap(s: str) -> str:
    return s.replace(TYPO_APOS, ASCII_APOS)

def normalize_keys(obj):
    """Récursivement, remplace les apostrophes typographiques par ASCII dans toutes les clés dict."""
    if isinstance(obj, dict):
        return {_swap(k) if isinstance(k, str) else k: normalize_keys(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [normalize_keys(x) for x in obj]
    return obj

def get(entry: dict, key: str, default=None):
    """Récupère une valeur en tentant les 2 variantes d'apostrophe."""
    if key in entry:
        return entry[key]
    alt = _swap(key) if TYPO_APOS in key else key.replace(ASCII_APOS, TYPO_APOS)
    return entry.get(alt, default)
