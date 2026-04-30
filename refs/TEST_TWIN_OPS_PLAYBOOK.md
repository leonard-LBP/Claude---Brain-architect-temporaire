# Playbook — Test fonctionnel Twin + Mission Ops DeepSecAI v0 (Phase B)

> **Scope** : Session
> **Date** : 30-04-2026
> **Statut** : v1.0 — playbook stabilisé post-test, 51 fiches créées
> **Ressources** : page test `352e1a18653c8079b1b6edd1c456aaeb` (BDD test - 26-04-2026 - Digital Twin update)

---

## 1. Contexte du test

Test fonctionnel **end-to-end** du remplissage des BDDs Twin + Mission Ops sur un scénario fictif réaliste :
- **Client mock** : DeepSecAI (entreprise tech, mission `dsai-01`)
- **Sources mock** : 3 sources (`SRC-RED-FIRE-001`, `SRC-NOISY-INCIDENT-002`, `SRC-GOV-GAP-003`) fournies par Clément
- **Casting** : 7 individus, 4 collectifs, 1 organisation, 2 actifs, 2 événements, 2 environnements
- **Scénario clé** : activation Feu Rouge sur Banc de Stress + bruit P1 récurrent + trou de décision gouvernance

**Objectif du test** : valider la doctrine de remplissage Twin/MO sur un scénario complet, depuis les sources brutes jusqu'aux indicateurs de pilotage et aux livrables documentaires (bricks).

**Couverture finale** : 51 fiches sur 17 BDDs (10 BDDs Twin + 5 BDDs Pilotage + 3 BDDs Mission Ops).

---

## 2. Architecture du remplissage en vagues

Le test a structuré le remplissage en **10 vagues** organisées en 4 couches doctrinales :

### Couche 1 — Substrat (vagues 1-3)
- **Vague 1** : Sources d'informations + Organisations + Collectifs (3 sources + 1 org + 4 coll)
- **Vague 2** : Individus + Postes (7 individus + 2 postes) + Environnements (2)
- **Vague 3** : Actifs + Événements (2 + 2)

### Couche 2 — Observation/Détection (vagues 4-6)
- **Vague 4** : Glossaire spécifique (2)
- **Vague 5** : Journal des signaux + Actions détectées + Enjeux (2+2+2)
- **Vague 6** : Process candidats sandbox (2)

### Couche 3 — Consolidation (vague 7)
- **Vague 7.1** : Process officiels (2)
- **Vague 7.2** : Pratiques organisationnelles (2)
- **Vague 7.3** : Principes organisationnels (2)
- **Vague 7.4** : Capacités métier candidates sandbox (2)

### Couche 4 — Pilotage + Mission Ops (vagues 8-9)
- **Vague 8.1** : Problématiques (2)
- **Vague 8.2** : OKR (2)
- **Vague 8.3** : Indicateurs (2)
- **Vague 9.1** : Meetings (2)
- **Vague 9.2** : Actions LBP (2)
- **Vague 9.3** : Bricks (2)

### Vague 10 — Vérifications transverses
Audit cross-BDD : auto-propagation des relations bidir, rollups 5D, cohérence chaînes D-009.

---

## 3. Apprentissages clés

### 3.1 Doctrine WR-RD-first (capturé en C-017)

**Découverte initiale** : sur les vagues 1-4, j'ai rempli les fiches en best-guess depuis le seul schéma Notion (data-source-state) + le json scenario. Résultat : 6 fiches au format Nom non conforme (Collectifs/Actifs sans `(Type)`/`(Sous-type)`), plusieurs anti-patterns documentés ignorés.

**Correctif** : à partir de la vague 5, lecture systématique du WR-RD `Manuels de BDD/<Domain>/WR-RD/WR-RD - <Nom BDD>.md` **avant** chaque vague + lecture des `.md` de taxonomies référencées.

**Règle stabilisée** : **C-017** — lire le WR-RD + les taxonomies référencées **avant** chaque vague de remplissage de BDD Notion.

### 3.2 Doctrine régime-aware (capturé en C-018)

