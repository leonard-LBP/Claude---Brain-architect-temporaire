# Audit factuel des frontmatter — Architecture data

> **Scope** : Session
> **Date** : 27-04-2026
> **Périmètre** : ensemble du vault `H:\Drive partagés\LBP - shared\Architecture data\` hors `00 - archives/`.
> **Objectif** : factualiser l'état des frontmatter de chaque typologie d'objets pour préparer une harmonisation. Lecture seule.

---

## 0) Distinction conceptuelle utilisée

- **(A) Frontmatter du template-doc** : YAML en haut de fichier qui décrit **le template lui-même** (en tant que doc résident dans la BDD Docs méta : title, doc_type=template, version, purpose, tags, etc.).
- **(B) Frontmatter à reproduire** : exemple-modèle de YAML que **les docs instanciés depuis ce template doivent porter**, normalement encapsulé dans un commentaire HTML / un bloc INSTR dans le **corps** du template.

Une bonne hygiène veut que (A) et (B) soient nettement séparés : (A) parle du template ; (B) parle de l'instance générée.

---

## 1) Audit Templates d'instanciation — `00 - Docs méta/Templates d'instanciation/`

13 templates actifs (hors archives). Verdict sommaire : **3 anomalies majeures**, **2 anomalies de mise en forme**, **8 templates conformes**.

| Template | Champs (A) — frontmatter du template | (A) cohérent ? | (B) présent ? | (B) localisation | Anomalie |
|---|---|---|---|---|---|
| `Template - Manuel de BDD - Digital Twin.md` | title, doc_type=template, purpose, version (6.3.0), tags, cleanup_rules, notes | OUI | **NON explicitement** | corps (settings) — **pas de bloc dédié `FRONTMATTER_INSTANCE`** | (B) absent : aucun gabarit explicite du frontmatter à reproduire |
| `Template - Manuel de BDD - Mission Ops.md` | title, doc_type=template, purpose, version (5.1.0), date_creation, tags, cleanup_rules, notes | OUI | **NON explicitement** | corps (settings) — **pas de bloc dédié `FRONTMATTER_INSTANCE`** | (B) absent : aucun gabarit explicite du frontmatter à reproduire |
| `Template - WR-RD - Digital Twin.md` | title, doc_type=template, purpose, version (1.3.0), tags, cleanup_rules, notes | OUI | OUI | bloc `<!-- @INSTR-START: FRONTMATTER_INSTANCE -->` (lignes 71+) | aucune |
| `Template - WR-RD - Mission Ops.md` | title, doc_type=template, purpose, version (1.0.0), date_creation, tags, cleanup_rules, notes | OUI | OUI | bloc `<!-- @INSTR-START: FRONTMATTER_INSTANCE -->` (lignes 74+) | aucune |
| `template-taxonomie.md` | canonical_name, namespace_code, summary, is_open, open_policy, scale_kind, is_ordinal, selection_mode, cardinality, aliases, keywords, detection_clues | **NON** — c'est un (B), pas un (A) | NON séparé : **(A) = (B)** | le frontmatter en tête est lui-même le modèle d'instance | **ANOMALIE MAJEURE** : pas de niveau (A). Le template-doc n'a **pas** son propre frontmatter (title, doc_type=template, version du template, purpose). Le YAML en tête est destiné à être recopié tel quel dans les taxonomies générées (avec les commentaires `#`). |
| `template-note_concept_lbp.md` | title, doc_type=template, purpose, version (1.1.1), tags | OUI | OUI | bloc `<!-- INSTR-START: FRONTMATTER_NOTE_INSTANCE -->` (lignes 40+) | aucune |
| `template-methode_lbp.md` | title, doc_type=template, purpose, version (1.1.0), status (prêt), tags | OUI | OUI | bloc `<!-- INSTR-START: FRONTMATTER -->` (lignes 14+) | (B) très divergent du (A) : `type:`/`titre:`/`statut:` au lieu de `doc_type:`/`title:`/`status:` (incohérence de nommage entre template-doc et instance) |
| `template-prompt_maitre_lbp.md` | title, doc_type=template, purpose, version (1.1.0), tags | OUI | OUI mais **double-encapsulation ambiguë** | (1) bloc `<!-- INSTR-START: FRONTMATTER -->` lignes 51-66 + (2) **second bloc YAML au format `---...---` lignes 67-79** placé en plein milieu du document hors commentaire HTML | **ANOMALIE de forme** : le second bloc YAML lignes 67-79 est techniquement dans le corps mais peut être interprété comme frontmatter par certains parsers ; double frontmatter visuel |
| `template-meta_logic_block_lbp.md` | title, doc_type=template, purpose, version (1.1.0), tags | OUI | OUI mais **double-encapsulation ambiguë** | (1) bloc `<!-- INSTR-START: FRONTMATTER -->` lignes 52-67 + (2) **second bloc YAML lignes 68-80** | **ANOMALIE de forme** identique à `template-prompt_maitre_lbp` |
| `Template de system prompt.md` | title, doc_type=template, purpose, version (1.0.0), tags | OUI | OUI mais minimal | bloc `<!-- INSTR-START: FRONTMATTER -->` (lignes 35-44) — descriptif texte, **pas de YAML modèle** | (B) sous-spécifié : juste une liste à puces ("title : System prompt — ..."), pas un YAML copiable |
| `Template-Fiche_outil_LBP.md` | title, doc_type=template, purpose, version (1.1.0), status, tags, cleanup_rules | OUI | **NON** | aucun bloc dédié au frontmatter à reproduire | (B) **absent** : le template ne dit pas quel frontmatter l'instance doit porter |
| `Template-prompt_lbp.md` | title (template-prompt-lbp), doc_type=template, purpose, version (1.1.0), status, tags, cleanup_rules, notes | OUI | NON formel | placeholder convention seule (settings) | (B) absent comme bloc dédié ; placeholders documentés mais pas de gabarit YAML |
| `Template méta de Brick.md` | title (`"Brick — {{titre_court_lisible}}"`), doc_type=`"brick"`, brick_type, purpose, version (0.1.0), status, mission, client_alias, timeframe, scope, inputs_structured, etc. | **NON** — c'est un (B), pas un (A) | NON séparé : **(A) = (B)** | frontmatter en tête = modèle d'instance | **ANOMALIE MAJEURE** : doc_type=`"brick"` (pas `"template"`), title contient des `{{placeholders}}`. Le template-doc lui-même n'a aucune métadonnée propre. |
| `template-db-manual-mission_ops.md` | title, doc_type=template, purpose, version (0.3.0), status, tags, cleanup_rules, notes | OUI | OUI mais **inhabituel** | bloc YAML décrit en texte brut au sein du commentaire `<!-- INSTR-START: GUIDE_GLOBAL -->` (lignes 33-41) | (B) présent mais pas dans un bloc dédié ; mêlé au guide global. Note : **template d'ancienne génération**, peut-être candidat à archivage si remplacé par `Template - Manuel de BDD - Mission Ops.md` v5.1.0 (à arbitrer avec Leonard). |

