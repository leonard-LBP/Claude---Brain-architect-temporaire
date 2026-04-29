"""
Phase A4.A.3 — Construit la liste des 99 actions sync (94 update + 5 create).
Lit drive_taxos.json + notion_validated_export.txt + drive_urls_taxos.json.
Exclut les 3 calibration déjà fait (OBJ.STATUT, SCALE.IMPACT_INTENSITY, BRAIN.LAYER).

Output: scripts/phase_a4/output/sync_actions.json
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).parent / "output"
EXPORT = Path(__file__).parent / "notion_validated_export.txt"

CALIBRATED = {"OBJ.STATUT", "SCALE.IMPACT_INTENSITY", "BRAIN.LAYER"}


def normalize_code(c: str) -> str:
    return c[:-4] if c.endswith(".LBP") else c


def to_bool(v):
    """Parse YAML-ish bool: True/False or 'true'/'false' string."""
    if isinstance(v, bool):
        return v
    if isinstance(v, str):
        return v.strip().lower() == "true"
    return False


def map_nature(scale_kind, is_ordinal):
    # Source de vérité = scale_kind (canonical taxon)
    if scale_kind == "ordinal" or to_bool(is_ordinal):
        return "ordinal"
    if scale_kind == "hierarchical":
        return "hierarchical"
    if scale_kind == "binary":
        return "binary"
    return "nominal"


def map_ouverture(open_policy, is_open):
    if open_policy == "open" or to_bool(is_open):
        return "ouverte"
    return "fermée"


def map_mode_selection(selection_mode):
    # Returns JSON array as string for Notion multi-select
    if selection_mode == "mono":
        return '["mono"]'
    if selection_mode == "multi":
        return '["multi"]'
    return '["mono","multi"]' if selection_mode == "both" else '["mono"]'


def build_props(d, drive_url):
    aliases = d.get("aliases") or []
    if not isinstance(aliases, list):
        aliases = []
    nature = map_nature(d.get("scale_kind"), d.get("is_ordinal"))
    props = {
        "Code unique": d["code"],
        "Nom canonique": d.get("title", ""),
        "Aliases": "; ".join(aliases),
        "Description (source)": d.get("summary", ""),
        "Description courte (usage)": d.get("purpose", ""),
        "Lien doc taxonomie (source)": drive_url,
        "Nature sémantique": nature,
        "Mode de sélection": map_mode_selection(d.get("selection_mode")),
        "Ouverture": map_ouverture(d.get("open_policy"), d.get("is_open")),
        "Statut de l’objet": "Validé",
        "Version du template": d.get("template_version", "2.0"),
    }
    # For non-hierarchical, set Niveaux autorisés to []. For hierarchical, omit (preserve existing manually set in Notion).
    if nature != "hierarchical":
        props["Niveaux autorisés"] = "[]"
    return props


def main():
    drive = json.loads((ROOT / "drive_taxos.json").read_text(encoding="utf-8"))
    drive_by_code = {e["code"]: e for e in drive if e.get("code")}
    drive_urls = json.loads((ROOT / "drive_urls_taxos.json").read_text(encoding="utf-8"))

    # Notion existing entries (Validé)
    notion_existing = {}
    for line in EXPORT.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        parts = line.split("|")
        if len(parts) != 5:
            continue
        name, statut, code_lbp, uuid, _ = parts
        norm = normalize_code(code_lbp)
        notion_existing[norm] = uuid

    actions = []
    for code, d in sorted(drive_by_code.items()):
        if code in CALIBRATED:
            continue
        drive_url = drive_urls.get(d["file"], {}).get("url", "")
        props = build_props(d, drive_url)
        if code in notion_existing:
            actions.append({"action": "update", "code": code, "page_id": notion_existing[code], "properties": props})
        else:
            actions.append({"action": "create", "code": code, "properties": props})

    out = ROOT / "sync_actions.json"
    out.write_text(json.dumps(actions, ensure_ascii=False, indent=2), encoding="utf-8")
    n_update = sum(1 for a in actions if a["action"] == "update")
    n_create = sum(1 for a in actions if a["action"] == "create")
    print(f"Actions: {len(actions)} ({n_update} update + {n_create} create)")
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