**Découverte** : en vague 7.1 (Processus), j'ai signalé comme « anomalie DDL » l'absence de relation `Source(s) d'information` côté Processus. Leonard a corrigé : c'est intentionnel (régime « consolidé/dérivé » selon D-009), la traçabilité passe par les BDDs amont (Process candidats sandbox).

**Règle stabilisée** : **C-018** — vérifier le régime de la BDD (extraction directe vs consolidation/dérivation) avant de juger une absence de relation comme anomalie. Lire WR-RD + chaînes D-009 dans `refs/DECISIONS_LBP.md` + R-012 (séparation des 4 régimes).

### 3.3 Calibration C-012 systématique

À partir de la vague 7.3, application stricte de **C-012** : produire 2-3 fiches d'une vague, valider le pattern auprès de Leonard, puis enchaîner. Très rentable :
- Coût : 2-5 min de pause
- Bénéfice : pas de repassage de masse en cas de pattern défaillant

### 3.4 Quirks techniques

| Quirk | Symptôme | Mitigation |
|---|---|---|
| **Apostrophes typographiques** (R-052) | `Statut de l'objet` (ASCII U+0027) refusé par schéma Notion | Toujours utiliser U+2019 (`'`) dans les noms de propriétés |
| **5D dans multi-select** | Refus si `Connexion à l'environnement (5D)` en ASCII | Idem — typographique requis pour les valeurs aussi |
| **Date avec heure** | `Date/heure` champ direct refusé | Utiliser format expanded `date:Date/heure:start` + `date:Date/heure:is_datetime` |
| **Checkbox** | True/false JSON | `"__YES__"` / `"__NO__"` |
| **Multi-select** | Liste Python refusée | JSON-encoded string `"[\"val1\", \"val2\"]"` |
| **Champ inexistant** | Erreur immédiate (ex. `Confidentialité (option)` sur OKR) | Fetch schéma avant chaque BDD pour vérifier disponibilité |

### 3.5 Relations bidir auto-propagées par Notion

