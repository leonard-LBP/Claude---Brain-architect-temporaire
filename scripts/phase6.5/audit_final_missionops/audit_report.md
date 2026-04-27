# Audit final Mission Ops — Symétrie Manuel ↔ Notion ↔ WR-RD

**Date** : 27-04-2026 · **Périmètre** : 4 BDDs Mission Ops (Sources d'informations, Meetings, Actions LBP, Bricks)
**Méthode** : 3 scripts Python (parse_manuel_missionops.py, diff_manuel_notion_missionops.py, audit_wrrd_missionops.py) sur les 4 manuels parsés (sections 4.x), schémas Notion live fetchés, WR-RD lus en parallèle. Comparaison Unicode-insensible (apostrophes U+2019/U+0027 normalisées).

## A. Symétrie Manuel ↔ Notion

| BDD | Manuel attendu | Notion live | MISSING_NOTION | EXTRA_NOTION | Pass4 différé |
|---|---:|---:|---:|---:|---:|
| Sources d'informations | 30 | 31 | 0 | 1 | 0 |
| Meetings | 26 | 26 | 1 | 1 | 0 |
| Actions LBP | 29 | 29 | 1 | 1 | 3 |
| Bricks | 23 | 23 | 1 | 1 | 0 |

### MISSING_NOTION (3 occurrences, même cause)

| BDD | Prop manuel | Cause |
|---|---|---|
| Meetings | `Notes consultant` (4.1) | **Écart de nom** : manuel dit `Notes consultant`, Notion dit `Notes du consultant` |
| Actions LBP | `Notes consultant` (4.1) | idem |
| Bricks | `Notes consultant` (4.1) | idem |

→ Le manuel **Sources d'informations** utilise correctement `Notes du consultant`. Les 3 autres manuels Mission Ops ont un nom de champ divergent (`Notes consultant` au lieu de `Notes du consultant`). C'est une **incohérence côté manuel** : Notion + WR-RD sont alignées entre elles.

### EXTRA_NOTION (4 occurrences)

| BDD | Prop Notion | Type | Hypothèse cause |
|---|---|---|---|
| Sources d'informations | `a pour dérivés (sources d'informations) (texte)` | text | Jumelle texte du miroir auto **non documentée** côté manuel ni WR-RD. Le manuel ne déclare la jumelle texte que pour `est dérivée de`, pas pour le miroir `a pour dérivés`. Vraie dette légère. |
| Meetings | `Notes du consultant` | text | Miroir de l'écart de nom (la prop existe avec ce nom Notion, le manuel cherche `Notes consultant`) |
| Actions LBP | `Notes du consultant` | text | idem |
| Bricks | `Notes du consultant` | text | idem |

3 des 4 EXTRA_NOTION sont la contrepartie des 3 MISSING_NOTION (même problème de naming). Le seul vrai EXTRA non-explicable par l'écart de nom est `a pour dérivés (sources d'informations) (texte)` sur Sources.

## B. Symétrie Manuel ↔ WR-RD

| BDD | Manuel | WR-RD | Missing WR-RD | Extra WR-RD |
|---|---:|---:|---:|---:|
| Sources d'informations | 28 | 30 | 0 | 2 (`Created Date`, `Last Updated Date`) |
| Meetings | 24 | 26 | 0 | 2 (idem) |
| Actions LBP | 30 | 32 | 0 | 2 (idem) |
| Bricks | 21 | 23 | 0 | 2 (idem) |

Les "extras" WR-RD sont uniquement les **2 props système Notion** (`Created Date` / `Last Updated Date`) qui sont déclarées en WR-RD comme jumelles de lecture mais pas dans la table 4.x du manuel — pratique standard Twin également. **Aucun écart fonctionnel.**

À noter : `Notes consultant` est dans les manuels Meetings/Actions LBP/Bricks ET dans leurs WR-RD respectives sous le **même nom divergent** (Manuel et WR-RD sont alignés entre eux ; seule Notion utilise `Notes du consultant`). La parité Manuel↔WR-RD est donc parfaite, c'est l'écart Manuel/WR-RD↔Notion qui pose problème.

## C. Apostrophes et typographie (R-052)

- Manuel : **0** apostrophe ASCII U+0027 dans les noms de props
- Notion : **0** apostrophe ASCII U+0027
- WR-RD : **0** apostrophe ASCII U+0027

✅ **R-052 respectée à 100% sur les 4 BDDs Mission Ops** (apostrophes U+2019 partout).

## D. Relations bidir / self-rel / miroirs auto

### Self-relations (2 attendues)

| BDD | Côté DDL | Côté miroir auto | Manuel | WR-RD | Notion |
|---|---|---|:-:|:-:|:-:|
| Actions LBP | `appartient à (activité)` | `contient (actions)` | ✅ | ✅ | ✅ |
| Sources d'informations | `est dérivée de (sources d'informations)` | `a pour dérivés (sources d'informations)` | ✅ | ✅ | ✅ |

### Relations bidir DUAL (6 paires)

| Paire | Côté A | Côté B | Notion |
|---|---|---|:-:|
| Meetings ↔ Actions LBP (préparation) | `est préparé par (actions LBP)` (Meetings) | `prépare (meetings)` (Actions LBP) | ✅ |
| Meetings ↔ Actions LBP (exécution) | `est exécuté avec (actions LBP)` (Meetings) | `se déroule pendant (meetings)` (Actions LBP) | ✅ |
| Meetings ↔ Actions LBP (suivi) | `est suivi par (actions LBP)` (Meetings) | `assure le suivi de (meetings)` (Actions LBP) | ✅ |
| Actions LBP ↔ Bricks (utilise) | `utilise (bricks)` (Actions LBP) | `est utilisée par (actions LBP)` (Bricks) | ✅ |
| Actions LBP ↔ Bricks (produit) | `produit (bricks)` (Actions LBP) | `est produite par (actions LBP)` (Bricks) | ✅ |
| Bricks ↔ Sources (documentation) | `est documentée par (sources d'informations)` (Bricks) | `documente (bricks)` (Sources) | ✅ |

✅ Les **6 paires bidir + 2 self-rel** sont complètes des deux côtés sur Notion (vérifié via les schémas live). Toutes les jumelles texte `(texte)` correspondantes sont présentes côté manuel + WR-RD + Notion.

### Pass 4 différée (Actions LBP)

3 props attendues présentes en Manuel + WR-RD section 4.5, **absentes Notion** comme prévu :
- `Nb actions (activité)` (Rollup)
- `Nb actions terminées (activité)` (Rollup)
- `Avancement (activité)` (Formule)

✅ État conforme à la décision Pass 4 différée. À matérialiser sur Notion lors d'un Pass 4 ultérieur.

### Indices observés / Indices d'existence (Sources)

✅ Bien absents de Notion ET du manuel ET de la WR-RD pour Sources d'informations (décision Leonard du 27-04-2026 propagée). Aucun signalement parasite.

## E. Verdict global

### ⚠ Petites incohérences à fixer (1 vraie + 1 déjà connue, faciles à corriger)

1. **Écart de nom `Notes consultant` ↔ `Notes du consultant`** sur 3 BDDs (Meetings, Actions LBP, Bricks)
   - **Source du défaut** : les 3 manuels (et leurs WR-RD alignées) utilisent `Notes consultant`, alors que Notion utilise `Notes du consultant`.
   - **Fix recommandé** : harmoniser les 3 manuels + 3 WR-RD vers `Notes du consultant` (le standard sémantique LBP, déjà présent sur Sources et sur tout le Twin). 6 fichiers à modifier (3 manuels × 1 prop + 3 WR-RD × 1 prop).
   - **Alternative** : renommer côté Notion `Notes du consultant` → `Notes consultant` sur 3 BDDs. Moins recommandé (rupture du standard "Notes du consultant" déjà en place sur Sources et Twin).

2. **Jumelle texte non documentée du miroir auto Sources** : `a pour dérivés (sources d'informations) (texte)` existe sur Notion mais n'est ni dans le manuel ni dans la WR-RD de Sources d'informations.
   - Le manuel déclare bien la jumelle texte de `est dérivée de` mais pas celle de `a pour dérivés`. Or si la jumelle texte côté DDL existe, son miroir n'a pas vocation systématique à être doublé. À arbitrer : soit la supprimer côté Notion (cohérent : un miroir auto n'a pas besoin de sa propre jumelle texte saisie), soit l'ajouter dans le manuel + WR-RD (incohérent avec le pattern Twin).
   - **Fix recommandé** : supprimer la jumelle texte `a pour dérivés (...) (texte)` côté Notion (pattern Twin = jumelle texte uniquement côté DDL, pas côté miroir).

