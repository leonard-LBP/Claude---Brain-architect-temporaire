# Etat courant de l'ecosysteme LBP

> Snapshot dynamique — mis a jour apres chaque changement.
> Derniere mise a jour : 28-04-2026 — Phase 6.5 Mission Ops **TERMINÉE** : 4 BDDs Mission Ops sur Notion (Sources d'informations, Meetings, Actions LBP, Bricks), 6 paires bidir DUAL + 2 self-rel + 2 monodir vers Twin, 12 SELECT instanciés depuis taxos, R-047 v2.2 appliqué, audit final 0 dette résiduelle. Captures : R-052 (apostrophe typographique U+2019). Backlog : doctrine Indices réservés aux objets pas containers + pattern self-rel DDL (1 ADD suffit). Pass 4 Actions LBP (rollups + formula 4.5) volontairement différée.

## À faire demain (29-04-2026)

**Chantier indexation Brain — gros dossier "tout doit être super clean"** :
1. **Plan d'indexation à présenter** dès l'arrivée demain : comment indexer dans le Brain les nouveaux docs Twin v2 + Mission Ops (manuels, WR-RD, taxos, notes de concept) avec **archivage propre** des anciens docs côté Architecture data **et** côté BDDs Brain (pas juste vault).
2. **Investigation Template Taxonomies** : possible asymétrie — son frontmatter ressemblerait plutôt à un "exemple de frontmatter attendu dans les taxos générées" qu'au frontmatter du template lui-même. À comparer avec les autres templates (Manuel de BDD Twin, Manuel de BDD Mission Ops, WR-RD Twin, WR-RD Mission Ops).
3. **Question harmonisation frontmatter docs méta (Brain)** : ouverte — vu la variété des docs qui cohabitent dans la BDD Docs méta (chartes, playbooks, templates, etc.), l'harmonisation peut ne pas être une bonne idée. À arbitrer.
4. **Taxonomies manquantes** : il en manque possiblement 1 ou 2 qu'on avait dit "on fera plus tard". À vérifier vs backlog (cf. entrée `Statut relationnel` notamment, et autres taxos pressenties).
5. **Convention de renaming des docs archivés** (idée Leonard 28-04-2026) : aujourd'hui le statut actif/archivé d'un doc dépend uniquement de son dossier (`00 - archives/`). Risque : agent qui cherche un doc par nom peut tomber sur la version archivée et la confondre avec l'active (collision de noms entre actif et archivé fréquente). À arbitrer : convention de suffix dans le filename, ex. `Manuel de BDD - Actifs (archivé 28-04-2026).md` ou `Manuel de BDD - Actifs.archive-28-04-2026.md`. Décision a impact sur ~150+ fichiers déjà archivés (à renommer rétroactivement) + R-043 (cohérence filename ↔ title — donc title du frontmatter à aligner aussi). Probablement candidate **règle R-XXX** si validée.

## Phase actuelle

**Phase 5 de la migration Twin v2 — Indexation Notion en cours.**

Phases 1-4 terminees :
- Arborescence Architecture data refondue (D-010)
- Anciens docs v1 archives (20 manuels Twin + 69 notes concept + 68 taxonomies)
- Nouveaux docs v2 migres (22 manuels + 6 sandboxes + 72 notes concept + 96 taxonomies + 1 template)
- Sync Drive validee, URLs accessibles via WF-011

Phase 5 en cours : indexation Notion par mini-batchs avec dry-run par doc.

**Mini-batch 0 (calibration) terminé** :
- 4 creations : Manuel Actifs, Taxo ASSET.SUBTYPE, Registre concept Actif, Glossaire Actif
- 3 relations : Manuel → Taxo, Glossaire → Registre, Glossaire → Manuel
- 4 archivages v1 : Manuel Ressources, Taxo Type/sous-type ressource, Glossaire Ressource, Note concept Ressource
- Ajout option `Digital Twin - socle structurel` dans taxo Notion Type fonctionnel

## Etat du Brain (11 BDD)

| BDD | Etat | Commentaire |
|-----|------|-------------|
| Glossaire LBP | Actif Ressource → Archive ; +1 entree v2 (Actif) | +1 a chaque batch |
| Registre notes de concept | +1 entree v2 (Actif), +1 archive (Ressource) | +1 a chaque batch |
| Registre taxonomies | +1 entree v2 (ASSET.SUBTYPE), +1 archive | +1 a chaque batch |
| Manuels de BDD | +1 entree v2 (Actifs), +1 archive (Ressources), +1 option `socle structurel` | +1 a chaque batch |
| Docs meta LBP | Inchange | Pas de mise a jour prevue |
| Prompts LBP | Inchange (obsoletes vs Twin v2) | Phase 7 a venir |
| Logic blocks | Inchange (obsoletes vs Twin v2) | Phase 7 a venir |
| Methodes LBP | Inchange | A verifier |
| Templates de Bricks | Inchange | A verifier |
| Agents LBP | Inchange | A verifier |
| Outils externes | Inchange | A verifier |

## Etat de la migration Twin v2

### Docs migres dans le vault (phases 2-3) - 24-04-2026

| Dossier | Etat | Archives |
|---------|------|----------|
| Manuels de BDD/Digital Twin/ | 22 manuels + 6 sandboxes | 20 archives v1 |
| Notes de Concept/ | 72 notes | 69 archives v1 |
| Taxonomies/ | 96 taxos | 68 archives v1 |
| 00 - Docs meta/Templates d'instanciation/ | 11 + 1 nouveau | 2 archives |

### Indexation Notion (Phase 5) — progression

> Ordre ajuste suite a R-035 (ordonnancement inter-types) : Taxonomies (A) avant Manuels (B) avant Notes concept + Glossaire (C).

| Batch | Statut | Volume | Commit |
|---|---|---|---|
| **Mini-batch 0 (calibration : Actif)** | ✅ Terminé | 4 creations + 4 archives + 3 relations | fdaaabd |
| **A1 Taxonomies socle structurel** (ORG, COL, ASSET sauf SUBTYPE, JOB, ENV, EVT, ORG_REL, STAKEHOLDER) | ✅ Terminé + enrichissement descriptions | 29 creations + 17 archives + 29 MAJ enrichies | 9327200 + 2984dc6 |
| **A2 Taxonomies extraction + pivots** (ACT, SIG, ENJ, CAP, INIT, IMPACT, EMO, IND) | ✅ Terminé | 17 creations (R-037) + 14 archives | en cours |
| **Correction R-036 doublons A1+A2** | ✅ Terminé | 25 MAJ v1 (ressuscitation enrichie) + 25 v2 [DOUBLON] supprimées par Leonard | (à commit) |
| **A3 Taxonomies couche analytique** (INDIC, INS, ORG5D, PRA, PROC, SCALE) | ✅ Terminé | 23 MAJ enrichies + 2 créations (INDIC.TIMEROLE, SCALE.COVERAGE) + R-038 | (à commit) |
| **A4 Taxonomies Brain/transverse** (AGENT, BRICK, GLO, MET, META, MTG, OBJ, OPS, OUT, PLATFORM, PROMPT, SKILL, SRC) | ✅ Terminé | 24 MAJ enrichies + 1 création (MTG.EXEC_STATUS) + housekeeping ACT (1 MAJ ACT.CONSOLIDATION_TARGET + 1 archive ACT.CANDIDATE_TYPE) | (à commit) |
| **B1 Manuels socle structurel** | ✅ Terminé | 8 manuels (3 MAJ + 5 créations dont Actifs avec dette 7 relations comblée) | (à commit) |
| **B2 Manuels extraction factuelle** | ✅ Terminé | 2 MAJ (Actions détectées, Enjeux) | (à commit) |
| **B3 Manuels sémantique/mouvement/pivot/observation** | ✅ Terminé | 4 (2 MAJ Glossaire + Journal des signaux ; 2 créations Initiatives orga + Processus candidats) | (à commit) |
| **B4 Manuels couche analytique officielle** | ✅ Terminé | 8 (7 MAJ + 1 création Processus, migration "post-traitement" → "analytique officiel") | (à commit) |
| **B5 Manuels sandboxes** | ✅ Terminé | 6 créations (Type fonctionnel = "Digital Twin - sandbox") | (à commit) |
| **+ D-013 + modifs template + schéma Notion** | ✅ Terminé | template_version "v6.1.0" : ajout propriété Notion + ajout aux 28 frontmatters vault + 3 modifs template + maj manuel "Manuels de BDD" + 4 nouveaux types fonctionnels Notion + housekeeping (5 entrées) | (à commit) |
| **C Notes de concept + Glossaire** | ✅ Terminé | 152 actions Notion : 135 MAJ (67 cas A × 2 + 1 relation Template de brick) + 10 créations (5 cas D × 2) + 5 relations cas D + 2 archivages UO + 2 renommages (Référentiel 3P → 3P, Process → Processus) | (à commit) |

## Anomalies a traiter

| # | Anomalie | Severite | Statut |
|---|----------|----------|--------|
| 1 | Glossaire : "est lie a (concepts)" en texte | Moyenne | Non traite |
| 2 | 3 relations Glossaire sans miroir | Faible | Non traite |
| 3 | Logic blocks : lien Drive en text | Faible | Non traite |
| 4 | Instructions ecriture / clefs lecture non indexees (Brain) | Moyenne | Non traite (Phase 6) |
| 5 | 6 BDD "XXX" a migrer | Moyenne | Non traite |
| 6 | ~50% Glossaire en Brouillon | Haute | En cours (refonte en masse via Phase 5) |
| 7 | Prompts maitres et logic blocks pointent vers ancienne archi Twin | Haute | Non traite (Phase 7) |
| 8 | Taxo `Type fonctionnel (BDD decrite)` sous-dimensionnee (socle structurel manquait) | Resolue | Option ajoutee 2026-04-24 |

## Modifications effectuees

| Date | Action | Commit |
|------|--------|--------|
| 2026-04-07 | Initialisation repo git + README | 970ccf4 |
| 2026-04-07 | Mise en place fondations de travail | a1ae7c1 |
| 2026-04-24 | Integration architecture Twin v2 (Panorama) dans refs/ | a411afa |
| 2026-04-24 | Phase 1 Twin v2 — refonte arborescence vault + D-012 | d8d9a3d |
| 2026-04-24 | Capture R-029 a R-034 (regles indexation Notion) | d7e21fa |
| 2026-04-24 | Phase 5 mini-batch 0 Actif | fdaaabd |
| 2026-04-24 | Capture R-035 (ordre d'indexation inter-types) + reseq | d7e21fa |
| 2026-04-24 | Batch A1 Taxonomies socle structurel (29 creations + 17 archives) + R-036 | (en cours) |
| 2026-04-25 | Batch A2 Taxonomies extraction + pivots (17 creations enrichies + 14 archives) + R-037 | (à commit) |
| 2026-04-25 | Correction R-036 doublons A1+A2 (25 MAJ v1 + 25 archives v2 [DOUBLON]) | (à commit) |
| 2026-04-25 | Capture R-038 (identifiant pivot par type d'objet : taxos = code, autres = nom) | (à commit) |
| 2026-04-25 | Batch A3 Taxonomies couche analytique (23 MAJ enrichies + 2 créations) | (à commit) |
| 2026-04-25 | Batch A4 Taxonomies Brain/transverse (24 MAJ enrichies + 1 création + housekeeping ACT.CANDIDATE_TYPE → ACT.CONSOLIDATION_TARGET) | (à commit) |
| 2026-04-25 | Capture D-013 (traçabilité de version de template d'instanciation) + modifs template Manuel de BDD + manuel "Manuels de BDD" | (à commit) |
| 2026-04-25 | Batch B Manuels Twin v2 (B1-B5 : 13 MAJ + 15 créations = 28 manuels) + 28 frontmatters vault avec template_version + housekeeping (5 entrées Notion) + 4 nouveaux types fonctionnels Notion | (à commit) |
| 2026-04-25 | Batch C Notes de concept + Glossaire (double indexation) : 152 actions Notion = 135 MAJ + 10 créations + 5 relations + 2 archivages + 2 renommages | (à commit) |
| 2026-04-25 | Capture R-039 (QA anti-artefacts IA dans tous les docs LBP) | (à commit) |
| 2026-04-26 | Audit terminologique vault hors Twin : suppression "UO" / "unités organisationnelles" + "Ressources" (sens objet) dans Manuels Brain/Mission Ops, Méthodes, Templates de Bricks. 13 fichiers vault modifiés (dont renommage Template Brick UO→Collectifs : PRF-UO-IND → PRF-COL-IND). | (à commit) |
| 2026-04-26 | Restructuration WR-RD (D-014) : 41 docs Clefs de lecture migrés (39 archivés Twin + 2 actifs Mission Ops Sources d'informations) ; sous-dossiers `WR-RD/` créés dans Brain/Digital Twin/Mission Ops ; dossier racine `Clefs de lectures/` supprimé. | (à commit) |
| 2026-04-26 | Convention nommage (D-015) : 12 dossiers `archives/` du vault renommés en `00 - archives/` pour visibilité (tri alpha en tête). | (à commit) |
| 2026-04-26 | D-016 + Template WR-RD v1.0.0 : rôle/contenu/format des WR-RD formalisés (projection stricte de la section 4 du manuel parent, 8 colonnes, 5 sections, frontmatter minimal). Template créé dans `00 - Docs méta/Templates d'instanciation/Template - WR-RD - Digital Twin.md`. | (à commit) |
| 2026-04-26 | R-040 + correction 6 templates : suppression des titres `# 0) GUIDE D'INSTANTIATION` (qui parasitaient la structure des docs instanciés). Tous les contenus d'instruction désormais exclusivement dans des blocs `@INSTR-*`. Templates touchés : Manuel de BDD Digital Twin v6.1→v6.2, WR-RD Digital Twin v1.0→v1.1, methode_lbp v1.0→v1.1, prompt_lbp v1.0→v1.1, Fiche_outil_LBP v1.0→v1.1, taxonomie. | (à commit) |
| 2026-04-26 | Pré-Phase 6 (D-016) : Notion BDD "Manuels de BDD" — propriété `Lien vers le doc du manuel` renommée → `Lien vers le manuel de BDD (.md)`, nouvelle propriété URL `Lien vers le doc WR-RD (.md)` ajoutée. Manuel `BDD - MANUELS DE BDD.md` mis à jour (v0.1.0→v0.2.0) : renommage + ajout ligne WR-RD en section 3.2 + 3.3 + 3.4 + 7 + checklist. Descriptions Notion à compléter manuellement par Leonard (DDL ne supporte pas). | (à commit) |
| 2026-04-26 | Test Phase 6 — 1er WR-RD instancié : `WR-RD - Actifs.md` (v0.2.0). Révision D-016 : colonne "Utilité pour le Digital Twin" réintégrée (8 → 9 colonnes du WR-RD). Template WR-RD bumpé v1.1.0 → v1.2.0. Cleanup vault : suppression de 2 dossiers vides résiduels (`Manuels de BDD/00 - archives/` racine + `Manuels de BDD/Digital Twin/WR-RD Digital Twin/`). | (à commit) |
| 2026-04-26 | C-008 + scission WORKFLOWS : nouveau scope explicite LBP vs Session sur les docs `refs/`. WORKFLOWS.md scindé en `WORKFLOWS_LBP.md` (WF-011, WF-012, +WF-013 prévu) et `SESSION_WORKFLOWS.md` (WF-010 démarrage Claude). CLAUDE.md mis à jour (section 3 + nouvelle règle C-008). | (à commit) |
| 2026-04-26 | Phase 6 — Trio test WR-RD : 3 WR-RD instanciés (Actifs v0.2.0, Pratiques organisationnelles v0.1.0, Journal des signaux v0.1.0). Profils représentatifs validés : standard, complexe (4 niveaux modulateurs), sans couche calculée native. R-041 + R-042 capturées (propagation manuel → WR-RD + QA stricte d'égalité). WF-013 formalisé dans WORKFLOWS_LBP.md. | (à commit) |
| 2026-04-26 | Cleanup vault avant génération massive WR-RD : (a) 6 manuels sandboxes déplacés `Manuels de BDD/Digital Twin/Sandbox/` → racine `Digital Twin/`, dossier Sandbox supprimé ; (b) 100 frontmatters harmonisés em dash `—` → dash ASCII `-` (28 manuels Twin + 71 notes de concept + corrections cas spéciaux : Capacité organisationnelle/Connaissance/Repères communs/Source d'information/Manuel de BDD/Soft skill) ; (c) 87 fichiers vault renommés pour aligner filename ↔ title (15 manuels Brain `BDD - X` → `Manuel de BDD - X`, 4 manuels Mission Ops idem, 65 notes de concept `concept - X` → `Concept - X` + cas spéciaux). R-043 capturée (cohérence filename ↔ title) ; R-027 révisé en cohérence. Audit final : 0 mismatch résiduel. | (à commit) |
| 2026-04-26 | Phase 6 lot 2 : WR-RD - Actions détectées v0.1.0 instancié. Reste 24 WR-RD à générer (18 manuels Twin actifs + 6 sandboxes) — délégation à un sous-agent general-purpose en cours (option B). | (à commit) |
| 2026-04-26 | **Phase 6 TERMINÉE** : 24 WR-RD restants générés par sous-agent (parser Python ; extraction stricte 9 colonnes). Total 28/28 WR-RD Twin v2 instanciés. QA post-agent : 2 corrections frontmatter (em dash → dash ASCII dans title pour cohérence R-027/R-043, created_at corrigé 2026-04-25 → 2026-04-26). 5 anomalies de fond signalées côté **manuels parents** : (1) `Problématiques` section 4.3 absente, (2) `Organisations` section 4.4 absente, (3) `Glossaire spécifique` 4.4+4.5 non applicables V1 (documenté), (4) `Problématiques sandbox` 4.5 absente, (5) ~10 manuels avec 4.5 marquée non applicable V1 (texte de prose au lieu de tableau). À investiguer si manques intentionnels ou à compléter côté manuels. | (à commit) |

## Prochaines etapes

- **Commit unifié** des batchs A1+A2+A3+A4+B+C + R-038 + R-039 + D-013 + housekeeping
- **Pré-Phase 6 résiduel** : Leonard ajoute manuellement sur Notion les descriptions des 2 propriétés URL de la BDD "Manuels de BDD" (`Lien vers le manuel de BDD (.md)` et `Lien vers le doc WR-RD (.md)`) — DDL Notion ne supporte pas la description.
- **Phase 6 TERMINÉE 26-04-2026** : 28 WR-RD générés (22 manuels Twin actifs + 6 sandboxes), Template v1.2.0, WF-013 documenté dans `refs/WORKFLOWS_LBP.md`.
- **Suites Phase 6** :
  - Investiguer les 5 anomalies signalées par le sous-agent côté manuels parents (sections absentes ou non applicables) : sont-elles intentionnelles ou des manques à combler ?
  - Renseigner sur Notion la propriété `Lien vers le doc WR-RD (.md)` pour les 28 fiches manuels Twin (URL Drive de chaque WR-RD) — workflow WF-011 + WF-013 étape 7.
- **Phase 7** : Prompts maitres et Logic blocks (refonte vers nouvelle archi Twin v2)
- **Enrichissement éditorial Phase 5bis** (option B) : remplir les champs avancés des fiches Glossaire LBP (Valeur ajoutée LBP, Usages IA potentiels, Règles d'usage et pièges, Équivalent langage courant) à partir du corps des notes de concept
- **Chantier "logique des codes uniques"** (backlog : voir `RULES_BRAIN_TWIN-backlog.md`) : définir une grammaire unifiée des codes pour tous les docs Brain/Motor — pas tout de suite, après Phases 6 et 7
