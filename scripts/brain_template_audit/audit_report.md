# Audit factuel des 11 manuels Brain — préparation du Template Brain

> **Scope** : Session (audit interne, support à la conception du Template Brain)
> **Date** : 27-04-2026
> **Périmètre** : 11 manuels Brain dans `H:\Drive partagés\LBP - shared\Architecture data\Manuels de BDD\Brain\`
> **Mode** : lecture seule, aucune modification
> **Données structurées** : voir `audit_data.json` (même dossier)

---

## 0. Liste des manuels audités

| # | BDD Brain | Fichier | Version FM | Scope déclaré (tags) |
|---|---|---|---|---|
| 1 | Manuels de BDD | `Manuel de BDD - Manuels de BDD.md` | 0.2.0 | core_brain, motor_brain |
| 2 | Registre des taxonomies | `Manuel de BDD - Registre des taxonomies.md` | 0.2.0 | core_brain, motor_brain |
| 3 | Prompts LBP | `Manuel de BDD - Prompts LBP.md` | 0.3.0 | motor_brain |
| 4 | Templates de bricks | `Manuel de BDD - Templates de bricks.md` | 0.2.0 | motor_brain |
| 5 | Méthodes LBP | `Manuel de BDD - Méthodes LBP.md` | 0.2.0 | motor_brain |
| 6 | Outils externes | `Manuel de BDD - Outils externes.md` | 0.2.0 | motor_brain |
| 7 | Docs méta LBP | `Manuel de BDD - Docs méta LBP.md` | 0.2.0 | motor_brain |
| 8 | Agents LBP | `Manuel de BDD - Agents LBP.md` | 0.2.0 | motor_brain |
| 9 | Registre des logic blocks | `Manuel de BDD - Registre des logic blocks.md` | 0.1.0 | motor_brain |
| 10 | Registre des notes de concept | `Manuel de BDD - Registre des notes de concept.md` | 0.1.0 | core_brain |
| 11 | Glossaire LBP | `Manuel de BDD - Glossaire LBP.md` | 0.1.0 | core_brain, motor_brain |

---

## 1. Structure du document — Sections H1

### 1.1 Tronc commun (factuel)

**Les 11 manuels respectent strictement la même séquence de 11 sections H1** :

```
1) Introduction et Contexte
2) Définition et rôle dans l'écosystème LBP
3) Architecture et structuration
4) Relations
5) Usages des taxonomies
6) Automatisations, formules, rollups
7) Paramétrage Notion - Ordre de mise en place
8) Gouvernance et maintenance
9) Checklist QA (GO / NO-GO)
10) Exemples d'utilisation
11) Bonnes pratiques et points de vigilance
```

Chaque H1 est suffixé du nom canonique de la BDD : `# 1) Introduction et Contexte - BDD <Nom>`. C'est rigoureusement homogène sur les 11.

### 1.2 Sous-sections H2 — patterns récurrents

| H2 | Présence | Notes |
|---|---|---|
| 1.1 Objet et finalité | 11/11 | |
| 1.2 Périmètre | 11/11 | Sous-structure interne (Inclus / Exclus / Règle de granularité) très récurrente |
| 2.1 Définition officielle | 11/11 | |
| 2.2 Rôle et utilité | 11/11 | |
| 3.1 Règles générales de remplissage | 11/11 | |
| 3.2 Champs (tableau unique) | 11/11 | Tableau à 9 colonnes canon |
| 3.3 Vues Notion recommandées | 11/11 | Sous-vues : Opérationnelles + Minimales (MVP). Méthodes ajoute "Vues QA" séparées. |
| 3.4 Workflows Motor Brain | 10/11 | Notes de concept utilise "Workflows Core Brain" (variante de scope) |
| 5.1 Principe + 5.2 Tableau | 11/11 | |
| 11.1 Bonnes pratiques + 11.2 Points de vigilance | 11/11 | |

