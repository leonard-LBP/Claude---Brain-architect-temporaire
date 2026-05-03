---
# === Identité ===
title: "Constitution des docs méta - LBP"
doc_type: doc_meta
code: "META_DOC_MAP_LBP"

# === Méta-gouvernance ===
version: "0.3"
template_code: "CHRT"
template_version: "1.0"
created_at: "03-05-2026"
updated_at: "03-05-2026"
status: "Validé"
scope: "LBP"

# === Spec d'usage ===
summary: "Constitution opérationnelle de la BDD `Docs méta LBP` : définit ce qu'est un doc méta, ce qui n'en est pas un, les 5 fonctions systémiques de gouvernance qu'un doc méta peut porter, la règle anti-doublon du propriétaire canonique unique, le découplage des 4 logiques (lecture / arborescence / index / graphe), la frontière Brain ↔ Mission, et la boucle de gouvernance documentaire en 7 temps."
purpose: "Servir de doc d'entrée pour tout intervenant (humain ou agent) qui doit comprendre comment fonctionne l'architecture des docs méta du Brain LBP, créer un nouveau doc méta dans le respect des conventions, ou auditer la cohérence de la BDD `Docs méta LBP`. Ce doc cadre toute la production future et toute la maintenance des docs méta."
aliases:
  - "Doc map - LBP"
  - "Constitution méta - LBP"
  - "Cartographie des docs méta"
  - "DOC_MAP_META_LBP"
tags:
  - doc_meta
  - constitution
  - control_plane
  - orienter
  - lbp
---

# Constitution des docs méta - LBP

