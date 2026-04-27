"""Parse 28 Twin manuals and extract props from sections 4.1, 4.2, 4.3 (jumelles), 4.4, 4.5.
Output: manuals_props.json — {bdd_name: {has_advanced_note, props: [{name, type, taxonomies, section, raw_type, formula}]}}
"""
import re, os, json

MANUAL_DIR = r'H:/Drive partagés/LBP - shared/Architecture data/Manuels de BDD/Digital Twin'
OUT = r'C:/Users/leona/LBP - dev/Claude - Brain architect temporaire/scripts/phase6.5/audit_p15/manuals_props.json'

REG = r'C:/Users/leona/LBP - dev/Claude - Brain architect temporaire/scripts/phase6.5/output/bdd_registry.json'
with open(REG, 'r', encoding='utf-8') as f:
    reg = json.load(f)
bdd_names = list(reg['databases'].keys())


def parse_frontmatter(content):
    m = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    fm = {}
    if not m:
        return fm
    for line in m.group(1).splitlines():
        mm = re.match(r'^(\w+):\s*(.*)$', line)
        if mm:
            v = mm.group(2).strip().strip('"').strip("'")
            fm[mm.group(1)] = v
    return fm


def get_section(content, n):
    """Get section ## 4.n body."""
    pat = rf'^## 4\.{n}[^\n]*$'
    m = re.search(pat, content, re.MULTILINE)
    if not m:
        return ''
    start = m.end()
    # find next ## or # heading
    end_m = re.search(r'^#{1,2} ', content[start:], re.MULTILINE)
    if end_m:
        return content[start:start + end_m.start()]
    return content[start:]


def parse_table(body):
    """Yield dict rows from any markdown table in body. Header column names are stripped."""
    lines = body.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.strip().startswith('|') and i + 1 < len(lines) and re.match(r'^\s*\|[\s\-:|]+\|\s*$', lines[i + 1]):
            # parse header
            headers = [c.strip() for c in line.strip().strip('|').split('|')]
            i += 2
            while i < len(lines) and lines[i].strip().startswith('|'):
                row_line = lines[i].strip().strip('|')
                # split but keep cell count
                cells = [c.strip() for c in row_line.split('|')]
                if len(cells) >= len(headers):
                    row = dict(zip(headers, cells[:len(headers)]))
                    yield row
                i += 1
        else:
            i += 1


def normalize_type(t):
    t = (t or '').strip().lower()
    if 'multi' in t and ('sél' in t or 'sel' in t):
        return 'MULTI_SELECT'
    if 'sél' in t or 'select' in t.lower():
        return 'SELECT'
    if 'texte' in t:
        return 'RICH_TEXT'
    if 'url' in t:
        return 'URL'
    if 'date' in t:
        return 'DATE'
    if 'nombre' in t or 'number' in t:
        return 'NUMBER'
    if 'relation' in t:
        return 'RELATION'
    if 'rollup' in t:
        return 'ROLLUP'
    if 'formule' in t or 'formula' in t:
        return 'FORMULA'
    if 'bool' in t or 'check' in t:
        return 'CHECKBOX'
    if 'people' in t or 'personne' in t:
        return 'PEOPLE'
    if 'fichier' in t or 'files' in t:
        return 'FILES'
    if 'titre' in t or 'title' in t:
        return 'TITLE'
    return t.upper().replace(' ', '_') or 'UNKNOWN'


def extract_taxos(s):
    """Return list of taxo codes referenced (e.g. ASSET.SUBTYPE.LBP)."""
    if not s:
        return []
    return re.findall(r'\b[A-Z][A-Z0-9_]+(?:\.[A-Z0-9_]+)+(?:\.LBP)?\b', s)


def parse_manual(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    fm = parse_frontmatter(content)
    res = {
        'has_advanced_note': fm.get('has_advanced_note', '').lower() == 'true',
        'code': fm.get('code', ''),
        'props': []
    }
    for n in [1, 2, 3, 4, 5]:
        body = get_section(content, n)
        if not body:
            continue
        for row in parse_table(body):
            # find the "name" column (first col, often "Champ" or "Nom" or "Propriété")
            name_keys = [k for k in row if k and re.match(r'^(champ|nom|propri|prop|relation|rollup)', k.lower())]
            name = ''
            if name_keys:
                name = row[name_keys[0]].strip()
            else:
                # take first non-empty
                for k, v in row.items():
                    if v.strip():
                        name = v.strip()
                        break
            if not name or name.startswith('-') or name.lower() in ('champ', 'nom', 'propriété', 'propriete', 'relation', 'rollup'):
                continue

            # Type column
            type_keys = [k for k in row if k and 'type' in k.lower()]
            raw_type = row[type_keys[0]] if type_keys else ''
            ntype = normalize_type(raw_type)

            # Taxonomy column
            taxo_keys = [k for k in row if k and 'taxo' in k.lower()]
            taxo_raw = row[taxo_keys[0]] if taxo_keys else ''
            taxos = extract_taxos(taxo_raw)

            # In section 4.5 (formula), capture the formula body in instructions if any
            res['props'].append({
                'name': name,
                'raw_type': raw_type,
                'type': ntype,
                'taxonomies': taxos,
                'section': f'4.{n}',
            })
    return res


out = {}
for bdd in bdd_names:
    fname = f'Manuel de BDD - {bdd}.md'
    p = os.path.join(MANUAL_DIR, fname)
    out[bdd] = parse_manual(p)
    print(f"{bdd}: {len(out[bdd]['props'])} props (has_adv={out[bdd]['has_advanced_note']})")

with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print('Wrote', OUT)
