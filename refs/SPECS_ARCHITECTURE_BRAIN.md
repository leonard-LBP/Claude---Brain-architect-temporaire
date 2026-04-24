# SPECS — Architecture Brain LBP

> Source de vérité : schémas Notion live, fetchés le 2026-04-07.
> Ce fichier documente l'écosystème complet des BDD Brain et leurs interconnexions.

---

## 1. Vue d'ensemble

Le Brain est la **couche de gouvernance documentaire de LBP**. Il contient les 11 BDD Notion qui définissent le vocabulaire, les méthodes, les prompts, les templates et les règles qui régissent l'ensemble de l'écosystème (Digital Twin, Mission Ops, etc.).

Le Brain est **autonome et indépendant** — aucune relation Notion ne le lie directement aux BDD Digital Twin ou Mission Ops. L'héritage se fait via les **Manuels de BDD** qui documentent les schémas des BDD opérationnelles.

### Principes fondamentaux

1. **Le doc Markdown (Drive) est la source de vérité.** Les propriétés Notion sont toujours dérivées du contenu du doc, jamais l'inverse. Cela garantit zéro asymétrie entre le doc et son index.

2. **Tout doc Brain est généré à partir d'un template.** Les templates de sortie (indexés dans Docs méta LBP) servent de moule pour chaque catégorie. L'agent utilise le template pour produire le doc, puis le doc pour remplir les propriétés Notion.

3. **Cycle de vie universel** : Template (Docs méta) → génération doc Markdown → validation humaine → rangement Drive → indexation BDD Notion (propriétés dérivées du doc) → création des relations → propagation d'impacts.