**Verdict** : structure macro homogène. Variations mineures dans le wording des sous-sections (ex. "Workflows Motor Brain" vs "Workflows Core Brain").

---

## 2. Frontmatter actuel (à plat)

### 2.1 Champs frontmatter — comparatif

| Champ FM | Manuels | Registre tax. | Prompts | Templates | Méthodes | Outils | Docs méta | Agents | Logic blocks | Notes concept | Glossaire |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `title` | x | x | x | x | x | x | x | x | x | x | x |
| `doc_type` | x | x | x | x | x | x | x | x | x | x | x |
| `purpose` | x | x | x | x | x | x | x | x | x | x | x |
| `version` | 0.2.0 | 0.2.0 | 0.3.0 | 0.2.0 | 0.2.0 | 0.2.0 | 0.2.0 | 0.2.0 | 0.1.0 | 0.1.0 | 0.1.0 |
| `status` | draft | draft | draft | draft | draft | draft | draft | draft | draft | draft | draft |
| `tags` | x | x | x | x | x | x | x | x | x | x | x |

**Tous les 11 manuels** ont exactement les **6 mêmes champs FM** : `title`, `doc_type`, `purpose`, `version`, `status`, `tags`. Aucun manuel Brain ne déclare de champs structurants spécifiques (`bdd_canonical_name`, `object_type`, `architecture_scope`, `bdd_id_notion`, `template_version`) que l'on retrouverait côté Twin/MO. C'est l'**asymétrie majeure** vs Twin/MO et la cible de la Phase 4.

Tous les `doc_type` valent `db_manual`. Tous les `status` valent `draft`. Les versions oscillent entre `0.1.0` (3 manuels les plus récents) et `0.3.0` (Prompts).

### 2.2 Tags — patterns

- Tous portent `notion`, `db_manual`, `lbp`.
- Discriminant scope : `core_brain` et/ou `motor_brain`.
- Token spécifique du domaine (ex. `prompts_lbp`, `methodes_lbp`, `outils_externes`, `agents_lbp`, `logic_blocks`, `templates_bricks`, `docs_meta_lbp`, `glossaire_lbp`, `taxonomies`, `notes_de_concept`, `manuels_bdd`, `catalogue`, `registry`).

---

## 3. Section 4 — Propriétés (cœur du modèle)

> Note : dans les manuels Brain, les propriétés sont **dans la section 3.2** (et non `4.x` comme côté Twin v7). La section H1 `# 4) Relations` documente uniquement les relations. Cette différence est notable pour la conception du template — voir §7.

### 3.1 Propriétés strictement génériques (11/11)

| Propriété | Type Notion | Taxo | Notes |
|---|---|---|---|
| Nom canonique | Title | — | Universel |
| Code unique | Texte court | — | Préfixe spécifique par BDD (voir §3.4) |
| Statut de l'objet | Sélection | OBJ.STATUT | Universel |
| Created Date | Created time | — | Système |
| Last Updated Date | Last edited time | — | Système |

### 3.2 Propriétés quasi-génériques (10/11 — absentes uniquement dans `Registre des notes de concept`)

| Propriété | Type | Notes |
|---|---|---|
| Description | Texte long | Absent dans Notes de concept (minimalisme assumé) |
| Aliases | Texte long (liste `;`) | idem |
| Valeur ajoutée LBP | Texte long | idem |
| Usages IA potentiels | Texte long | idem |

Le **Registre des notes de concept est volontairement minimal** (pointeur pur vers la note source, pas de texte de synthèse) — c'est documenté dans son §3.1 "Minimalisme volontaire".

### 3.3 Propriétés partiellement génériques

#### Domaine(s) d'usage (multi-select Core/Motor/Digital Twin/Mission Ops)

