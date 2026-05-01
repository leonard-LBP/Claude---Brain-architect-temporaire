---
# === Identité ===
title: "Doctrine Digital Twin - Macro-architecture, chaînes de valeur et logique analytique"
doc_type: doc_meta
code: "CHRT_DOCTRINE_TWIN"

# === Méta-gouvernance ===
version: "4.0"
template_code: "CHRT"
template_version: "1.0"
created_at: "22-04-2026"
updated_at: "01-05-2026"
status: "Validé"
scope: "LBP"

# === Spec d'usage ===
summary: "Doctrine détaillée du Digital Twin LBP : régimes de structuration des données, chaînes de transformation de la connaissance (15 chaînes détaillées), moteurs analytiques (11 lectures), traversées à forte valeur (11 traversées), gouvernance Twin (qualité, traçabilité, merge/consolidation/promotion, sandbox→officiel)."
purpose: "Servir de doctrine narrative détaillée pour le Digital Twin. Complémentaire à SPECS_ARCHITECTURE_TWIN_LBP (modèle conceptuel synthétique) et DOCTRINE_LBP (doctrines transverses des 3 domaines)."
tags:
  - doc_meta
  - doctrine
  - digital_twin
  - lbp
  - regimes_de_structuration
  - chaines_de_transformation
  - gouvernance_twin
---

