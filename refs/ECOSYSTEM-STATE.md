# Etat courant de l'ecosysteme LBP

> Snapshot dynamique — mis à jour après chaque changement.
> Dernière mise à jour : 03-05-2026 — **Phase 1.0 du chantier d'architecture des docs méta close.** Livrables : (1) nouvelle taxo `META.FUNCTION` (5 fonctions systémiques : Orienter / Expliquer / Structurer / Normer / Opérer) créée dans `Taxonomies/`. (2) Ancienne taxo `META.FAMILY` archivée selon R-053 (suffixe `(archivé v1.0 le 03-05-2026)`) avec note d'archivage explicite. (3) Doc constitution `Constitution des docs méta - LBP.md` v0.1 créé (code `META_DOC_MAP_LBP`, 8 sections + 3 annexes incluant arborescence cible et trajectoire workflows → agents). (4) 3 nouvelles règles dans `RULES_LBP` (section 5.8 « Architecture des docs méta du Brain LBP ») : R-064 (naming filename humain + code `META_*` + scope), R-065 (définition opérationnelle « gouverne plusieurs objets »), R-066 (propriétaire canonique unique). (5) 3 nouvelles décisions dans `DECISIONS_LBP` : D-024 (préfixe `META_` remplace `CHRT_`), D-025 (5 fonctions systémiques `META.FUNCTION` remplacent `META.FAMILY`), D-026 (BDD `Templates méta Brain` séparée + `Templates de Bricks` reste séparée par scope agent kontext). RULES_LBP bumpée 1.1→1.2, DECISIONS_LBP bumpée 1.0→1.1, miroirs `refs/` rafraîchis. **Sync Notion DIFFÉRÉE** (Phase 2-3) : statut `META.FAMILY` → archivé sur Notion + indexer `META.FUNCTION` dans Registre des taxonomies + créer fiche `Constitution des docs méta - LBP` dans BDD `Docs méta LBP` + ajouter propriété `Fonction systémique` sur BDD `Docs méta LBP`. **Avant Phase 1.0** : Phase B (test Twin DeepSecAI v0) close + investigation MCP Obsidian Q1-Q4 close avec 7 règles capturées (C-020 à C-026).

> _Précédent_ : 30-04-2026 — **Phase B (test Twin DeepSecAI v0) close.** 51 fiches sur 17 BDDs Twin/MO mobilisées sur la page test `352e1a18653c8079b1b6edd1c456aaeb`. Vague 9 Mission Ops complète (2 Meetings + 2 Actions LBP + 2 Bricks). Vague 10 vérifs transverses : ✓ bidir auto-propagation Notion (Meeting↔Action, Action↔Brick, Source↔Brick), ✓ chaînes D-009 indicateurs (5 relations + correctif `mesure (problématiques)` post-audit). Playbook stabilisé : `refs/TEST_TWIN_PLAYBOOK.md`. Captures session : C-017 (lecture WR-RD obligatoire avant remplissage) + C-018 (vérifier régime BDD avant signaler anomalie). Reste post-test : (a) cogitation propriété 'Régime de l'entité', (b) Phase C audit final + figement Brain, (c) Phases D/E chantiers M et P.

## Phase actuelle