| Manuel | Présence |
|---|---|
| Manuels de BDD | x (libellé "Domaine(s) d'usage" — déclaré "Spécifique") |
| Prompts LBP | x |
| Templates de bricks | x |
| Méthodes LBP | x |
| Outils externes | x |
| Docs méta LBP | absent (anomalie : n'apparaît pas dans le tableau 3.2 alors qu'attendu par cohérence) |
| Agents LBP | x |
| Glossaire LBP | x — mais limité à Core/Motor uniquement (pas DT/MO) |
| Registre des taxonomies | en rollup uniquement (`Domaine(s) d'usage (via manuels)`) |
| Notes de concept | en rollup uniquement (`Domaine(s) d'usage (rollup)` via Glossaire) |
| Logic blocks | absent |

→ Le champ existe en saisie directe pour 7 BDD, dérivé en rollup pour 2 BDD, absent pour 2.

#### Famille (taxo dédiée, niveau taxon)

| Manuel | Champ | Taxo |
|---|---|---|
| Templates de bricks | Famille de brick générée | BRICK.FAMILY |
| Méthodes LBP | Famille (Méthode) | MET.FAMILY |
| Outils externes | Famille (Outil externe) | OUT.FAMILY |
| Docs méta LBP | Famille (Doc méta) | META.FAMILY |
| Agents LBP | Famille (Agent) | AGENT.FAMILY |
| Glossaire LBP | Type de concept (3 valeurs strictes, pas une taxo formelle) |  — |
| Prompts LBP | Type de prompt + Rôle architectural (deux taxos hiérarchiques) | PROMPT.TYPE + PROMPT.ARCH_ROLE |

→ Pattern fort : **6 BDD Motor sur 11 ont un champ "Famille (X)" basé sur une taxo dédiée `<NS>.FAMILY` au niveau taxon**. Les autres ont des classifications spécifiques (Glossaire, Prompts) ou pas de famille (Manuels de BDD, Notes de concept, Taxonomies, Logic blocks).

### 3.4 Préfixes de codes (Code unique)

| BDD | Préfixe | Format |
|---|---|---|
| Manuels de BDD | `DBMAN_` | `DBMAN_NOM_BDD_CANON` |
| Registre des taxonomies | (pas de préfixe) | `NAMESPACE.FAMILLE` (ex. `OBJ.STATUT`) |
| Prompts LBP | `PROMPT-` | `PROMPT-[DOMAINE]_[SUJET]` |
| Templates de bricks | `TPL-BRICK_` | `TPL-BRICK_{BRICK_CODE}` |
| Méthodes LBP | `MET-` | `MET-[TOKEN]_[TOKEN]` |
| Outils externes | `OUT-` | `OUT-[TOKEN]_[TOKEN]` |
| Docs méta LBP | `META-` | `META-[TOKEN]_[TOKEN]` |
| Agents LBP | `AGENT-` (ou `AGENT_` selon exemples) | `AGENT_ROLE_DOMAINE` (incohérence interne) |
| Logic blocks | `LGBLK_` | `LGBLK_[OPERATION]_[CIBLE]` |
| Notes de concept | `CPT-` | `CPT-TOKEN` (partagé avec Glossaire) |
| Glossaire LBP | `CPT-` | identique aux notes de concept (clé pivot) |

**Anomalie repérée** : le manuel Agents LBP donne `AGENT_ROLE_DOMAINE` dans la description ≤280 mais `AGENT-ANALYSE_SYSTEMIQUE` en exemple → confusion underscore vs tiret pour le séparateur principal.

### 3.5 Rollups par BDD

| BDD | Rollups |
|---|---|
| Manuels de BDD | aucun |
| Taxonomies | Domaine(s) d'usage (via manuels) |
| Prompts LBP | 4 rollups Familles (bricks/méthodes/outils/docs méta) |
| Templates | Méthodes (via Prompts), Outils externes (via Prompts) |
| Méthodes | Outils externes mobilisés, Templates de bricks mobilisés |
| Outils | Agents mobilisés, Méthodes mobilisées, Templates mobilisés |
| Docs méta | 4 rollups (Agents, Outils, Templates, Méthodes) |
| Agents | 4 rollups (Méthodes, Docs méta, Outils, Templates) |
| Logic blocks | Nb prompts liés, Nb manuels adressés |
| Notes de concept | Domaine(s) d'usage (rollup) |
| Glossaire | Lien note concept (rollup) |

