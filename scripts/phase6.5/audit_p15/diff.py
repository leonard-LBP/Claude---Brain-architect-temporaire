"""Compute diff: manuel props - notion props - exclusions
Output: missing_props.json
"""
import json, re, unicodedata

ROOT = r'C:/Users/leona/LBP - dev/Claude - Brain architect temporaire/scripts/phase6.5/audit_p15'

manuals = json.load(open(f'{ROOT}/manuals_props.json','r',encoding='utf-8'))
schemas = json.load(open(f'{ROOT}/notion_schemas.json','r',encoding='utf-8'))


def norm(s):
    """Normalize: NFC, lowercase, strip, collapse spaces, replace fancy quotes."""
    if not s: return ''
    s = unicodedata.normalize('NFC', s)
    s = s.replace('’', "'").replace('‘', "'")
    s = s.replace('–', '-').replace('—', '-')
    s = s.replace(' ', ' ')
    s = re.sub(r'\s+', ' ', s).strip().lower()
    return s


# Excluded (system / handled elsewhere)
SYSTEM_EXCLUDED_NORM = {norm(x) for x in [
    'Created Date', 'Last Updated Date', 'Nom', 'createdtime', 'url'
]}


def should_exclude_manual_prop(prop, has_advanced_note):
    """Return reason or None."""
    name = prop['name']
    nm = norm(name)
    t = prop['type']
    sec = prop['section']

    if nm in SYSTEM_EXCLUDED_NORM:
        return 'system'
    # Relations are handled in Pass 2.1 (skip relation rows in 4.3)
    if t == 'RELATION':
        return 'relation_pass21'
    # Rollups handled Pass 2.2
    if t == 'ROLLUP':
        return 'rollup_pass22'
    # Section 4.5 formulas: per consigne, exclure les formules différées complexes.
    # Conservative: exclure toutes les formules 4.5 (les natives simples seront ajoutées manuellement plus tard si besoin).
    if sec == '4.5' and t == 'FORMULA':
        return 'formula_deferred_45'
    # Source d'information relation (without (texte)) — relation, kept differed
    if 'source' in nm and 'information' in nm and '(texte)' not in nm:
        return 'source_info_relation_deferred'
    # Lien vers la note avancée only if has_advanced_note=False
    if 'lien vers la note' in nm and not has_advanced_note:
        return 'no_advanced_note'
    # Skip headings/empty
    if not name or name.startswith('-'):
        return 'invalid_name'
    return None


# Compute diffs only for BDDs we have schemas for
diffs = {}
for bdd, schema in schemas.items():
    if bdd not in manuals:
        diffs[bdd] = {'error': 'no manual'}
        continue
    has_adv = manuals[bdd]['has_advanced_note']
    notion_norm = {norm(x) for x in schema}
    seen = set()
    missing = []
    excluded_log = []
    for p in manuals[bdd]['props']:
        nm = norm(p['name'])
        if nm in seen:
            continue
        seen.add(nm)
        reason = should_exclude_manual_prop(p, has_adv)
        if reason:
            excluded_log.append({'name': p['name'], 'type': p['type'], 'section': p['section'], 'reason': reason})
            continue
        if nm not in notion_norm:
            missing.append(p)
    diffs[bdd] = {
        'has_advanced_note': has_adv,
        'missing': missing,
        'excluded_count': len(excluded_log),
    }

with open(f'{ROOT}/missing_props.json','w',encoding='utf-8') as f:
    json.dump(diffs, f, ensure_ascii=False, indent=2)

# Print summary
for bdd, d in diffs.items():
    if 'error' in d:
        print(f"{bdd}: ERROR {d['error']}")
        continue
    miss = d['missing']
    print(f"{bdd}: {len(miss)} missing — " + ", ".join(f"[{p['section']}] {p['name']} ({p['type']})" for p in miss[:6]))