**Phase A4 close + Phase B en cours (test Twin DeepSecAI v0, ~75% close).** Cumul A1+A2+A3+A4 : **447 actions Notion**. **Phase B Vagues 1-7 close** sur la nouvelle page : 41 entités Twin/MO (3 Sources + 1 Org + 4 Coll + 7 Ind + 2 Postes + 2 Env + 2 Actifs + 2 Évén + 2 Glossaire + 2 JdS + 2 AD + 2 Enjeux + 2 Process candidats sandbox + 2 Process officiels + 2 Pratiques + 2 Principes + 2 Capacités métier candidates sandbox). Captures règles : C-017 (lecture WR-RD obligatoire), C-018 (vérifier régime BDD avant signaler une anomalie de relation absente). Reste : Vague 8 (6 fiches Pilotage) + Vague 9 (6 fiches Mission Ops final) + Vague 10 (vérifs) + post-test : créer `refs/TEST_TWIN_PLAYBOOK.md` + cogitation propriété 'Régime de l'entité'. **Phase A4.B** (relations Manuels ↔ Taxonomies) : 43 manuels mis à jour avec `utilise (taxonomies)` peuplé depuis le parsing de leur section « Usages des taxonomies ». 87+ codes uniques référencés transverse, 100% mappables. **Phase A4.A** (Taxonomies) : 102 taxos Markdown synchronisées avec BDD `Registre des taxonomies` Notion. 96 updates (codes `<X>.<Y>.LBP` migrés vers `<X>.<Y>` per R-054, props complètes : Aliases, Descriptions, Lien Drive, Nature sémantique, Mode de sélection, Ouverture, Statut Validé, Version 2.0) + 6 creates (BRAIN.LAYER, BRAIN.SUBTYPE, DBMAN.SCOPE, DOC.TYPE, JOB.COVERAGE, LGBLK.FAMILY). Architecture Glossaire / Registre stabilisée : Glossaire = identité + sémantique du concept (Code, Aliases, Mots clés, Type, Définition, Valeur ajoutée, Règles d'usage, Usages IA, Équivalent langage courant) ; Registre = méta du fichier source (Code `CPT_*`, Version du template, Statut, Lien Drive). Captures règles : C-013, C-014, C-015 + amendement R-054 (paire `CPT/GLO`). Outils : `scripts/lib/notion_keys.py`, `scripts/phase_a3/build_drive_url_resolver.py`, `scripts/phase_a3/a3bis_plan.py`, `scripts/phase_a3/a3_6_migration.py`. Prochaine étape : **Phase A4** (Taxonomies, 102 taxos) + relations utilise (taxonomies) cross-BDDs.

### Phases terminées (chronologie)

| Phase | Volume | Notes |
|---|---|---|
| Mini-phase 1f-g | 2 taxos (`BRAIN.SUBTYPE`, `BRAIN.LAYER`) + `Template - Manuel de BDD - Brain.md` v1.1 | Pattern v1.1 inauguré |
| Phase 4 | 43 manuels de BDD migrés au canon | Frontmatter R-054 / R-055 / R-056 |
| Phase 5 | 32 WR-RD migrés au canon | idem |
| Phase 6 | 72 notes de concept migrées au canon | Split anti-pattern `version: "DATE vX.Y.Z"` → `version` + `created_at` |
| Phase 6.5 | Refonte de 4 templates secondaires en v2.0 + MAJ 5 manuels Brain | Voir détail ci-dessous |
| Audit transverse Notion ↔ Manuels Brain | Rapport `scripts/notion_brain_audit/audit_notion_brain.md` | A déclenché la sync DDL |
| Sync DDL Notion BDDs Brain | ~26 actions sur les 11 BDDs Brain | Voir détail ci-dessous |
| Phase 7 | 24 instances migrées au canon (20 Templates de Bricks + 3 Méthodes + 1 Doc méta playbook) | Codes `TPL_BRICK_*`, `METH_*`, `CHRT_*` (conformes R-054 ; à vérifier dans le vault si certains fichiers utilisent encore les préfixes ad hoc `TPL_BRK_/MET_`) |
| Création `Template - WR-RD - Brain.md` v1.0 | 1 template `TPL_WRRD_BR` | Aligné sur templates Twin et Mission Ops, adapté aux spécificités Brain (pas de couche 5D, pas de jumelles texte R-058) |
| Génération des 11 WR-RD Brain | 11 fichiers `WR-RD - X.md` dans `Manuels de BDD/Brain/WR-RD/` | Extraction stricte depuis manuels parents (R-041/R-042). Section couche calculée supprimée partout (rollups Brain tous relationnels). |
| Audit transverse taxonomies | 87/87 référencées présentes ; 1 manquante détectée (`JOB.COVERAGE`) ; 14 orphelines à arbitrer plus tard | Rapport via agent + grep cross-manuels |
| Création `JOB.COVERAGE` | 1 taxo (BDD Postes Twin) — 6 valeurs (Couvert / Partiellement couvert / Vacant / Sur-couvert (doublon) / En transition / Gelé) | Au canon R-054 + ALTER Notion `État de couverture du poste` SET SELECT |
| 11 `Lien WR-RD` posés sur Notion | 11 fiches BDD `Manuels de BDD` mises à jour avec URL Drive du WR-RD Brain correspondant | Via WF-011 (lecture SQLite Drive locale) + notion-update-page |
| Capture **D-020** + Lot 1 DDL | ADD `Version du template` (RICH_TEXT) sur 10 BDDs Brain + ALTER Manuels de BDD (select→text) + RENAME `Lien vers le doc du manuel` → `Lien vers le manuel de BDD (.md)` + RENAME apostrophe Logic blocks (typo U+2019) | 14 actions DDL Notion réussies |
| Lot 2 (manuels + WR-RD) | Documentation `Version du template` ajoutée à 10 manuels Brain + propagée à 11 WR-RD Brain. 3 props Méthodes (`Erreurs fréquentes / anti-patterns`, `Quand l'utiliser`, `Variantes & adaptations`) documentées dans Manuel + WR-RD Méthodes. | 22 fichiers Markdown enrichis |
| Lot 3 (audit-correction Lien manuel) | 21 entrées Notion `Manuels de BDD` désynchronisées corrigées (URL Drive posée, 7 renames de Nom canonique) + 7 archivages V1 orphelins (Insights, Impacts de Modulateurs, Rôles officiels, Ressources, Unités Organisationnelles, Appartenances, Edges) | Script réutilisable `scripts/get_manuels_urls.py` |