→ Tous les rollups Motor passent **par le hub Prompts** (les spokes voient leurs cousins via le hub). Conformité totale à la doctrine hub-and-spoke pour 8 BDD Motor.

---

## 4. Section 5 — Architecture relationnelle

Côté Brain, la **section H1 = `# 4) Relations`** (équivalent fonctionnel d'une "architecture relationnelle"). Elle est présente dans les 11 manuels avec un tableau canonique : nom propriété, Type, Direction, BDD cible, Propriété miroir, Cardinalité cible, Règles, Notes.

### Doctrine relationnelle observée — 4 patterns

1. **Hub-and-spoke standard (5 BDD spokes)** : Templates, Méthodes, Outils, Docs méta, Logic blocks → hub Prompts. Spoke porte `est utilisé dans (Prompts LBP)` ↔ hub porte `utilise (X)`.

2. **Cas particulier Agents** : sens inversé. Agents LBP porte `utilise (Prompts LBP)` ↔ hub porte `est utilisé par (Agents LBP)`. C'est explicitement justifié par la sémantique (un agent consomme un prompt, alors qu'un template est consommé par un prompt).

3. **Relation transversale Brain (justifiée)** : `Manuels de BDD ↔ Registre des taxonomies`, bidirectionnelle, hors hub Prompts. Justifiée par la QA et l'héritage de Domaine(s) d'usage via rollup.

4. **Doctrine Glossaire (exception assumée)** : relations **monodirectionnelles** vers Notes de concept, Méthodes LBP, Manuels de BDD ; miroirs non exposés. Auto-relation `est lié à (concepts)` autorisée.

### Anomalies / dettes relationnelles

- **Logic blocks → Manuels de BDD** : relation `s'applique à (Manuels de BDD)` monodirectionnelle, sans miroir documenté côté Manuels de BDD. C'est une **relation spoke vers spoke** que la doctrine Prompts interdit par défaut. Documentée comme exception, mais asymétrique : à reconsidérer en Phase 4.
- **Glossaire → Méthodes LBP** : relation directe `est mis en oeuvre par (méthodes LBP)`, hors hub Prompts. Idem **spoke→spoke** assumé.

---

## 5. Sections 6-8

### 5.1 Section 5 (Usages des taxonomies)

Présent dans les 11 manuels avec structure homogène : `5.1 Principe` (rappel des règles d'or : codes en MAJUSCULES, pas stockés dans la donnée, apparaissent dans les ≤280) + `5.2 Tableau` (Propriété consommatrice, Code taxo, Niveau, Usage select/multi, Sortie, Indices, Exemples IN/OUT, Notes).

### 5.2 Section 6 (Automatisations, formules, rollups)

11/11. Tableau (Champ, Type, Description, Règle/formule, Dépendances, Editable). Lignes minimales communes : Created Date, Last Updated Date. Lignes additionnelles selon les rollups de la BDD.

### 5.3 Section 7 (Paramétrage Notion — Ordre de mise en place)

11/11. Séquence canonique : 1) propriétés génériques → 2) propriétés spécifiques → 3) relations → 4) rollups → 5) vues → 6) test minimal avant GO.

### 5.4 Section 8 (Gouvernance et maintenance)

11/11. Structure : Owner / Contributeurs / Routines (Hebdo / Mensuelle / Trimestrielle) / Garde-fous.

### 5.5 Section 9 (Checklist QA GO/NO-GO)

11/11. Liste de checks `[ ]` + bloc "Micro-check post-génération".

### 5.6 Section 10 (Exemples) et 11 (Bonnes pratiques + Points de vigilance)

