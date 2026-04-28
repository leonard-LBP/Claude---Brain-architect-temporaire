# Etat courant de l'ecosysteme LBP

> Snapshot dynamique — mis à jour après chaque changement.
> Dernière mise à jour : 28-04-2026 — fin de session après Phase 7 (24 instances migrées au canon Brain) + sync DDL Notion Brain (~26 actions sur les 11 BDDs) + captures R-053→R-059 et D-019.

## Phase actuelle

**Migration au canon Brain — Phases 4 à 7 terminées. Sync DDL Notion Brain terminée. Prochaine étape : Template WR-RD Brain → 11 WR-RD Brain → indexation Markdown au canon dans Notion Brain.**

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
| Phase 7 | 24 instances migrées au canon (20 Templates de Bricks + 3 Méthodes + 1 Doc méta playbook) | Codes `TPL_BRK_*`, `MET_*`, `CHRT_*` |

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
- **R-054** — codification universelle des objets Brain (table de préfixes `BRK_`, `MET_`, `TPL_BRK_`, `CHRT_`, `DBMAN_`, `WRRD_`, `LGBLK_`, `PROMPT_`, `OUT_`, `AGENT_`, etc.)
- **R-055** — frontmatter canon Brain en 3 zones balisées (Identité / Méta-gouvernance / Spec d’usage)
- **R-056** — versioning `X.Y` (sans PATCH)
- **R-057** — discipline d’usage des backticks Markdown
- **R-058** — interdiction des jumelles texte sur les BDDs Brain
- **R-059** — hygiène d’écriture des docs Brain (pas de bruit historique ni de spéculation future)
- **D-019** — Brain = environnement documentaire en évolution ; Core+Motor unifié au niveau modèle de données ; isolation stricte Brain ↔ MO/Twin

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

1. **Re-audit BDDs Notion Brain** (vérification post-sync) — confirmer que les ~26 actions DDL ont bien produit l’état attendu.
2. **Création `Template - WR-RD - Brain.md`** — aligner sur les 2 templates WR-RD existants (`Digital Twin`, `Mission Ops`).
3. **Génération des 11 WR-RD Brain** — un par BDD du Brain.
4. **Indexation des Markdown au canon dans les BDDs Notion Brain** — **mise à jour des entrées existantes** plutôt qu’archivage+recréation (préservation des relations Notion existantes).

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