#### Détail Phase 6.5 (refonte templates secondaires)

- `template-db-manual-mission_ops.md` v0.3 → archivé (doublon)
- `template-methode_lbp.md` → `Template - Méthode LBP.md` v2.0 (canon, pattern v1.1)
- `Template-Fiche_outil_LBP.md` → `Template - Outil externe.md` v2.0
- `Template méta de Brick.md` → `Template - Template de Brick.md` v2.0 (méta-template mince)
- MAJ des 5 manuels Brain : Glossaire LBP, Manuels de BDD, Méthodes LBP, Agents LBP, Prompts LBP (suite à audit transverse)

#### Détail sync DDL Notion Brain (~26 actions)

- DROP `actif` (Prompts LBP)
- ADD `Domaine(s) d'usage` multi-select (4 BDDs Motor : Méthodes, Templates, Agents, Outils)
- ADD `System prompt (lien source)` URL (Agents LBP)
- DROP `Type fonctionnel (BDD décrite)` (Manuels de BDD) — application D-019
- DROP 2 jumelles texte (Logic blocks) — application R-058
- DROP `Entrées attendues` (ancien champ, Méthodes) ; DROP `actif` (Prompts)
- ALTER options `Statut de déploiement` (5 valeurs PROMPT.DEPLOY_STATUS), `Environnement(s) de déploiement` (5 valeurs PLATFORM.ENV), harmonisation casse `Domaine(s) d'usage` (Prompts)
- RENAME apostrophes ASCII → typographiques (Logic blocks `Statut de l’objet`) — R-052
- RENAME accents (Outils : `Valeur ajoutée`, `Entrées attendues`)
- CONVERT 8 propriétés `text` → `rollup` (Méthodes 2, Templates 2, Agents 4)
- CREATE 3 rollups manquants (Outils externes : Agents/Méthodes/Templates mobilisés via prompts)

#### Out of scope Phase 7 (différé)

- **Logic Blocks (101)** + **Prompts (76)** : obsolètes vs Twin v2, refonte/regen ultérieure → **Phase 7 bis**.

### Règles et décisions captées dans cette série

- **R-053** — convention de renaming des docs archivés (suffix `(archivé v<X> le JJ-MM-YYYY)`)
- **R-054** — codification universelle des objets Brain (table de préfixes officielle : `CPT_`, `GLO_`, `METH_`, `TPL_BRICK_`, `CHRT_`, `DBMAN_TW/MO/BR_`, `WRRD_TW/MO/BR_`, `LGBLK_`, `PRMPT_M/S/U/T_`, `OUT_`, `AGT_`, etc. — cf. `CODIFICATION_LBP.md`)
- **R-055** — frontmatter canon Brain en 3 zones balisées (Identité / Méta-gouvernance / Spec d’usage)
- **R-056** — versioning `X.Y` (sans PATCH)
- **R-057** — discipline d’usage des backticks Markdown
- **R-058** — interdiction des jumelles texte sur les BDDs Brain
- **R-059** — hygiène d’écriture des docs Brain (pas de bruit historique ni de spéculation future)
- **D-019** — Brain = environnement documentaire en évolution ; Core+Motor unifié au niveau modèle de données ; isolation stricte Brain ↔ MO/Twin
- **C-011** (CLAUDE.md) — mise à jour systématique de `ECOSYSTEM-STATE.md` à chaque fin de phase, avant le commit de la phase
- **D-020** (DECISIONS_LBP.md) — propagation de la propriété `Version du template` (RICH_TEXT, type texte libre format X.Y) à toutes les BDDs Brain ; permet l'audit mécanique des docs stale lors de bumps majeurs de templates
- **D-021** (DECISIONS_LBP.md) — Architecture des 3 agents LBP : Brain architect (évolution du Brain) / Twin architect (modélisation Twin client) / KONTEXT (Mission Ops, agent central consultant). Frontière d'isolation infranchissable : KONTEXT ⊥ Brain architect (le Brain est utilisé pendant les missions mais n'évolue pas). 3 fiches `Agents LBP` à créer post-Chantier P.

