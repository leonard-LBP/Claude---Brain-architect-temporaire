"""
Phase A3.bis — plan complet : 22 concepts non-matchés + 6 corrections de collisions.

Construit la liste complète des updates à faire avec valeurs cibles.
"""
from __future__ import annotations
import json
import re
from pathlib import Path

DRIVE = Path(r"H:/Drive partagés/LBP - shared/Architecture data/Notes de Concept")
ROOT = Path(__file__).parent / "output"

FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_fm(text):
    m = FM_RE.match(text)
    if not m:
        return {}
    raw = m.group(1)
    fm = {}
    cur = None
    buf = []
    for line in raw.splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        if line.startswith(("  - ", "- ")) and cur is not None:
            v = line.lstrip(" -").strip().strip('"').strip("'")
            buf.append(v)
            fm[cur] = buf
            continue
        m2 = re.match(r"^([A-Za-z0-9_\-]+)\s*:\s*(.*)$", line)
        if m2:
            k = m2.group(1)
            v = m2.group(2).strip()
            cur = k
            buf = []
            if v == "" or v == "[]":
                fm[k] = []
                buf = []
            else:
                fm[k] = v.strip('"').strip("'")
                cur = None
    return fm


# Glossaire URLs found via search
A3BIS = {
    # 22 nouveaux matches
    "Concept - Actif.md": "34ce1a18653c8181b7ede2139f6f1eac",
    "Concept - Alignement (organisation).md": "2f7e1a18653c8074b046f7f4985ec5c4",
    "Concept - Apprentissage intégré au travail.md": "30fe1a18653c80349b96f9676350465d",
    "Concept - Asymétrie de connaissances.md": "30fe1a18653c804aa136d5fe2068b18d",
    "Concept - Brick.md": "2f7e1a18653c80049b43d8a3c7ba19aa",
    "Concept - Capacité habilitante.md": "2f7e1a18653c8013be4fc67fd6460d74",
    "Concept - Capacité motrice.md": "2f7e1a18653c80ebbca9dbb3d4b26fb1",
    "Concept - Collectif.md": "34de1a18653c8137be5ec4050716bf03",
    "Concept - Contexte.md": "30fe1a18653c8060acb7e7e2f0112e53",
    "Concept - Découverte d’objets.md": "c1414e80363a425bba89185c7e6ddb96",
    "Concept - Dédoublonnage.md": "bad83ea00a4e4e0bb8f931ee92ff0b47",
    "Concept - Initiative organisationnelle.md": "34de1a18653c81618dddf492e2f3daf5",
    "Concept - Input - Output (Processus).md": "34de1a18653c819ca977d02b1148a547",
    "Concept - Instructions d’écriture et clefs de lecture.md": "a219d258979e44979ad2f0899bc2e916",
    "Concept - Logic block.md": "325e1a18653c80068322f4c13c0979d9",
    "Concept - Mad skill.md": "30fe1a18653c800eaa89fc63fae582c7",
    "Concept - Poste.md": "34de1a18653c8170804df17ee50cca07",
    "Concept - Prompt maître.md": "077e4833a77c46c29d6aca009b44806f",
    "Concept - Refactor.md": "e7ca5ad220fa4b179ab06d188a7442ec",
    "Concept - Relation inter-organisations.md": "34de1a18653c8109b395debec4882da0",
    "Concept - Relations Maker.md": "bc2735e3194b443c962dc3c3daa20c1f",
    "Concept - Source de vérité.md": "30fe1a18653c80c191cbf450899f2081",
    "Concept - System prompt.md": "4fde880c18b34e4589143c9478525aa8",
    "Concept - Vision partagée.md": "30fe1a18653c80178da9ed2817186ddb",
}

# 6 collision corrections (true Glossaire URLs)
COLLISION_FIX = {
    "Concept - Compétence.md": "2f7e1a18653c8013bc5be3b0a28d1cfc",
    "Concept - Cohérence (LBP).md": "2f7e1a18653c8066a193c671ac74e4f1",
    "Concept - Hard skill.md": "2f7e1a18653c806c9221f410c063f1a2",
    "Concept - Glossaire LBP.md": "2f7e1a18653c8025943fefa82f7e6b8e",
    "Concept - Glossaire spécifique.md": "2f7e1a18653c803397adf18d4568c8e3",
    "Concept - Indicateur.md": "2f7e1a18653c80b1bc08c4809aeddd02",
}


def build_glossaire_props(fm):
    code = fm.get("code", "")
    canonical_name = fm.get("canonical_name", "")
    aliases = fm.get("aliases", []) or []
    keywords = fm.get("keywords", []) or []
    tags = fm.get("tags", []) or []
    template_version = fm.get("template_version", "")
    if not isinstance(aliases, list):
        aliases = []
    if not isinstance(keywords, list):
        keywords = []
    if not isinstance(tags, list):
        tags = []
    type_concept = "Concept LBP" if "lbp" in [t.lower() for t in tags] else "Concept externe"
    return {
        "Code unique": code,
        "Nom canonique": canonical_name,
        "Aliases": "; ".join(aliases),
        "Mots clés": "; ".join(keywords),
        "Type de concept": type_concept,
        "Version du template": template_version,
    }


def main():
    out = []
    truly_missing = ["Concept - Capacité générique.md"]

    all_files = {**A3BIS, **COLLISION_FIX}
    for file, gloss_id in all_files.items():
        p = DRIVE / file
        if not p.exists():
            print(f"  MISSING DRIVE FILE: {file}")
            continue
        fm = parse_fm(p.read_text(encoding="utf-8"))
        out.append({
            "file": file,
            "phase": "a3bis_new" if file in A3BIS else "a3bis_collision_fix",
            "glossaire_page_id": gloss_id,
            "glossaire_props": build_glossaire_props(fm),
        })

    output_path = ROOT / "a3bis_plan.json"
    output_path.write_text(json.dumps({
        "updates": out,
        "truly_missing": truly_missing,
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Plan: {len(out)} Glossaire updates ({len(A3BIS)} new + {len(COLLISION_FIX)} collision_fix)")
    print(f"Truly missing (no Glossaire entry yet): {truly_missing}")
    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()