11/11. Toujours 3 exemples fictifs (sans contenu client) numérotés 10.1/10.2/10.3.

---

## 6. Taxonomies consommées

### 6.1 Tableau croisé Manuels × Taxos

| Manuel | OBJ.STATUT | Famille (X.FAMILY) | Autres taxos |
|---|---|---|---|
| Manuels de BDD | x | — | — |
| Registre des taxonomies | x | — | — (sélections internes : Ouverture, Nature sémantique, Mode de sélection, Niveaux autorisés) |
| Prompts LBP | x | — | PROMPT.TYPE, PROMPT.ARCH_ROLE, PROMPT.DEPLOY_STATUS, PLATFORM.ENV |
| Templates de bricks | x | BRICK.FAMILY | — |
| Méthodes LBP | x | MET.FAMILY | — |
| Outils externes | x | OUT.FAMILY | — |
| Docs méta LBP | x | META.FAMILY | — |
| Agents LBP | x | AGENT.FAMILY | — |
| Logic blocks | x | — | — (V1 minimaliste) |
| Notes de concept | x | — | — |
| Glossaire LBP | x | — | — (Type de concept = sélection interne, pas une taxo) |

### 6.2 Synthèse

- **Taxo strictement transverse** : `OBJ.STATUT` (11/11). Seule taxonomie systématiquement présente, candidate génériques absolue du Template Brain.
- **Pattern Famille spécifique** : 5 BDD Motor (Templates, Méthodes, Outils, Docs méta, Agents) ont chacune leur taxo `<NS>.FAMILY`. Pas d'unification possible — c'est le sens même du domaine.
- **Prompts LBP est l'exception** : 4 taxos additionnelles, signe de sa nature de hub orchestrateur.

---

## 7. Synthèse pour la conception du Template Brain

> **Section interprétative** — distincte des constats factuels ci-dessus.

### 7.1 Champs frontmatter génériques (à intégrer dans le futur Niveau B)

Recommandation, par ordre de priorité :

1. **Champs FM minimaux actuels (11/11)** : `title`, `doc_type` (= `db_manual`), `purpose`, `version`, `status`, `tags`. Conserver.
2. **Champs FM structurants à ajouter (Phase 4)** — alignement sur Twin/MO :
   - `bdd_canonical_name` (nom de la BDD Notion décrite, ex. "Prompts LBP")
   - `bdd_id_notion` (UUID Notion)
   - `architecture_scope` (= `Brain`)
   - `brain_layer` (= `Core` | `Motor` | `Core+Motor`) — discriminant interne au scope Brain, déduit des tags actuels
   - `object_type` (= `catalogue` | `registre` | `hub` | `spoke` | `glossaire` | `notes_source`)
   - `template_version` (= version du futur template Brain)
3. **Champs FM optionnels** :
   - `code_prefix` (ex. `PROMPT-`, `MET-`, `LGBLK_`) — utile pour la QA automatisée

### 7.2 Champs frontmatter optionnels selon type de BDD Brain

Le scope Brain comporte au moins **6 sous-types fonctionnels** :

| Sous-type | Exemples | Particularités |
|---|---|---|
| `catalogue` | Manuels de BDD | Index transverse |
| `registre_pivot` | Taxonomies, Notes de concept, Logic blocks | Minimaliste, pointeurs vers source de vérité |
| `hub` | Prompts LBP | Orchestrateur central, ~6 relations sortantes |
| `spoke_motor` | Templates, Méthodes, Outils, Docs méta, Agents | 1 relation vers hub Prompts + rollups remontants |
| `glossaire` | Glossaire LBP | Doctrine relationnelle particulière (monodir) |
| `meta_brain` | (potentiel futur) | — |

→ Le template Brain devra **factoriser le commun** et permettre **modulariser le spécifique** par sous-type via un champ `brain_subtype` dans le FM.

### 7.3 Sections corps — recommandation

