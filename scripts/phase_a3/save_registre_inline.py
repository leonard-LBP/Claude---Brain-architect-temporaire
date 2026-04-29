"""
Phase A3.0 — saves the two inline Registre batches into a unified JSON.
Reads them from already-fetched data embedded in this script (paste from tool results).
"""
# Helper: this script is meant to be run AFTER manually pasting the two batches below.
# To avoid re-querying Notion, we'll re-extract from the conversation tool-results dir if available.
import json
from pathlib import Path
import os

ROOT = Path(__file__).parent / "output" / "raw"
ROOT.mkdir(parents=True, exist_ok=True)

# Search the tool-results directory for the most recent two notion-query-database-view results
TR = Path(r"C:/Users/leona/.claude/projects/C--Users-leona-LBP---dev-Claude---Brain-architect-temporaire/665c6c60-dd66-4615-ac98-78b9622882d5/tool-results")
files = sorted(TR.glob("mcp-44de9dc4-*notion-query-database-view*.txt"), key=lambda p: p.stat().st_mtime)
print(f"Found {len(files)} notion-query-view tool-result files")
for i, p in enumerate(files):
    print(f"  [{i}] {p.name} ({p.stat().st_size} bytes)")