**Backlog enrichi** (28-04-2026) :
- **Chantier P** — Tri massif `Prompts/` + `Logic Blocks/` + création des 3 fiches `Agents LBP` (Brain architect, Twin architect, KONTEXT) ; mise à jour des system prompts/prompts maîtres/logic blocks pour cohérence Twin v2 + D-019 + D-021. À traiter avant indexation Notion de ces 3 BDDs.
- **Chantier M** — Réactualisation PLAYBOOK macro-archi v2 + tri des entrées Notion `Docs méta LBP` sans Markdown actif. **Réflexion bundle** : produire un bundle de docs méta dédiés à chaque ensemble de doctrines/règles/chartes avec périmètre bien défini par doc (maintenable, améliorable, durable).
- **Convention** : "Statut de l'objet vide = à créer" (induction Méthodes LBP, à confirmer transverse).
- **Patterns techniques DDL Notion** : multi-select string JSON-encoded, types `CREATED_TIME`/`LAST_EDITED_TIME` (DDL fonctionnels mais non documentés), statements séquentiels en API séparés.
- **Propriété "Maître"** — figement d'une entité avérée Twin pour gouvernance dédoublonnage : entité maître = entité d'accueil en cas de fusion (les autres sont archivées dedans). À cogiter pendant Phase B.

---

## Plan global — vue d'ensemble (28-04-2026, ré-ordonné)

### Phase 0 (préalable) — Remplissage `summary` / `purpose` AVANT indexation

**Doctrine Leonard 28-04-2026** : remplir les `summary` / `purpose` des docs au canon **avant** d'indexer Notion (sinon on indexe des champs vides). Sous-étapes en miroir des BDDs à indexer ensuite :

0a. **Taxonomies** (96-102 docs) — `purpose` à écrire pour chaque taxo (les `summary` sont déjà partiellement présents)
0b. **Manuels de BDD** (43 docs) — `summary` à écrire (pour compléter avant Phase A1)
0c. **WR-RD** (32 docs Twin + 4 MO + 11 Brain = 47 docs) — `summary` à écrire si vide
0d. **Notes de concept** (72 docs) — `purpose` à écrire si vide
0e. **Templates de bricks** (20 docs) — `summary` à écrire si vide

→ **Markdown-only**, aucun coût Notion. Peut être fait pendant les pauses Notion.

### Phase A — Indexation Brain restante (4 BDDs, ~270 entrées)

A1. **Manuels de BDD** (43 entrées) — partiellement fait au Lot 3, reste les autres propriétés à dériver des manuels (préalable 0b)
A2. **Templates de bricks** (20 entrées) (préalable 0e)
A3. **Glossaire LBP + Registre des notes de concept** (72 + 72, double indexation cohérente) (préalable 0d)
A4. **Registre des taxonomies** (102 entrées) (préalable 0a)

→ **Out of scope court terme** : Prompts LBP (Chantier P), Registre des logic blocks (Chantier P), Agents LBP (Chantier P + D-021), Docs méta LBP (Chantier M).

### Phase B — Tests fonctionnels Twin + Mission Ops

