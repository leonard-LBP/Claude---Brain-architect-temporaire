#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 3 Pass A — Propagation .LBP strip + extraction citations taxos.

Usage:
    python run.py --dry-run   (default)
    python run.py --apply
"""
import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

VAULT_ROOT = Path(r"H:/Drive partagés/LBP - shared/Architecture data")
MANUELS_ROOT = VAULT_ROOT / "Manuels de BDD"

SCRIPT_DIR = Path(__file__).parent

# Regex
LBP_RE = re.compile(r"\.LBP\b")
# Taxon (Pattern B) checked first (longer), then taxo (Pattern A)
TAXON_RE = re.compile(r"\b[A-Z][A-Z0-9_]*\.[A-Z][A-Z0-9_]+\.[A-Z0-9_]+\b")
TAXO_RE = re.compile(r"\b[A-Z][A-Z0-9_]*\.[A-Z][A-Z0-9_]+\b")


def collect_targets():
    targets = []
    # 1. Manuels Twin (non récursif, hors WR-RD et 00 - archives)
    twin = MANUELS_ROOT / "Digital Twin"
    for f in sorted(twin.glob("*.md")):
        targets.append(f)
    # 2. WR-RD Twin
    twin_wrrd = twin / "WR-RD"
    if twin_wrrd.exists():
        for f in sorted(twin_wrrd.glob("*.md")):
            targets.append(f)
    # 3. Manuels Mission Ops
    mops = MANUELS_ROOT / "Mission Ops"
    for f in sorted(mops.glob("*.md")):
        targets.append(f)
    # 4. WR-RD Mission Ops
    mops_wrrd = mops / "WR-RD"
    if mops_wrrd.exists():
        for f in sorted(mops_wrrd.glob("*.md")):
            targets.append(f)
    # 5. Manuels Brain
    brain = MANUELS_ROOT / "Brain"
    for f in sorted(brain.glob("*.md")):
        targets.append(f)
    return targets


def extract_citations(content, file_rel):
    citations = []
    for lineno, line in enumerate(content.splitlines(), start=1):
        # Find all taxons first
        taxon_matches = list(TAXON_RE.finditer(line))
        taxon_spans = [(m.start(), m.end(), m.group()) for m in taxon_matches]

        line_trunc = line[:200]

        for start, end, code in taxon_spans:
            parent = ".".join(code.split(".")[:2])
            citations.append({
                "line_number": lineno,
                "line_content": line_trunc,
                "cited_code": code,
                "code_type": "taxon",
                "parent_taxo": parent,
            })

        # Find taxos (Pattern A) but skip those that are inside a taxon match
        for m in TAXO_RE.finditer(line):
            inside_taxon = False
            for ts, te, _ in taxon_spans:
                if m.start() >= ts and m.end() <= te:
                    inside_taxon = True
                    break
            if inside_taxon:
                continue
            citations.append({
                "line_number": lineno,
                "line_content": line_trunc,
                "cited_code": m.group(),
                "code_type": "taxo",
                "parent_taxo": None,
            })
    return citations


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="Apply changes (default: dry-run)")
    args = parser.parse_args()

    apply_mode = args.apply
    mode_label = "APPLY" if apply_mode else "DRY-RUN"
    print(f"[Phase 3 Pass A] mode={mode_label}")

    targets = collect_targets()
    print(f"[Phase 3 Pass A] {len(targets)} files in scope")

    files_report = []
    total_strips = 0
    files_modified = 0
    unique_codes = set()

    for fpath in targets:
        try:
            content = fpath.read_text(encoding="utf-8")
        except Exception as e:
            print(f"  ERROR reading {fpath}: {e}", file=sys.stderr)
            continue

        n_lbp = len(LBP_RE.findall(content))
        new_content = content
        if n_lbp > 0:
            new_content = LBP_RE.sub("", content)
            files_modified += 1
            total_strips += n_lbp
            if apply_mode:
                fpath.write_text(new_content, encoding="utf-8")

        citations = extract_citations(new_content, fpath)
        for c in citations:
            unique_codes.add(c["cited_code"])

        try:
            rel = fpath.relative_to(VAULT_ROOT).as_posix()
        except ValueError:
            rel = str(fpath)

        files_report.append({
            "file_path": rel,
            "lbp_strips": n_lbp,
            "citations": citations,
        })

    citations_report = {
        "metadata": {
            "generated_at": date.today().isoformat(),
            "mode": mode_label,
            "total_files_scanned": len(targets),
            "total_files_modified": files_modified,
            "total_lbp_strips": total_strips,
            "total_citations": sum(len(f["citations"]) for f in files_report),
            "unique_codes_count": len(unique_codes),
        },
        "files": files_report,
    }

    summary = {
        "metadata": citations_report["metadata"],
        "unique_codes": sorted(unique_codes),
        "per_file_strips": [
            {"file": f["file_path"], "lbp_strips": f["lbp_strips"], "citations_count": len(f["citations"])}
            for f in files_report
        ],
    }

    out_citations = SCRIPT_DIR / "citations_report.json"
    out_summary = SCRIPT_DIR / "migration_summary.json"
    out_citations.write_text(json.dumps(citations_report, ensure_ascii=False, indent=2), encoding="utf-8")
    out_summary.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"[Phase 3 Pass A] Files scanned : {len(targets)}")
    print(f"[Phase 3 Pass A] Files with .LBP : {files_modified}")
    print(f"[Phase 3 Pass A] Total .LBP strips : {total_strips}")
    print(f"[Phase 3 Pass A] Total citations  : {citations_report['metadata']['total_citations']}")
    print(f"[Phase 3 Pass A] Unique codes     : {len(unique_codes)}")
    print(f"[Phase 3 Pass A] Reports written  : {out_citations.name}, {out_summary.name}")


if __name__ == "__main__":
    main()