### Ce qui est bon

- ✅ R-052 (apostrophes U+2019) : 100 % conforme sur les 4 BDDs
- ✅ Relations bidir DUAL (6 paires) et self-rel (2) : symétrie Notion parfaite des deux côtés
- ✅ Pass 4 différée Actions LBP : 3 props correctement présentes en manuel/WR-RD et absentes Notion
- ✅ Décision Sources sans `Indices observés` / `Indices d'existence` propagée correctement partout
- ✅ Parité Manuel↔WR-RD : 0 écart fonctionnel (seules les 2 props système `Created Date` / `Last Updated Date` sont en WR-RD et pas dans la table 4.x manuel — pattern standard)

### Bilan

- **Dette réelle** : 2 sujets (1 écart de nom sur 3 BDDs, 1 jumelle texte parasite sur Sources). Total **4 modifications** côté manuels + 3 côté WR-RD + 1 côté Notion (option recommandée).
- **Aucune anomalie majeure** 🔴.
- **Verdict** : **⚠ Très proche de la symétrie parfaite**. Les écarts détectés sont mineurs, locaux et facilement corrigeables.

---

**Annexes** : `manuels_parsed/*.json`, `notion_schemas.json`, `missing_in_notion.json`, `extra_in_notion.json`, `audit_wrrd_report.json`, `apos_violations.json`, `apos_wrrd.json`, `diff_summary.json` dans `scripts/phase6.5/audit_final_missionops/`.