B1. Création **fausses entités test** sur les 28 BDDs Twin
B2. Création **fausses entités test** sur les 4 BDDs Mission Ops
B3. **Validation combo Twin + Mission Ops** : instanciation actions de mission, fixation RDV, génération bricks, mise à jour Twin
B4. **Réflexion ordonnancement de remplissage** : intra-BDD (dans quel ordre remplir les propriétés d'une fiche ?) + inter-BDD (qu'est-ce qu'on remplit d'abord quand on extrait des infos d'un document ?)
B5. **Cogitation propriété "Maître"** (cf. backlog) : si elle se révèle utile pendant les tests, formaliser en R-XXX ou D-XXX

### Phase C — Audit final symétrie + figement Brain

C1. Audit ultime symétrie manuels Brain ↔ BDDs Notion (dernier passage)
C2. Correction des écarts résiduels éventuels
C3. **Figement / freeze** du Brain (état stable de référence)

### Phase D — Chantier M (Docs méta — bundle réfléchi)

D1. Réflexion bundle docs méta : recensement des ensembles thématiques (architecture macro, codification, cycle de vie docs, doctrine isolation agents, gouvernance, etc.) + définition du périmètre de chaque doc
D2. Production du **bundle de docs méta** (un doc par périmètre, au canon, articulés sans recouvrement)
D3. Tri des entrées Notion `Docs méta LBP` (refondre ou archiver)
D4. Indexation Notion BDD Docs méta LBP

### Phase E — Chantier P (Prompts / Logic Blocks / Agents)

E1. Tri massif des dossiers `Prompts/` et `Logic Blocks/` (séparer ancien du code app vs docs de travail)
E2. Mise à jour des system prompts / prompts maîtres / logic blocks (cohérence Twin v2 + D-019 + D-021)
E3. Création des 3 fiches Agents LBP (Brain architect, Twin architect, KONTEXT) au canon
E4. Indexation Notion BDDs Prompts + Logic Blocks + Agents

### Phase F — Hors-scope ponctuel (à programmer)

F1. Remplissage `summary` / `purpose` TODO (~275 docs : 43 manuels + 64 WR-RD + 72 notes + 96 taxos)
F2. Audit nettoyage backticks abusifs (R-057)
F3. Phase 7 bis : refonte structurelle des 101 logic blocks + 76 prompts (post-Chantier P)

## Etat du Brain (11 BDD) — post-sync DDL

| BDD | Score audit | Manuel à jour ? | Notion à jour ? |
|---|---|---|---|
| Docs méta LBP | Conforme | OK | OK (au canon) |
| Glossaire LBP | Conforme (post-MAJ) | MAJ 28-04-2026 (`Notes` documenté + dates auto) | OK |
| Registre des notes de concept | Conforme | OK | OK |
| Registre des taxonomies | Conforme | OK | OK |
| Manuels de BDD | Conforme (Type fonctionnel retiré) | MAJ 28-04-2026 | DROP Type fonctionnel appliqué |
| Prompts LBP | Conforme (post-sync) | OK | DROP `actif`, taxos alimentées, casse harmonisée |
| Logic blocks | Conforme (post-sync) | OK | DROP 2 jumelles texte, apostrophe alignée |
| Méthodes LBP | Conforme (post-sync) | MAJ 28-04-2026 (Entrées MUST/SHOULD/NICE) | DROP ancien Entrées + 2 rollups corrects |
| Templates de bricks | Conforme (post-sync) | OK | + Domaine(s) d’usage, 2 rollups corrects |
| Agents LBP | Conforme (post-sync) | MAJ 28-04-2026 (relation §7 corrigée) | + Domaine(s) d’usage + System prompt + 4 rollups |
| Outils externes | Conforme (post-sync) | OK | + Domaine(s) d’usage + 3 rollups + accents corrigés |

## A faire (prochaines étapes)

**Court terme — chantier Brain au canon Notion** :

1. **Indexation des Markdown au canon dans les BDDs Notion Brain** — **mise à jour des entrées existantes** plutôt qu’archivage+recréation (préservation des relations Notion existantes).
2. **Renseigner les `Lien vers le doc WR-RD (.md)`** dans la BDD Manuels de BDD pour les 11 manuels Brain (chaque manuel pointera vers son WR-RD).

**Moyen terme** :

5. **Remplissage `summary` / `purpose`** sur ~275 docs où ces champs sont en TODO (par moi avec vision globale).
6. **Audit nettoyage backticks abusifs** (R-057).

**Out of scope court terme (différé)** :

- **Phase 7 bis** : refonte/regen des Logic Blocks + Prompts (obsolètes vs Twin v2).
- **Phases 9-12** : taxos manquantes (JOB.COVERAGE, etc.), audit cross-éco, audit final, indexation Brain Notion étendue.

## Notes diverses

- **R-052** : apostrophes typographiques `’` (U+2019) appliquées partout (vault + Notion).
- **R-044** : dates au format `JJ-MM-YYYY` partout dans les sections vivantes.
- **D-019** : la distinction Core/Motor est conservée comme étiquette de discours et matérialisée dans la propriété `Domaine(s) d’usage` (5 BDDs Motor), mais elle n’est plus une partition stricte du modèle de données.
- **R-058** : les jumelles texte sont **interdites sur Brain**, autorisées Twin, expérimentales Mission Ops.