Conserver la **structure 11 sections H1** actuelle (très solide, 11/11). Le template doit :
- Préserver la séquence 1 → 11.
- Documenter dans le commentaire de chaque section H1 ce qui est obligatoire vs optionnel selon `brain_subtype`.
- Pour `# 3.2 Champs`, fournir un **tableau de propriétés génériques pré-remplies** (les 5+4 = 9 propriétés génériques/quasi-génériques identifiées au §3.1-3.2), avec les ≤280 standardisés.
- Pour `# 4) Relations`, fournir des **patterns de relations selon le sous-type** : hub, spoke standard, spoke inversé (cas Agents), monodir (cas Glossaire), transversale Brain.
- Pour `# 5) Usages des taxonomies`, ligne pré-remplie pour `OBJ.STATUT` + slot pour la taxo `<NS>.FAMILY` du domaine.

### 7.4 Anomalies de cohérence détectées (à anticiper en Phase 4)

1. **Champ Domaine(s) d'usage non systématique** : présent dans 7/11 en saisie directe, absent dans Docs méta LBP (anomalie : devrait y être par cohérence avec Templates/Méthodes/Outils/Agents).
2. **Format du préfixe Agents** : description ≤280 dit `AGENT_ROLE_DOMAINE` (underscore) mais l'exemple donne `AGENT-ANALYSE_SYSTEMIQUE` (tiret). À trancher.
3. **Granularité sémantique du champ "Famille"** : 5 nommages différents (Famille de brick générée / Famille (Méthode) / Famille (Outil externe) / Famille (Doc méta) / Famille (Agent)). Choisir : harmoniser en `Famille (<scope>)` partout, ou conserver les nommages en place ?
4. **Logic blocks → Manuels de BDD** : relation spoke vers spoke monodir sans miroir documenté côté Manuels. À documenter explicitement comme exception OU à requalifier.
5. **Glossaire** : doctrine monodirectionnelle complète, divergente du standard hub-and-spoke. À assumer comme exception explicite OU à propager (peu probable, doctrine spécifique).
6. **Versions FM hétérogènes** : `0.1.0` à `0.3.0`. La Phase 4 / régénération via template Brain devra réinitialiser les versions de manière cohérente.
7. **Manuel Notes de concept volontairement minimal** (pas de Description, Aliases, Valeur ajoutée, Usages IA) : **à respecter** dans le template Brain — créer un sous-mode `registre_minimaliste` qui désactive les champs génériques optionnels.
8. **Manuel Registre des taxonomies** : exemples résiduels Phase 3 dette mineure (lignes 67/82/214 : référence à `NAMESPACE.FAMILLE.LBP` ; ligne 91 : alias `OPS.EXEC_STATUS`). Hors scope audit (déjà signalé par Leonard).
9. **Manuel Glossaire** : `BDD concernées (texte)` est un champ texte libre dupliquant partiellement la relation `est modélisé par (Manuels de BDD)` — risque d'asymétrie, à arbitrer.
10. **Section 3.4 Workflows** : "Motor Brain" pour 10/11, "Core Brain" pour Notes de concept. Le template doit prévoir un placeholder dynamique selon `brain_layer`.

### 7.5 Données structurées

Le fichier `audit_data.json` (même dossier) contient le détail programmatique : par manuel, frontmatter complet, listes de propriétés génériques/spécifiques/rollups, taxos consommées, relations avec direction et miroirs, particularités. Exploitable pour générer les sections du futur Template Brain ou des contrôles QA automatisés.

---

## Pointeurs

- Manuels source : `H:\Drive partagés\LBP - shared\Architecture data\Manuels de BDD\Brain\`
- Templates existants à comparer : `Template - Manuel de BDD - Digital Twin.md` (v7.0), `Template - Manuel de BDD - Mission Ops.md` (v6.0)
- Cible : `Template - Manuel de BDD - Brain.md` (à créer)
- Données structurées de cet audit : `scripts/brain_template_audit/audit_data.json`
