# Playbook - Mise à jour majeure de l'écosystème LBP du 01-05-2026

> **Salut Clément**,
> Ce document est ton **point d'entrée** pour absorber la grande mise à jour de l'écosystème documentaire LBP qui a été menée par Leonard et Claude pendant le mois d'avril 2026.
> Il introduit la MAJ, synthétise les chantiers réalisés et ceux qui restent à faire, et te donne le mode d'emploi des 13 documents joints.
> **Lis-le en premier**, avant tout autre doc du bundle.

---

## 1. Contexte de la MAJ

Tu as travaillé jusqu'ici avec l'architecture telle qu'elle était au **22-04-2026** (`Panorama V2 v3` du Digital Twin). Pendant les 10 derniers jours, l'écosystème a été **profondément refondu** sur 3 axes :

1. **Cadrage architectural** : formalisation des 3 domaines co-égaux (Brain / Digital Twin / Mission Ops), de leurs frontières d'isolation, et de la stack technique cible (Notion pour Brain, Supabase pour Twin + MO).
2. **Stabilisation doctrinale** : 9 doctrines structurantes formalisées, 23 décisions architecturales tracées, 62 règles atomiques cataloguées, 17 workflows opérationnels documentés, grammaire de codification universelle posée.
3. **Validation opérationnelle** : test fonctionnel Phase B sur scénario fictif DeepSecAI v0 (51 fiches Twin+MO créées sur la maquette Notion test, validation des chaînes de transformation et des articulations).

Cette MAJ touche uniquement la **couche documentaire** (manuels, doctrines, règles). Aucune modification structurelle de l'app Brain Studio que tu maintiens. Mais elle **change le contrat** entre la doctrine et l'app : c'est ce contrat que tu vas devoir auditer et porter sur la stack cible.

---

## 2. Synthèse des chantiers réalisés

### 2.1 Brain - gouvernance documentaire

- **D-019** : Brain unifié au niveau modèle de données. Les zones Core / Motor sont conservées comme étiquette de discours mais ne sont plus une partition stricte.
- **D-021** : architecture des **3 agents LBP** formalisée (Brain architect / Twin architect / KONTEXT) avec frontières d'isolation infranchissables.
- **R-054** : codification universelle des objets Brain (table de préfixes stable : `CPT_`, `GLO_`, `METH_`, `TPL_BRICK_`, `CHRT_`, `DBMAN_TW/MO/BR_`, `WRRD_TW/MO/BR_`, `LGBLK_`, `PRMPT_M/S/U/T_`, `OUT_`, `AGT_`).
- **R-055/056/058/059** : hygiène d'écriture des docs Brain (frontmatter en 3 zones balisées, versioning X.Y, anti-jumelles texte, pas de bruit historique).
- **318 docs migrés au canon** sur les Phases 4-7 (43 manuels + 32 WR-RD + 72 notes de concept + 96 taxonomies + 24 instances de templates).
- **102 taxonomies migrées au canon** (Phase A4.A) : codes `<X>.<Y>.LBP` migrés vers `<X>.<Y>` (suffix `LBP` éliminé).
- **Sync DDL Notion Brain** (28-04) : ~26 actions DDL (DROP/ADD/ALTER) pour aligner Notion sur les manuels.
- **D-020** : propagation de la propriété `Version du template` à toutes les BDDs Brain.
- **D-022** : différenciation assumée des frontmatters Twin et Mission Ops (régimes de connaissance distincts).

### 2.2 Digital Twin - modèle ontologique du client

- **Architecture stabilisée** : 28 BDDs (22 officielles + 6 sandboxes), 8 principes cardinaux, chaînes D-009 de transformation de la connaissance, 11 moteurs analytiques, 11 traversées à forte valeur.
- **Test Phase B** (30-04-2026) : scénario fictif DeepSecAI v0, 51 fiches créées sur la maquette Notion test (35 Twin + 10 Pilotage + 6 Mission Ops). Validation des chaînes D-009 + auto-propagation Notion + bricks D-018.
- **Captures C-017 et C-018** : doctrine WR-RD-first (lire le WR-RD avant remplissage) + régime-aware (vérifier le régime de la BDD avant signaler une anomalie).

