"""Renomme les fichiers archivés du vault Architecture data selon R-053 + R-056.

Format cible (R-053 + R-056) :
  - Avec version : `<nom> (archivé v<X.Y> le JJ-MM-YYYY).md` (format MAJOR.MINOR)
  - Sans version : `<nom> (archivé le JJ-MM-YYYY).md`

Le script gère 3 cas :
1. Fichier non encore archivé (sans suffix) → ajoute le suffix complet (R-053 initial)
2. Fichier archivé avec version `X.Y.Z` (legacy avant R-056) → tronque le PATCH (`X.Y.Z` → `X.Y`)
3. Fichier déjà au format R-053 + R-056 (`X.Y` ou sans version) → skip

Spec :
- Glob récursif sous `H:\\Drive partagés\\LBP - shared\\Architecture data` des fichiers
  dans un dossier `00 - archives/`.
- Migration de la version dans le filename ET dans le `title` du frontmatter (R-043).
- Mode --dry-run par défaut. --apply pour exécuter.
- Date forfaitaire pour les nouveaux : 26-04-2026 (sweep Phase 1-4).

Usage :
  python rename_archives.py            # dry-run (par défaut)
  python rename_archives.py --apply    # applique les renamings
"""
import argparse
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

VAULT_ROOT = Path(r"H:\Drive partagés\LBP - shared\Architecture data")
ARCHIVE_DATE = "26-04-2026"

# Regex R-053 + R-056 : filename strictement conforme (X.Y ou pas de version)
ALREADY_CONFORM_RE = re.compile(r"\(archivé( v\d+\.\d+)? le (\d{2}-\d{2}-\d{4})\)\.md$")

# Regex legacy R-053 pré-R-056 : filename archivé avec format X.Y.Z (à migrer)
LEGACY_XYZ_IN_FILENAME_RE = re.compile(r"\(archivé v(\d+)\.(\d+)\.(\d+) le (\d{2}-\d{2}-\d{4})\)\.md$")

# Frontmatter parsing (simple, suffit pour notre cas)
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
VERSION_LINE_RE = re.compile(r"^version:\s*[\"']?([\d.]+)[\"']?\s*$", re.MULTILINE)
TITLE_LINE_RE = re.compile(r"^title:\s*[\"']?(.*?)[\"']?\s*$", re.MULTILINE)


def parse_frontmatter(content):
    """Retourne (frontmatter_str, body) ou (None, content) si pas de frontmatter."""
    m = FRONTMATTER_RE.match(content)
    if m:
        return m.group(1), content[m.end():]
    return None, content


def extract_version(frontmatter):
    if not frontmatter:
        return None
    m = VERSION_LINE_RE.search(frontmatter)
    return m.group(1) if m else None


def build_archive_suffix(version):
    """Construit le suffix R-053."""
    if version:
        return f" (archivé v{version} le {ARCHIVE_DATE})"
    return f" (archivé le {ARCHIVE_DATE})"


def build_new_filename(old_stem, version):
    """Retourne le nouveau filename (sans extension)."""
    return old_stem + build_archive_suffix(version)


def update_title_in_frontmatter(frontmatter, new_title):
    """Remplace la ligne title: par la nouvelle, ou retourne tel quel si absente."""
    if not frontmatter:
        return frontmatter
    if TITLE_LINE_RE.search(frontmatter):
        return TITLE_LINE_RE.sub(f'title: "{new_title}"', frontmatter, count=1)
    return frontmatter