> **Scope** : 🟦 LBP - Bundle écosystème (durable, indexé dans BDD `Docs méta` du Brain).
> **Historique** : ce doc est dérivé du *Panorama V2 v3* du 22-04-2026 (archivé sous `Architecture data\00 - Docs méta\Doctrines & playbooks\00 - archives\Panorama V2 - ... v3 (archivé v3 le 01-05-2026).md`). Il a été renommé `DOCTRINE_TWIN_LBP.md` et **mis à jour** au 01-05-2026 pour intégrer les évolutions doctrinales postérieures au 22-04 (D-019 Brain unifié, D-021 3 agents, D-022 frontmatters Twin/MO différenciés, D-023 MO co-égal + stack Notion/Supabase, R-054 codification universelle, R-055/056/058/059 hygiène d'écriture).
> **Place dans le bundle** : doctrine **détaillée Twin** (vs `DOCTRINE_LBP.md` = doctrines **transverses** des 3 domaines). Pour la vue macro 3 ensembles voir `PANORAMA_LBP.md`. Pour les specs schématiques voir `SPECS_ARCHITECTURE_TWIN_LBP.md`.

---

# 1) Objet du document

## 1.1 Finalité de la doctrine

Ce document fournit une vue d'ensemble **autonome, exhaustive et doctrinale** du Digital Twin LBP.

Il sert à :
- clarifier ce qu'est le Digital Twin,
- présenter l'ensemble de ses BDD dans une **carte canonique unique**,
- expliquer comment la donnée s'y transforme en lecture systémique,
- rendre lisibles les grandes chaînes de valeur du Twin,
- distinguer les différents niveaux de preuve, de structuration, d'analyse et d'action,
- fournir un cadre de référence commun pour la conception, la maintenance et l'interrogation du Twin.

## 1.2 Ce que ce document couvre

Cette doctrine couvre :
- les **BDD** composant l'architecture du Twin,
- les **objets** qu'elles portent,
- leurs **régimes architecturaux**,
- leurs **modes d'alimentation**,
- leur **régime relationnel**,
- leur **valeur systémique**,
- et les **familles de fonctions analytiques** qu'elles rendent possibles.

## 1.3 Ce que ce document ne remplace pas

Cette doctrine ne remplace pas :
- les WR-RD (Write Rules / Read Keys),
- les manuels complets de BDD,
- les taxonomies,
- les notes de concept,
- les docs du bundle (`PANORAMA_LBP`, `SPECS_ARCHITECTURE_TWIN_LBP`, `DOCTRINE_LBP`, `RULES_LBP`, `DECISIONS_LBP`).

Elle ne redécrit pas champ par champ chaque BDD.
Elle expose la **logique d'ensemble** du système Twin.

## 1.4 Comment lire ce document

Ce document suit une progression simple :

1. définir ce qu’est le Twin,
2. poser ses principes structurants,
3. présenter la carte canonique de toutes les BDD,
4. clarifier les objets et leurs frontières,
5. regrouper les BDD selon plusieurs prismes,
6. montrer ce que ces familles produisent comme valeur.

La seconde partie du panorama décrira ensuite :
- l’architecture logique d’une BDD,
- les chaînes de transformation de la connaissance,
- les moteurs analytiques,
- les traversées à forte valeur,
- et la gouvernance d’ensemble du Twin.

# 2) Ce qu’est le Digital Twin LBP

## 2.1 Définition architecturale

Le Digital Twin LBP est une **architecture de représentation structurée d’une organisation réelle**, conçue pour transformer :
- des preuves,
- des observations,
- des formulations,
- des objets,
- des relations,
en lectures systémiques exploitables pour :
- le diagnostic,
- la compréhension du fonctionnement réel,
- la priorisation,
- le pilotage,
- et la transformation.

Le Twin ne se réduit donc pas à une base de données.  
Il articule :
- un **système d’objets**,
- un **système de liens**,
- un **système de preuves**,
- un **système de lectures**,
- et un **système d’action**.

## 2.2 Ce que le Twin n’est pas

Le Digital Twin n’est pas :
- un simple inventaire de tables,
- une base d’extraction brute,
- un tableau de bord,
- un entrepôt documentaire,
- un schéma de reporting,
- ni une ontologie abstraite sans ancrage terrain.

Il vise au contraire à tenir ensemble :
- le **réel observé**,
- le **réel structuré**,
- le **diagnostic consolidé**,
- et le **pilotage de transformation**.

## 2.3 Sa promesse de valeur

Le Twin produit de la valeur parce qu’il permet à la fois de :

- **décrire** le système,
- **qualifier** ce qui s’y passe,
- **expliquer** ce qui le fait tenir ou dérailler,
- **relier** le diagnostic à des leviers concrets,
- **objectiver** ce qui est mesuré,
- **contextualiser** dans le temps, les environnements et l’écosystème,
- **traverser** intelligemment plusieurs couches de lecture.

## 2.4 Les cinq fonctions systémiques du Twin

### Décrire
Rendre visible :
- qui existe,
- quoi existe,
- où cela se situe,
- avec quelles dépendances,
- dans quels cadres et sur quels périmètres.

### Qualifier
Transformer la matière brute en objets structurés :
- signaux,
- actions,
- enjeux,
- regroupements,
- hypothèses de consolidation.

### Expliquer
Faire apparaître :
- les logiques de fonctionnement,
- les tensions,
- les écarts,
- les causes,
- les vulnérabilités,
- les conditions d’effectivité.

### Piloter
Relier le diagnostic à :
- des objectifs explicites,
- des initiatives,
- des indicateurs,
- des arbitrages.

### Transformer
Permettre la formulation de leviers concrets :
- sur les pratiques,
- sur les capacités,
- sur les conditions systémiques,
- sur les trajectoires de transformation.

# 3) Les principes structurants du Twin

## 3.1 Séparer preuve, qualification, consolidation et action

Le Twin distingue plusieurs régimes de connaissance :

- **preuve source** : ce qui est observé, documenté, cité ou transcrit ;
- **qualification structurée** : ce qui est typé, relié ou mis en forme ;
- **consolidation analytique** : ce qui est stabilisé comme objet de lecture ou de diagnostic ;
- **pilotage / action** : ce qui oriente, mesure ou transforme.

Cette séparation évite :
- les glissements trop rapides entre symptôme et diagnostic,
- la sur-interprétation du brut,
- la confusion entre ce qui est vu, ce qui est pensé et ce qui est décidé.

## 3.2 Préserver des frontières fortes entre objets

Le Twin produit de la valeur à condition que ses objets restent conceptuellement nets.

Exemples de frontières fortes :
- une **organisation** n’est pas un **collectif** ;
- un **poste** n’est pas un **individu** ;
- un **actif** n’est pas un **environnement** ;
- une **pratique** n’est pas un **processus** ;
- une **problématique** n’est pas un **enjeu** ;
- un **modulateur** n’est ni une **capacité**, ni une **pratique**, ni une **problématique**.

Le panorama doit donc toujours distinguer :
- les **BDD**,
- les **objets** qu’elles portent,
- et les **régimes exploratoires** qui ne créent pas nécessairement de nouveaux objets ontologiques.

## 3.3 N’introduire des relations réelles que lorsqu’elles créent une vraie valeur analytique

Une relation réelle est gardée lorsqu’elle apporte un gain clair de :
- compréhension,
- traversée,
- consolidation,
- comparaison,
- ou diagnostic.

Le Twin évite :
- la saturation relationnelle,
- les edges décoratifs,
- les raffinements de relation qui n’apportent pas encore de gain net.

## 3.4 Assumer une doctrine spécifique pour les sandboxes

Les BDD sandbox ont une fonction spécifique :
- glaner des indices,
- tester des regroupements,
- préparer des promotions vers une BDD officielle,
- préserver des hypothèses sans rigidifier trop tôt le graphe officiel.

### Règle structurante

Les **BDD sandbox n’ont jamais de relations réelles**, à une seule exception :
- la relation vers **`Sources d’informations`**.

Elles utilisent :
- des **jumelles textes** comme indices,
- des propriétés spécifiques utiles à l’exploration,
- et, quand c’est utile, une couche 5D exploratoire.

## 3.5 Faire de la 5D une matrice de lecture, pas une preuve primaire

La matrice 5D sert à :
- rendre visibles des structures,
- comparer des objets hétérogènes,
- synthétiser des traversées,
- produire des vues macro.

Elle ne remplace jamais la preuve primaire, qui reste portée par :
- les objets,
- les relations,
- les propriétés spécifiques,
- les sources,
- les indices observés,
- les indices d’existence.

## 3.6 Utiliser rollups et formules avec sobriété

Les couches calculées du Twin n’ont pas pour but de “faire riche”.  
Elles servent uniquement à révéler :
- des écarts,
- des dépendances,
- des profils agrégés,
- des tensions,
- des vulnérabilités,
- des états utiles à la lecture.

Un rollup ou une formule ne doit être conservé que s’il améliore réellement l’intelligibilité.

## 3.7 Spécialiser les propriétés génériques sans casser le socle commun

Les propriétés génériques existent dans beaucoup de BDD :
- `Description`,
- `Indices observés`,
- `Indices d’existence`,
- `Commentaires`,
- `Merge Notes`,
- etc.

Mais leur **fonction commune** n’implique pas une **grammaire de remplissage identique**.

Exemple :
- on ne décrit pas un **individu** comme un **actif**,
- ni un **principe** comme une **initiative**,
- ni une **problématique** comme un **environnement**.

Le Twin assume donc :
> un socle générique commun,  
> mais des instructions d’écriture spécifiques à chaque objet.

# 4) Tableau maître canonique des BDD du Digital Twin

> **Note d'actualisation 01-05-2026** : depuis D-023 (30-04-2026), `Sources d'informations` est officiellement reclassée comme **BDD Mission Ops** (avec `Meetings`, `Actions LBP`, `Bricks`), pas Twin. Elle reste **incluse dans ce tableau** parce qu'elle joue un rôle de **satellite de traçabilité transverse** pour les objets Twin (origine traçable des fiches Twin via la chaîne d'extraction directe - cf. C-018). Décompte officiel actuel : **28 BDDs Twin** (22 officielles + 6 sandboxes) + **4 BDDs Mission Ops** (dont Sources d'informations). Pour la spec Mission Ops voir `SPECS_ARCHITECTURE_MISSION_OPS_LBP.md`.

## 4.1 Tableau maître exhaustif des BDD

| BDD | Objet principal porté | Famille architecturale | Mode d'alimentation dominant | Régime relationnel | Valeur systémique dominante |
|---|---|---|---|---|---|
| `Sources d'informations` (MO, satellite Twin) | Source d'information | Registre / satellite de traçabilité (Mission Ops, articule MO ↔ Twin) | Humain + ingestion | Référentiel source ; relations documentaires | Assurer la traçabilité primaire de tout le Twin |
| `Glossaire spécifique entreprise` | Terme / expression située | Socle sémantique | Curation / clarification | Relations réelles + jumelles textes | Stabiliser le langage client et réduire l’ambiguïté sémantique |
| `Journal des signaux` | Signal faible ou indice qualitatif | Observation qualitative amont | Extraction / lecture qualitative | Relations réelles + jumelles textes | Capter les indices faibles avant consolidation |
| `Actions détectées` | Action observée ou dite | Extraction factuelle | Extraction IA + revue | Relations réelles + jumelles textes | Donner la matière brute du faire réel |
| `Enjeux` | Enjeu formulé | Extraction factuelle stratégique | Extraction IA + revue | Relations réelles + jumelles textes | Faire remonter besoins, tensions, objectifs, opportunités et craintes |
| `Organisations` | Organisation | Socle structurel institutionnel | Curation / structuration | Relations réelles + jumelles textes | Décrire les acteurs institués du système |
| `Relations inter-organisations` | Relation directionnelle entre deux organisations | BDD edge structurelle | Curation / structuration | Relations réelles + jumelles textes | Cartographier l’écosystème relationnel externe |
| `Collectifs` | Collectif opérant | Socle structurel social | Curation / structuration | Relations réelles + jumelles textes | Décrire les groupes humains où le travail se coordonne réellement |
| `Individus` | Individu | Socle structurel humain | Extraction + curation | Relations réelles + jumelles textes | Rendre visibles les personnes significatives du système |
| `Postes` | Poste | Structure formelle | Curation / structuration | Relations réelles + jumelles textes | Décrire la charpente formelle des fonctions |
| `Actifs` | Actif | Supports / moyens | Curation / structuration | Relations réelles + jumelles textes | Rendre visibles les supports, dépendances et vulnérabilités |
| `Environnements` | Environnement | Contextes / contraintes | Curation / structuration | Relations réelles + jumelles textes | Expliciter les cadres d’usage, d’exposition et de contrainte |
| `Événements` | Événement | Temps / trajectoire | Curation / structuration | Relations réelles + jumelles textes | Donner les jalons, bascules et épisodes structurants |
| `Initiatives organisationnelles` | Initiative organisationnelle | Mouvement / transformation | Curation / pilotage | Relations réelles + jumelles textes | Décrire les efforts temporaires structurés de transformation |
| `Processus candidats` | Processus candidat | Pivot de qualification | Analyse / consultant | Relations réelles + jumelles textes | Préparer la consolidation des fonctionnements |
| `Processus` | Processus | Fonctionnement consolidé | Analyse / consultant | Relations réelles + jumelles textes | Modéliser les fonctionnements structurés et stabilisés |
| `Pratiques organisationnelles` | Pratique organisationnelle | Réel opérant consolidé | Analyse / consultant | Relations réelles + jumelles textes | Rendre visibles les patterns opérants récurrents |
| `Principes organisationnels` | Principe organisationnel | Couche normative | Analyse / consultant | Relations réelles + jumelles textes | Formaliser la couche normative du système |
| `Capacités organisationnelles` | Capacité organisationnelle | Couche capacitaire | Analyse / consultant | Relations réelles + jumelles textes | Rendre visibles les aptitudes collectives durables |
| `Problématiques` | Problématique | Couche diagnostique | Analyse / consultant | Relations réelles + jumelles textes | Produire les nœuds diagnostiques consolidés |
| `OKR` | OKR | Couche de pilotage | Analyse / consultant | Relations réelles + jumelles textes | Relier diagnostic, pilotage et transformation |
| `Indicateurs` | Indicateur | Couche de mesure | Analyse / consultant | Relations réelles + jumelles textes | Objectiver la performance, les écarts et la progression |
| `Modulateurs` | Modulateur | Couche d’effectivité | Référentiel préchargé + évaluation consultant | Relations réelles + jumelles textes | Expliquer les conditions d’effectivité et les plafonds systémiques |
| `Capacités métier candidates (sandbox)` | Capacité métier candidate | Sandbox d’exploration | Extraction / analyse exploratoire | Jumelles textes uniquement + relation à `Sources d’informations` | Tester des capacités pressenties avant migration vers la BDD officielle |
| `OKR (sandbox)` | OKR exploratoire | Sandbox d’exploration | Analyse exploratoire / consultant | Jumelles textes uniquement + relation à `Sources d’informations` | Tester des objectifs avant promotion dans la BDD officielle `OKR` |
| `Pratiques organisationnelles (sandbox)` | Pratique organisationnelle exploratoire | Sandbox d’exploration | Extraction / analyse exploratoire | Jumelles textes uniquement + relation à `Sources d’informations` | Tester des pratiques pressenties avant promotion dans la BDD officielle des pratiques |
| `Principes organisationnels (sandbox)` | Principe organisationnel exploratoire | Sandbox d’exploration | Analyse exploratoire / consultant | Jumelles textes uniquement + relation à `Sources d’informations` | Tester des principes pressentis avant entrée dans la couche normative officielle |
| `Problématiques (sandbox)` | Problématique exploratoire | Sandbox d’exploration | Analyse exploratoire / consolidation initiale | Jumelles textes uniquement + relation à `Sources d’informations` | Tester des formulations diagnostiques encore instables avant consolidation officielle |
| `Processus candidats (sandbox)` | Processus candidat exploratoire | Sandbox d’exploration | Extraction / analyse exploratoire | Jumelles textes uniquement + relation à `Sources d’informations` | Tester des regroupements fonctionnels pressentis sans engager trop tôt le pivot officiel |

## 4.2 Ce que montre le tableau maître

Le tableau maître met immédiatement en évidence cinq faits structurants :

### a) Toutes les BDD n’ont pas le même statut architectural
Le Twin comprend :
- des registres,
- des socles structurels,
- des couches analytiques,
- des pivots,
- et des sandboxes.

### b) Toutes les BDD ne produisent pas le même type de valeur
Certaines servent surtout à :
- **décrire**,
d’autres à :
- **capturer le brut**,
- **expliquer**,
- **piloter**,
- **mesurer**,
- ou **tester**.

### c) Le Twin n’est pas un graphe homogène
Le graphe officiel ne se confond pas avec l’ensemble des BDD :
- les BDD sandbox ne s’y branchent pas par relations réelles,
- `Sources d’informations` joue un rôle de satellite,
- `Relations inter-organisations` joue un rôle de BDD edge.

### d) Le Twin organise une progression
Le tableau donne déjà à lire une logique de transformation :
- de la **preuve**,
- vers la **qualification**,
- puis la **consolidation**,
- puis la **lecture analytique**,
- puis le **pilotage**.

### e) Le tableau maître est la carte canonique du système
Toute nouvelle BDD, tout changement de statut, tout ajout de sandbox ou toute refonte d’objet doit être arbitré à partir de cette carte.

## 4.3 Règle de gouvernance du tableau maître

Le tableau maître constitue la **référence canonique** du Twin.

Cela signifie que :
- toute création de BDD doit y être ajoutée,
- toute suppression doit y être arbitrée,
- tout changement de régime architectural doit y être explicité,
- et toute sandbox doit être distinguée de sa BDD officielle cible.

# 5) Cartographie des objets portés par le Twin

## 5.1 Objets ontologiques principaux

| Objet | Définition architecturale | Ne doit pas être confondu avec |
|---|---|---|
| **Source d’information** | pièce documentaire, entretien, note, support, transcript ou artefact servant de preuve primaire | actif, glossaire, événement |
| **Terme de glossaire** | unité sémantique stabilisée dans le contexte client | principe, capacité, actif, nom de projet |
| **Signal** | indice faible ou qualitatif encore peu consolidé | enjeu, problématique, événement |
| **Organisation** | acteur collectif institué, doté d’une existence institutionnelle ou juridique | collectif, poste, relation inter-organisations |
| **Relation inter-organisations** | lien structurant directionnel entre deux organisations distinctes | hiérarchie institutionnelle, simple mention de partenaire |
| **Collectif** | groupe humain opérant, stable ou temporaire, où du travail se coordonne | organisation, poste, initiative |
| **Individu** | personne physique significative dans le système étudié | poste, collectif |
| **Poste** | position formelle contextualisée, indépendante de son titulaire | individu, rôle informel, collectif |
| **Actif** | objet non humain gouvernable, mobilisable, administrable ou transformable | environnement, source, pratique |
| **Environnement** | cadre d’usage, d’exposition ou de contrainte | actif, événement |
| **Événement** | repère temporel daté ou datable, ponctuel ou borné | initiative, action, simple contexte |
| **Initiative organisationnelle** | effort intentionnel, temporaire et délimité | événement, collectif, pratique |
| **Action détectée** | unité minimale de faire observé ou dit | pratique, processus |
| **Enjeu** | formulation structurée d’un besoin, d’une tension, d’une opportunité, d’un objectif ou d’une crainte | problématique consolidée, signal faible |
| **Processus candidat** | regroupement plausible d’actions avant consolidation | processus consolidé, simple suite d’actions sans cohérence |
| **Processus** | fonctionnement structuré, stabilisé, doté d’une logique de transformation | pratique, initiative |
| **Pratique organisationnelle** | pattern opérant récurrent produisant une valeur durable | action isolée, processus, principe |
| **Principe organisationnel** | intention normative stable guidant des arbitrages récurrents | valeur décorative, règle locale, pratique |
| **Capacité organisationnelle** | aptitude collective durable que le système possède ou doit renforcer | pratique, projet, poste |
| **Problématique** | nœud diagnostique consolidé et structurant | enjeu, signal, symptôme isolé |
| **OKR** | objectif piloté et structuré, orienté résultats | initiative, indicateur, principe |
| **Indicateur** | mesure, proxy ou dispositif de suivi | objectif, problème, actif |
| **Modulateur** | condition d’effectivité transversale influençant fortement les pratiques et les capacités | capacité, pratique, problématique |

## 5.2 Régimes exploratoires des sandboxes

Les lignes ci-dessous ne décrivent pas de nouvelles classes ontologiques fondamentales.  
Elles décrivent des **régimes exploratoires provisoires** appliqués à certains objets.

| Régime sandbox | Sert à | Doit migrer vers | Ne doit pas être confondu avec |
|---|---|---|---|
| **Capacité métier candidate (sandbox)** | documenter une aptitude plausible mais encore insuffisamment arbitré | `Capacités organisationnelles` | une capacité officielle, une pratique, un poste |
| **OKR (sandbox)** | tester un objectif avant stabilisation dans la couche officielle de pilotage | `OKR` | une initiative, un enjeu, un indicateur |
| **Pratique organisationnelle (sandbox)** | documenter une pratique pressentie avant promotion dans la BDD officielle | `Pratiques organisationnelles` | une action isolée, un processus, une pratique consolidée |
| **Principe organisationnel (sandbox)** | tester une hypothèse normative encore trop instable | `Principes organisationnels` | une valeur affichée, un principe officiel, une règle locale |
| **Problématique (sandbox)** | tester une formulation diagnostique avant consolidation officielle | `Problématiques` | une problématique consolidée, un enjeu, un signal |
| **Processus candidat (sandbox)** | tester un regroupement fonctionnel encore trop exploratoire pour le pivot officiel | `Processus candidats` | un processus candidat consolidé, un processus officiel |

## 5.3 Cas particuliers : satellites, edges et bacs

| Type particulier | BDD concernée | Particularité architecturale |
|---|---|---|
| **Satellite de traçabilité** | `Sources d’informations` | ne porte pas un objet du Twin au même titre que les autres ; sert de colonne vertébrale documentaire |
| **BDD edge** | `Relations inter-organisations` | porte un lien structurant directionnel entre deux organisations, plutôt qu’un objet “plein” de type entité |
| **BDD sandbox** | les 6 sandboxes spécialisées | servent à explorer, glaner et qualifier sans ajouter de relations réelles au graphe officiel |

# 6) Les familles de BDD par grands régimes architecturaux

## 6.1 Registres et satellites

### BDD concernée
- `Sources d’informations`

### Fonction architecturale
Ce bloc sert à porter la **preuve primaire** du Twin :
- ce qui a été lu,
- entendu,
- observé,
- ou utilisé pour documenter un objet.

Il ne joue pas le même rôle que les autres BDD :
- il ne décrit pas directement le système,
- il décrit ce qui **permet de décrire** le système.

## 6.2 Socle sémantique

### BDD concernée
- `Glossaire spécifique entreprise`

### Fonction architecturale
Cette BDD stabilise :
- le vocabulaire client,
- les expressions internes,
- les acronymes,
- les formulations ambiguës,
- les termes sectoriels.

Elle améliore :
- l’extraction,
- la consolidation,
- la recherche,
- la lisibilité des restitutions,
- et la compréhension par les agents.

## 6.3 Extraction qualitative et factuelle

### BDD concernées
- `Journal des signaux`
- `Actions détectées`
- `Enjeux`

### Fonction architecturale
Ce bloc capte la matière amont du Twin :
- indices faibles,
- gestes réels,
- formulations stratégiques,
- tensions exprimées,
- besoins et opportunités.

C’est le bloc qui permet d’éviter un Twin purement top-down ou purement descriptif.

## 6.4 Socle structurel institutionnel, social, formel et contextuel

### BDD concernées
- `Organisations`
- `Relations inter-organisations`
- `Collectifs`
- `Individus`
- `Postes`
- `Actifs`
- `Environnements`
- `Événements`

### Fonction architecturale
Ce bloc donne au Twin sa **charpente structurelle** :
- qui existe,
- qui agit,
- avec quels supports,
- dans quels cadres,
- à quel moment,
- et avec quelles dépendances externes.

C’est le bloc qui rend le système :
- localisable,
- situable,
- traversable,
- et contextualisable.

## 6.5 Mouvement et transformation

### BDD concernée
- `Initiatives organisationnelles`

### Fonction architecturale
Cette BDD porte les **efforts temporaires structurés** :
- projets,
- programmes,
- missions,
- chantiers,
- pilotes.

Elle relie le Twin :
- au changement en cours,
- à la dynamique de transformation,
- aux trajectoires de déploiement.

## 6.6 Pivots de qualification

### BDD concernée
- `Processus candidats`

### Fonction architecturale
Cette BDD sert de **sas de qualification fonctionnelle**.  
Elle permet de tester si un regroupement d’actions :
- est assez cohérent,
- assez récurrent,
- assez finalisé,
pour être consolidé en processus officiel.

## 6.7 Digital Twin analytique officiel

### BDD concernées
- `Processus`
- `Pratiques organisationnelles`
- `Principes organisationnels`
- `Capacités organisationnelles`
- `Problématiques`
- `OKR`
- `Indicateurs`
- `Modulateurs`

### Fonction architecturale
Ce bloc constitue la couche où le Twin devient véritablement :
- analytique,
- explicatif,
- pilotable,
- actionnable.

Il porte :
- la compréhension du fonctionnement réel,
- les écarts,
- les normes,
- les aptitudes,
- les conditions d’effectivité,
- les objectifs,
- la mesure.

## 6.8 Sandboxes exploratoires

### BDD concernées
- `Capacités métier candidates (sandbox)`
- `OKR (sandbox)`
- `Pratiques organisationnelles (sandbox)`
- `Principes organisationnels (sandbox)`
- `Problématiques (sandbox)`
- `Processus candidats (sandbox)`

### Fonction architecturale
Ces BDD servent à :
- tester des hypothèses,
- documenter des objets pas encore stabilisés,
- préparer une migration,
- préserver des options,
- éviter d’alourdir trop tôt le graphe officiel.

### Règle structurante
Elles n’ont :
- **pas de relations réelles** avec le Twin officiel,
- mais des **jumelles textes**,
- et, si nécessaire, une relation vers `Sources d’informations`.

# 7) Les familles de BDD par fonction dans la chaîne de valeur

## 7.1 Stabiliser la preuve et le langage

### BDD centrales
- `Sources d’informations`
- `Glossaire spécifique entreprise`

### Ce que cette famille produit
Elle stabilise :
- ce qui sert de preuve,
- ce que les mots veulent dire,
- et la manière de relier le langage client à l’architecture du Twin.

Sans cette famille, le Twin devient rapidement :
- ambigu,
- fragile,
- difficile à auditer,
- et difficile à exploiter par des agents.

## 7.2 Décrire le système

### BDD centrales
- `Organisations`
- `Relations inter-organisations`
- `Collectifs`
- `Individus`
- `Postes`
- `Actifs`
- `Environnements`
- `Événements`

### Ce que cette famille produit
Elle donne le portrait du système :
- ses acteurs,
- ses groupes,
- ses fonctions,
- ses supports,
- ses cadres,
- son temps,
- son écosystème.

C’est la couche qui répond à :
> qui existe, quoi existe, où, avec quoi, et dans quel cadre ?

## 7.3 Capturer la matière brute

### BDD centrales
- `Journal des signaux`
- `Actions détectées`
- `Enjeux`

### Ce que cette famille produit
Elle permet :
- de capter le terrain,
- de remonter les tensions,
- d’éviter que le diagnostic ne soit déconnecté du réel,
- de faire entrer dans le Twin ce qui est encore peu structuré mais déjà significatif.

## 7.4 Qualifier avant consolidation

### BDD centrales
- `Processus candidats`
- `Capacités métier candidates (sandbox)`
- `OKR (sandbox)`
- `Pratiques organisationnelles (sandbox)`
- `Principes organisationnels (sandbox)`
- `Problématiques (sandbox)`
- `Processus candidats (sandbox)`

### Ce que cette famille produit
Elle évite les consolidations trop précoces.

Elle sert à :
- tester,
- regrouper,
- qualifier,
- comparer,
- et arbitrer avant promotion dans une BDD officielle.

C’est une famille clé pour maintenir la qualité du graphe.

## 7.5 Expliquer le fonctionnement réel

### BDD centrales
- `Processus`
- `Pratiques organisationnelles`

### BDD contributrices
- `Actions détectées`
- `Actifs`
- `Collectifs`
- `Environnements`

### Ce que cette famille produit
Elle rend visible :
- comment le système fonctionne réellement,
- à travers quels mécanismes,
- avec quels patterns,
- avec quels supports,
- dans quels contextes.

C’est le cœur de la lecture opératoire du Twin.

## 7.6 Expliquer les tensions

### BDD centrales
- `Enjeux`
- `Problématiques`
- `Journal des signaux`

### BDD contributrices
- `Environnements`
- `Événements`
- `Relations inter-organisations`

### Ce que cette famille produit
Elle permet de répondre à :
- qu’est-ce qui coince ?
- qu’est-ce qui inquiète ?
- où se situent les nœuds majeurs ?
- quels problèmes sont conjoncturels, structurels, contextuels ou écologiques ?

## 7.7 Expliquer les aptitudes, les normes et les conditions d’effectivité

### BDD centrales
- `Capacités organisationnelles`
- `Principes organisationnels`
- `Modulateurs`

### BDD contributrices
- `Pratiques organisationnelles`
- `Problématiques`
- `Environnements`

### Ce que cette famille produit
Elle permet de répondre à :
- ce que le système sait durablement faire,
- ce qu’il prétend guider normativement,
- ce qui permet à ses pratiques de tenir,
- ce qui les limite,
- ce qui doit être renforcé.

C’est la couche la plus explicative du Twin après le diagnostic.

## 7.8 Piloter, transformer et mesurer

### BDD centrales
- `OKR`
- `Initiatives organisationnelles`
- `Indicateurs`

### BDD contributrices
- `OKR (sandbox)`
- `Capacités`
- `Problématiques`

### Ce que cette famille produit
Elle permet :
- de relier diagnostic et objectifs,
- objectifs et initiatives,
- initiatives et mesure,
- mesure et arbitrage.

C’est la couche qui rend le Twin actionnable.

### 7.9 Tableau croisé BDD × fonction de valeur

**Légende**
- `●` = fonction dominante
- `○` = contribution importante mais secondaire
- `-` = fonction non centrale

| BDD | Stabiliser la preuve et le langage | Décrire le système | Capturer la matière brute | Qualifier avant consolidation | Expliquer le fonctionnement réel | Expliquer les tensions | Expliquer les aptitudes, les normes et les conditions d’effectivité | Piloter, transformer et mesurer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Sources d’informations` | ● | - | ○ | - | - | - | - | - |
| `Glossaire spécifique entreprise` | ● | ○ | - | - | - | - | - | - |
| `Journal des signaux` | ○ | - | ● | ○ | - | ● | - | - |
| `Actions détectées` | - | ○ | ● | ○ | ○ | - | - | - |
| `Enjeux` | - | - | ● | ○ | - | ● | - | ○ |
| `Organisations` | - | ● | - | - | ○ | ○ | - | ○ |
| `Relations inter-organisations` | - | ● | - | - | - | ○ | - | ○ |
| `Collectifs` | - | ● | - | - | ○ | ○ | - | ○ |
| `Individus` | - | ● | - | - | ○ | ○ | - | ○ |
| `Postes` | - | ● | - | - | ○ | - | - | ○ |
| `Actifs` | - | ● | - | - | ○ | ○ | ○ | - |
| `Environnements` | - | ● | - | - | ○ | ● | ○ | - |
| `Événements` | - | ● | - | - | ○ | ○ | - | ○ |
| `Initiatives organisationnelles` | - | ○ | - | - | ○ | ○ | ○ | ● |
| `Processus candidats` | - | - | - | ● | ○ | - | - | - |
| `Processus` | - | ○ | - | - | ● | ○ | ○ | ○ |
| `Pratiques organisationnelles` | - | ○ | - | - | ● | ○ | ● | ○ |
| `Principes organisationnels` | - | - | - | - | ○ | ○ | ● | ○ |
| `Capacités organisationnelles` | - | - | - | - | ○ | ○ | ● | ○ |
| `Problématiques` | - | - | - | ○ | ○ | ● | ○ | ○ |
| `OKR` | - | - | - | - | - | ○ | ○ | ● |
| `Indicateurs` | - | - | - | - | ○ | ○ | ○ | ● |
| `Modulateurs` | - | - | - | - | ○ | ○ | ● | ○ |
| `Capacités métier candidates (sandbox)` | - | - | - | ● | - | ○ | ○ | - |
| `OKR (sandbox)` | - | - | - | ● | - | ○ | ○ | ○ |
| `Pratiques organisationnelles (sandbox)` | - | - | - | ● | ○ | ○ | ○ | - |
| `Principes organisationnels (sandbox)` | - | - | - | ● | - | ○ | ○ | - |
| `Problématiques (sandbox)` | - | - | - | ● | - | ○ | ○ | - |
| `Processus candidats (sandbox)` | - | - | - | ● | ○ | - | - | - |

# 8) Les régimes de structuration des données

Le Digital Twin n’est pas seulement un ensemble de BDD.  
C’est un système où plusieurs **régimes de structuration** coexistent, selon le niveau de maturité de la donnée, sa vocation analytique, et son statut dans le graphe officiel.

Autrement dit, une donnée n’a pas partout le même statut :
- parfois elle vaut comme **preuve**,
- parfois comme **indice**,
- parfois comme **relation consolidée**,
- parfois comme **lecture calculée**,
- parfois comme **hypothèse exploratoire**.

Comprendre ces régimes est essentiel, car c’est ce qui évite :
- les consolidations trop précoces,
- les lectures artificiellement sûres,
- les faux graphes relationnels,
- et les analyses déconnectées de la qualité réelle de la preuve.

## 8.1 Relations réelles

Les **relations réelles** sont les liens structurés du graphe officiel du Twin.  
Elles sont utilisées lorsque le lien entre deux objets apporte une valeur analytique suffisamment forte pour justifier sa stabilisation.

### Une relation réelle sert à :
- traverser le système rapidement,
- faire émerger des chaînes de dépendance,
- rendre possible des rollups fiables,
- croiser plusieurs couches de lecture,
- et éviter de réécrire manuellement la même information.

### Exemples de relations réelles à forte valeur
- `Organisation → comprend → Collectif`
- `Collectif → a pour membres → Individu`
- `Poste → est occupé par → Individu`
- `Processus → utilise → Actif`
- `Pratique → alimente → Capacité`
- `Problématique → est adressée par → OKR`
- `OKR → est mesuré par → Indicateur`
- `Organisation → est source de / est cible de → Relations inter-organisations`

### Principe directeur
Une relation réelle est créée quand elle améliore clairement :
- la lisibilité,
- la traversée,
- la consolidation,
- ou la capacité d’analyse.

Elle n’est pas créée juste parce qu’un lien “pourrait exister”.

## 8.2 Jumelles textes

Les **jumelles textes** sont les miroirs textuels des relations.

Elles jouent un rôle central dans l’architecture, car elles permettent de conserver :
- la **formulation observée**,
- la **trace amont d’un lien**,
- la **possibilité de rapprocher avant arbitrage**,
- et une **souplesse de travail** très utile en phase d’extraction ou de curation.

### Une jumelle texte sert à :
- préserver l’expression telle qu’elle apparaît dans les sources,
- faciliter la consolidation progressive,
- garder un indice relationnel même si la relation n’est pas encore validée,
- servir de base de vérification pour un humain ou un agent.

### Exemple
Dans une BDD officielle :
- `est conduite par (collectifs) (texte)` conserve les formulations observées,
- `est conduite par (collectifs)` porte la relation consolidée.

Dans une sandbox :
- seule la **jumelle texte** subsiste,
- précisément pour ne pas figer trop tôt le graphe officiel.

## 8.3 Propriétés spécifiques

Les **propriétés spécifiques** sont les champs qui donnent à chaque objet sa valeur analytique propre.

Sans elles, le Twin ne serait qu’un graphe descriptif.  
Ce sont elles qui rendent les objets :
- comparables,
- explicatifs,
- hiérarchisables,
- et actionnables.

### Leur rôle
Elles servent à rendre explicites :
- la nature d’un objet,
- sa portée,
- sa criticité,
- sa maturité,
- sa temporalité,
- sa logique d’usage,
- ses effets,
- ses vulnérabilités,
- ou sa fonction systémique.

### Exemples
- `Actifs` : type, criticité, substituabilité, cycle de vie
- `Processus` : finalité, déclencheur, inputs, outputs, niveau de processisation
- `Pratiques` : pattern opérant, intention dominante, horizon de valeur
- `Capacités` : distinctivité, maturité actuelle, maturité cible, criticité stratégique
- `Problématiques` : causalités, impacts, risques, tension structurante
- `Indicateurs` : unité, fréquence, baseline, cible, type d’usage

## 8.4 Propriétés génériques spécialisées

Le Twin repose sur un socle générique commun :
- nom,
- statut,
- aliases,
- description,
- indices,
- logs,
- traces de merge,
- etc.

Mais ce socle est **spécialisé à l’écriture** selon l’objet.

### Exemple clé : `Description`
- la description d’un **individu** présente la place actuelle de la personne dans le système ;
- celle d’un **actif** explique ce que c’est, à quoi il sert et pour qui ;
- celle d’une **initiative** décrit un effort temporaire, son objectif et sa sortie attendue ;
- celle d’une **problématique** explicite un nœud diagnostique, son périmètre et sa logique centrale.

### Exemple clé : `Indices observés`
- pour un **processus**, ils justifient la structuration du fonctionnement ;
- pour une **capacité**, ils justifient l’évaluation de maturité et de criticité ;
- pour un **principe**, ils justifient le niveau d’incarnation normative ;
- pour un **indicateur**, ils justifient le cadrage de la mesure.

### Conséquence architecturale
Le Twin n’est pas seulement gouverné par des objets et des relations.  
Il est aussi gouverné par une **doctrine d’écriture de la preuve**.

## 8.5 Couche 5D

La couche 5D donne à chaque BDD une **traversabilité systémique**.

Elle ne sert pas à reclassifier les objets.  
Elle sert à répondre à des questions comme :
- où cet objet agit-il principalement ?
- de quoi dépend-il ?
- où se situent ses fragilités ?
- où produit-il ses effets ?
- quelle zone du système est mesurée, pilotée ou exposée ?

### Usages typiques
- **contribution** : ce qu’un objet fait évoluer dans le système
- **exposition** : ce qu’il subit
- **dépendance** : ce dont il a besoin pour tenir
- **causalité / impact / risque** : comment les effets se propagent
- **pilotage / mesure** : ce que le système vise ou lit effectivement

### Exemples
- une **initiative** a des sous-dimensions 5D principalement travaillées ;
- un **actif** soutient certaines sous-dimensions et en fragilise d’autres en cas d’indisponibilité ;
- une **problématique** a des causalités, impacts et risques par sous-dimension ;
- un **indicateur** lit certaines sous-dimensions avec une nature de couverture plus ou moins directe.

## 8.6 Couche calculée : rollups

Les **rollups** sont des lectures agrégées fondées sur des relations réelles.

Ils servent à rendre visible, dans une fiche :
- ce qui existe déjà ailleurs,
- mais qui devient beaucoup plus parlant quand c’est synthétisé au bon endroit.

### Ce qu’un bon rollup doit faire apparaître
- un profil agrégé,
- une couverture,
- une dépendance,
- un faisceau de liens,
- ou une structure transversale difficile à lire sans agrégation.

### Exemples forts
- `Organisations` : profils 5D agrégés d’exposition, d’action, de pilotage, de mesure
- `Collectifs` : profils 5D de contribution, d’exposition, de dépendance, de pilotage
- `Individus` : profils 5D d’intervention, d’exposition, d’expression, de dépendance fonctionnelle
- `OKR` : sous-dimensions impactées par les problématiques adressées, sous-dimensions visées via initiatives et indicateurs
- `Indicateurs` : agrégation des objets qu’ils mesurent ou des sous-dimensions qu’ils couvrent

### Règle importante
Un rollup suppose :
- une relation réelle stable,
- un gain de lecture clair,
- et une information assez structurée dans la BDD cible.

Il n’a pas sa place dans une sandbox sans relations réelles.

## 8.7 Couche calculée : formules

Les **formules** produisent des lectures synthétiques à partir de champs déjà présents dans une fiche.

Elles ne doivent jamais être décoratives.  
Elles doivent rendre visible quelque chose qu’un lecteur ne voit pas immédiatement.

### Ce qu’une bonne formule peut révéler
- un état,
- une tension,
- un écart,
- une vulnérabilité,
- une cohérence,
- une pression,
- une nature d’engagement,
- une valeur stratégique.

### Exemples structurants
- `Actifs` : **Dépendance externe de l’actif**, **Vulnérabilité nette de l’actif**
- `Capacités` : **Écart de maturité de la capacité**, **Valeur stratégique de la capacité métier**
- `Initiatives` : **Statut temporel de l’initiative**, **Nature d’engagement de l’initiative**
- `Modulateurs` : **Amplitude potentielle d’impact**, **Risque de plafond systémique**
- `Actions détectées` : **Pression opératoire de l’action**
- `Environnements` : **Pression contextuelle nette**, **Régime d’environnement**

### Doctrine de formulation
Dans les WR/RD, les formules sont documentées comme :
- logique de calcul,
- entrées,
- sorties attendues,
- cas limites.

Elles ne dépendent donc pas d’une syntaxe spécifique à un outil.

## 8.8 Ce que les sandboxes ont / n’ont pas

Les sandboxes ne sont pas des sous-BDD “pauvres”.  
Ce sont des **sas exploratoires spécialisés**.

Elles ont une vraie utilité :
- explorer,
- documenter,
- qualifier,
- préparer,
- retarder l’arbitrage jusqu’à ce que la preuve soit suffisante.

### Elles ont généralement
- des propriétés génériques,
- des propriétés spécifiques,
- des jumelles textes,
- parfois une couche 5D,
- une relation possible à `Sources d’informations`.

### Elles n’ont pas
- de relations réelles avec les autres BDD du Twin,
- de rollups fondés sur un graphe officiel absent,
- de vocation à rester durablement parallèles aux BDD officielles.

### Lecture des sandboxes actuelles

| Sandbox | Fonction exploratoire principale | BDD officielle cible |
|---|---|---|
| `Capacités métier candidates (sandbox)` | tester des aptitudes métier pressenties | `Capacités organisationnelles` |
| `OKR (sandbox)` | tester des objectifs avant stabilisation pilotage | `OKR` |
| `Pratiques organisationnelles (sandbox)` | tester des patterns opérants avant consolidation | `Pratiques organisationnelles` |
| `Principes organisationnels (sandbox)` | tester des hypothèses normatives | `Principes organisationnels` |
| `Problématiques (sandbox)` | tester des formulations diagnostiques | `Problématiques` |
| `Processus candidats (sandbox)` | tester des regroupements fonctionnels encore trop précoces | `Processus candidats` |

---

# 9) L’architecture logique d’une BDD du Twin

## 9.1 Modèle cible d’une BDD bien spécifiée

Une BDD importante du Twin est généralement pensée comme un **empilement cohérent de couches**.

### Couche 1 - Propriétés génériques
Elle rend la fiche :
- gouvernable,
- traçable,
- lisible,
- fusionnable si besoin,
- et audit-able.

### Couche 2 - Relations + jumelles textes
Elle relie l’objet aux autres objets du système, tout en conservant :
- la formulation observée,
- et un espace de consolidation progressive.

### Couche 3 - Propriétés spécifiques
Elle donne à la BDD son **pouvoir explicatif propre**.

### Couche 4 - Couche 5D
Elle rend l’objet traversable dans la matrice systémique.

### Couche 5 - Couche calculée
Elle produit :
- des synthèses agrégées,
- des états calculés,
- des signaux utiles à la lecture.

### Résumé visuel

| Couche | Question à laquelle elle répond |
|---|---|
| Propriétés génériques | cette fiche est-elle claire, traçable et gouvernable ? |
| Relations + jumelles textes | à quels autres objets est-elle liée, et comment ces liens ont-ils été observés ? |
| Propriétés spécifiques | qu’est-ce qui fait la singularité analytique de cet objet ? |
| Couche 5D | où cet objet agit-il, dépend-il, expose-t-il ou mesure-t-il le système ? |
| Couche calculée | que faut-il voir rapidement sans relire toute la fiche ? |

## 9.2 Variantes selon les familles de BDD

Toutes les BDD ne mobilisent pas ces couches avec la même intensité.

### a) Registre / satellite
Exemple : `Sources d’informations`

- la couche relationnelle sert surtout à documenter les usages de preuve ;
- la couche 5D n’est pas centrale ;
- la couche calculée n’est pas prioritaire.

### b) Socle sémantique
Exemple : `Glossaire spécifique entreprise`

- très forte intensité sur les propriétés génériques et spécifiques,
- relations utiles mais plus sémantiques que systémiques,
- pas de besoin structurel fort en 5D,
- pas de besoin fort en rollups.

### c) Extraction factuelle
Exemples : `Journal des signaux`, `Actions détectées`, `Enjeux`

- relations et jumelles textes très importantes,
- propriétés spécifiques orientées qualification,
- 5D utilisée comme lecture d’orientation, pas comme vérité primaire,
- formules sobres et ciblées.

### d) Socle structurel
Exemples : `Organisations`, `Collectifs`, `Individus`, `Postes`, `Actifs`, `Environnements`, `Événements`

- relations nombreuses et très structurantes,
- propriétés spécifiques de portée, criticité, temporalité, type,
- 5D souvent agrégée ou orientée exposition / dépendance,
- rollups très utiles.

### e) Pivots et post-traitement analytique
Exemples : `Processus candidats`, `Processus`, `Pratiques`, `Principes`, `Capacités`, `Problématiques`, `OKR`, `Indicateurs`, `Modulateurs`

- forte intensité sur les propriétés spécifiques,
- forte articulation avec diagnostic, pilotage et mesure,
- 5D très utile,
- formules et rollups souvent stratégiques.

## 9.3 Cas particuliers : registre, glossaire, sandbox

### `Sources d’informations`
Cette BDD ne doit pas être lue comme un “objet du système” au même titre que les autres.  
Elle documente ce qui permet de fonder les autres fiches.

### `Glossaire spécifique entreprise`
Cette BDD est transversale :
- elle n’explique pas directement le fonctionnement,
- mais elle améliore massivement la qualité de toutes les autres couches.

### Sandboxes
Les sandboxes sont des **pré-objets consolidables**.  
Elles ont donc une architecture volontairement incomplète :
- elles peuvent porter une bonne part du formalisme de l’objet cible,
- mais sans entrer dans le graphe officiel tant que l’arbitrage n’est pas fait.

---

# 10) Les grandes chaînes de transformation de la connaissance

Le Twin produit de la valeur parce qu’il transforme progressivement la connaissance.

Il ne stocke pas seulement des objets ; il organise des **chaînes de passage** entre :
- preuve,
- structuration,
- consolidation,
- lecture,
- pilotage,
- action.

## 10.1 Sources → objets documentés

`Sources d’informations` → toutes les BDD documentées

### Ce que cette chaîne produit
- l’auditabilité,
- la vérifiabilité,
- la possibilité de revenir à la preuve primaire.

### Exemple
Une fiche `Actif`, `Initiative` ou `Problématique` n’est pas seulement “renseignée” :
elle est **rattachée à des preuves**.

## 10.2 Glossaire → clarification des autres couches

`Glossaire spécifique entreprise` → meilleure extraction, meilleure consolidation, meilleure restitution

### Ce que cette chaîne produit
- moins d’ambiguïtés,
- plus de cohérence de nommage,
- une meilleure qualité de matching entre sources et objets.

### Exemple
Un terme client ambigu peut empêcher :
- de bien repérer une action,
- de bien qualifier un enjeu,
- de bien nommer une capacité ou un actif.

Le glossaire corrige cela à la racine.

## 10.3 Journal des signaux → Enjeux

`Journal des signaux` → `Enjeux`

### Ce que cette chaîne produit
- passage d’indices faibles à une matière stratégique structurée.

### Exemple
Un motif faible récurrent du type :
> “on ne sait jamais qui tranche”
peut alimenter un enjeu explicite sur la gouvernance ou la coordination.

## 10.4 Enjeux → Problématiques

`Enjeux` → `Problématiques`

### Ce que cette chaîne produit
- passage du besoin, de la tension, de l’opportunité ou de la crainte
- vers un nœud diagnostique consolidé.

### Exemple
Plusieurs enjeux distincts peuvent converger vers une même problématique racine.

## 10.5 Actions détectées → Processus candidats

`Actions détectées` → `Processus candidats`

### Ce que cette chaîne produit
- premiers regroupements fonctionnels plausibles à partir du faire observé.

### Exemple
Des actions récurrentes de qualification, d’escalade et de clôture peuvent faire émerger un processus candidat support.

## 10.6 Actions détectées → Pratiques organisationnelles

`Actions détectées` → `Pratiques organisationnelles`

### Ce que cette chaîne produit
- passage du geste observé au pattern opérant récurrent.

### Exemple
Des actions dispersées mais récurrentes peuvent révéler un rituel, une routine ou une manière de faire stable.

## 10.7 Actions détectées → Initiatives organisationnelles

`Actions détectées` → `Initiatives organisationnelles`

### Ce que cette chaîne produit
- détection d’efforts temporaires structurés à partir du terrain.

### Exemple
Plusieurs actions liées à un déploiement, un pilote ou une transformation peuvent justifier une initiative.

## 10.8 Processus candidats → Processus

`Processus candidats` → `Processus`

### Ce que cette chaîne produit
- passage de la plausibilité fonctionnelle à la consolidation structurée.

### Exemple
Un fonctionnement devient processus officiel lorsqu’il présente :
- une finalité claire,
- un déclencheur,
- des inputs / outputs,
- une récurrence,
- une preuve suffisante de stabilité.

## 10.9 Pratiques → Capacités

`Pratiques organisationnelles` → `Capacités organisationnelles`

### Ce que cette chaîne produit
- passage du pattern opérant à l’aptitude durable.

### Exemple
Une pratique de coordination bien ancrée peut nourrir une capacité de coordination transverse robuste.

## 10.10 Principes → Pratiques

`Principes organisationnels` → `Pratiques organisationnelles`

### Ce que cette chaîne produit
- passage de l’intention normative à l’incarnation concrète.

C’est le cœur de la lecture **3P** :
- philosophie,
- principes,
- pratiques.

## 10.11 Problématiques → OKR → Indicateurs

`Problématiques` → `OKR` → `Indicateurs`

### Ce que cette chaîne produit
- transformation du diagnostic en objectif explicite,
- puis de l’objectif en système de mesure.

### Exemple
Une problématique de coordination transverse peut être traduite :
- en objectif piloté,
- puis en métriques de délai, de qualité ou de friction.

## 10.12 OKR → Initiatives

`OKR` → `Initiatives organisationnelles`

### Ce que cette chaîne produit
- passage du pilotage explicite à l’effort temporaire qui doit produire le changement.

## 10.13 Modulateurs ↔ Pratiques ↔ Capacités

`Modulateurs` ↔ `Pratiques organisationnelles` ↔ `Capacités organisationnelles`

### Ce que cette chaîne produit
- lecture des conditions d’effectivité,
- explication des plafonds,
- compréhension des variations de robustesse.

### Exemple
Une pratique pertinente peut exister mais rester peu efficace si :
- les règles de décision sont floues,
- le système de connaissances est pauvre,
- ou la coordination est peu outillée.

## 10.14 Environnements / Événements / Relations inter-organisations comme chaînes de contextualisation

`Environnements` + `Événements` + `Relations inter-organisations`

### Ce que cette chaîne produit
- contexte,
- trajectoire,
- et lecture écosystémique.

Cette chaîne ne “crée” pas directement le diagnostic ou le pilotage, mais elle donne leur **cadre de sens**.

## 10.15 Chaînes exploratoires de pré-consolidation

Le Twin comporte aussi des chaînes d’exploration, qui passent par les sandboxes.

### Exemples
- `Sources / analyses / observations` → `Capacités métier candidates (sandbox)` → `Capacités organisationnelles`
- `Enjeux / Problématiques / discussions de pilotage` → `OKR (sandbox)` → `OKR`
- `Actions / observations` → `Pratiques organisationnelles (sandbox)` → `Pratiques organisationnelles`
- `Valeurs / arbitrages / verbatims dirigeants` → `Principes organisationnels (sandbox)` → `Principes organisationnels`
- `Enjeux / signaux / premières consolidations` → `Problématiques (sandbox)` → `Problématiques`
- `Actions / premiers regroupements` → `Processus candidats (sandbox)` → `Processus candidats`

### Ce que ces chaînes produisent
- une **zone tampon d’exploration**,
- une **pré-consolidation réversible**,
- une **meilleure hygiène du graphe officiel**.

---

# 11) Les grands moteurs analytiques du Twin

Le Twin peut être lu selon plusieurs moteurs analytiques complémentaires.

Chaque moteur répond à une famille de questions.

## 11.1 Lecture structurelle

### BDD noyau
- `Organisations`
- `Collectifs`
- `Individus`
- `Postes`
- `Actifs`

### Question typique
> Qui existe dans le système, avec quelle structure, quels rattachements et quels supports ?

### Ce que cette lecture produit
- une carte de structure,
- une lecture du formel et du vivant,
- une base pour les analyses de responsabilité, couverture et dépendance.

## 11.2 Lecture du fonctionnement réel

### BDD noyau
- `Actions détectées`
- `Processus candidats`
- `Processus`
- `Pratiques organisationnelles`

### Question typique
> Comment cela fonctionne-t-il réellement, au-delà des organigrammes et des discours ?

### Ce que cette lecture produit
- compréhension des mécanismes réels,
- compréhension des patterns opérants,
- lecture des écarts entre procédure et pratique.

## 11.3 Lecture diagnostique

### BDD noyau
- `Journal des signaux`
- `Enjeux`
- `Problématiques`

### Question typique
> Qu’est-ce qui bloque, se tend, inquiète ou appelle une réponse ?

### Ce que cette lecture produit
- hiérarchisation des tensions,
- passage du diffus au structuré,
- formulation de nœuds diagnostiques.

## 11.4 Lecture normative (3P)

### BDD noyau
- `Principes organisationnels`
- `Pratiques organisationnelles`

### Cadre de lecture associé
- philosophie de l’organisation comme cadre conceptuel
- principes comme intentions stables
- pratiques comme incarnation réelle

### Question typique
> Ce que l’organisation dit vouloir guider se retrouve-t-il réellement dans le fonctionnement ?

### Ce que cette lecture produit
- lecture des écarts norme ↔ réel,
- compréhension des arbitrages implicites,
- distinction entre principe vivant et principe décoratif.

## 11.5 Lecture capacitaire

### BDD noyau
- `Capacités organisationnelles`
- `Pratiques`
- `Initiatives`
- `Indicateurs`

### Question typique
> Que sait durablement faire le système, que doit-il renforcer, et par quels leviers ?

### Ce que cette lecture produit
- cartographie des aptitudes collectives,
- lecture des écarts de maturité,
- articulation entre pratiques, transformation et montée en capacité.

## 11.6 Lecture contextuelle et temporelle

### BDD noyau
- `Environnements`
- `Événements`
- `Relations inter-organisations`

### Question typique
> Dans quel cadre et à quel moment tout cela prend-il sens ?

### Ce que cette lecture produit
- contexte,
- exposition,
- trajectoire,
- dépendance externe,
- effets de bascule.

## 11.7 Lecture de pilotage

### BDD noyau
- `OKR`
- `Initiatives organisationnelles`

### Question typique
> Que le système vise-t-il explicitement à transformer, et comment cela se traduit-il en action ?

### Ce que cette lecture produit
- clarté des intentions explicites,
- alignement entre diagnostic et action,
- lecture de la transformation vivante.

## 11.8 Lecture de mesure

### BDD noyau
- `Indicateurs`

### BDD liées
- `OKR`
- `Processus`
- `Pratiques`
- `Capacités`
- `Problématiques`
- `Collectifs`
- `Organisations`

### Question typique
> Qu’est-ce qui est réellement objectivé, et qu’est-ce qui reste angle mort ?

### Ce que cette lecture produit
- cartographie des zones mesurées,
- détection des angles morts,
- évaluation de la qualité du système de mesure.

## 11.9 Lecture 5D

### BDD support
Presque toutes les BDD significatives du Twin :
- structurelles,
- fonctionnelles,
- diagnostiques,
- normatives,
- capacitaires,
- pilotage / mesure.

### Question typique
> Où cet objet agit-il, dépend-il, expose-t-il ou mesure-t-il le système ?

### Ce que cette lecture produit
- une lecture transversale et comparable,
- une visualisation macro des zones du système,
- une capacité de synthèse inter-objets.

## 11.10 Lecture des conditions d’effectivité

### BDD noyau
- `Modulateurs`

### BDD satellites
- `Pratiques`
- `Capacités`
- `Actifs`
- `Organisations`

### Question typique
> Pourquoi certaines pratiques ou capacités tiennent-elles, plafonnent-elles ou échouent-elles ?

### Ce que cette lecture produit
- explication des variations d’effectivité,
- identification des plafonds systémiques,
- lecture des conditions de réussite ou de blocage.

## 11.11 Lecture calculée

### Supports
- rollups
- formules

### Question typique
> Quelles synthèses doivent apparaître sans relire manuellement toutes les fiches liées ?

### Ce que cette lecture produit
- profils agrégés,
- états synthétiques,
- signaux calculés,
- priorités lisibles,
- synthèses robustes sans duplication manuelle.

---

# 12) Les traversées analytiques à plus forte valeur

Le Twin devient particulièrement puissant lorsqu’on l’interroge non pas “table par table”, mais par **traversées**.

## 12.1 Structure formelle et structure vivante

### Traversée
`Organisation → Collectif → Poste → Individu`

### Ce qu’elle permet
- lire la structure institutionnelle,
- lire la structure opérante,
- voir les écarts entre structure formelle et couverture réelle,
- repérer vacance, multi-appartenance, surcharge ou dépendance à certaines personnes.

### Données à compiler
- hiérarchie organisationnelle,
- rattachements collectifs,
- postes couverts / vacants,
- individus occupant les postes,
- profils 5D agrégés d’exposition ou d’intervention.

## 12.2 Dépendances de fonctionnement

### Traversée
`Collectif / Processus / Pratique → Actif → Environnement`

### Ce qu’elle permet
- voir avec quoi le système fonctionne,
- dans quels cadres il fonctionne,
- où se concentrent les dépendances critiques,
- comment les supports et contextes façonnent le réel opérant.

### Données à compiler
- actifs mobilisés,
- criticité,
- substituabilité,
- environnements d’hébergement ou d’usage,
- fragilités 5D liées.

## 12.3 Écosystème externe

### Traversée
`Organisation → Relation inter-organisations → Organisation`

### Ce qu’elle permet
- lire coopération, fourniture, dépendance, régulation, co-développement, fusion,
- situer l’organisation dans son écosystème,
- comprendre les interdépendances structurantes.

### Données à compiler
- nature des relations,
- statut relationnel,
- ancienneté,
- réciprocité,
- événements associés,
- actifs ou initiatives liés si pertinent.

## 12.4 Transformation vivante

### Traversée
`Organisation / Collectif / Poste / Individu → Initiative → Événement`

### Ce qu’elle permet
- voir ce qui est réellement en cours,
- qui porte l’effort,
- quelles fonctions sponsorisent,
- quels jalons structurent la trajectoire.

### Données à compiler
- portage institutionnel,
- portage opératoire,
- sponsoring,
- état d’avancement,
- jalons,
- statuts temporels,
- actifs concernés,
- capacités renforcées.

## 12.5 Passage du brut à l’analytique

### Traversée
`Actions détectées → Processus candidats / Pratiques / Initiatives`

### Ce qu’elle permet
- comprendre comment la matière brute devient objet analytique,
- tester la cohérence des consolidations,
- éviter les glissements arbitraires.

### Données à compiler
- récurrence,
- granularité,
- niveau de processisation,
- intention dominante,
- orientation de consolidation probable,
- traces factuelles suffisantes ou non.

## 12.6 Chaîne diagnostic → pilotage

### Traversée
`Journal des signaux → Enjeux → Problématiques → OKR → Indicateurs`

### Ce qu’elle permet
- suivre la continuité entre perception, formulation, diagnostic, objectif et mesure,
- voir si le système traite réellement ce qu’il perçoit,
- repérer les ruptures de chaîne.

### Données à compiler
- signaux alimentant les enjeux,
- enjeux consolidés,
- problématiques adressées,
- OKR formulés,
- indicateurs réellement utilisés.

## 12.7 Qui porte réellement le système ?

### Traversée
`Collectifs ↔ Individus ↔ Postes ↔ Initiatives ↔ Pratiques`

### Ce qu’elle permet
- distinguer portage formel et portage réel,
- identifier les nœuds humains critiques,
- voir où repose la coordination,
- repérer héroïsation, centralité excessive ou fragilité de couverture.

### Données à compiler
- rôles de sponsor,
- couverture réelle des postes,
- pratiques incarnées,
- implication dans les initiatives,
- événements affectants,
- profils 5D d’intervention et d’exposition.

## 12.8 Où sont les angles morts de mesure ?

### Traversée
`Problématiques / Capacités / Pratiques / Processus / OKR → Indicateurs`

### Ce qu’elle permet
- voir ce qui est mesuré,
- ce qui n’est pas mesuré,
- ce qui n’est mesuré que par proxy faible,
- ce qui est piloté sans vraie instrumentation.

### Données à compiler
- relations de mesure,
- nature de couverture 5D,
- type d’usage de l’indicateur,
- baseline, cible,
- fréquence,
- objets non couverts.

## 12.9 Où agir en priorité ?

### Traversée
`Problématiques → Collectifs / Organisations affectés → Capacités en écart → OKR / Initiatives / Indicateurs`

### Ce qu’elle permet
- hiérarchiser les nœuds prioritaires,
- voir les objets touchés,
- évaluer si une réponse existe déjà,
- repérer les zones sans pilotage ou sans action.

### Données à compiler
- criticité,
- horizon,
- certitude,
- collectifs affectés,
- capacités en écart,
- OKR existants,
- initiatives actives,
- indicateurs de suivi.

## 12.10 Quelles pratiques développer pour faire monter une capacité ?

### Traversée
`Capacités → Pratiques → Modulateurs → Initiatives → Indicateurs`

### Ce qu’elle permet
- passer d’une capacité cible à des leviers concrets de développement,
- comprendre les conditions d’effectivité,
- proposer un chemin de montée robuste.

### Données à compile
r
- pratiques alimentantes,
- maturité actuelle / cible,
- criticité stratégique,
- modulateurs forts,
- initiatives de renforcement,
- indicateurs potentiels ou existants.

## 12.11 Une hypothèse mérite-t-elle de sortir du sandbox ?

### Traversée
`sandbox spécialisée → Sources d’informations → indices observés / indices d’existence → BDD officielle cible`

### Ce qu’elle permet
- décider si une hypothèse doit être promue,
- éviter les promotions trop précoces,
- garder le graphe officiel propre et utile.

### Données à compiler
- densité de preuve,
- cohérence sémantique,
- stabilité de la formulation,
- proximité avec des objets officiels existants,
- valeur analytique attendue après promotion,
- risques de doublon ou de confusion.

---

# 13) Gouvernance du Twin

## 13.1 Principes de qualité

Le Twin reste robuste si les règles suivantes sont respectées :

- une BDD ne doit pas compenser une ambiguïté conceptuelle non résolue ;
- une relation réelle n’est créée que si elle apporte une vraie valeur de lecture ;
- un rollup n’est gardé que s’il révèle une synthèse utile ;
- une formule n’est gardée que si elle produit un signal clair ;
- une sandbox ne doit jamais devenir une BDD parallèle semi-officielle ;
- une lecture 5D ne doit jamais remplacer la preuve primaire.

## 13.2 Règles de traçabilité

Toute fiche importante doit rester **réaudit-able** :
- par ses sources,
- par ses indices observés,
- par ses indices d’existence,
- par ses logs,
- et, si besoin, par ses traces de merge.

Le Twin assume qu’un diagnostic ou une lecture doit toujours pouvoir être :
- relu,
- questionné,
- justifié,
- recontextualisé.

## 13.3 Doctrine de merge et de consolidation

Le Twin distingue trois opérations très différentes :

### a) fusionner
Quand plusieurs fiches désignent réellement le même objet.

### b) consolider
Quand plusieurs entrées amont convergent vers un objet plus structuré :
- signaux → enjeu,
- enjeux → problématique,
- actions → processus candidat,
- actions → pratique.

### c) promouvoir
Quand une sandbox devient une BDD officielle.

Ces opérations ne doivent jamais être confondues.

## 13.4 Doctrine sandbox → BDD officielle

La promotion depuis une sandbox vers le Twin officiel doit rester explicite.

### Critères minimaux de promotion
- preuves suffisantes,
- formulation stabilisée,
- absence de confusion majeure avec un objet déjà existant,
- valeur analytique nette,
- cohérence avec la frontière conceptuelle de la BDD cible.

### Tableau de migration

| Sandbox | BDD officielle cible | Question de promotion |
|---|---|---|
| `Capacités métier candidates (sandbox)` | `Capacités organisationnelles` | cette capacité est-elle assez réelle, utile et stable pour entrer dans le référentiel capacitaire officiel ? |
| `OKR (sandbox)` | `OKR` | cet objectif est-il assez explicite, pilotable et distinct pour entrer dans la couche officielle de pilotage ? |
| `Pratiques organisationnelles (sandbox)` | `Pratiques organisationnelles` | ce pattern est-il assez récurrent, reconnaissable et utile pour être consolidé ? |
| `Principes organisationnels (sandbox)` | `Principes organisationnels` | cette intention normative est-elle assez stable, assumée et structurante pour devenir un principe officiel ? |
| `Problématiques (sandbox)` | `Problématiques` | cette formulation diagnostique est-elle assez consolidée pour devenir un nœud officiel du diagnostic ? |
| `Processus candidats (sandbox)` | `Processus candidats` | ce regroupement fonctionnel est-il assez cohérent pour entrer dans le pivot officiel ? |

## 13.5 Progressivité de remplissage

Le Twin n’est pas conçu pour être “plein” immédiatement.

Il est conçu pour être :
- densifié progressivement,
- testé en mission,
- requalifié à mesure que la preuve augmente,
- relu par traversées plutôt que rempli de façon uniforme.

### Conséquence
Toutes les BDD n’ont pas besoin du même niveau de densité au même moment.

Ce qui compte n’est pas :
- la complétude formelle uniforme,
mais :
- la qualité de ce qui est utile pour la question analytique du moment.

## 13.6 Conditions de cohérence globale du modèle

Le Twin reste cohérent si :
- le tableau maître canonique est tenu à jour,
- les frontières d’objets restent nettes,
- les sandboxes restent des sas et non des couches parallèles,
- les champs calculés restent sobres,
- les taxonomies restent stables et justifiées,
- les propriétés génériques restent spécialisées dans leur grammaire,
- et les relations réelles restent analytiquement rentables.

---

# 14) Résumé doctrinal

## 14.1 Ce que le Twin produit comme valeur systémique

Le Digital Twin LBP produit de la valeur parce qu’il rend l’organisation :

### Traçable
On peut remonter :
- d’un diagnostic à ses preuves,
- d’un objectif à ses raisons,
- d’une capacité à ses signes observés,
- d’une pratique à ses occurrences.

### Traversable
On peut passer :
- des acteurs aux fonctionnements,
- des fonctionnements aux supports,
- des signaux aux problématiques,
- des problématiques aux objectifs,
- des objectifs aux initiatives,
- des initiatives aux mesures,
- des objets aux contextes et au temps.

### Comparable
On peut comparer :
- des collectifs,
- des capacités,
- des pratiques,
- des environnements,
- des profils 5D,
- des couvertures de mesure,
- des formes de portage ou d’exposition.

### Diagnostique
On peut identifier :
- des écarts,
- des tensions,
- des vulnérabilités,
- des dépendances,
- des conditions d’effectivité,
- des angles morts de pilotage ou de mesure.

### Actionnable
On peut transformer le diagnostic en :
- leviers de pratiques,
- cibles de capacités,
- objectifs explicites,
- initiatives,
- et systèmes de mesure.

## 14.2 Ce qui fait sa robustesse

La robustesse du Twin vient de l’articulation entre :
- un tableau maître canonique,
- des frontières d’objets fortes,
- une séparation claire des régimes de connaissance,
- une doctrine relationnelle sobre,
- une couche 5D lisible,
- une couche calculée utile,
- et une gestion stricte des sandboxes.

## 14.3 Règles de lecture finales

Le Twin doit toujours être lu selon trois niveaux simultanés :

### Niveau 1 - ce qui existe
Objets, acteurs, supports, contextes, temps.

### Niveau 2 - ce qui se passe
Actions, pratiques, processus, signaux, enjeux, transformations.

### Niveau 3 - ce que cela signifie et ce qu’il faut en faire
Problématiques, capacités, principes, modulateurs, OKR, indicateurs.

## 14.4 Formule de synthèse

Le Digital Twin LBP est une architecture qui :

- distingue la **preuve**, la **qualification**, la **consolidation** et l’**action** ;
- rend visibles les objets de **structure**, de **fonctionnement**, de **diagnostic**, de **pilotage** et de **contexte** ;
- utilise les **relations réelles** quand elles créent une vraie valeur analytique ;
- conserve des **jumelles textes** pour préserver la traçabilité et l’optionalité de consolidation ;
- fait de la **5D** une matrice de lecture humaine macro, sans la confondre avec la preuve primaire ;
- utilise **rollups** et **formules** comme révélateurs d’écarts, de profils, de dépendances et de vulnérabilités ;
- traite les **sandboxes** comme des sas d’exploration sans relations réelles, sauf avec `Sources d’informations` ;
- transforme la matière du terrain en **diagnostic systémique**, puis le diagnostic en **pilotage, mesure et leviers d'action**.

En ce sens, le Digital Twin LBP n'est pas seulement une base "sur l'organisation".

---

# 15) Articulation avec le bundle docs méta (mai 2026)

Cette doctrine détaillée s'articule avec les autres docs du bundle de la façon suivante :

| Tu veux... | Va voir... |
|---|---|
| Comprendre l'écosystème complet (3 ensembles : Brain / Twin / Mission Ops) | `PANORAMA_LBP.md` |
| Comprendre les **doctrines transverses** (régimes de connaissance, isolation Brain ↔ Twin/MO, agnosticisme backend, propagation Markdown-first, hygiène d'écriture) | `DOCTRINE_LBP.md` |
| Voir le **modèle conceptuel synthétique** du Twin (tableau maître + cartographie objets + couches logiques) | `SPECS_ARCHITECTURE_TWIN_LBP.md` |
| Voir le modèle conceptuel des autres domaines | `SPECS_ARCHITECTURE_BRAIN_LBP.md`, `SPECS_ARCHITECTURE_MISSION_OPS_LBP.md` |
| Lookup d'une règle, décision ou workflow précis | `RULES_LBP.md` (R-XXX), `DECISIONS_LBP.md` (D-XXX), `WORKFLOWS_LBP.md` (WF-XXX) |
| Coder un nouvel objet selon la grammaire LBP | `CODIFICATION_LBP.md` |
| Propager une modification sans rien casser | `PROPAGATION_RULES_LBP.md` (cheat sheet) ou `WORKFLOWS_LBP.md` § WF-008 (détail) |

## 15.1 Évolutions doctrinales depuis le 22-04-2026

Cette doctrine était figée le 22-04-2026. Depuis, plusieurs évolutions structurantes ont été décidées et formalisées **hors de ce doc**, dans le bundle :

| Évolution | Capture | Lieu |
|---|---|---|
| Brain unifié au niveau modèle de données + isolation stricte Brain ↔ Twin/MO | D-019 | DECISIONS_LBP, DOCTRINE_LBP §2 |
| Architecture des 3 agents LBP (Brain architect / Twin architect / KONTEXT) | D-021 | DECISIONS_LBP, DOCTRINE_LBP §7 |
| Différenciation assumée des frontmatters Twin et Mission Ops | D-022 | DECISIONS_LBP |
| Mission Ops co-égal Brain/Twin + stack Notion (Brain) / Supabase (Twin+MO) | D-023 | DECISIONS_LBP, PANORAMA_LBP §4 |
| Codification universelle des objets Brain (table de préfixes) | R-054 | RULES_LBP, CODIFICATION_LBP |
| Frontmatter canon en 3 zones balisées | R-055 | RULES_LBP |
| Versioning X.Y sans PATCH | R-056 | RULES_LBP |
| Pas de jumelles texte sur Brain | R-058 | RULES_LBP |
| Hygiène d'écriture des docs Brain | R-059 | RULES_LBP |
| Lecture WR-RD obligatoire avant remplissage de fiches | C-017 | CLAUDE.md |
| Vérifier le régime de la BDD avant signaler une anomalie de relation | C-018 | CLAUDE.md |
| Workflow de propagation d'impacts formalisé | WF-008 | WORKFLOWS_LBP |
| Validation Phase B test Twin+MO sur scénario DeepSecAI v0 (51 fiches) | TEST_TWIN_OPS_PLAYBOOK | TEST_TWIN_OPS_PLAYBOOK.md |

Ces évolutions concernent surtout le **Brain**, **Mission Ops** et la **stack technique cible**. La doctrine Twin elle-même (régimes de structuration, chaînes de transformation, moteurs analytiques, traversées, gouvernance) **est restée stable** pendant les 8 jours et reste décrite ici de façon canonique.

---

> Doctrine Twin v4.0 - mise à jour 01-05-2026 post-bundle. Pour l'historique antérieur voir `Architecture data\00 - Docs méta\Doctrines & playbooks\00 - archives\Panorama V2 - ... v3 (archivé v3 le 01-05-2026).md`.

C’est une **machine de lecture systémique de l’organisation**.