### 2.3 Mission Ops - gouvernance opérationnelle

- **D-023** : Mission Ops formalisé comme domaine **co-égal** au Brain et au Twin, gouverné par 4 BDDs (`Sources d'informations`, `Meetings`, `Actions LBP`, `Bricks`).
- **4 manuels MO + 4 WR-RD MO** stabilisés au canon.
- **Test Phase B** valide les 3 ponts MO ↔ Twin (Sources / Bricks / Actions).
- **Stack cible Supabase** pour Twin et MO (post-Phase C).

### 2.4 Bundle de docs méta durables (créé 01-05-2026)

11 documents structurants `*_LBP.md` créés et indexés dans la BDD `Docs méta LBP` du Brain. Ces docs sont la **référence permanente** de l'écosystème (cf. tableau §4).

### 2.5 Stack technique cible (D-023)

| Domaine | Stack actuelle | Stack cible | Horizon |
|---|---|---|---|
| Brain | Notion + Markdown vault | Notion (à moyen terme) | 12-18 mois, pas de migration prévue |
| Digital Twin | Maquette Notion test + Markdown vault | **Supabase** | Portage post-Phase C |
| Mission Ops | Maquette Notion test + Markdown vault | **Supabase** | Portage post-Phase C |

---

## 3. Chantiers non encore réalisés (à venir)

### 3.1 Chantier P - Logic Blocks / Prompts / Agents / 4 templates legacy

**Périmètre** :
- Refonte de **4 templates legacy** (templates secondaires non encore migrés au canon v2 : `Template de system prompt.md`, `template-prompt_maitre_lbp.md`, `Template-prompt_lbp.md`, `template-meta_logic_block_lbp.md`)
- Tri massif des **101 Logic Blocks** (état Twin v2)
- Tri massif des **76 Prompts** (état Twin v2)
- Création des **3 fiches `Agents LBP`** (Brain architect / Twin architect / KONTEXT) une fois Prompts et Logic Blocks à jour
- Mise à jour des system prompts / prompts maîtres / logic blocks pour cohérence Twin v2 + D-019 + D-021

**Priorité** : Haute - à enchaîner après stabilisation du bundle docs méta.

**Conséquence pour toi** : tant que ce chantier n'est pas fait, les Logic Blocks et Prompts dans Notion sont en partie obsolètes vs Twin v2. À ne pas s'appuyer dessus pour l'app sans validation préalable.

### 3.2 Chantier M - Templates par type de doc Brain + tri Notion

**Périmètre** :
- Créer un template d'instanciation pour chaque type de doc Brain (charte rédactionnelle, charte graphique, panorama, doctrine, specs d'architecture, codification, règles de propagation, etc.)
- Réactualisation `PLAYBOOK macro-archi v2`
- Tri des entrées Notion `Docs méta LBP` sans Markdown actif
- Refactoring des 11 docs `*_LBP.md` actuels au canon des nouveaux templates (bump `version` à `2.0`)

**Priorité** : Moyenne, post-Chantier P.

### 3.3 Phase C - Audit final + figement Brain

**Périmètre** :
- Audit transverse Notion ↔ Manuels Brain (WF-016)
- Figement de l'architecture Brain (pas de modifs sans D-XXX explicite)
- Cogitation propriété `Régime de l'entité` (sandbox / officiel / avéré-figé / doublon archivé)

**Priorité** : Post-bundle docs méta complet.

### 3.4 Portage Supabase Twin + Mission Ops

**Périmètre** :
- Modélisation Postgres des 28 BDDs Twin + 4 BDDs MO + relations (foreign keys)
- Migration des taxonomies LBP en tables de référence
- Préservation des patterns de codification (R-054 + grammaire bricks)
- Workflows d'instanciation par mission
- Synchronisation Brain (Notion) ↔ Twin/MO (Supabase) en lecture seule

**Priorité** : Post-Phase C. **Chantier dédié à cadrer ensemble**.

### 3.5 Migration Notion Brain (éventuelle)

