---
# === Identité ===
"Doctrine de l'écosystème LBP"
doc_type: doc_meta
code: "CHRT_DOCTRINE_LBP"

# === Méta-gouvernance ===
version: "1.0"
template_code: "CHRT"
template_version: "1.0"
created_at: "01-05-2026"
updated_at: "01-05-2026"
status: "Validé"
scope: "LBP"

# === Spec d'usage ===
summary: "Synthèse narrative des 9 doctrines structurantes transverses qui sous-tendent l'écosystème LBP : régimes de connaissance, isolation Brain ↔ Twin/MO, agnosticisme backend, sandboxes, chaînes de transformation, Bricks pivot, 3 agents, propagation Markdown-first, hygiène d'écriture, pile d'orchestration."
purpose: "Expliquer le POURQUOI structurel, là où RULES_LBP énumère les règles atomiques (R-XXX) et DECISIONS_LBP archive les choix datés (D-XXX). Lisible d'une traite en 30 min."
tags:
  - doc_meta
  - doctrine
  - lbp
  - regimes_de_connaissance
  - isolation
  - propagation
  - hygiene_ecriture
---

# Doctrine de l'écosystème LBP

> **Scope** : 🟦 LBP - Bundle écosystème (durable, indexé dans BDD `Docs méta` du Brain).
> Synthèse narrative des **paradigmes structurants** qui sous-tendent l'écosystème LBP. Ce doc explique le **pourquoi**, là où `RULES_LBP.md` énumère les règles atomiques (R-XXX) et `DECISIONS_LBP.md` archive les choix datés (D-XXX).
> **Public visé** : nouveau dev (Clément, futurs collaborateurs), agents en re-contextualisation, toute personne qui doit comprendre la **logique d'ensemble** avant de modifier l'écosystème.
> **Format** : narratif. Lisible d'une traite, ~30 min de lecture.
> Dernière mise à jour : 01-05-2026 - création post-bundle.

---

## Préambule - pourquoi ce doc ?

LBP n'est pas une collection de règles arbitraires. C'est un **système** dont chaque règle (R-XXX) et chaque décision (D-XXX) découle d'un petit nombre de **paradigmes structurants**. Si tu comprends ces paradigmes, tu peux deviner la plupart des règles sans les avoir lues - et inversement, tu peux comprendre pourquoi telle règle existe et où elle s'applique.

Ce doc présente les **9 doctrines** qui structurent l'écosystème :
1. Les 4 régimes de connaissance
2. L'isolation Brain ↔ Twin/Mission Ops
3. L'agnosticisme backend
4. Les sandboxes comme sas d'exploration
5. Les chaînes de transformation de la connaissance
6. Les Bricks comme pivot documentaire
7. Les 3 agents et leurs frontières
8. La propagation Markdown-first
9. L'hygiène d'écriture

Chacune renvoie aux R-XXX et D-XXX qui en découlent.

---

## 1. Les 4 régimes de connaissance (R-012)

### La distinction fondamentale

LBP repose sur la séparation stricte entre **4 régimes de connaissance**, qui ne se mélangent jamais dans la même BDD :

| Régime | Nature | Exemples de BDDs |
|---|---|---|
| **Preuve** | Documentation primaire (sources, signaux, observations directes) | Sources d'informations, Journal des signaux |
| **Qualification** | Extraction et structuration de la matière brute | Actions détectées, Enjeux, Process candidats sandbox |
| **Consolidation** | Modélisation analytique stabilisée | Processus, Pratiques, Principes, Capacités, Problématiques |
| **Action** | Pilotage et mesure | OKR, Indicateurs, Initiatives organisationnelles |

### Pourquoi cette séparation est vitale

Mélanger les régimes produit des asymétries silencieuses : une fiche qui mêle preuve et consolidation devient impossible à auditer (« d'où ça sort ? » sans réponse fiable), à mettre à jour (« qu'est-ce qui change si la source évolue ? » indéterminé) et à dédoublonner (« 2 fiches qui parlent du même phénomène à des niveaux différents » impossibles à fusionner sainement).