> **Scope** : 🟦 LBP - Bundle écosystème (durable, indexé dans BDD `Docs méta LBP`).
> **Fonction systémique** : `META.FUNCTION.ORIENTER` (porte d'entrée pour comprendre les docs méta).
> **Public visé** : intervenants LBP (Leonard, Clément, futurs collaborateurs), agents (brain architect, agents d'analyse).

---

## 1. Objet

### 1.1 Posture : control plane, pas grenier

La BDD `Docs méta LBP` est le **plan de contrôle** de l'écosystème LBP, pas un dépôt de « docs importants ». Son rôle n'est pas de stocker la connaissance opérationnelle (qui vit dans les manuels de BDD, taxonomies, notes de concept, prompts, méthodes, templates, etc.), mais de **rendre possible** la compréhension, la maintenance, l'évolution, l'audit et l'orchestration de tout le reste.

Concrètement, un doc méta sert à **gouverner** d'autres objets, pas à les remplacer.

### 1.2 Articulation avec les règles fondatrices

- **R-001** (Markdown SoT) : tous les docs méta vivent en Markdown dans le vault `Architecture data`. Notion est un miroir d'index.
- **D-023** (stack) : Brain = Notion (BDD `Docs méta LBP` indexée dans Notion), Twin + Mission Ops = Supabase.
- **R-002, R-003, D-007** (zero contamination) : aucun contenu spécifique à une mission client n'entre dans `Docs méta LBP`. Les docs méta sont **transverses cross-mission**, stables, réutilisables.

---

## 2. Définition opérationnelle

### 2.1 Règle frontière (R-065)

> **Un doc est méta s'il gouverne plusieurs objets, plusieurs BDD, plusieurs familles d'artefacts ou plusieurs workflows.**
> **Un doc n'est pas méta s'il décrit un objet, une BDD, une taxonomie, un prompt, une méthode ou un template spécifique.**

### 2.2 Table de classement opérationnelle

| Va dans BDD `Docs méta LBP` | Va dans une autre BDD |
|---|---|
| `[[Panorama LBP]]` | Manuel de BDD `Actifs`, `Collectifs`, `Bricks`, etc. → BDD `Manuels de BDD` |
| `[[Cadre LBP]]` (pourquoi de l'écosystème) | Mini-docs de taxonomies → BDD `Registre des taxonomies` |
| `[[Cadre Twin]]` (pourquoi du Twin) | Notes de concept (définitions du glossaire) → BDD `Notes de Concept LBP` |
| `[[Architecture Brain]]`, `[[Architecture Twin]]`, `[[Architecture Mission Ops]]` | Prompts maîtres, system prompts → BDD `Prompts LBP` |
| `[[Règles intrinsèques LBP]]`, `[[Décisions architecturales LBP]]`, `[[Workflows opérationnels LBP]]`, `[[Codification LBP]]`, `[[Règles de propagation LBP]]` | Méthodes LBP → BDD `Méthodes LBP` |
| Chartes (rédactionnelle, graphique, sécurité/RGPD) **transverses LBP** | Logic blocks, agents, outils externes → BDDs dédiées |
| Quality control (par domaine : Brain, Twin, MO) | **Templates** (dans `Templates Brain/` racine vault) → BDD `Templates Brain` |
| **Constitution** elle-même (ce doc) | Templates de bricks → BDD `Templates de Bricks` (existante, séparée par scope agent — utilisée par kontext) |

### 2.3 Cas limites

- **Une charte spécifique à une mission client** (ex. charte rédactionnelle d'un livrable client X) → **n'est PAS un doc méta LBP**. Elle vit dans le Twin de la mission ou dans Mission Ops, pas dans le Brain (zero contamination).
- **Un doc qui mélange plusieurs fonctions à parts égales** → c'est probablement un signal de redécoupage (cf. §5 propriétaire canonique unique). Envisager un split en plusieurs docs.

---

## 3. Les 5 fonctions systémiques

Tout doc méta indexé dans `Docs méta LBP` porte **une fonction systémique dominante** (taxo `META.FUNCTION`, mono-sélection). Les 5 fonctions sont stables, exhaustives, fermées :

| Fonction | Question répondue | Exemples LBP | Code |
|---|---|---|---|
| **Orienter** | Où suis-je dans l'écosystème ? | Panorama LBP, Constitution des docs méta | `META.FUNCTION.ORIENTER` |
| **Expliquer** | Pourquoi le système est conçu comme ça ? | Cadre LBP, Cadre Twin, Décisions architecturales | `META.FUNCTION.EXPLIQUER` |
| **Structurer** | Quels objets, quelles frontières ? | Architecture Brain, Architecture Twin, Architecture MO | `META.FUNCTION.STRUCTURER` |
| **Normer** | Qu'est-ce qui est obligatoire ? | Règles intrinsèques, Codification, Chartes, Quality control | `META.FUNCTION.NORMER` |
| **Opérer** | Comment faire ? Dans quel ordre ? | Workflows opérationnels, Règles de propagation, Procédures d'audit | `META.FUNCTION.OPERER` |

Pour la définition complète, les observables et les règles d'arbitrage : voir `[[META.FUNCTION]]` (taxonomie source).

---

## 4. Frontière Brain ↔ Mission (zero contamination)

### 4.1 Ce qui DOIT vivre dans `Docs méta LBP`

- Doctrine, cadre, règles, conventions, chartes, workflows **transverses cross-mission**.
- Outils de gouvernance documentaire **stables et réutilisables** d'une mission à l'autre.
- Tout ce qui sert à pérenniser le savoir-faire LBP entre les missions.

### 4.2 Ce qui ne DOIT PAS vivre dans `Docs méta LBP`

- Charte ou convention **spécifique à une mission client** → vit dans le Twin de la mission, BDD `Conventions instance` ou similaire.
- Données client (noms, profils, contenu missionnel) → vit dans le Twin ou Mission Ops, **jamais** dans le Brain.
- Règles ou playbooks dédiés à un livrable client précis → vit dans Mission Ops.

### 4.3 Articulation

- **R-002, R-003** (séparation Brain / Twin / Mission Ops)
- **D-007** (zero contamination)
- **C-018** (régimes de connaissance différents)
- **R-012** (séparation des 4 régimes)

---

## 5. Règle anti-doublon : propriétaire canonique unique

### 5.1 Énoncé (R-066)

> **Une information structurante a un seul propriétaire canonique. Tous les autres docs peuvent la résumer ou la citer, mais doivent pointer vers le propriétaire — jamais la redéfinir.**

### 5.2 Table de propriété canonique (cas LBP)

| Information | Propriétaire canonique | Autres docs : que peuvent-ils faire ? |
|---|---|---|
| Liste des 11 BDDs Brain | `[[Architecture Brain]]` | `[[Panorama LBP]]` résume ; manuels de BDD détaillent |
| Liste des 28 BDDs Twin | `[[Architecture Twin]]` | `[[Cadre Twin]]` explique la logique ; manuels détaillent |
| Champs exacts d'une BDD | Manuel de BDD correspondant | Spec architecture **ne reproduit pas** le DDL |
| Valeurs d'une taxonomie | Mini-doc de taxonomie | Manuels indiquent **comment** la propriété consomme la taxo, pas les valeurs |
| Code d'un objet Brain | `[[Codification LBP]]` + frontmatter du doc | Les autres docs **citent** le code, sans redéfinir la grammaire |
| Pourquoi une décision a été prise | `[[Décisions architecturales LBP]]` (D-XXX) | `[[Règles intrinsèques LBP]]` (R-XXX) **applique** la règle dérivée |
| Comment appliquer une règle | `[[Règles intrinsèques LBP]]` ou `[[Workflows opérationnels LBP]]` selon le cas | Doctrine explique le paradigme, pas l'application |
| Que faire après modification | `[[Règles de propagation LBP]]` ou `[[Workflows opérationnels LBP]]` (WF-008) | Les docs concernés indiquent seulement « voir propagation » |
| Définition d'un concept du glossaire | Note de concept correspondante (BDD `Notes de Concept LBP`) | Les docs méta peuvent **citer** le concept, pas le redéfinir |
| Template d'instanciation d'un objet | BDD `Templates Brain` | Les docs méta peuvent **citer** le template utilisé via la propriété `Template`, pas le copier |

### 5.3 Mécanisme technique de mise en œuvre

- **Renvois via wikilinks** (cf. C-024) : utiliser `[[Doc cible]]` pour pointer vers le propriétaire canonique. Lisible humain ET agent, résilient au rename via Obsidian UI.
- **Backlinks bidirectionnels** (cf. C-025) : la lecture inverse (« qui me cite ») est calculée automatiquement par Obsidian — pas besoin de déclarer la relation des 2 côtés.
- **Interdire la transclusion `![[]]` dans les docs canoniques** (cf. C-023) : la transclusion est invisible aux agents et aux audits programmatiques. Réservée aux docs de navigation/dashboard.

---

## 6. Découplage des 4 logiques

Une même information sur les docs méta vit dans **4 vues distinctes**, qui répondent à des besoins différents et **ne doivent pas être confondues** :

| Logique | Sert à | Implémentation LBP |
|---|---|---|
| **Pyramide de lecture** | Guider un humain ou un agent qui découvre LBP | Section dans `[[Panorama LBP]]` |
| **Arborescence de fichiers** | Ranger proprement les sources Markdown | Dossier `00 - Docs méta/` avec sous-dossiers numérotés par fonction systémique (10-Orienter, 20-Expliquer, 30-Structurer, 40-Normer, 50-Opérer + 90-États & audits + 99-Archives) |
| **Index Notion `Docs méta LBP`** | Filtrer, relier, auditer, piloter les docs | BDD Notion avec propriétés enrichies (`Fonction systémique`, `Template`, `Statut`, `Version`, `Lien Drive`, etc.) |
| **Graphe de dépendances** | Voir qui gouverne quoi et quoi propager | Relations Brain (`Gouverne / Est gouverné par`) + backlinks Obsidian + relations Notion `est utilisé dans` |

**Conséquence pratique** : une même fiche peut être en niveau 2 dans la pyramide de lecture, rangée dans `30 - Structurer/`, et reliée à 40 manuels comme doc gouvernant. **Forcer tout dans une seule hiérarchie** = perdre soit la lisibilité, soit la maintenabilité.

---

## 7. Boucle de gouvernance documentaire (7 temps)

Tout changement structurant dans l'écosystème suit cette boucle, qui est l'équivalent documentaire des chaînes de transformation Twin (cf. D-009) :

```
Signal de dérive ou de besoin
   ↓
Décision D-XXX (capturée dans [[Décisions architecturales LBP]])
   ↓
Règle R-XXX (codifiée dans [[Règles intrinsèques LBP]])
   ↓
Workflow WF-XXX (formalisé dans [[Workflows opérationnels LBP]])
   ↓
Propagation Markdown-first (cascade WF-008 — cf. [[Règles de propagation LBP]])
   ↓
Audit / Quality Control (à formaliser : Quality control - Brain)
   ↓
Mise à jour de l'état de l'écosystème (ECOSYSTEM-STATE — scope Session)
```

### 7.1 Articulation entre les 4 types d'IDs

- **D-XXX** (Décisions) : pourquoi un choix a été fait. Historique. Vit dans `[[Décisions architecturales LBP]]`.
- **R-XXX** (Règles) : règle atomique à respecter. Dérivée d'une ou plusieurs décisions. Vit dans `[[Règles intrinsèques LBP]]`.
- **WF-XXX** (Workflows) : opération standardisée. Souvent dérivée d'une règle qui définit le « quoi », tandis que le workflow définit le « comment ». Vit dans `[[Workflows opérationnels LBP]]`.
- **C-XXX** (Conventions session) : règles de la collaboration Claude/Leonard, hors bundle LBP. Vivent dans `CLAUDE.md`.

### 7.2 Cycle de revue (esquisse)

- **Constitution (ce doc)** : audit annuel + revue après tout changement structurel de l'architecture des docs méta.
- **Catalogues (RULES, DECISIONS, WORKFLOWS)** : pas de revue cyclique, bumpés au fil de l'eau (R-063 — patch sur ajout d'entrée atomique).
- **Cadres** : revue trimestrielle ou à milestone (refonte d'une section structurante).
- **Specs d'architecture** : revue à chaque évolution structurelle d'un domaine.
- **Chartes** : revue annuelle ou à changement de positionnement éditorial / graphique.

---

## 8. Statut de cette constitution

- **Bump version** : suit R-063 (patch sur enrichissement compatible, minor sur refonte structurelle).

---

## Annexe A — Arborescence cible des docs méta

> **Convention de nommage des fichiers (R-064)** : le filename d'un doc méta est strictement identique à son `title:` frontmatter (= nom canonique humain), et à son `Nom canonique` côté Notion. Le code `META_*` vit dans le frontmatter et dans la propriété `Code unique` côté Notion, mais **n'apparaît pas dans le filename**. Cohérence : 1 doc = 1 nom humain, sans bruit visuel.

```
00 - Docs méta/
  10 - Orienter/
    Panorama - LBP.md                          (code : META_PANORAMA_LBP)
    Constitution des docs méta - LBP.md        (code : META_DOC_MAP_LBP)
    Philosophie - LBP.md                       (code : META_PHILOSOPHIE_LBP)
    Profil - LBP.md                            (code : META_PROFIL_LBP)

  20 - Expliquer/
    Cadre - LBP.md                             (code : META_CADRE_LBP)
    Cadre - Brain.md                           (code : META_CADRE_BRAIN)
    Cadre - Twin.md                            (code : META_CADRE_TWIN)
    Cadre - Mission Ops.md                     (code : META_CADRE_MO)
    Principes structurants - LBP.md            (code : META_PRINCIPES_LBP)
    Décisions architecturales - LBP.md         (code : META_DECISIONS_LBP)

  30 - Structurer/
    Architecture - Brain.md                    (code : META_SPECS_ARCHITECTURE_BRAIN)
    Architecture - Twin.md                     (code : META_SPECS_ARCHITECTURE_TWIN)
    Architecture - Mission Ops.md              (code : META_SPECS_ARCHITECTURE_MO)
    Interfaces Brain↔Twin↔MO.md                (code : META_INTERFACES_LBP)

  40 - Normer/
    Règles intrinsèques - LBP.md               (code : META_RULES_LBP)
    Codification - LBP.md                      (code : META_CODIFICATION_LBP)
    Charte rédactionnelle - LBP.md             (code : META_CHARTE_REDACTIONNELLE_LBP)
    Charte graphique - LBP.md                  (code : META_CHARTE_GRAPHIQUE_LBP)
    Sécurité & RGPD - LBP.md                   (code : META_SECURITY_RGPD_LBP)
    Quality control - Brain.md                 (code : META_QC_BRAIN)
    Quality control - Twin.md                  (code : META_QC_TWIN)
    Quality control - Mission Ops.md           (code : META_QC_MO)

  50 - Opérer/
    Workflows opérationnels - LBP.md           (code : META_WORKFLOWS_LBP)
    Règles de propagation - LBP.md             (code : META_PROPAGATION_RULES_LBP)

  90 - États & audits/
    AUDIT_REPORTS/

  99 - Archives/
    (anciennes versions des docs refondus, suffixées selon R-053)
```

**Conventions résumées (R-064)** :
- **Filename = nom canonique humain** (identique au `title:` frontmatter et au `Nom canonique` Notion). Pas de code dans le filename.
- **Code** : préfixe `META_` pour tous les docs méta indexés.
- **Scope dans le code** : suffix `_LBP` pour transverse (Brain + Twin + MO), suffix `_BRAIN` / `_TWIN` / `_MO` pour domaine spécifique (jamais les deux).
- **Wikilinks systématiques** (cf. C-024) : les renvois inter-docs utilisent `[[Nom humain]]`, ex. `[[Constitution des docs méta - LBP]]`. Aliases dans frontmatter pour résilience au rename via Obsidian UI.

---

## Annexe C — Trajectoire workflows → prompts/agents/logic blocks

> **Note prospective** (vision long terme, à confirmer en v1.0 après refonte des agents).

Les workflows actuels (`Workflows opérationnels - LBP`, `Règles de propagation - LBP`) sont des **artefacts transitoires**. Ils servent aujourd'hui à formaliser les opérations standardisées de manière lisible humain ET agent, en l'absence d'agents complets opérationnels.

### Trajectoire pressentie

- **Aujourd'hui** : workflows en docs Markdown, pilotés humainement (Leonard) ou par agent simple (Claude en collaboration session).
- **Étape intermédiaire** : workflows Twin déjà partiellement couverts par les prompts / system prompts / logic blocks de **twin architect** (en cours de stabilisation).
- **Étape cible** : quand **brain architect** sera complet (system prompt + prompts maîtres + logic blocks), une partie significative des workflows Brain (`META_WORKFLOWS_LBP`) migrera vers cet outillage opérationnel. Le doc Markdown deviendra alors :
  - soit un **catalogue de référence court** (avec pointeurs vers les logic blocks effectifs),
  - soit **archivé** (R-053) si totalement remplacé par les agents.

### Implication pratique

Ne pas surinvestir dans `META_WORKFLOWS_LBP` au-delà du nécessaire. Garder le doc clean et factuel, mais éviter de le sur-architecturer en sachant qu'il aura à terme un autre médium. Idem pour `META_PROPAGATION_RULES_LBP` (cheat sheet WF-008).

### Articulation à formaliser

Une décision architecturale dans `[[Décisions architecturales LBP]]` tranchera, quand brain architect sera proche de l'opérationnel : (a) garder les workflows Markdown comme catalogue de référence + outillage agent en parallèle ; ou (b) archiver les workflows Markdown et basculer entièrement sur l'outillage agent.

---

## Annexe B — Articulations clés

- **Préfixe code `META_`** : D-024 — préfixe `META_` pour tous les codes des docs méta indexés.
- **Naming des docs méta** : R-064 — code `META_<TOKEN>_<SCOPE>`, nom canonique humain `<Type lisible> - <Scope>`, suffix `_LBP` pour scope transverse / `_BRAIN` / `_TWIN` / `_MO` pour domaine spécifique.
- **5 fonctions systémiques** : taxo `[[META.FUNCTION]]` (D-025).
- **BDD `Templates Brain`** : D-026 — BDD séparée des docs méta indexant les templates d'instanciation (consommée par brain architect). Distincte de la BDD `Templates de Bricks` (consommée par kontext).
- **Anti-pattern transclusion `![[]]`** : C-023 — pas de transclusion dans les docs canoniques.
- **Pattern wikilinks `[[]]`** : C-024 — utiliser systématiquement les wikilinks pour les renvois inter-docs (résilience au rename).
- **Backlinks bidirectionnels Obsidian** : C-025 — relations bidirectionnelles natives, à exploiter pour découvrir « qui me cite ».