4. **Deux hubs** dans le graphe : **Glossaire LBP** (hub sémantique — un concept peut rayonner vers notes de concept, méthodes, manuels de BDD) et **Prompts LBP** (hub d'exécution — orchestre méthodes, logic blocks, templates, outils, docs méta, agents).

### Organisation en zones

```
ADMIN BRAIN (gouvernance du Brain lui-même)
  └── Docs méta LBP

CORE BRAIN (concepts + référentiels)
  ├── Glossaire LBP
  ├── Registre des notes de concept
  └── Registre des taxonomies

MOTOR BRAIN (exécution + orchestration)
  ├── Prompts LBP              ← HUB CENTRAL (6 relations)
  ├── Registre des logic blocks
  ├── Méthodes LBP
  ├── Templates de Bricks
  ├── Agents LBP
  └── Outils externes

CROSS-ZONE (pont Brain → systèmes opérationnels)
  └── Manuels de BDD
```

---

## 2. Propriétés communes

Toutes les BDD Brain partagent un socle commun :

| Propriété | Type | Description |
|-----------|------|-------------|
| `Nom canonique` | title | Intitulé lisible et stable |
| `Code unique` | text | Identifiant MAJUSCULES stable (format variable par BDD) |
| `Statut de l'objet` | select | `Brouillon` / `Validé` / `À revoir` / `Archivé` |
| `Created Date` | created_time ou date | Date de création automatique |
| `Last Updated Date` | last_edited_time ou date | Date de dernière modification |

> Les 11 BDD utilisent les mêmes valeurs exactes : `Brouillon`, `Validé`, `À revoir`, `Archivé`.

### Propriété "Lien source"

Chaque BDD a un champ URL pointant vers le document Markdown source sur Google Drive :

| BDD | Nom de la propriété | Type |
|-----|---------------------|------|
| Docs méta | `Lien doc méta (source)` | url |
| Glossaire | *(pas de lien source direct — via rollup Notes de concept)* | — |
| Notes de concept | `Lien note concept (source)` | url |
| Taxonomies | `Lien doc taxonomie (source)` | url |
| Prompts | `Lien prompt (source)` | url |
| Logic blocks | `Lien Drive du logic block` | **text** (pas url !) |
| Méthodes | `Lien méthode (source)` | url |
| Templates de Bricks | `Lien vers fichier template (source)` | url |
| Agents | *(pas de lien source)* | — |
| Outils externes | `Lien source` | url |
| Manuels de BDD | `Lien vers le doc du manuel` | url |

> **Anomalie** : Logic blocks stocke le lien Drive en `text` au lieu de `url`.

---

## 3. Catalogue des BDD

---

### 3.1 Docs méta LBP

**Zone** : ADMIN BRAIN
**Collection ID** : `64e99b5d-88bc-474e-b94f-b33af5700423`
**Notion URL** : https://www.notion.so/6b6acdc61ade4c6bbd7f2da23087ea68
**Rôle** : Règles de gouvernance, conventions de nommage, workflows, QA du Brain lui-même.
**Format Code unique** : `META-[TOKEN]_[TOKEN]`

#### Propriétés spécifiques

| Propriété | Type | Valeurs / Description |
|-----------|------|-----------------------|
| `Famille (Doc méta)` | select | Naming conventions, Quality QA, Charts, Workflows playbooks, Tooling rules, Template rules, Data model rules, Security privacy |
| `Description` | text | 3-10 lignes |
| `Périmètre d'application` | text | Où s'applique la doctrine |
| `Quand l'appliquer` | text | Déclencheurs + À faire + À éviter |
| `Règles clés (overview)` | text | 3-12 bullets |
| `Objets encadrés (overview)` | text | 3-10 items |
| `Mots-clés de déclenchement` | text | Séparés par `;` |
| `Usages IA potentiels` | text | 3-7 usages |
| `Valeur ajoutée LBP` | text | |
| `Aliases` | text | Séparés par `;` |

#### Relations

| Propriété | Cible | Direction |
|-----------|-------|-----------|
| `est utilisé dans (Prompts LBP)` | Prompts LBP | ← miroir de `utilise (Docs méta LBP)` |

#### Rollups

- Agents mobilisés (via prompts)
- Méthodes mobilisées (via prompts)
- Outils externes mobilisés (via prompts)
- Templates de bricks mobilisés (via prompts)

---

### 3.2 Glossaire LBP

**Zone** : CORE BRAIN
**Collection ID** : `349d8191-1f74-418d-acdd-9d78fbd4ac28`
**Notion URL** : https://www.notion.so/2f2a5381131649279b73116a1fe4a1c0
**Rôle** : Vocabulaire canonique LBP — chaque concept a une définition, un domaine et des règles d'usage.
**Format Code unique** : `CPT-TOKEN` ou `CPT-TOKEN1_TOKEN2`

#### Propriétés spécifiques

| Propriété | Type | Valeurs / Description |
|-----------|------|-----------------------|
| `Définition` | text | 3-10 lignes, sens LBP |
| `Type de concept` | select | Concept LBP, Concept externe, Produit-marque |
| `Domaine d'usage` | multi_select | Core, Motor |
| `BDD concernées (texte)` | text | Noms exacts de BDD Notion, séparés par `;` |
| `Mots clés` | text | 5-15 mots-clés séparés par `;` |
| `Règles d'usage et pièges` | text | Bon usage / Mauvais usage / Confusions / Signaux |
| `est lié à (concepts)` | **text** | Concepts connexes (pas une relation !) |
| `Équivalent langage courant` | text | Traduction non-jargon |
| `Notes` | text | |
| `Aliases` | text | Séparés par `;` |
| `Usages IA potentiels` | text | 3-7 usages |
| `Valeur ajoutée LBP` | text | |

> **Anomalie** : `est lié à (concepts)` est un champ **texte**, pas une relation Notion. Les liens inter-concepts ne sont pas matérialisés structurellement.

#### Relations

| Propriété | Cible | Direction |
|-----------|-------|-----------|
| `est documenté par (notes de concept)` | Notes de concept | → miroir : `documente (Glossaire LBP)` |
| `est mis en oeuvre par (méthodes LBP)` | Méthodes LBP | → (pas de miroir visible côté Méthodes) |
| `est modélisé par (Manuels de BDD)` | Manuels de BDD | → (pas de miroir visible côté Manuels) |

#### Rollups

- Lien note concept (rollup) — depuis Notes de concept

---

### 3.3 Registre des notes de concept

**Zone** : CORE BRAIN
**Collection ID** : `4bd4e3a2-eda0-4ba4-8970-4ed1e4a30f7a`
**Notion URL** : https://www.notion.so/6190771e19564bcb83905a89928271d4
**Rôle** : Fiches détaillées des concepts LBP — chaque note documente un terme du Glossaire en profondeur.
**Format Code unique** : `CPT-TOKEN` ou `CPT-TOKEN1_TOKEN2` (aligné avec Glossaire)

#### Propriétés spécifiques

| Propriété | Type | Valeurs / Description |
|-----------|------|-----------------------|
| `Lien note concept (source)` | url | Document Markdown source (Drive) |

> BDD très **légère** en propriétés — le contenu vit dans le document Drive lié.

#### Relations

| Propriété | Cible | Direction |
|-----------|-------|-----------|
| `documente (Glossaire LBP)` | Glossaire LBP | ← miroir de `est documenté par` |

#### Rollups

- Domaine(s) d'usage (rollup) — hérité du Glossaire via la relation

---

### 3.4 Registre des taxonomies

**Zone** : CORE BRAIN
**Collection ID** : `421c715c-f69e-40b8-891a-07903e134f27`
**Notion URL** : https://www.notion.so/8632ab091829489e9e36ea4fa345420e
**Rôle** : Registre de toutes les taxonomies (listes de valeurs contrôlées) utilisées dans les BDD Notion.
**Format Code unique** : `NAMESPACE.FAMILLE.LBP`

#### Propriétés spécifiques

| Propriété | Type | Valeurs / Description |
|-----------|------|-----------------------|
| `Description (source)` | text | Intention, règles d'usage, exclusions |
| `Description courte (usage)` | text | 1 phrase résumé |
| `Lien doc taxonomie (source)` | url | Mini-doc Markdown (Drive) |
| `Nature sémantique` | select | hierarchical, ordinal, nominal, binary |
| `Ouverture` | select | ouverte, fermée |
| `Niveaux autorisés` | multi_select | category, subdomain, taxon |
| `Mode de sélection` | multi_select | mono, multi |
| `Aliases` | text | Séparés par `;` |

#### Relations

| Propriété | Cible | Direction |
|-----------|-------|-----------|
| `est utilisée dans (manuels de BDD)` | Manuels de BDD | ↔ miroir : `utilise (taxonomies)` |

#### Rollups

- Domaine(s) d'usage (via manuels) — hérité des Manuels de BDD

---

### 3.5 Prompts LBP

**Zone** : MOTOR BRAIN
**Collection ID** : `307c5df7-8d00-4973-97e2-4ae1f1bb5931`
**Notion URL** : https://www.notion.so/92903d0d35044b3ba899a2cc550463fa
**Rôle** : **HUB CENTRAL du Brain** — registre de tous les prompts LBP avec 6 relations vers d'autres BDD.
**Format Code unique** : `PROMPT-[DOMAINE]_[SUJET]`

#### Propriétés spécifiques

| Propriété | Type | Valeurs / Description |
|-----------|------|-----------------------|
| `Description` | text | 3-10 lignes |
| `Objectif opérationnel` | text | 1 phrase à l'infinitif |
| `Rôle architectural` | select | System prompt, Prompt d'Exécution, Prompt maître, Template de Prompt, Prompt de fonction, Autre |
| `Type de prompt` | select | Génération de brick, Contrôle qualité, Routage / sélection, Déduplication / consolidation, Création de relations, Gestion Digital Twin, Idéation assistée, Conversion / rendu |
| `Mode du prompt` | select | Simple, Itératif |
| `Domaine(s) d'usage` | multi_select | core, motor, digital twin, mission ops |
| `Entrées attendues` | text | Structure : Indispensables / Recommandées / Bonus |
| `Règles d'usage` | text | Structure : Objectif / Quand / Ne pas / Entrées / Sortie / Garde-fous / Validation |
| `Lien prompt (source)` | url | Document Markdown (Drive) |
| `Code registry` | text | Localisation dans le code plateforme |
| `Autoriser recherche web` | select | Oui, Non, À valider |
| `Environnement(s) de déploiement` | multi_select | *(vide actuellement)* |
| `Version(s) de plateforme` | multi_select | *(vide actuellement)* |
| `Statut de déploiement` | select | *(options vides)* |
| `actif` | checkbox | En utilisation sur la plateforme |
| `Aliases` | text | |
| `Usages IA potentiels` | text | |
| `Valeur ajoutée LBP` | text | |

#### Relations (6 — le plus connecté du Brain)

| Propriété | Cible | Direction |
|-----------|-------|-----------|
| `est utilisé par (Agents LBP)` | Agents LBP | ↔ miroir : `utilise (Prompts LBP)` |
| `utilise (Méthodes LBP)` | Méthodes LBP | ↔ miroir : `est utilisé dans (Prompts LBP)` |
| `utilise (Logic blocks)` | Logic blocks | ↔ miroir : `est utilisé dans (Prompts LBP)` |
| `utilise (Docs méta LBP)` | Docs méta | ↔ miroir : `est utilisé dans (Prompts LBP)` |
| `utilise (Outils externes)` | Outils externes | ↔ miroir : `est utilisé dans (Prompts LBP)` |
| `utilise (Templates de bricks)` | Templates de Bricks | ↔ miroir : `est utilisé dans (Prompts LBP)` |

#### Rollups

- Familles bricks (via templates)
- Familles docs méta (via docs méta)
- Familles méthodes (via méthodes)
- Familles outils (via outils)

---

### 3.6 Registre des logic blocks

**Zone** : MOTOR BRAIN
**Collection ID** : `101e108f-ec56-408d-8ebf-3877064c7fbe`
**Notion URL** : https://www.notion.so/51646fc79f7a4324b83bf1d0ae9a8732
**Rôle** : Modules de raisonnement réutilisables, chacun ciblant une opération sur une BDD spécifique.
**Format Code unique** : `LGBLK_[OPERATION]_[CIBLE]`

#### Propriétés spécifiques

| Propriété | Type | Valeurs / Description |
|-----------|------|-----------------------|
| `Description` | text | 3-10 lignes |
| `Opération` | select | Extract, Dédoublonnage, Découverte, Refactor, Relations Maker inter-BDD, Relations Maker intra-BDD, Complétion, Transformation, Préqualification |
| `Lien Drive du logic block` | **text** | URL Drive (anomalie : devrait être `url`) |
| `Aliases` | text | |
| `est utilisé dans (Prompts LBP) [texte]` | text | Jumelle texte manuelle (en attendant conversion) |
| `s'applique à (Manuels de BDD) [texte]` | text | Jumelle texte manuelle (en attendant conversion) |
| `Usages IA potentiels` | text | |
| `Valeur ajoutée LBP` | text | |

#### Relations

| Propriété | Cible | Direction |
|-----------|-------|-----------|
| `est utilisé dans (Prompts LBP)` | Prompts LBP | ↔ miroir : `utilise (Logic blocks)` |
| `s'applique à (Manuels de BDD)` | Manuels de BDD | → (pas de miroir visible côté Manuels) |

#### Rollups

- Nb prompts liés
- Nb manuels adressés

---

### 3.7 Méthodes LBP

**Zone** : MOTOR BRAIN
**Collection ID** : `df08a0a0-9e9a-4b39-949a-eb78a5bcb514`
**Notion URL** : https://www.notion.so/ae1b2407129d48c6837f5e12dc22f2e6
**Rôle** : Méthodes d'analyse, de structuration et de production utilisées par les agents et consultants.
**Format Code unique** : `MET-[TOKEN]_[TOKEN]`

#### Propriétés spécifiques

| Propriété | Type | Valeurs / Description |
|-----------|------|-----------------------|
| `Description` | text | 3-10 lignes |
| `Objectif opérationnel` | text | 1 phrase à l'infinitif |
| `Famille (Méthode)` | multi_select | Collecte & entretien, Structuration & modélisation, Analyse & diagnostic, Synthèse & formalisation, Recommandation & décision, Planification & roadmap, Qualité & QA, Gouvernance écosystème, Publication & communication |
| `Lien méthode (source)` | url | Document Markdown (Drive) |
| `Entrées attendues` | text | Structure Indispensables / Recommandées / Bonus |
| `Entrées attendues - MUST` | text | Types d'entrées indispensables |
| `Entrées attendues - SHOULD` | text | Types recommandées |
| `Entrées attendues - NICE` | text | Types optionnelles |
| `Sorties attendues (nature)` | text | |
| `Déroulé (overview)` | text | 3-6 lignes |
| `Quand l'utiliser` | text | 3-7 situations |
| `Règles d'usage` | text | Structure imposée |
| `Erreurs fréquentes / anti-patterns` | text | 3-7 erreurs |
| `Variantes & adaptations` | text | |
| `Version de la méthode (option)` | text | Ex: `0.1.0` |
| `Aliases` | text | |
| `Usages IA potentiels` | text | |
| `Valeur ajoutée LBP` | text | |

#### Relations

| Propriété | Cible | Direction |
|-----------|-------|-----------|
| `est utilisé dans (Prompts LBP)` | Prompts LBP | ↔ miroir : `utilise (Méthodes LBP)` |

#### Rollups

- Outils externes mobilisés (via prompts)
- Templates de bricks mobilisés (via prompts)

---

### 3.8 Templates de Bricks

**Zone** : MOTOR BRAIN
**Collection ID** : `fefc8f39-e125-45fc-b6b4-f2e79421c6c8`
**Notion URL** : https://www.notion.so/9ffb4670e49f4310a7150fbf48df103d
**Rôle** : Gabarits de production pour les bricks (livrables intermédiaires et finaux).
**Format Code unique** : `TPL-BRICK_{BRICK_CODE}`

#### Propriétés spécifiques

| Propriété | Type | Valeurs / Description |
|-----------|------|-----------------------|
| `Description` | text | 3-10 lignes |
| `Famille de brick générée` | select | Profil, Meeting, Compte-rendu, Analyse, Livrable, Correspondance, Sources, Glossaire |
| `Lien vers fichier template (source)` | url | Fichier template Markdown (Drive) |
| `Aliases` | text | |
| `Usages IA potentiels` | text | |
| `Valeur ajoutée LBP` | text | |

> Statuts harmonisés avec les autres BDD : `Brouillon`, `À revoir`, `Validé`, `Archivé`.

#### Relations

| Propriété | Cible | Direction |
|-----------|-------|-----------|
| `est utilisé dans (Prompts LBP)` | Prompts LBP | ↔ miroir : `utilise (Templates de bricks)` |

#### Rollups

- Méthodes (via Prompts)
- Outils externes (via Prompts)

---

### 3.9 Agents LBP

**Zone** : MOTOR BRAIN
**Collection ID** : `82a8a779-1ad0-4add-9322-1ba090ec09a2`
**Notion URL** : https://www.notion.so/885d548d50e7455384422d3fdf9c6069
**Rôle** : Registre des agents IA LBP — rôle, périmètre, prompts mobilisés.
**Format Code unique** : `AGENT_ROLE_DOMAINE`

#### Propriétés spécifiques

| Propriété | Type | Valeurs / Description |
|-----------|------|-----------------------|
| `Description` | text | 3-10 lignes |
| `Famille (Agent)` | select | Analyse, Génération de bricks, Mission ops, Gestion Digital Twin, Gouvernance écosystème, Marketing/communication, Admin LBP |
| `Fonctions (overview)` | text | 3-7 bullets, verbes à l'infinitif |
| `Garde-fous (overview)` | text | 3-10 garde-fous |
| `Périmètre et exclusions (overview)` | text | |
| `Qualité et limites (overview)` | text | |
| `Aliases` | text | |
| `Usages IA potentiels` | text | |
| `Valeur ajoutée LBP` | text | |

#### Relations

| Propriété | Cible | Direction |
|-----------|-------|-----------|
| `utilise (Prompts LBP)` | Prompts LBP | ↔ miroir : `est utilisé par (Agents LBP)` |

#### Rollups

- Docs méta mobilisés (via prompts)
- Méthodes mobilisées (via prompts)
- Outils externes mobilisés (via prompts)
- Templates de bricks mobilisés (via prompts)

---

### 3.10 Outils externes

**Zone** : MOTOR BRAIN
**Collection ID** : `347a3db7-477f-4d60-9f72-496cb1fdc574`
**Notion URL** : https://www.notion.so/0b8d11bc0efa425593767208c4ffbbbe
**Rôle** : Outils et formats standards utilisés par les prompts pour produire des sorties exploitables.
**Format Code unique** : `OUT-[TOKEN]_[TOKEN]`

#### Propriétés spécifiques

| Propriété | Type | Valeurs / Description |
|-----------|------|-----------------------|
| `Description` | text | 3-10 lignes |
| `Nature` | select | Outil, Format standard |
| `Famille (Outil externe)` | select | Visualisation, Presentation, Document, Data, Automation, Collaboration, Communication |
| `Lien source` | url | Documentation officielle ou ressource interne |
| `Entrees attendues` | text | Structure Indispensables / Recommandées / Bonus |
| `Sorties produites` | text | 1-5 lignes |
| `Mode d'emploi (IA)` | text | Objectif / Inputs / Output / Validation / Erreurs |
| `Gabarit de sortie (IA)` | text | Template copiable avec placeholders |
| `Aliases` | text | |
| `Usages IA potentiels` | text | |
| `Valeur ajoutee LBP` | text | **(anomalie : pas d'accent sur "ajoutée")** |

#### Relations

| Propriété | Cible | Direction |
|-----------|-------|-----------|
| `est utilisé dans (Prompts LBP)` | Prompts LBP | ↔ miroir : `utilise (Outils externes)` |

#### Rollups

- Agents mobilisés (via prompts)
- Méthodes mobilisées (via prompts)
- Templates de bricks mobilisés (via prompts)

---

### 3.11 Manuels de BDD

**Zone** : CROSS-ZONE (pont Brain → systèmes opérationnels)
**Collection ID** : `4d8f54e7-ce93-483a-b886-bf9edc96fb0c`
**Notion URL** : https://www.notion.so/698c6c7809ae4cf6ba6bf20346459114
**Rôle** : Documentation des schémas des BDD Notion — le pont entre le Brain et les systèmes opérationnels (Digital Twin, Mission Ops).
**Format Code unique** : `DBMAN_NOM_BDD_CANON`

#### Propriétés spécifiques

| Propriété | Type | Valeurs / Description |
|-----------|------|-----------------------|
| `Description` | text | 3-8 lignes |
| `Nom de la BDD Notion` | text | Libellé exact de la BDD décrite |
| `Domaine(s) d'usage` | multi_select | Core, Motor, Digital Twin, Mission Ops |
| `Type fonctionnel (BDD décrite)` | select | Catalogue, Registre, Templates, DT - extraction directe, DT - pivot de qualification, DT - post-traitement, DT - sandbox, Mission Ops |
| `Lien vers la BDD Notion` | url | URL de la BDD décrite |
| `Lien vers le doc du manuel` | url | Document Markdown (Drive) |
| `Aliases` | text | |
| `Usages IA potentiels` | text | |
| `Valeur ajoutée LBP` | text | |

#### Relations

| Propriété | Cible | Direction |
|-----------|-------|-----------|
| `utilise (taxonomies)` | Taxonomies | ↔ miroir : `est utilisée dans (manuels de BDD)` |

---

## 4. Graphe de relations inter-BDD

### 4.1 Diagramme

```
                        ┌──────────────┐
                        │  Docs méta   │
                        │    LBP       │
                        └──────┬───────┘
                               │ est utilisé dans
                               ▼
┌───────────┐    ┌─────────────────────────────┐    ┌───────────┐
│  Agents   │◄──►│        PROMPTS LBP          │◄──►│  Logic    │
│   LBP     │    │      (HUB CENTRAL)          │    │  blocks   │
└───────────┘    └──┬──────┬──────┬──────┬──────┘    └─────┬─────┘
                    │      │      │      │                 │
                    ▼      ▼      ▼      ▼                 ▼
              ┌─────────┐ ┌──────────┐ ┌──────────┐  ┌──────────┐
              │Méthodes │ │Templates │ │  Outils  │  │ Manuels  │
              │  LBP    │ │de Bricks │ │ externes │  │  de BDD  │
              └─────────┘ └──────────┘ └──────────┘  └────┬─────┘
                                                          │
                                                          ▼
┌───────────┐    ┌──────────────┐    ┌──────────────┐ ┌──────────┐
│Glossaire  │───►│    Notes     │    │  Taxonomies  │◄┘
│   LBP     │    │  de concept  │    │              │
└──┬────────┘    └──────────────┘    └──────────────┘
   │
   ├───► Méthodes LBP (est mis en oeuvre par)
   └───► Manuels de BDD (est modélisé par)
```

### 4.2 Liste exhaustive des relations Notion

| # | BDD Source | Propriété | BDD Cible | Propriété miroir | Bidirectionnelle |
|---|-----------|-----------|-----------|-----------------|------------------|
| 1 | Prompts LBP | `est utilisé par (Agents LBP)` | Agents LBP | `utilise (Prompts LBP)` | Oui |
| 2 | Prompts LBP | `utilise (Méthodes LBP)` | Méthodes LBP | `est utilisé dans (Prompts LBP)` | Oui |
| 3 | Prompts LBP | `utilise (Logic blocks)` | Logic blocks | `est utilisé dans (Prompts LBP)` | Oui |
| 4 | Prompts LBP | `utilise (Docs méta LBP)` | Docs méta | `est utilisé dans (Prompts LBP)` | Oui |
| 5 | Prompts LBP | `utilise (Outils externes)` | Outils externes | `est utilisé dans (Prompts LBP)` | Oui |
| 6 | Prompts LBP | `utilise (Templates de bricks)` | Templates de Bricks | `est utilisé dans (Prompts LBP)` | Oui |
| 7 | Glossaire | `est documenté par (notes de concept)` | Notes de concept | `documente (Glossaire LBP)` | Oui |
| 8 | Glossaire | `est mis en oeuvre par (méthodes LBP)` | Méthodes LBP | *(pas de miroir visible)* | Partielle |
| 9 | Glossaire | `est modélisé par (Manuels de BDD)` | Manuels de BDD | *(pas de miroir visible)* | Partielle |
| 10 | Taxonomies | `est utilisée dans (manuels de BDD)` | Manuels de BDD | `utilise (taxonomies)` | Oui |
| 11 | Logic blocks | `s'applique à (Manuels de BDD)` | Manuels de BDD | *(pas de miroir visible)* | Partielle |

> **3 relations partiellement bidirectionnelles** (8, 9, 11) : le miroir n'est pas exposé comme propriété visible côté cible. Notion gère la bidirectionnalité en interne, mais l'absence de propriété miroir nommée rend ces relations moins exploitables.

### 4.3 Chaînes de propagation

Quand un document Brain change, les impacts se propagent le long du graphe :

```
Glossaire ──► Notes de concept
Glossaire ──► Méthodes LBP ──► Prompts LBP ──► Agents LBP
Glossaire ──► Manuels de BDD ──► Taxonomies
Taxonomies ──► Manuels de BDD
Docs méta ──► Prompts LBP ──► tout le Motor Brain
Logic blocks ──► Prompts LBP + Manuels de BDD
Templates ──► Prompts LBP
Outils externes ──► Prompts LBP
Méthodes ──► Prompts LBP
```

**Profondeur max recommandée** : 2 niveaux (pour éviter les boucles de propagation).

---

## 5. Anomalies et points d'attention

| # | BDD | Anomalie | Sévérité |
|---|-----|----------|----------|
| 1 | Logic blocks | `Lien Drive du logic block` est **text** au lieu de **url** | Faible — empêche la validation d'URL native |
| 2 | Outils externes | `Valeur ajoutee LBP` sans accent | Faible — cosmétique |
| 3 | Glossaire | `est lié à (concepts)` est **text**, pas une relation | Moyenne — liens non structurés entre concepts |
| 4 | Logic blocks | Champs texte `[texte]` doublons des relations | Faible — héritage pré-conversion |

---

## 6. Stockage technique

### Pinecone
- **Index** : `lbp-internal`
- **Namespace** : unique (pas multi-tenant pour le Brain)
- Contient les embeddings de toutes les entrées Brain

### Neo4j
- **Scope** : `tenant_slug = "lbp-internal"`
- Contient le graphe de relations entre entrées Brain
- Reconstruit intégralement lors de chaque régénération

### Redis
- **Clé** : `brain:entries` — cache des entrées Brain
- Ontology snapshots et stats de régénération

### Pipeline de régénération
- **Fichier** : `packages/lbp-core/src/lbp_core/features/maintenance/flows/regen_lbp_brain.py`
- **Constantes** : `LBP_INTERNAL_SLUG = "lbp-internal"`, `DB_NOTES_BRAIN_PAGE_ID = "20be1a18653c8079aeb1e01047fddddd"`
- **Processus** : ontologie discovery → vectorisation Pinecone → reconstruction graphe Neo4j
- **Limitation** : full rebuild uniquement, pas de sync incrémental

---

## 7. Frontend (état actuel)

### Pages Brain dans Query Studio
| Page (subPage) | Composant | État |
|----------------|-----------|------|
| `apercu` | `BrainOverview.tsx` | Fonctionnel (read-only) |
| `glossaire` | `GlossaireHub.tsx` | Fonctionnel (read-only) |
| `catalogue` | `BrainCatalogue.tsx` | Fonctionnel (read-only) |
| `agents_prompts` | `AgentsPromptsHub.tsx` | Fonctionnel (read-only) |
| `brain_studio` | `BrainStudio.tsx` → `BrainStudioChat.tsx` | **100% MOCK** (`buildMockReply()`) |
| `prompt_lab` | `PromptLab.tsx` | Fonctionnel (read-only) |
| `maintenance` | *(inline dans BrainSection)* | **Stub vide** |
| `brain_regenerer` | `BrainRegen` (dans BrainSection) | Fonctionnel (admin SSE) |
| `brain_admin` | `BrainAdmin.tsx` | Fonctionnel (admin) |

### Fichiers clés
- Routeur principal : `apps/query-studio/src/components/sections/BrainSection.tsx`
- Navigation : `apps/query-studio/src/components/shell/Rail2.tsx` (lignes 89-124)
- Studio mock : `apps/query-studio/src/components/brain/BrainStudioChat.tsx`
- Sessions localStorage : `apps/query-studio/src/hooks/useBrainStudioSessions.ts`

---

## 8. Référence rapide des Collection IDs

| BDD | Collection ID |
|-----|--------------|
| Docs méta LBP | `64e99b5d-88bc-474e-b94f-b33af5700423` |
| Glossaire LBP | `349d8191-1f74-418d-acdd-9d78fbd4ac28` |
| Notes de concept | `4bd4e3a2-eda0-4ba4-8970-4ed1e4a30f7a` |
| Taxonomies | `421c715c-f69e-40b8-891a-07903e134f27` |
| Prompts LBP | `307c5df7-8d00-4973-97e2-4ae1f1bb5931` |
| Logic blocks | `101e108f-ec56-408d-8ebf-3877064c7fbe` |
| Méthodes LBP | `df08a0a0-9e9a-4b39-949a-eb78a5bcb514` |
| Templates de Bricks | `fefc8f39-e125-45fc-b6b4-f2e79421c6c8` |
| Agents LBP | `82a8a779-1ad0-4add-9322-1ba090ec09a2` |
| Outils externes | `347a3db7-477f-4d60-9f72-496cb1fdc574` |
| Manuels de BDD | `4d8f54e7-ce93-483a-b886-bf9edc96fb0c` |

**Page maître Brain** : `20be1a18653c8079aeb1e01047fddddd`