### Conséquences pratiques

- Les BDDs **analytiques** (régime consolidation) **n'ont pas** de relation directe vers Sources d'informations. Leur traçabilité est **transitive** via les BDDs amont (C-018, D-009).
- Une fiche **sandbox** (régime qualification exploratoire) ne peut pas être reliée à une fiche **officielle** (régime consolidation) tant que son arbitrage n'a pas été fait - les sandboxes ne se relient qu'aux Sources (R-014).
- Toute production de connaissance dans LBP **passe par un parcours** preuve → qualification → consolidation → action (cf. §5 chaînes D-009).

### Règles dérivées
R-012 (séparation des 4 régimes), R-014 (sandboxes), C-018 (régime BDD avant audit relation).

---

## 2. L'isolation Brain ↔ Twin / Mission Ops (D-019, D-021)

### Le principe directeur

L'écosystème LBP est partitionné en **3 domaines co-égaux** :
- **Brain** = référentiel doctrinal (manuels, taxonomies, méthodes, templates, prompts, agents, outils). **Stable**, évolue **hors mission**.
- **Digital Twin** = représentation structurée d'une organisation cliente. **Instancié par mission**.
- **Mission Ops** = gouvernance opérationnelle de la mission elle-même. **Instancié par mission**.

### Pourquoi l'isolation est infranchissable

Pendant une prestation chez un client, **le Brain ne change pas**. Cette frontière est doctrinalement infranchissable parce que :
- Le Brain est l'outil de production LBP - il évolue par bumps cadrés (refontes), pas en flux de mission
- Un changement de Brain en cours de mission perturberait toutes les missions actives
- Les responsabilités sont distinctes : faire évoluer le Brain est un acte **méta-LBP** (gouvernance documentaire), pas un acte de mission

### Conséquences pratiques

- **Aucune relation Notion** ne lie directement les BDDs Brain aux BDDs Twin ou Mission Ops
- L'héritage se fait via les **Manuels de BDD** (qui décrivent les schémas Twin/MO mais vivent dans le Brain)
- Twin et MO **lisent** le Brain à l'instanciation (templates, méthodes, taxos, prompts) mais **n'écrivent jamais** dedans
- L'agent **KONTEXT** (orchestration MO, D-021) **ne peut pas** appeler **Brain architect**. Si KONTEXT identifie un besoin d'évolution Brain, il **flagge** une remontée à traiter hors mission, pas plus

### Règles dérivées
D-019 (Brain unifié + isolation), D-021 (3 agents avec frontière), R-058 (anti-jumelles texte Brain spécifique).

---

## 3. L'agnosticisme backend

### Le principe directeur

Les **manuels de BDD et templates** sont rédigés indépendamment du backend technique qui les implémente. Aujourd'hui c'est Notion, demain ça sera Supabase pour Twin/MO (D-023), peut-être autre chose dans 5 ans pour le Brain. Les manuels survivent à toutes ces migrations.

### Pourquoi cet agnosticisme

- Les manuels sont des **spécifications conceptuelles** (qu'est-ce qu'un Actif ? quelles sont ses propriétés sémantiques ?), pas des dumps DDL
- Mentionner Notion dans un manuel le couplerait à un outil transitoire
- Quand le backend change, on ne réécrit pas les manuels - on génère un nouveau DDL à partir d'eux

### Conséquences pratiques

- **Aucune mention de Notion** dans les templates et manuels de BDD (Twin, MO, Brain)
- Le formalisme est conceptuel : « relation bidirectionnelle de cardinalité 0..N », pas « propriété Notion de type relation avec dual mirror »
- Les exemples de codes restent agnostiques (`BRK_<mission>_<brick>_<discriminant>_<rev>`, pas « page Notion ID »)
- Les WR-RD eux-mêmes (Write Rules / Read Keys) sont écrits pour des agents qui peuvent lire Notion **ou Supabase** indifféremment

### Règles dérivées
R-001 (Markdown source de vérité), C-015 (vocabulaire Drive/Markdown distinct des liens Drive Google).

---

## 4. Les sandboxes comme sas d'exploration (R-014)