def process_file(path, apply_mode):
    """Traite un fichier archivé. Retourne dict de log."""
    filename = path.name
    stem = path.stem

    log = {
        "path": str(path),
        "old_filename": filename,
        "new_filename": None,
        "version": None,
        "has_frontmatter": False,
        "action": "SKIP",
        "reason": "",
    }

    # Skip si déjà strictement conforme R-053 + R-056
    if ALREADY_CONFORM_RE.search(filename):
        log["reason"] = "already conform"
        return log

    # Cas 2 : filename archivé legacy X.Y.Z → tronquer le PATCH (migration R-056)
    legacy_match = LEGACY_XYZ_IN_FILENAME_RE.search(filename)
    if legacy_match:
        major, minor, patch, date = legacy_match.groups()
        new_stem = stem[: legacy_match.start()] + f"(archivé v{major}.{minor} le {date})"
        new_filename = new_stem + ".md"
        new_path = path.parent / new_filename
        log["new_filename"] = new_filename
        log["version"] = f"{major}.{minor}.{patch} → {major}.{minor}"
        log["action"] = "MIGRATE_R056"
        log["reason"] = "truncate PATCH per R-056"

        # Lire pour aligner title si frontmatter présent
        try:
            content = path.read_text(encoding="utf-8")
        except Exception as e:
            log["action"] = "ERROR"
            log["reason"] = f"read failed: {e}"
            return log
        frontmatter, body = parse_frontmatter(content)
        log["has_frontmatter"] = frontmatter is not None
        new_content = None
        if frontmatter:
            new_frontmatter = update_title_in_frontmatter(frontmatter, new_stem)
            new_content = f"---\n{new_frontmatter}\n---\n{body}"

        if apply_mode:
            if new_path.exists():
                log["action"] = "ERROR"
                log["reason"] = "target exists, collision"
                return log
            if new_content is not None:
                path.write_text(new_content, encoding="utf-8")
            path.rename(new_path)
        return log

    # Cas 1 : fichier non encore archivé (pas de suffix) → ajouter le suffix complet
    # Lire le contenu pour parser le frontmatter
    try:
        content = path.read_text(encoding="utf-8")
    except Exception as e:
        log["action"] = "ERROR"
        log["reason"] = f"read failed: {e}"
        return log

    frontmatter, body = parse_frontmatter(content)
    log["has_frontmatter"] = frontmatter is not None
    version = extract_version(frontmatter) if frontmatter else None
    # Tronquer en X.Y si X.Y.Z détecté (cohérence R-056)
    if version:
        parts = version.split(".")
        if len(parts) >= 2:
            version = f"{parts[0]}.{parts[1]}"
    log["version"] = version

    # Build new filename
    new_stem = build_new_filename(stem, version)
    new_filename = new_stem + ".md"
    new_path = path.parent / new_filename
    log["new_filename"] = new_filename

    # Préparer le contenu rewritten si frontmatter
    new_content = None
    if frontmatter:
        # Aligner title sur le nouveau stem
        new_frontmatter = update_title_in_frontmatter(frontmatter, new_stem)
        new_content = f"---\n{new_frontmatter}\n---\n{body}"

    log["action"] = "RENAME"

    if apply_mode:
        # Sécurité : ne pas écraser si target existe
        if new_path.exists():
            log["action"] = "ERROR"
            log["reason"] = "target exists, collision"
            return log
        # Écrire le nouveau contenu si frontmatter
        if new_content is not None:
            path.write_text(new_content, encoding="utf-8")
        # Renommer
        path.rename(new_path)

    return log


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="Applique les renamings (dry-run par défaut)")
    args = parser.parse_args()

    if not VAULT_ROOT.exists():
        print(f"ERREUR : VAULT_ROOT introuvable : {VAULT_ROOT}")
        sys.exit(1)

    # Trouver tous les .md sous un dossier '00 - archives/'
    archived_files = []
    for path in VAULT_ROOT.rglob("*.md"):
        if "00 - archives" in path.parts:
            archived_files.append(path)

    print(f"Mode : {'APPLY' if args.apply else 'DRY-RUN'}")
    print(f"Fichiers archivés détectés : {len(archived_files)}\n")

    logs = []
    counts = {"RENAME": 0, "MIGRATE_R056": 0, "SKIP": 0, "ERROR": 0}
    with_version = 0
    without_frontmatter = 0

    for path in archived_files:
        log = process_file(path, args.apply)
        logs.append(log)
        counts[log["action"]] = counts.get(log["action"], 0) + 1
        if log["version"]:
            with_version += 1
        if not log["has_frontmatter"]:
            without_frontmatter += 1

    # Résumé
    print(f"== Résumé ==")
    print(f"  RENAME       : {counts.get('RENAME', 0)} (premier archivage)")
    print(f"  MIGRATE_R056 : {counts.get('MIGRATE_R056', 0)} (X.Y.Z → X.Y)")
    print(f"  SKIP         : {counts.get('SKIP', 0)} (déjà conformes)")
    print(f"  ERROR        : {counts.get('ERROR', 0)}")
    print(f"  Avec version frontmatter : {with_version}")
    print(f"  Sans frontmatter         : {without_frontmatter}\n")

    # Erreurs
    errors = [l for l in logs if l["action"] == "ERROR"]
    if errors:
        print("== ERREURS ==")
        for e in errors:
            print(f"  {e['path']}")
            print(f"    raison : {e['reason']}")

    # Sample des renames
    renames = [l for l in logs if l["action"] == "RENAME"]
    if renames:
        print(f"\n== Sample (10 premiers RENAME) ==")
        for r in renames[:10]:
            v = f"v{r['version']}" if r["version"] else "no version"
            print(f"  [{v}] {r['old_filename']}")
            print(f"    → {r['new_filename']}")

    # Save full log JSON
    import json
    out_path = Path(__file__).parent / ("rename_log_apply.json" if args.apply else "rename_log_dryrun.json")
    json.dump(logs, open(out_path, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    print(f"\nLog complet : {out_path}")

    if not args.apply and counts.get("RENAME", 0) > 0:
        print(f"\n>>> Pour appliquer : python {Path(__file__).name} --apply")


if __name__ == "__main__":
    main()
