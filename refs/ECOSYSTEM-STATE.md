# Etat courant de l'ecosysteme LBP

> Snapshot dynamique — mis à jour après chaque changement.
> Dernière mise à jour : 28-04-2026 — calibration indexation Brain réussie sur BDD Méthodes LBP + correctif transverse `Created Date`/`Last Updated Date` (5 BDDs Motor Brain : Méthodes, Prompts, Agents, Outils externes, Docs méta) : conversion type `date` → `created_time` / `last_edited_time` (auto-remplis). Patterns Notion DDL validés : multi-select (string JSON-encoded), CREATED_TIME / LAST_EDITED_TIME comme types DDL.

## Phase actuelle

**Calibration indexation Brain validée sur Méthodes LBP. Prochaine étape : indexation des autres BDDs Brain (Manuels de BDD, Templates de bricks, Glossaire LBP + Notes de concept en double indexation, Registre des taxonomies). Out of scope court terme : Prompts LBP, Logic blocks, Agents LBP (chantier P : tri massif à venir) ; Docs méta LBP (chantier M : réactualisation PLAYBOOK).**

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
- **R-054** — codification universelle des objets Brain (table de préfixes `BRK_`, `MET_`, `TPL_BRK_`, `CHRT_`, `DBMAN_`, `WRRD_`, `LGBLK_`, `PROMPT_`, `OUT_`, `AGENT_`, etc.)
- **R-055** — frontmatter canon Brain en 3 zones balisées (Identité / Méta-gouvernance / Spec d’usage)
- **R-056** — versioning `X.Y` (sans PATCH)
- **R-057** — discipline d’usage des backticks Markdown
- **R-058** — interdiction des jumelles texte sur les BDDs Brain
- **R-059** — hygiène d’écriture des docs Brain (pas de bruit historique ni de spéculation future)
- **D-019** — Brain = environnement documentaire en évolution ; Core+Motor unifié au niveau modèle de données ; isolation stricte Brain ↔ MO/Twin
- **C-011** (CLAUDE.md) — mise à jour systématique de `ECOSYSTEM-STATE.md` à chaque fin de phase, avant le commit de la phase
- **D-020** (DECISIONS.md) — propagation de la propriété `Version du template` (RICH_TEXT, type texte libre format X.Y) à toutes les BDDs Brain ; permet l'audit mécanique des docs stale lors de bumps majeurs de templates

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
