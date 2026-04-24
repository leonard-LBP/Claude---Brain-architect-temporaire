# Règles de gestion du Brain et du Digital Twin

> Ce fichier recense les règles **intrinsèques à l'écosystème LBP** (Brain + Twin + Mission Ops).
> Les règles contextuelles à notre collaboration (comportement de Claude, outillage) sont dans `CLAUDE.md` (IDs `C-XXX`).
> Chaque règle a un ID stable (`R-XXX`) qui ne change jamais, même si la règle déménage de section.
> Dernière mise à jour : 2026-04-24

---

## Format d'une règle

Chaque règle suit ce format pour homogénéité et lisibilité :

```markdown
### R-XXX : Titre court

- **Portée** : Brain / Twin / Mission Ops / Transverse
- **Statut** : Actif / En discussion / Archivé
- **Why** : Motivation (raison d'être, incident à l'origine)
- **How to apply** : Quand et comment appliquer concrètement
- **Exemples** : ✅ bon usage / ❌ mauvais usage
- **Découverte** : Date + contexte d'émergence
```

---

## Règles d'évolution de ce document (auto-restructuration)

Ces règles sont mes engagements pour maintenir la lisibilité du document à mesure qu'il grossit. Je les applique proactivement et je propose les restructurations — tu arbitres.