### Synthèse Section 1

- **3 anomalies majeures sur (A)** : `template-taxonomie.md`, `Template méta de Brick.md`, et dans une moindre mesure les deux templates avec **double frontmatter en clair** (`template-prompt_maitre_lbp.md`, `template-meta_logic_block_lbp.md`).
- **5 templates sans (B) explicite** : Template Manuel Twin, Template Manuel Mission Ops, Template Fiche outil, Template-prompt_lbp, Template de system prompt.
- **Doublon templates Mission Ops Manuel** suspecté : `Template - Manuel de BDD - Mission Ops.md` (v5.1.0) vs `template-db-manual-mission_ops.md` (v0.3.0) — coexistent. À clarifier.

---

## 2) Audit instances — par typologie d'objet généré

### 2.1 Manuels de BDD — Digital Twin (28 fichiers)

**Pattern observé (échantillon : Actifs, Problématiques, OKR sandbox)** :
```yaml
title, doc_type=db_manual, purpose, version, template_version (6.1.0), bdd_canonical_name, object_type, architecture_family, ui_family, knowledge_regime, officiality_regime, has_advanced_note, tags
```

| Champ | Présence | Conformité (B) du template Manuel Twin |
|---|---|---|
| title, doc_type, purpose, version, tags | toutes les 28 | conforme |
| **template_version** | toutes (6.1.0) | **DÉCALAGE** : le template actuel est v6.3.0 → les 28 manuels sont **2 versions en retard** sur le template |
| bdd_canonical_name, object_type | toutes | OK |
| architecture_family, ui_family, knowledge_regime, officiality_regime | toutes | OK |
| has_advanced_note | toutes | OK |
| **code** (DBMAN_xxx) | **ABSENT** côté Twin | **ASYMÉTRIE** vs Mission Ops qui le porte |
| **created_at / date_creation** | **ABSENT** côté Twin | **ASYMÉTRIE** vs Mission Ops |