### Le principe directeur

Le Twin a 6 BDDs **sandboxes** spécialisées (Process candidats sandbox, Pratiques sandbox, Principes sandbox, Capacités candidates sandbox, OKR sandbox, Problématiques sandbox). Elles permettent d'explorer **sans engager** la modélisation officielle.

### Pourquoi des sandboxes

Modéliser une organisation cliente est un acte risqué - une mauvaise qualification crée des relations parasites qui polluent le Twin et faussent les lectures. Les sandboxes sont des **sas où on peut tester** une hypothèse (« cette pratique existe-t-elle vraiment ? ») avant de la promouvoir comme officielle.

### Conséquences pratiques

- Une fiche sandbox **ne peut pas** avoir de relations dures vers d'autres fiches Twin (sauf vers `Sources d'informations`)
- Les jumelles texte sont autorisées sur les sandboxes (relations « molles » qui préfigurent une relation officielle future)
- La promotion sandbox → officiel est un **acte explicite** du consultant : on crée la fiche officielle en s'appuyant sur la sandbox, puis on archive la sandbox
- Un agent qui audite une asymétrie de relations vérifie d'abord si la BDD est sandbox avant de signaler une anomalie

### Règles dérivées
R-014 (sandboxes), C-018 (régime BDD).

---

## 5. Les chaînes de transformation de la connaissance (D-009)

### Le principe directeur

La valeur du Twin n'est pas dans ses fiches isolées, mais dans les **chaînes** qu'il permet de tracer. Ces chaînes transforment progressivement la matière brute en lectures actionnables :

```
Sources ─────────────────────► toutes les BDDs documentées          [auditabilité]
Glossaire ────────────────────► extraction/consolidation             [clarté sémantique]
Journal signaux → Enjeux                                             [signal → stratégique]
Enjeux → Problématiques                                              [besoin → diagnostic]
Actions → Process candidats → Process                                [brut → structuré]
Actions → Pratiques organisationnelles                               [geste → pattern]
Actions → Initiatives organisationnelles                             [effort détecté]
Pratiques → Capacités                                                [pattern → aptitude durable]
Principes → Pratiques                                                [norme → incarnation, cœur 3P]
Problématiques → OKR → Indicateurs                                   [diagnostic → pilotage → mesure]
OKR → Initiatives                                                    [pilotage → action]
Modulateurs ↔ Pratiques ↔ Capacités                                  [conditions d'effectivité]
sandbox → Sources → indices → BDD officielle cible                   [exploration → promotion]
```

### Pourquoi ces chaînes

Sans chaînes, on aurait des silos : « voici les enjeux du client », « voici ses processus », « voici ses indicateurs » - mais aucun lien entre ces lectures. Avec chaînes, on peut répondre à des questions transverses : « cet indicateur reflète quel diagnostic, qui découle de quel enjeu, qui a été remonté par quel signal, qui vient de quelle source ? ».

### Conséquences pratiques

- Chaque BDD a un **régime amont** (d'où elle est alimentée) et **aval** (ce qu'elle alimente). Documenté en SPECS_TWIN_LBP §6.
- Les BDDs **analytiques** (régime consolidation) n'ont pas de Sources directes - leur preuve est **transitive** via les BDDs amont (C-018)
- Les **traversées analytiques à forte valeur** (cf. SPECS_TWIN_LBP §8) exploitent ces chaînes pour produire des lectures multi-couches : structure formelle + dépendances + diagnostic + pilotage

### Règles dérivées
D-009 (chaînes), R-012 (séparation régimes), C-018 (régime BDD avant audit).

---

## 6. Les Bricks comme pivot documentaire (D-018)

### Le principe directeur

Les **Bricks** sont l'unité documentaire pivot entre Mission Ops et Digital Twin. Elles sont :
- **Livrables MO** (output d'une `Action LBP`, traçables)
- **Notes avancées Twin** - peuvent détailler une fiche Twin (profil organisationnel, analyse 3P, livrable client)

### Pourquoi des Bricks

LBP produit beaucoup de documents pendant une mission (CR de meeting, profils organisationnels, analyses, livrables). Sans structure, ces docs sont éparpillés dans le Drive, non traçables, non réutilisables. Les Bricks rendent chaque document :
- **Codifié** (`BRK_<mission>_<brick>_<discriminant>_<rev>`, R-054 + grammaire G3)
- **Versionné** (`R01`, `R02`, ... - une nouvelle version crée une nouvelle Brick)
- **Tracé** (relié à l'Action LBP qui l'a produite, aux Sources qui le documentent, et éventuellement aux fiches Twin qu'il enrichit)
- **Réutilisable** (instancié à partir d'un `Template de Bricks` du Brain - `TPL_BRICK_*`)

### Conséquences pratiques

- Une Brick **toujours** reliée à une `Action LBP` qui l'a produite (`est produite par`)
- Une Brick **peut** être documentée par des `Sources d'informations` (`est documentée par`)
- Une Brick **peut** servir de note avancée d'une fiche Twin via le champ `Lien vers la note avancée` côté Twin
- Le Brick ID est l'identifiant pivot : nom du fichier `.md` sans extension, segments éclatés en propriétés (`mission_code`, `brick_code`, `Discriminant`, `rev`)

### Règles dérivées
D-018 (bricks = notes avancées Twin), R-054 (codification), CODIFICATION_LBP §4 (grammaire G3 bricks).

---

## 7. Les 3 agents et leurs frontières (D-021)

### Le principe directeur

LBP repose sur **3 agents IA spécialisés** avec des rôles strictement séparés :

| Agent | Rôle | Domaine d'évolution | Frontière |
|---|---|---|---|
| **Brain architect** | Évolution du Brain (manuels, taxos, méthodes, templates, prompts, etc.) | Activité méta-LBP, hors mission | Évolue le Brain |
| **Twin architect** | Modélisation Twin client (peuplement, dédoublonnage, qualification) | Activité de mission | Évolue le Twin client |
| **KONTEXT** | Orchestration de la mission (Mission Ops : meetings, actions, bricks) | Activité de mission | Évolue Mission Ops |

### Pourquoi ces 3 agents

Mélanger ces rôles produirait de l'incohérence :
- Si Brain architect intervenait pendant une mission, le Brain changerait sans gouvernance - risque doctrinal
- Si KONTEXT pouvait modifier le Twin directement, sans Twin architect, le Twin perdrait sa cohérence ontologique - risque de modélisation
- Si Twin architect pouvait modifier le Brain, on confondrait observation client et doctrine LBP

### Frontière infranchissable

> **KONTEXT ⊥ Brain architect** - KONTEXT ne peut pas appeler Brain architect.

Cette frontière garantit la **stabilité du Brain pendant les missions**. Si KONTEXT identifie un besoin d'évolution Brain (par exemple, un nouveau template de bricks utile), il **flagge une remontée** à traiter hors mission par Brain architect, mais ne le fait pas lui-même.

### Délégations autorisées

- KONTEXT → Twin architect : ✅ (mise à jour du Twin client = activité légitime de mission)
- Twin architect → Brain architect : ❌ (probable, à confirmer si le besoin émerge - même justification)

### Conséquences pratiques

- Les 3 fiches `Agents LBP` (`AGT_*`) à créer dans la BDD `Agents LBP` du Brain (post-Chantier P)
- Les system prompts respectent les frontières (un prompt Brain architect ne peut pas être appelé par KONTEXT)
- Toute évolution Brain en cours de mission est **flaggée**, pas faite

### Règles dérivées
D-021 (3 agents), D-019 (isolation Brain), R-XXX sur les frontières d'isolation à formaliser au moment de la création des 3 fiches.

---

## 8. La propagation Markdown-first (R-001 + R-041/042 + WF-008)

### Le principe directeur

> **Le doc Markdown du vault est la source de vérité unique. Tout dérivé (WR-RD, fiche Notion, indexation) est aligné sur lui, jamais l'inverse.**

### Pourquoi Markdown-first

- **Portabilité** : un Markdown survit à tout outil. Notion peut disparaître, le `.md` reste lisible
- **Versioning fin** : git versionne chaque caractère, Notion ne versionne pas finement
- **Auditabilité** : un agent peut lire un dossier de `.md` sans accès Notion
- **Traçabilité** : les renvois entre docs Markdown survivent aux backends

### Conséquences pratiques

La **propagation est strictement descendante** :

```
[Doc Markdown source de vérité]
        │
        ├── Manuel de BDD ─→ WR-RD (section 4 → sections 1-5) ─→ Notion (lien WR-RD)
        ├── Taxonomie ─→ Manuels qui la référencent ─→ WR-RD ─→ Notion (options select)
        ├── Note de concept ─→ Glossaire LBP Notion + Registre des notes de concept Notion (paire CPT/GLO)
        ├── Règle R-XXX (RULES_LBP) ─→ Docs concernés si format-impactante
        └── Décision D-XXX (DECISIONS_LBP) ─→ Mise à jour règles + manuels + ECOSYSTEM-STATE
```

Aucune propagation **remontante** : si tu vois une coquille dans un WR-RD, tu repasses par le manuel parent (R-041 - interdiction stricte).

Tout cycle de propagation est annoncé explicitement (C-009), tracé dans ECOSYSTEM-STATE (C-011), commit + push (C-013).

### Règles dérivées
R-001 (source de vérité), R-029 (indexation Notion), R-041 (propagation Manuel→WR-RD), R-042 (QA stricte d'égalité), C-009 (annonce), C-011 (ECOSYSTEM-STATE), C-013 (push), WF-008 (workflow exhaustif), PROPAGATION_RULES_LBP (cheat sheet).

---

## 9. L'hygiène d'écriture (R-055/056/058/059)

### Le principe directeur

Un doc bien écrit est **immédiatement utile à un agent** sans pré-traitement. Un doc mal écrit (bruit historique, spéculation future, frontmatter en soupe) gaspille du contexte agent et crée des ambiguïtés.

### Les 4 règles d'hygiène

1. **Frontmatter en 3 zones balisées (R-055)** : Identité / Méta-gouvernance / Spec d'usage. Permet à 3 agents distincts (gouvernance / maintenance / consommation) de lire ce qui les concerne sans soupe.

2. **Versioning X.Y sans PATCH (R-056)** : entiers naturels, séparateur `.`, pas de zéro-padding. Les bumps mineurs (X.Y → X.(Y+1)) sont fréquents ; les bumps majeurs (X.Y → (X+1).0) sont rares et déclenchent une migration au canon (WF-015).

3. **Pas de jumelles texte sur Brain (R-058)** : un champ texte qui doublonne une relation Notion crée de la désync. Sur le Brain, les relations sont structurelles ; sur le Twin, elles sont autorisées comme indices relationnels avant qualification.

4. **Hygiène d'écriture (R-059)** : chaque doc = source de vérité brute à l'instant t. **Pas de bruit historique** (« avant on faisait X mais maintenant Y ») : l'historique vit dans git + DECISIONS_LBP. **Pas de spéculation future** (« on pourrait éventuellement X ») : les pistes vivent dans le backlog.

### Pourquoi cette discipline

Un agent qui lit un manuel n'a pas le contexte historique. S'il voit « avant on faisait X », il ne sait pas si « avant » c'est il y a 1 jour ou 1 an, et ne peut pas distinguer ce qui est encore vrai. De même pour la spéculation future. Le doc doit être **vrai maintenant**, point.

### Conséquences pratiques

- Les commits git portent l'historique (changelog par phase)
- DECISIONS_LBP archive le « pourquoi tel choix » avec date
- ECOSYSTEM-STATE garde le journal vivant (C-011)
- Les manuels ne contiennent **que** ce qui est vrai au moment de la lecture
- La codification des codes doit elle-même respecter cette discipline (cf. CODIFICATION_LBP, anti-pattern §8)

### Règles dérivées
R-055 (frontmatter 3 zones), R-056 (versioning X.Y), R-058 (anti-jumelles texte Brain), R-059 (hygiène d'écriture), R-052 (apostrophes typographiques), R-044 (dates JJ-MM-YYYY).

---

## 10. La pile d'orchestration des prompts (Brain Motor)

### Le principe directeur

Quand un agent IA exécute une opération structurée dans LBP (génération de brick, contrôle qualité, déduplication, création de relations, etc.), il mobilise une **pile en couches** d'objets Brain Motor. Chaque couche apporte un niveau d'abstraction distinct, et toutes ne sont pas systématiquement traversées - mais le pattern est canonique.

### La pile en 6 couches

```
1. System prompt          - identité stable de l'agent (quel agent, quel rôle, quelles limites)
2. Prompt maître          - protocole général d'une opération (quelles étapes, quel ordre)
3. Logic block(s)         - logique locale opération × cible (comment qualifier un signal,
                            comment dédoublonner, comment traiter un cas limite)
4. Manuels / taxonomies   - vérité métier (structure, sens, contraintes des objets cibles)
5. Instructions écriture / clefs lecture (WR-RD) - cohérence champ par champ
6. Template de sortie     - forme du rendu (Brick, livrable, exports)
```

### Pourquoi cette pile

Sans cette stratification, chaque prompt deviendrait monolithique (tout dans un seul prompt géant) et impossible à maintenir. La pile permet :
- **Réutilisation** : un même Logic block sert plusieurs prompts maîtres
- **Cohérence** : les Manuels/WR-RD garantissent que tous les agents écrivent dans la même grammaire
- **Audit** : on peut tracer précisément quel composant produit quelle décision
- **Évolution indépendante** : on peut bumper un Logic block sans toucher le prompt maître qui le mobilise

### Conséquences pratiques

- Tous les prompts ne traversent pas toute la pile (pattern privilégié pour les opérations **structurées**, optionnel pour des opérations simples).
- Le **hub central** côté Notion est `Prompts LBP` qui porte 6 relations bidirectionnelles vers Méthodes / Logic blocks / Docs méta / Outils externes / Templates de bricks / Agents (cf. SPECS_ARCHITECTURE_BRAIN_LBP §6.1).
- Les 3 agents D-021 (Brain architect / Twin architect / KONTEXT) consomment chacun leur propre system prompt + prompts maîtres + logic blocks selon leurs domaines d'intervention.

### Règles dérivées
D-021 (3 agents), R-058 (anti-jumelles texte Brain), structure des BDDs Brain Motor (cf. SPECS_ARCHITECTURE_BRAIN_LBP §3).

---

## Conclusion - comment lire le reste du bundle

Tu connais maintenant les 9 doctrines. Voici comment elles éclairent les autres docs :

| Tu veux comprendre... | Va voir... |
|---|---|
| L'organisation macro de l'écosystème | `PANORAMA_LBP.md` |
| Le détail des 11 BDDs Brain | `SPECS_ARCHITECTURE_BRAIN_LBP.md` |
| Le détail des 28 BDDs Twin | `SPECS_ARCHITECTURE_TWIN_LBP.md` |
| Le détail des 4 BDDs Mission Ops | `SPECS_ARCHITECTURE_MISSION_OPS_LBP.md` |
| Une règle atomique précise | `RULES_LBP.md` (R-XXX) |
| Une décision archivée | `DECISIONS_LBP.md` (D-XXX) |
| Un workflow opérationnel | `WORKFLOWS_LBP.md` (WF-XXX) |
| Comment coder une nouvelle entrée | `CODIFICATION_LBP.md` |
| Comment propager une modification | `PROPAGATION_RULES_LBP.md` (cheat sheet) ou `WORKFLOWS_LBP.md` § WF-008 (détail) |

Et inversement : si tu vois une règle dans `RULES_LBP.md` que tu ne comprends pas, regarde quelle doctrine elle dérive (renvois en fin de section ci-dessus).

---

> Ce doc capture l'essence doctrinale de LBP. Il évolue lentement (bumps majeurs rares). Si une nouvelle doctrine émerge, elle est d'abord captée en R-XXX/D-XXX, puis intégrée ici à la prochaine refonte du doc.