- **Stabilité des IDs** : l'ID `R-XXX` est immuable. On ne renumérote jamais, même si la règle déménage de section.
- **Déplacement** : si une règle change de section, on la déplace mais on garde l'ID. On note l'ancienne section dans le champ *Découverte* si utile.
- **Remplacement** : si une règle est supplantée, on marque l'ancienne `Archivé` (sans la supprimer) avec un pointeur vers la nouvelle.
- **Règle de scission** : si une sous-section dépasse ~8 règles, je propose de la scinder en sous-sous-sections thématiques.
- **Règle de promotion (inbox)** : dès que la section *À classer (inbox)* accumule 3+ entrées, je propose de les reclasser.
- **Règle de fusion / conflit** : si deux règles se chevauchent ou se contredisent, je le signale et je propose fusion, fusion partielle, ou révision avec archivage.
- **Housekeeping périodique** : à chaque milestone majeur (fin d'un gros chantier), je propose une revue structurelle du doc (ordre des sections, dénomination, détection de doublons).
- **Cohérence avec le backlog** : quand je promeus une règle du backlog vers ce doc, je laisse une trace dans le backlog (section historique).

---

## Sommaire

- [1. Règles transverses (gouvernance globale)](#1-règles-transverses)
- [2. Règles Brain](#2-règles-brain)
- [3. Règles Digital Twin](#3-règles-digital-twin)
- [4. Règles Mission Ops](#4-règles-mission-ops)
- [5. Règles de propagation d'impacts](#5-règles-de-propagation-dimpacts)
- [6. À classer (inbox)](#6-à-classer-inbox)

---

## 1. Règles transverses

*Règles qui s'appliquent à tout l'écosystème, indépendamment du domaine.*

### 1.1 Source de vérité et gouvernance

#### R-001 : Source de vérité = doc Markdown

- **Portée** : Transverse
- **Statut** : Actif
- **Why** : Éviter la divergence entre le contenu et son index. Le doc est portable, versionable, lisible IA ; Notion peut évoluer sans perte.
- **How to apply** : Pour modifier un objet, on modifie d'abord le doc MD, puis on aligne Notion. Jamais l'inverse.
- **Découverte** : Principe architectural originel.

> Les règles R-003 (confirmation humaine), R-009 (vault unique) et R-010 (git) ont été déplacées vers `CLAUDE.md` (IDs `C-001`, `C-002`, `C-003`) car elles relèvent de notre collaboration plutôt que de l'écosystème lui-même.

### 1.2 Zero contamination

#### R-002 : Zero donnée client dans Core / Motor

- **Portée** : Transverse (frontière Brain / Twin / MissOps)
- **Statut** : Actif
- **Why** : Le Brain est réutilisable entre missions. Contamination = perte de réutilisabilité.
- **How to apply** : Les domaines Core et Motor Brain ne contiennent jamais de données client. Seuls Digital Twin et Mission Ops sont instanciés par mission.
- **Exemples** : ✅ "Capacité Organisationnelle" dans Glossaire LBP / ❌ "Capacité Organisationnelle - Client X" dans Glossaire LBP
- **Découverte** : Principe architectural originel.

---

## 2. Règles Brain

*Règles spécifiques à la gouvernance du Brain (Core + Motor + Admin).*

### 2.1 Nommage et identification des objets

#### R-005 : Code unique stable

- **Portée** : Brain
- **Statut** : Actif
- **Why** : Référencement stable entre BDD, résistance aux renommages.
- **How to apply** : Le code unique d'un objet Brain (ex: `CPT.GOV.LBP.SSOT`) ne change jamais, même si le nom canonique évolue.
- **Découverte** : Règle initiale.

*Sous-section à enrichir quand on formalisera les conventions de nommage des nouveaux objets (actif, poste, collectif, etc.).*

### 2.2 Templates et instanciation

#### R-004 : Template obligatoire pour tout nouveau doc Brain

- **Portée** : Brain
- **Statut** : Actif
- **Why** : Homogénéité, gouvernance par les Docs méta, agents IA capables d'instancier.
- **How to apply** : Tout doc Brain est généré à partir d'un template (indexé dans Docs méta LBP). Cycle : Template → instanciation → cleanup → validation → indexation Notion.
- **Découverte** : Principe architectural originel.

### 2.3 Indexation Notion (doc → BDD)

#### R-006 : Descriptions Notion ≤280 caractères

- **Portée** : Brain
- **Statut** : Actif
- **Why** : Lisibilité Notion, cohérence inter-BDD, utilisabilité par les agents.
- **How to apply** : Les descriptions de propriétés dans Notion commencent par un verbe à l'infinitif, restent en texte brut, ne dépassent pas 280 caractères. On les copie directement depuis le manuel de BDD.
- **Découverte** : Convention établie dans les templates de manuels de BDD.

*Sous-sections à créer : conventions de lien source, règles de remplissage des rollups, etc.*

### 2.4 Gouvernance des taxonomies

#### R-007 : Taxonomies par codes

- **Portée** : Brain
- **Statut** : Actif
- **Why** : Séparer le stockage lisible (libellés) du référencement stable (codes).
- **How to apply** : Les BDD stockent des libellés humains. Les codes taxonomiques (ex: `OBJ.STATUT.LBP`) apparaissent uniquement dans les descriptions ≤280 et dans la documentation. Pas de codes dans le corps des textes.
- **Découverte** : Convention établie dans les templates.

#### R-008 : Statuts harmonisés

- **Portée** : Brain
- **Statut** : Actif
- **Why** : Uniformité de gouvernance à travers les 11 BDD Brain.
- **How to apply** : Toutes les BDD Brain utilisent la taxonomie `OBJ.STATUT.LBP` avec les valeurs `Brouillon`, `Validé`, `À revoir`, `Archivé`.
- **Découverte** : Convention établie.

### 2.5 Génération d'une BDD à partir d'un manuel

*Section à remplir quand on documentera le workflow "manuel de BDD → BDD Notion".*

### 2.6 Archivage des docs Brain

*Section à remplir quand on traitera l'archivage des docs obsolètes (UO, ressources, rôles officiels...).*

### 2.7 Relations inter-BDD Brain

*Section à remplir quand on formalisera les règles de relations (hub-spoke, miroirs, bidirectionnalité...).*

### 2.8 Hiérarchies et héritage

*Section à remplir quand on clarifiera les patterns d'héritage (notes de concept ← glossaire, manuels ← taxonomies, etc.).*

---

## 3. Règles Digital Twin

*Règles spécifiques à la gouvernance des BDD instanciées du Digital Twin.*

### 3.1 Instanciation

*Section à remplir quand on formalisera le workflow de création d'un Twin.*

### 3.2 Extraction / Post-traitement / Sandbox

*Section à remplir quand on clarifiera les règles par type fonctionnel de BDD.*

### 3.3 Relations inter-BDD Twin

*Section à remplir.*

---

## 4. Règles Mission Ops

*Règles spécifiques à la gouvernance de Mission Ops.*

### 4.1 Instanciation

*Section à remplir.*

### 4.2 Relations Twin ↔ Mission Ops

*Section à remplir — notamment la règle de monodirectionnalité Mission Ops → Twin sans miroir.*

---

## 5. Règles de propagation d'impacts

*Règles qui décrivent comment propager un changement à travers l'écosystème.*

### 5.1 Renommage d'un objet

*Section à remplir quand on traitera ressources→actifs, rôles officiels→postes, etc.*

### 5.2 Suppression / archivage d'une BDD

*Section à remplir quand on traitera l'archivage de l'ancienne UO.*

### 5.3 Modification d'une taxonomie

*Section à remplir.*

### 5.4 Mise à jour d'un template

*Section à remplir.*

---

## 6. À classer (inbox)

*Zone tampon pour les règles qui émergent mais dont la section définitive n'est pas encore évidente. À reclasser régulièrement.*

*(vide pour l'instant)*

---

## Annexe : règles archivées

*Règles qui ne sont plus actives, conservées pour traçabilité.*

*(vide pour l'instant)*