**Bonne nouvelle** : pour chaque relation bidirectionnelle déclarée au DDL, Notion auto-peuple les **deux côtés** dès qu'une fiche relie l'autre. Vérifié sur :
- Meeting → Action (`est suivi par (actions LBP)` — peuplé auto côté Meeting dès création de l'Action liée)
- Action → Brick (`produit (bricks)` — peuplé auto côté Action dès création de la Brick liée)
- Source → Brick (`documente (bricks)` — peuplé auto côté Source dès création de la Brick liée)

**Conséquence** : on remplit toujours côté **enfant** (Brick reliée à Action, pas Action reliée à Brick), et l'autre côté suit. Économise des update_page après création.

### 3.6 R-014 sandboxes (relations dures = uniquement Sources)

Vérifié : les BDDs sandbox (Process candidats sandbox, Capacités métier candidates sandbox, etc.) ne se relient **dur** qu'aux Sources d'informations. Toutes les autres relations passent par les jumelles texte. Conforme R-014 stricte.

---

## 4. Patterns de remplissage par couche

### 4.1 Sources d'informations
- **Nom** descriptif court + **ID externe** = code stable (`SRC-RED-FIRE-001`)
- **Cibles d'extraction recommandées** : multi-select renseigné systématiquement (Individus, Collectifs, Postes, etc.)
- **Confiance / solidité** : 4 si fait établi avéré dans le mock, 3 si recoupé sans preuve, 2 si signal partiel
- **Notes du consultant** : capture les indices de doublons + les fiches Twin à créer en priorité depuis cette source

### 4.2 Twin couche substrat (Org/Coll/Ind/Postes/Env/Actifs/Événements)
- **Format des Noms** :
  - Collectifs : `<Nom> (<Type>)` — ex. `Équipe Stress Bank (équipe-projet)`
  - Actifs : `<Nom> (<Sous-type>)` — ex. `Banc de Stress (Système-applicatif)`
  - Postes : verbe à l'infinitif ou intitulé fonction — ex. `Pilote opérationnelle Banc de Stress`
- **5D** : 1-2 dimensions + 1-2 sous-dimensions principales, jamais tout coché
- **Relations vers Sources** : systématiques côté Twin (régime « extraction directe »)

### 4.3 Twin couche observation (Glossaire/JdS/AD/Enjeux)
- **Glossaire spécifique** : termes propres au client/secteur, distincts du Glossaire LBP
- **Journal des signaux** : 1 signal = 1 phrase factuelle observée + relation vers Source(s)
- **Actions détectées** : verbe à l'infinitif, format pré-Process
- **Enjeux** : énoncé orienté tension/objectif, non solution

### 4.4 Sandbox (Process candidats / Capacités candidates)
- Relations dures uniquement vers Sources (R-014)
- Notes consultant : explicite la transition pressentie sandbox → officiel

### 4.5 Twin couche consolidée (Process officiels / Pratiques / Principes / Capacités)
- **Pas de relation directe vers Sources** (régime consolidé/dérivé, D-009)
- Process : verbe à l'infinitif (`Arbitrer un incident critique`)
- Pratiques : nom + cadence (`Revue Feu Rouge hebdomadaire`)
- Principes : énoncé doctrinal court
- Relations transitives via amont (Process ← Process candidats sandbox ← Sources)

### 4.6 Pilotage (Problématiques / OKR / Indicateurs)
- **Problématiques** : `Intitulé de la problématique` court + `Description` structurée + Criticité 1-5 + Horizon
- **OKR** : Cycle T2-2026 + KR1 + KR2 dans `Description`, relations `traduit (enjeux)` + `adresse (problématiques)`
- **Indicateurs** : Nature (KPI/KRI) + Type d'usage (KR si suit un OKR) + Unité + Fréquence + Rôle temporel (Leading/Lagging) + Mode de calcul + Baseline + Cible + Sens de lecture
- **Chaîne D-009 complète** côté Indicateurs : `mesure l'atteinte de (OKR)` + `mesure (problématiques)` + `mesure (pratiques)` + `mesure (processus)` + `est affecté par (événements)` + `mesure la performance de (collectifs)`

### 4.7 Mission Ops (Meetings / Actions LBP / Bricks)
- **Meetings** :
  - Code stable : `MTG-<TYPE>-<DISCRIMINANT>-<DATE-ISO>` (ex. `MTG-ENT-MAYA-2026-04-22`)
  - Sections structurées dans `Hypothèses / questions à clarifier` (avant) et `Résultats et décisions` (après)
  - `réunit (individus)` peuplé en relation + jumelle texte
  - Date/heure expanded format
- **Actions LBP** :
  - Verbe à l'infinitif : `Générer CR interne LBP`, `Produire profil organisationnel`
  - Code `ACT-<DISCRIMINANT>-<DATE>` ou `ACT-<DISCRIMINANT>-NNN`
  - **Type d'entrée** : Action (atomique) vs Activité (lot)
  - **Famille d'action** : Synthèse et livrables, Animation en direct, Coordination, etc.
  - **Responsable principal** : Consultant LBP (test) — distinct des assignations individuelles
  - **Description et critères de done** : Contexte / Fait quand / Livrable / Vigilance
  - `assure le suivi de (meetings)` pour les actions post-meeting
- **Bricks** :
  - Brick ID = nom fichier sans extension : `BRK_<mission-code>_<brick-code>_<discriminant>_<rev>`
  - Famille : Compte-rendu, Profil, Analyse, Livrable, etc.
  - **mission_code** + **brick_code** + **Discriminant** + **rev** extraits du Brick ID
  - `est produite par (actions LBP)` + `est documentée par (sources d'informations)` (si applicable)
  - `Generated at` au format expanded

---

## 5. Anomalies détectées et corrigées

| # | Anomalie | Vague | Correctif |
|---|---|---|---|
| 1 | 6 fiches Collectifs/Actifs sans `(Type)`/`(Sous-type)` | 1-3 | Renommage post-audit |
| 2 | Apostrophe ASCII dans 5D multi-select | 8.3 | Re-création avec U+2019 |
| 3 | Champ `Confidentialité (option)` testé sur OKR (n'existe pas) | 8.2 | Champ retiré, relancé |
| 4 | Faux signalement « anomalie DDL » sur absence Source côté Process | 7.1 | C-018 capturé |
| 5 | Indicateurs sans relation `mesure (problématiques)` | 8.3 | Update post-vérif vague 10 |
| 6 | URL malformée Événements sur Tom Alvarez | 3 | Correction page_id |
| 7 | JSON syntax error vague 5 Enjeu (oubli `[]`) | 5 | Re-soumission |

---

## 6. Découvertes architecturales en cours de test

### 6.1 Propriété "Régime de l'entité" — à cogiter

Pendant le test, plusieurs entités auraient gagné à porter une propriété explicite indiquant leur régime :
- **Sandbox** : entrée à valider, en cours de promotion vers BDD officielle
- **Officiel** : entrée stabilisée, source de vérité
- **Avéré/figé** : entrée mature, ne devrait plus être modifiée sans procédure
- **Doublon archivé** : entrée fusionnée vers une entité maître

À cogiter post-test (cf. `Maître` déjà au backlog `RULES_BRAIN_TWIN-backlog.md`).

### 6.2 Article D-009 vivant

Le test a validé en pratique les chaînes de transformation D-009 :
- Source → Action détectée → Process candidat sandbox → Process officiel ✓
- Source → Action détectée → Pratique organisationnelle ✓
- Source → Enjeu → Problématique → OKR → Indicateur ✓
- Pratique → Capacité (via candidats sandbox) ✓

### 6.3 Templates de bricks comme socle

Les bricks créées (`TPL_BRICK_MTG_INT_IND_CR`, `TPL_BRICK_PRF_ORG`) ont été référencées dans le champ `Utilise aussi en inputs` mais pas reliées (les templates étant au Brain, pas au Twin). À cogiter : faut-il une relation `instancie (template)` côté Brick → Templates de bricks Brain ?

---

## 7. Limites du test (non exhaustif)

- **Volumétrie faible** : 51 fiches vs cible production (centaines/milliers). Patterns validés en petit, à stress-tester en grand.
- **Pas de doublons réels traités** : `M. Chen duplicate` créé mais non fusionné dans Maya Chen (dédup à automatiser plus tard).
- **Rollups 5D pas testés en lecture finale** : structure présente mais pas vérifié visuellement que toutes les sous-dim 5D remontent bien aux Indicateurs.
- **Pas testé** : Initiatives organisationnelles, Modulateurs, Relations inter-organisations.
- **Mission Ops minimal** : 2 fiches par BDD, pas de scénario multi-meetings/actions imbriquées.

---

## 8. Recommandations pour Phase C+

1. **Capitaliser cette page test** : la conserver comme exemple de référence pour onboarding nouveaux consultants ou agents.
2. **Industrialiser le pipeline** : script de remplissage à partir de bricks JSON structurées (post Phase E chantier P).
3. **Cogiter la propriété "Régime de l'entité"** comme proposé en §6.1.
4. **Étendre le test à 200-500 fiches** sur un client mock plus complet pour stress-tester volumétrie + dédup + rollups 5D.
5. **Tester Initiatives + Modulateurs** dans une vague Phase B bis.

---

## 9. Référentiel de fichiers utiles post-test

- Mappings page IDs : `scripts/phase_b/output/page_ids_v2.json` (35 fiches dupliquées) + `scripts/phase_b/output/page_ids.json` (anciennes IDs)
- Mappings data sources : `scripts/phase_b/output/bdd_test_data_sources_v2.json`
- Snapshot Twin : `scripts/phase_b/output/fiches_snapshot.json`
- Captures règles session : `CLAUDE.md` (C-017, C-018), `refs/RULES_BRAIN_TWIN-backlog.md`

---

> Dernière mise à jour : 30-04-2026 — playbook v1.0 stabilisé après vague 10.
