"""
Phase 6.5 — Propagation R-050 : ajout de la propriété 'Lien vers la note avancée'
dans les manuels Twin concernés + leurs WR-RD, et du champ frontmatter
'has_advanced_note: true|false' dans les 28 manuels.

Idempotent : skip les manuels déjà mis à jour.
"""

import json
import os
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(r"C:/Users/leona/LBP - dev/Claude - Brain architect temporaire/scripts/phase6.5/output")
REGISTRY = json.load(open(ROOT / "bdd_registry.json", encoding="utf-8"))

VAULT_TWIN = Path(r"H:/Drive partagés/LBP - shared/Architecture data/Manuels de BDD/Digital Twin")
VAULT_WRRD = VAULT_TWIN / "WR-RD"

# 18 BDD avec has_advanced_note: true (R-050)
HAS_ADVANCED_NOTE_TRUE = {
    "Organisations", "Collectifs", "Postes", "Individus",
    "Actifs", "Environnements", "Événements", "Relations inter-organisations",
    "Glossaire spécifique", "Initiatives organisationnelles", "Modulateurs",
    "Capacités organisationnelles", "OKR", "Pratiques organisationnelles",
    "Principes organisationnels", "Problématiques", "Processus", "Enjeux",
}

ROW_MANUEL = (
    "| Lien vers la note avancée | Générique | URL | — | 0..1 | Saisie | URL stable | "
    "Renseigner, si elle existe, l'URL d'une note avancée (Brick de connaissance) qui approfondit l'objet ; "
    "laisser vide si non pertinent ; utiliser des liens stables. | "
    "Must: note avancée réellement existante ; Should: cohérence de l'intitulé de la note avec le Nom de la fiche ; Nice: Brick structuré aligné avec les codes de taxonomies. | "
    "URL de la note avancée approfondissant l'objet (Brick de connaissance, profil organisationnel/individu, carte causale, etc.). | "
    "Permet de relier la fiche structurée à une analyse narrative plus complète et donne aux agents un canal d'approfondissement contextuel. | "
    "https://notion.so/Profil-Organisationnel-XXX |"
)

ROW_WRRD = (
    "| Lien vers la note avancée | URL | — | 0..1 | URL stable | "
    "Renseigner, si elle existe, l'URL d'une note avancée (Brick de connaissance) qui approfondit l'objet ; "
    "laisser vide si non pertinent ; utiliser des liens stables. | "
    "URL de la note avancée approfondissant l'objet (Brick de connaissance, profil organisationnel/individu, carte causale, etc.). | "
    "Permet de relier la fiche structurée à une analyse narrative plus complète et donne aux agents un canal d'approfondissement contextuel. | "
    "https://notion.so/Profil-Organisationnel-XXX |"
)


def update_frontmatter(content, has_note):
    """Ajoute ou met à jour has_advanced_note: true|false dans le frontmatter."""
    val = "true" if has_note else "false"
    if re.search(r"^has_advanced_note\s*:", content, re.MULTILINE):
        content = re.sub(
            r"^has_advanced_note\s*:\s*\w+",
            f"has_advanced_note: {val}",
            content,
            count=1,
            flags=re.MULTILINE,
        )
    else:
        # Insert after officiality_regime line, or after ui_family if present
        anchor_match = re.search(r"^(officiality_regime\s*:.*?)$", content, re.MULTILINE)
        if anchor_match:
            content = (
                content[: anchor_match.end()]
                + f"\nhas_advanced_note: {val}"
                + content[anchor_match.end():]
            )
    return content


def insert_advanced_note_row_manuel(content):
    """Insère la ligne 'Lien vers la note avancée' dans la section 4.1 du manuel,
    juste avant la ligne contenant 'Created Date'."""
    if "Lien vers la note avancée" in content:
        return content, False  # déjà présent
    # Find the line with 'Created Date' in section 4.1 (table row)
    pattern = re.compile(r"(^\|\s*Created Date\s*\|.*?\|.*?$)", re.MULTILINE)
    m = pattern.search(content)
    if not m:
        return content, False
    insertion_pos = m.start()
    new = content[:insertion_pos] + ROW_MANUEL + "\n" + content[insertion_pos:]
    return new, True


def insert_advanced_note_row_wrrd(content):
    """Insère la ligne dans la section 1) du WR-RD, juste avant 'Created Date'."""
    if "Lien vers la note avancée" in content:
        return content, False
    pattern = re.compile(r"(^\|\s*Created Date\s*\|.*?\|.*?$)", re.MULTILINE)
    m = pattern.search(content)
    if not m:
        return content, False
    insertion_pos = m.start()
    new = content[:insertion_pos] + ROW_WRRD + "\n" + content[insertion_pos:]
    return new, True


def main():
    n_fm = 0
    n_manuel = 0
    n_wrrd = 0
    skipped_manuel = []
    skipped_wrrd = []

    for canonical in sorted(REGISTRY["databases"].keys()):
        has_note = canonical in HAS_ADVANCED_NOTE_TRUE

        # 1. Manuel : update frontmatter (toujours) + insert row (si has_note)
        manuel_path = VAULT_TWIN / f"Manuel de BDD - {canonical}.md"
        if not manuel_path.exists():
            skipped_manuel.append(canonical)
            continue
        with open(manuel_path, "r", encoding="utf-8") as f:
            content = f.read()
        old_content = content
        content = update_frontmatter(content, has_note)
        if content != old_content:
            n_fm += 1
        if has_note:
            content, inserted = insert_advanced_note_row_manuel(content)
            if inserted:
                n_manuel += 1
        with open(manuel_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  [{'TRUE' if has_note else 'FALSE':5s}] manuel: {canonical}")

        # 2. WR-RD : insert row (si has_note seulement)
        if has_note:
            wrrd_path = VAULT_WRRD / f"WR-RD - {canonical}.md"
            if not wrrd_path.exists():
                skipped_wrrd.append(canonical)
                continue
            with open(wrrd_path, "r", encoding="utf-8") as f:
                content = f.read()
            content, inserted = insert_advanced_note_row_wrrd(content)
            if inserted:
                n_wrrd += 1
            with open(wrrd_path, "w", encoding="utf-8") as f:
                f.write(content)

    print(f"\n=== TOTAL ===")
    print(f"Frontmatters has_advanced_note ajoutés/MAJ : {n_fm}/28")
    print(f"Lignes 'Lien vers la note avancée' ajoutées dans manuels : {n_manuel}/18")
    print(f"Lignes 'Lien vers la note avancée' ajoutées dans WR-RD : {n_wrrd}/18")
    if skipped_manuel:
        print(f"Manuels skipped: {skipped_manuel}")
    if skipped_wrrd:
        print(f"WR-RD skipped: {skipped_wrrd}")


if __name__ == "__main__":
    main()