**Pas de plan à court terme**. Notion suffit pour Brain à 12-18 mois. Si une migration devient nécessaire, ce sera un chantier dédié à part.

---

## 4. Mode d'emploi des 13 documents fournis

### Tableau détaillé

| # | Document | Type | Rôle | Quand le consulter | Durée lecture |
|---|---|---|---|---|---|
| 1 | `MIGRATION_REPORT_2026-04.md` | 🟣 One-shot | Narratif daté qui détaille le delta vs ce que tu connais | **À lire en 1er** | ~30 min |
| 2 | `PANORAMA_LBP.md` | 🟢 Vue d'entrée | Vue macro des 3 ensembles, frontières, stack technique | **À lire en 2e** | ~15 min |
| 3 | `DOCTRINE_LBP.md` | 🟢 Doctrine | 9 paradigmes structurants - le pourquoi de l'écosystème | **À lire en 3e** pour saisir la logique d'ensemble | ~30 min |
| 4 | `DOCTRINE_TWIN_LBP.md` | 🟢 Doctrine | Doctrine détaillée du Digital Twin (régimes, chaînes, gouvernance) | À lire si tu travailles sur le Twin | ~45 min |
| 5 | `SPECS_ARCHITECTURE_BRAIN_LBP.md` | 🟢 Specs | Modèle conceptuel des 11 BDDs Brain | À consulter avant toute modif Brain | ~20 min |
| 6 | `SPECS_ARCHITECTURE_TWIN_LBP.md` | 🟢 Specs | Modèle conceptuel des 28 BDDs Twin | À consulter avant toute modif Twin | ~20 min |
| 7 | `SPECS_ARCHITECTURE_MISSION_OPS_LBP.md` | 🟢 Specs | Modèle conceptuel des 4 BDDs Mission Ops | À consulter avant toute modif MO | ~20 min |
| 8 | `CODIFICATION_LBP.md` | 🟢 Outil transverse | Grammaire de tous les codes LBP (Brain + Twin + MO + IDs systèmes) | **À garder à portée de main** avant toute production de code | Référence |
| 9 | `PROPAGATION_RULES_LBP.md` | 🟢 Outil transverse | Cheat sheet 1-pager : si tu modifies X, où propager ? | **À garder à portée de main** avant toute modif structurante | Référence |
| 10 | `RULES_LBP.md` | 🟢 Catalogue | 62 règles atomiques (R-XXX) | Lookup ponctuel par ID ou mot-clé | Référence |
| 11 | `DECISIONS_LBP.md` | 🟢 Catalogue | 23 décisions architecturales (D-XXX) | Lookup ponctuel - pour comprendre le pourquoi d'un choix | Référence |
| 12 | `WORKFLOWS_LBP.md` | 🟢 Catalogue | 17 workflows opérationnels (WF-XXX) | À suivre pas-à-pas pour les opérations standardisées | Référence |
| 13 | `TEST_TWIN_OPS_PLAYBOOK.md` | 🟡 Apprentissages | Apprentissages du test Phase B (51 fiches DeepSecAI v0) | Pour comprendre les patterns de remplissage Twin/MO | ~15 min |

### Légende des types

- 🟣 **One-shot** : doc daté, figé, pas réactualisé. Sert juste à comprendre le delta.
- 🟢 **Bundle docs méta durables** (`*_LBP.md`) : référence permanente de l'écosystème, indexée dans la BDD `Docs méta LBP` Notion. Évolue par bumps de version (X.Y).
- 🟡 **Apprentissages** : hors bundle durable mais utile à connaître pour les patterns pratiques.

### Pyramide de navigation

```
NIVEAU 1 - Vue d'entrée (lire en premier)
├── MIGRATION_REPORT_2026-04 (delta)
└── PANORAMA_LBP (macro 3 ensembles)

NIVEAU 2 - Doctrine et règles (pour comprendre)
├── DOCTRINE_LBP (transverse)
├── DOCTRINE_TWIN_LBP (Twin spécifique)
├── RULES_LBP (R-XXX)
├── DECISIONS_LBP (D-XXX)
└── WORKFLOWS_LBP (WF-XXX)

NIVEAU 3 - Spécifications par domaine (pour construire)
├── SPECS_ARCHITECTURE_BRAIN_LBP
├── SPECS_ARCHITECTURE_TWIN_LBP
└── SPECS_ARCHITECTURE_MISSION_OPS_LBP

NIVEAU 4 - Outils transverses (à portée de main)
├── CODIFICATION_LBP
└── PROPAGATION_RULES_LBP

HORS BUNDLE - Apprentissages pratiques
└── TEST_TWIN_OPS_PLAYBOOK
```