### 2.2 Manuels de BDD — Mission Ops (4 fichiers)

**Pattern observé (Actions LBP, Bricks, Meetings, Sources d'informations)** :
```yaml
title, doc_type=db_manual, purpose, version, template_version (5.1.0), date_creation, code (DBMAN_ACTS/BRKS/...), bdd_canonical_name, object_type, architecture_scope, mission_ops_family, knowledge_regime, execution_tracking, tags
```

| Champ | Présence | Conformité (B) du template Manuel Mission Ops |
|---|---|---|
| title, doc_type, purpose, version, template_version, date_creation, tags | toutes les 4 | conforme |
| **code** | toutes les 4 | conforme — **présent ici, absent côté Twin** |
| architecture_scope, mission_ops_family, knowledge_regime, execution_tracking | toutes | OK |

### 2.3 WR-RD — Digital Twin (28 fichiers)

**Pattern observé (Actifs, Problématiques)** :
```yaml
title, doc_type=wr_rd, target_bdd_canonical_name, target_bdd_code (DBMAN_xxx), parent_manual, wr_rd_code (WRRD_xxx), domain, version, template_version (1.2.0), created_at (JJ-MM-YYYY), tags
```

| Champ | Présence | Conformité |
|---|---|---|
| title, doc_type=wr_rd, target_bdd_canonical_name, target_bdd_code, parent_manual, wr_rd_code, domain | toutes | conforme |
| **created_at** au format **`JJ-MM-YYYY`** (`"26-04-2026"`) | toutes (28) | conforme à R-044 |
| **template_version 1.2.0** | toutes | **DÉCALAGE LÉGER** : le template actuel WR-RD Twin est v1.3.0 → 28 WR-RD à mettre à jour |

### 2.4 WR-RD — Mission Ops (4 fichiers)

**Pattern observé (Bricks)** :
```yaml
title, doc_type=wr_rd, target_bdd_canonical_name, target_bdd_code, parent_manual, wr_rd_code, domain (Mission Ops), version, template_version (1.0.0), date_creation (YYYY-MM-DD), tags
```

| Champ | Présence | Conformité |
|---|---|---|
| Tous les champs structurels | toutes | conforme |
| **`date_creation: "2026-04-27"` au format ISO** | toutes (4) | **ASYMÉTRIE** vs WR-RD Twin qui utilise `created_at: "JJ-MM-YYYY"` |

> **Anomalie transverse importante** : entre Twin et Mission Ops, **deux noms de champ différents** (`created_at` vs `date_creation`) **et deux formats de date différents** (JJ-MM-YYYY vs YYYY-MM-DD). R-044 impose JJ-MM-YYYY transverse → **les 4 manuels Mission Ops + 4 WR-RD Mission Ops sont non conformes à R-044**.

### 2.5 Taxonomies (~96 fichiers, échantillon : ASSET.SUBTYPE.LBP, COL.TYPE.LBP, INDIC.TIME_ROLE.LBP)

**Pattern observé** : pas de `title:`, pas de `doc_type:` — frontmatter qui démarre directement par `canonical_name:`, conforme au gabarit (B) du `template-taxonomie.md`.

```yaml
canonical_name, namespace_code, summary, is_open, open_policy, scale_kind, is_ordinal, selection_mode, cardinality, aliases, keywords, detection_clues
```

| Observation | Détail |
|---|---|
| Conformité au template (B) | OK structurellement |
| **Hétérogénéité de style** | Certaines taxos (ASSET.SUBTYPE, COL.TYPE) gardent les commentaires `#` du template ; d'autres (INDIC.TIME_ROLE en `Taxonomies/`) les ont supprimés. Le template recommande de les garder. |
| **DOUBLON CRITIQUE** | `INDIC.TIME_ROLE.LBP.md` existe à **deux emplacements** : `Architecture data/INDIC.TIME_ROLE.LBP.md` (racine !) ET `Architecture data/Taxonomies/INDIC.TIME_ROLE.LBP.md`, avec **frontmatter différents**. La version `Taxonomies/` a en outre **un double `---`** (lignes 25-27) cassant la fermeture du frontmatter. |
| **Absence de niveau (A)-instance** | Pas de `title:`, pas de `doc_type: "taxonomy"`, pas de `version` du doc. Cohérent avec le template (qui n'a pas non plus de (A)) mais **anomalie de gouvernance** : ces 96 docs n'ont pas de métadonnées de doc-niveau pour la BDD Taxonomies / les agents. |

### 2.6 Notes de Concept (~72 fichiers, échantillon : Actif, Brick, Connaissance)

**Pattern observé** :
```yaml
title, doc_type=concept, concept_code (CPT.xxx.LBP.xxx), canonical_name, summary, aliases, keywords, detection_clues, anti_confusions, version, tags
```

| Observation | Détail |
|---|---|
| Conformité au template (B) | très bonne |
| Format `version` | mixte : `"07-04-2026 v0.5.0"`, `"22-02-2026 v0.1.0"` (Concept Actif, Brick) — concatène date + semver. **À normaliser** : c'est un anti-pattern (deux infos dans un seul champ). Le champ `version` devrait être pur semver et la date être un `created_at` ou `updated_at` séparé. |

### 2.7 Méthodes (3 fichiers actifs)

**Pattern observé** : ne respecte **pas** le (A) de `template-methode_lbp.md`, respecte le (B).
```yaml
type=methode_lbp, id (METH_xxx), titre, purpose, version, statut
```
- Champs `type:` (au lieu de `doc_type:`), `titre:` (au lieu de `title:`), `statut:` (au lieu de `status:`) → **divergence de nommage canonique** vs reste du vault. Volontaire selon le template, mais incohérent transversalement.

### 2.8 Prompts maîtres Twin (9 fichiers)

**Pattern observé (Refactor)** :
```yaml
title, doc_type=master_prompt, prompt_code (PRMPT.xxx), canonical_name, target_function, intended_agent, summary, aliases, status, version, tags
```
Très conforme au (B) du template `template-prompt_maitre_lbp.md`.

### 2.9 Prompts maîtres Brain Architect (3 fichiers) + System Prompts (≥8) + User Prompts (≥8) + Function Prompts (≥5)

Échantillon `PRMPT-SYS_BRAIN-ARCHITECT.md` :
```yaml
title, doc_type=system_prompt, agent, prompt_code, purpose, version, status, tags
```
→ utilise `agent:` (champ propre, pas dans le template système), conforme par ailleurs.

### 2.10 Logic Blocks (échantillon : `Logic block - Refactor - Problématiques.md`)

```yaml
title, doc_type=logic_block, logic_block_code (LGBLK.xxx), canonical_name, operation, target_scope, summary, aliases, status, version, tags
```
Conforme au (B) du `template-meta_logic_block_lbp.md`.

### 2.11 Templates de Bricks (échantillon : Profil - Organisation, Visualisation Mermaid, Enjeux pré-identifiés)

**Pattern observé** :
```yaml
type=template_brick, id (TPL_BRICK_xxx), version, title, purpose, format
```
Très minimaliste, **divergent de tout le reste** : `type:` au lieu de `doc_type:`, pas de `tags`, pas de `status`, pas de `created_at`. Cohérent intra-typologie mais non aligné transversalement.

---

## 3) Audit autres docs méta + docs satellites

| Catégorie | Frontmatter typique | Variabilité interne | Anomalies |
|---|---|---|---|
| Doctrines & playbooks (1 fichier actif : Playbook Macro-archi v2) | title, version, status, audience, purpose, tags | n/a (1 fichier) | absence de `doc_type` (devrait être `playbook` ou `doctrine`) |
| Méthodes (3 fichiers) | type=methode_lbp, id, titre, purpose, version, statut | uniforme entre les 3 | nommage de champs divergent du reste (cf. 2.7) |
| Prompts maîtres Twin (9) | title, doc_type, prompt_code, ... | uniforme | OK |
| System prompts agents (≥8) | title, doc_type=system_prompt, agent, prompt_code, ... | présence variable de `agent` | OK |
| Logic blocks (≥20 dans sous-dossiers BDD) | title, doc_type=logic_block, logic_block_code, ... | uniforme sur l'échantillon | OK |
| Templates de Bricks (≥12) | type=template_brick, id, version, title, purpose, format | uniforme intra | divergent transversalement |
| Taxonomies (~96) | canonical_name, namespace_code, ... (sans title/doc_type) | hétérogénéité commentaires `#` ; doublon INDIC.TIME_ROLE | cf. 2.5 |
| Notes de Concept (~72) | title, doc_type=concept, concept_code, ... | format `version` parfois date+semver | cf. 2.6 |

---

## 4) Synthèse Common Ground & recommandations

### 4.1 Common ground actuel (présent dans une majorité de typologies)

- `title` (sauf taxonomies, méthodes utilisent `titre`, templates de bricks oui)
- `version` (présent partout)
- `purpose` (très majoritaire)
- `tags` (très majoritaire)
- `doc_type` (présent partout sauf : taxonomies, méthodes (`type`), templates de bricks (`type`))

### 4.2 Common ground théorique recommandé pour tout doc Brain (à arbitrer)

| Champ | Pourquoi |
|---|---|
| `title` | clé d'affichage humain |
| `doc_type` | discriminant pour les agents et BDD Docs méta (uniformisé : préférer `doc_type` partout, retirer `type`) |
| `code` (ou nom métier : `concept_code`, `prompt_code`, `taxonomy_code`, `wr_rd_code`, `dbman_code`) | identifiant pivot stable, immuable |
| `version` | semver pur de l'instance |
| `template_version` | traçabilité génération (déjà appliqué Manuels & WR-RD) |
| `created_at` ou `date_creation` | un seul nom canonique à choisir, format JJ-MM-YYYY (R-044) |
| `status` | gouvernance documentaire (draft / review / validated / archived) |
| `tags` | indexation |
| `purpose` ou `summary` | description courte pour retrieval |

### 4.3 Extensions par type (légitimes, à conserver)

- Manuels : `bdd_canonical_name`, `object_type`, `architecture_family/scope`, `knowledge_regime`, `officiality_regime`, `has_advanced_note`, `mission_ops_family`, `execution_tracking`
- WR-RD : `target_bdd_canonical_name`, `target_bdd_code`, `parent_manual`, `wr_rd_code`, `domain`
- Taxonomies : `canonical_name`, `namespace_code`, `is_open`, `open_policy`, `scale_kind`, `is_ordinal`, `selection_mode`, `cardinality`, `aliases`, `keywords`, `detection_clues`
- Concepts : `concept_code`, `canonical_name`, `summary`, `aliases`, `keywords`, `detection_clues`, `anti_confusions`
- Prompts/Logic blocks : `prompt_code`, `logic_block_code`, `target_function`, `intended_agent`, `operation`, `target_scope`

### 4.4 Recommandations de mise à jour des templates

| Template | Recommandation |
|---|---|
| `template-taxonomie.md` | **Refonte** : ajouter un vrai (A) en tête (`title: template-taxonomie`, `doc_type: template`, `version`, etc.), encapsuler le YAML actuel dans `<!-- @INSTR-START: FRONTMATTER_INSTANCE -->` |
| `Template méta de Brick.md` | **Refonte** : créer un (A) propre, encapsuler le YAML actuel dans un bloc INSTR (B) |
| `template-prompt_maitre_lbp.md`, `template-meta_logic_block_lbp.md` | **Encapsuler** le second YAML lignes 67+ dans un commentaire HTML INSTR pour éviter la confusion deux-frontmatters |
| `Template - Manuel de BDD - Digital Twin.md`, `Template - Manuel de BDD - Mission Ops.md`, `Template-Fiche_outil_LBP.md`, `Template-prompt_lbp.md`, `Template de system prompt.md` | **Ajouter** un bloc explicite `<!-- @INSTR-START: FRONTMATTER_INSTANCE -->` avec un YAML modèle complet (sur le modèle des templates WR-RD) |
| `template-methode_lbp.md` | **Décider** : aligner les noms de champs avec le canon (`title/doc_type/status` au lieu de `titre/type/statut`) ou conserver l'écart documenté |
| `template-db-manual-mission_ops.md` | **Archiver** s'il est remplacé par `Template - Manuel de BDD - Mission Ops.md` |

---

## 5) Anomalies prioritaires (par ordre d'impact)

### Priorité HIGH

1. **`template-taxonomie.md` : pas de niveau (A)** — le frontmatter en tête est un (B). Le template-doc lui-même n'a pas de métadonnée propre. Impact : 1 template + ~96 taxonomies sans `doc_type/title/version` au niveau doc.
   - Fichier : `H:\Drive partagés\LBP - shared\Architecture data\00 - Docs méta\Templates d'instanciation\template-taxonomie.md`
2. **`Template méta de Brick.md` : pas de niveau (A)** — frontmatter avec placeholders `{{...}}`, `doc_type: "brick"` au lieu de `"template"`.
   - Fichier : `H:\Drive partagés\LBP - shared\Architecture data\00 - Docs méta\Templates d'instanciation\Template méta de Brick.md`
3. **DOUBLON `INDIC.TIME_ROLE.LBP.md`** : 2 versions divergentes du même fichier, et la version `Taxonomies/` a un frontmatter mal fermé (`---` doublé lignes 25-27).
   - Fichiers :
     - `H:\Drive partagés\LBP - shared\Architecture data\INDIC.TIME_ROLE.LBP.md` (racine vault, à dégager)
     - `H:\Drive partagés\LBP - shared\Architecture data\Taxonomies\INDIC.TIME_ROLE.LBP.md` (à corriger : retirer le second `---`)
4. **R-044 non appliqué côté Mission Ops** : 4 manuels + 4 WR-RD Mission Ops utilisent `date_creation: "2026-04-27"` (ISO) au lieu de `JJ-MM-YYYY`. **Asymétrie** avec WR-RD Twin (`created_at: "26-04-2026"`).
   - Fichiers : tous les `Manuel de BDD - *.md` et `WR-RD - *.md` sous `Manuels de BDD/Mission Ops/`
5. **Asymétrie nommage du champ date** : `created_at` (Twin WR-RD) vs `date_creation` (Mission Ops Manuels & WR-RD) — choisir un canon unique.

### Priorité MEDIUM

6. **`template_version: 6.1.0` obsolète** sur les 28 Manuels Twin (template actuel = 6.3.0).
7. **`template_version: 1.2.0` obsolète** sur les 28 WR-RD Twin (template actuel = 1.3.0).
8. **Absence de `code: DBMAN_xxx`** sur les 28 Manuels Twin (présent côté Mission Ops).
9. **Double frontmatter visuel** dans `template-prompt_maitre_lbp.md` et `template-meta_logic_block_lbp.md` — encapsuler le second YAML dans un bloc INSTR.
10. **`(B) absent`** dans 5 templates : Manuel Twin, Manuel Mission Ops, Fiche outil, Prompt LBP, System prompt — pas de gabarit YAML explicite pour l'instance.

### Priorité LOW

11. **Format `version` mixte sur les Notes de Concept** : `"07-04-2026 v0.5.0"` mélange date + semver dans un seul champ. À séparer (`version: "0.5.0"` + `created_at: "07-04-2026"`).
12. **Hétérogénéité commentaires `#` dans frontmatter taxonomies** : certaines les gardent, d'autres les ont enlevés.
13. **Méthodes : `type/titre/statut`** vs canon `doc_type/title/status` — divergence à arbitrer.
14. **Templates de Bricks : `type: template_brick`** au lieu de `doc_type: template` + pas de `tags`/`status` — divergence intra-vault.
15. **Coexistence `Template - Manuel de BDD - Mission Ops.md` (v5.1.0) vs `template-db-manual-mission_ops.md` (v0.3.0)** : doublon ou succession mal nettoyée.
16. **Playbook Macro-archi v2** : pas de `doc_type`.

---

## 6) Pointeurs précieux pour la phase 2

- Tous les chemins de fichiers ci-dessus sont absolus, copiables tels quels.
- Pour cibler vite tous les manuels Twin obsolètes en `template_version` : `Manuels de BDD/Digital Twin/Manuel de BDD - *.md` (28 fichiers).
- Pour cibler tous les WR-RD Twin : `Manuels de BDD/Digital Twin/WR-RD/WR-RD - *.md` (28 fichiers).
- Pour cibler les non-conformités R-044 : `Manuels de BDD/Mission Ops/**/*.md` (8 fichiers).
- Le fichier `INDIC.TIME_ROLE.LBP.md` à la **racine du vault** est le plus suspect — à examiner en priorité (probablement un fichier déposé hors taxos par erreur).