---

## 5. Roadmap suggérée pour ta reprise

### Étape 1 - Lecture (1 à 2 jours)

Dans cet ordre :
1. Ce playbook (~30 min) - tu es ici
2. `MIGRATION_REPORT_2026-04.md` (~30 min) - le delta narratif
3. `PANORAMA_LBP.md` (~15 min) - macro
4. `DOCTRINE_LBP.md` (~30 min) - le pourquoi
5. Le reste selon ton périmètre

### Étape 2 - Audit de l'app vs architecture cible (~1 semaine)

L'app que tu maintiens est sur l'ancienne architecture. À auditer :
- Quelles BDDs de l'app correspondent encore aux BDDs cibles décrites dans `SPECS_X_LBP` ?
- Quelles propriétés de l'app sont obsolètes / manquantes / désynchronisées ?
- Comment l'app gère-t-elle la stack technique cible (Notion Brain + Supabase Twin+MO) ?

À l'issue : produire un **rapport d'écart app vs architecture cible** pour prioriser les évolutions.

### Étape 3 - Cadrage portage Supabase (à arbitrer ensemble, post-Phase C)

Cadrer ensemble :
- Schémas Postgres pour Twin et MO
- Stratégie de migration des données existantes
- Workflows d'instanciation par mission
- Synchronisation Brain (Notion) ↔ Twin/MO (Supabase) en lecture seule

### Étape 4 - Évolutions app au fil de l'eau

Au fur et à mesure que les Chantiers P et M avancent (Prompts, Logic Blocks, Agents, docs méta, templates), ces évolutions devront se refléter dans l'app. À cadrer en flux continu.

---

## 6. Règles essentielles à connaître

> Si tu ne dois retenir que 5 choses, ce sont celles-ci :

1. **R-001 - Markdown source de vérité unique**
   Le doc Markdown du vault `Architecture data\` est source de vérité. Notion (et demain Supabase) est miroir d'application, **jamais l'inverse**. Pour modifier un objet : 1) modifier d'abord le Markdown, 2) aligner ensuite Notion.

2. **D-019 / D-021 - Isolation Brain ↔ Twin/MO**
   Le Brain ne change pas pendant les missions. L'évolution du Brain est une activité **méta-LBP** (gouvernance documentaire), pas une activité de mission. KONTEXT (orchestration MO) **ne peut pas** appeler Brain architect.

3. **D-023 - Stack technique cible**
   Brain reste sur **Notion** (12-18 mois, pas de migration prévue). Twin et Mission Ops migrent vers **Supabase** post-Phase C. La maquette Notion Twin+MO actuelle est une **fixture de validation de schéma**, pas une production.

4. **R-054 - Codification universelle**
   Tous les objets Brain ont un code stable conforme à la table de préfixes officielle. Avant toute production de code, consulter `CODIFICATION_LBP.md`.

5. **WF-008 - Propagation d'impacts**
   Avant toute modification structurante, ouvrir `PROPAGATION_RULES_LBP.md` (cheat sheet) ou consulter `WORKFLOWS_LBP.md` § WF-008 (détail). La propagation est strictement descendante (Markdown → dérivés), jamais l'inverse.

---

## 7. Si tu as des questions

On peut en discuter au fil de l'eau. Tous les docs renvoient les uns vers les autres pour faciliter la navigation. N'hésite pas à me solliciter dès qu'un point est flou.

Bonne reprise !

— Leonard

---

> Ce playbook est figé au 01-05-2026. Toute évolution ultérieure de l'écosystème sera dans les docs durables (`*_LBP.md`) sur Drive, pas dans ce snapshot.
