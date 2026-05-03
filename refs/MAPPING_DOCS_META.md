# MAPPING_DOCS_META — Cartographie de la conversion des docs méta LBP

> **Scope** : 🟪 Session (collaboration Claude/Leonard, doc de chantier).
> **Statut** : Vivant — mis à jour au fil de Phase 4.
> **Vocation** : Servir de SoT temporaire pour piloter la conversion des docs méta legacy vers la nouvelle architecture (10 templates × 24 docs cibles). Le contenu structurant sera absorbé par `Constitution des docs méta - LBP` v1.0 en Phase 5, puis ce doc sera archivé.
> **Articulation** : C-027 (pas d'infos temporaires dans les SoT — celles-ci vivent ici), R-066 (propriétaire canonique unique), R-049 (taxonomies orthogonales).

---

## 1. Récap : 10 templates → 24 docs cibles

| # | Template | Code | Docs cibles produits | Réutilisation |
|---|---|---|---|---|
| 1 | TPL_META_PANORAMA | `TPL_META_PANORAMA` | 1 (Panorama) | Unique |
| 2 | TPL_META_CONSTITUTION | `TPL_META_CONSTITUTION` | 1 (Constitution des docs méta) | Unique |
| 3 | TPL_META_MANIFEST | `TPL_META_MANIFEST` | 2 (Philosophie + Profil) | Réutilisé 2× |
| 4 | TPL_META_CADRE | `TPL_META_CADRE` | 4 (LBP, Brain, Twin, MO) | Réutilisé 4× |
| 5 | TPL_META_PRINCIPES | `TPL_META_PRINCIPES` | 1 (Principes structurants) | Unique |
| 6 | TPL_META_CATALOGUE | `TPL_META_CATALOGUE` | 5 (Décisions, Règles, Codification, Workflows, Propagation) | Réutilisé 5× |
| 7 | TPL_META_SPECS_ARCHI | `TPL_META_SPECS_ARCHI` | 3 (Architecture Brain/Twin/MO) | Réutilisé 3× |
| 8 | TPL_META_INTERFACES | `TPL_META_INTERFACES` | 1 (Interfaces Brain↔Twin↔MO) | Unique |
| 9 | TPL_META_CHARTE | `TPL_META_CHARTE` | 3 (Rédac, Graphique, Sécurité & RGPD) | Réutilisé 3× |
| 10 | TPL_META_QC | `TPL_META_QC` | 3 (QC Brain/Twin/MO) | Réutilisé 3× |

**Pourquoi 10 templates pour 5 fonctions systémiques** : la fonction (Orienter/Expliquer/Structurer/Normer/Opérer) classe le **rôle** d'un doc, pas sa **structure**. Au sein d'une même fonction, deux docs peuvent avoir des structures profondément différentes (ex. dans `40-Normer/`, `Règles intrinsèques` = catalogue d'IDs atomiques vs `Charte rédactionnelle` = guidelines narratives). Inversement, plusieurs fonctions partagent parfois la même structure (`TPL_META_CATALOGUE` sert dans 20-Expliquer, 40-Normer et 50-Opérer).

---

## 2. Détail par doc cible

Statuts possibles : 🔴 à faire / 🟡 en cours / 🟢 fait.

### `10-Orienter/`

| # | Doc cible | Source(s) actuelle(s) | Logique de conversion | Points de vigilance | Statut |
|---|---|---|---|---|---|
| O.1 | `Panorama - LBP.md` | `PANORAMA_LBP.md` | Reprendre la vue 3 ensembles (Brain / Twin / MO) en intro, restructurer selon le canon TPL_META_PANORAMA. | Garder court (porte d'entrée). Renvoyer vers Cadres et Specs pour les détails. | 🔴 |
| O.2 | `Constitution des docs méta - LBP.md` | `Constitution des docs méta - LBP.md` v0.3 (déjà créée) | Refondre via TPL_META_CONSTITUTION ; intégrer le contenu de ce mapping en Phase 5. | Doc gouvernant tous les autres docs méta — exiger une revue spéciale. | 🟡 |
| O.3 | `Philosophie - LBP.md` | _from scratch_ (distillation possible de `DOCTRINE_LBP`) | Manifeste court (10-30 lignes) sur la posture LBP, ses convictions fondatrices. | Pas de contenu redondant avec Cadre LBP (qui explique le pourquoi structurel). | 🔴 |
| O.4 | `Profil - LBP.md` | _from scratch_ | Description du positionnement LBP (qui, quoi, pour qui), public visé, périmètre. | Distinguer de Philosophie (Profil = identité ; Philosophie = convictions). | 🔴 |

### `20-Expliquer/`

| # | Doc cible | Source(s) actuelle(s) | Logique de conversion | Points de vigilance | Statut |
|---|---|---|---|---|---|
| E.1 | `Cadre - LBP.md` | `DOCTRINE_LBP.md` (parties transverses) | Extraire les 9 doctrines transverses, restructurer en cadre narratif via TPL_META_CADRE. | Ne pas dupliquer ce qui ira dans Cadre Brain/Twin/MO. Identifier ce qui est vraiment transverse. | 🔴 |
| E.2 | `Cadre - Brain.md` | `DOCTRINE_LBP.md` (sections spécifiques Brain) | Extraire ce qui est propre au Brain (control plane, motor, core). | Risque : actuel `DOCTRINE_LBP` mélange transverse et Brain — désentrelacer proprement. | 🔴 |
| E.3 | `Cadre - Twin.md` | `DOCTRINE_TWIN_LBP.md` | Reprendre les régimes, chaînes, gouvernance Twin. | Doc déjà bien structuré, conversion légère via TPL_META_CADRE. | 🔴 |
| E.4 | `Cadre - Mission Ops.md` | _from scratch_ (extraction possible de `DOCTRINE_LBP`) | Construire à partir de zéro le cadre MO (livrables, opérations, articulation Twin↔MO). | Domaine moins documenté actuellement — préparer un brouillon avant template. | 🔴 |
| E.5 | `Principes structurants - LBP.md` | `DOCTRINE_LBP.md` (extraits principes) | Lister les principes atomiques (ex. zero contamination, R-001 SoT Markdown, etc.) en mode catalogue. | Distinguer Principes (énoncés courts axiomatiques) de Cadre (narration explicative). | 🔴 |
| E.6 | `Décisions architecturales - LBP.md` | `DECISIONS_LBP.md` | Conversion via TPL_META_CATALOGUE. Schéma item D-XXX : Contexte / Options / Décision / Conséquences / Date. | Schéma item à figer en publication v1.0. | 🔴 |

### `30-Structurer/`

| # | Doc cible | Source(s) actuelle(s) | Logique de conversion | Points de vigilance | Statut |
|---|---|---|---|---|---|
| S.1 | `Architecture - Brain.md` | `SPECS_ARCHITECTURE_BRAIN_LBP.md` | Restructurer via TPL_META_SPECS_ARCHI : modèle conceptuel des 11 BDDs + frontières + relations. | Appliquer R-XXX (b) — pointage enrichi vers fiches Notion + Drive pour chaque BDD. | 🔴 |
| S.2 | `Architecture - Twin.md` | `SPECS_ARCHITECTURE_TWIN_LBP.md` | Idem Brain mais 28 BDDs Twin + couche 5D + chaînes D-009. | Idem. | 🔴 |
| S.3 | `Architecture - Mission Ops.md` | `SPECS_ARCHITECTURE_MISSION_OPS_LBP.md` | Idem mais 4 BDDs MO. | Idem. | 🔴 |
| S.4 | `Interfaces Brain↔Twin↔MO.md` | _from scratch_ (extraction transverse des 3 SPECS) | Cataloguer les points de jonction inter-domaines (ex. relations Brain-gouverne-Twin, propagation MO→Twin, etc.). | Doc nouveau — structure à bâtir avec template TPL_META_INTERFACES. | 🔴 |

### `40-Normer/`

| # | Doc cible | Source(s) actuelle(s) | Logique de conversion | Points de vigilance | Statut |
|---|---|---|---|---|---|
| N.1 | `Règles intrinsèques - LBP.md` | `RULES_LBP.md` | Conversion via TPL_META_CATALOGUE. Schéma item R-XXX : Portée / Statut / Why / How / Articulation / Découverte. **Devient le nouveau réceptacle des futurs R-XXX.** | Schéma item à figer en v1.0. Recapter R-072 capturée 03-05-2026 dans le nouveau format. | 🔴 |
| N.2 | `Codification - LBP.md` | `CODIFICATION_LBP.md` | Conversion via TPL_META_CATALOGUE. Schéma item : Type d'objet / Format du code / Exemples / Anti-patterns. | Doc référentiel — vérifier exhaustivité au moment du bump. | 🔴 |
| N.3 | `Charte rédactionnelle - LBP.md` | _from scratch_ | Guidelines d'écriture transverses LBP : ton, structure, conventions de prose, tableaux, etc. | Risque doublons avec règles déjà dans RULES_LBP — extraire et migrer ce qui est rédactionnel. | 🔴 |
| N.4 | `Charte graphique - LBP.md` | _from scratch_ | Conventions visuelles : couleurs, icônes Notion, emoji conventions, mise en page docs. | Bas niveau de priorité tant que pas d'asset graphique standardisé. | 🔴 |
| N.5 | `Sécurité & RGPD - LBP.md` | _from scratch_ | Règles de manipulation des données client, anonymisation, accès, rétention. | Critique pour les missions client — bonne base avant prochain client. | 🔴 |
| N.6 | `Quality control - Brain.md` | _from scratch_ | Procédures d'audit du Brain : check-list de cohérence, automation possibles, fréquences. | Articuler avec Workflows opérationnels (les QC sont aussi des workflows). | 🔴 |
| N.7 | `Quality control - Twin.md` | _from scratch_ | Idem pour Twin (régimes, chaînes D-009, intégrité 5D). | Idem. | 🔴 |
| N.8 | `Quality control - Mission Ops.md` | _from scratch_ | Idem pour MO (livrables, opérations). | Idem. | 🔴 |

### `50-Opérer/`

| # | Doc cible | Source(s) actuelle(s) | Logique de conversion | Points de vigilance | Statut |
|---|---|---|---|---|---|
| Op.1 | `Workflows opérationnels - LBP.md` | `WORKFLOWS_LBP.md` | Conversion via TPL_META_CATALOGUE. Schéma item WF-XXX : Trigger / Préconditions / Étapes / Sortie / Garde-fous. **Devient le nouveau réceptacle des WF-XXX.** | Les workflows qui déclenchent une cascade citent les règles de propagation (ne les redéfinissent pas). | 🔴 |
| Op.2 | `Règles de propagation - LBP.md` | `PROPAGATION_RULES_LBP.md` | Conversion via TPL_META_CATALOGUE. Schéma item PROP-XXX : Source / Cible / Condition / Action de propagation / Audit. **SoT atomique des règles de cascade**, importé par Workflows opérationnels. | Articulation explicite avec Workflows pour éviter doublons (cf. décision à formaliser : doc N.x ci-dessous décrira PROP-XXX comme source unique). | 🔴 |

---

## 3. Bonnes pratiques de gestion de la connaissance pour les docs méta

Garde-fous à appliquer pendant la conversion. Ces bonnes pratiques seront formalisées en R-XXX dans `Règles intrinsèques - LBP` au fil de Phase 4 (capture déclenchée à la production de chaque template concerné, pas avant — sinon on pollue le catalogue de règles non encore applicables).

### 3.1 Stabilité temporelle (couvert par C-027, à appliquer)

Les docs méta SoT décrivent **l'état stable courant**, jamais le plan de migration ni le calendrier de production. Marqueurs proscrits : « (à créer) », « (à venir) », « (en attente de) », « (remplace) », « (provisoire) », mentions de versions passées ou d'hypothèses futures. Si une info est légitimement provisoire ou planifiée → vit dans `ECOSYSTEM-STATE.md` ou dans le commit message, pas dans la SoT.

### 3.2 Pointage croisé enrichi vers les entités de l'écosystème (à formaliser en R-XXX)

Quand un doc méta cite une entité (BDD, manuel, taxo, note de concept, doc méta, etc.), enrichir le pointeur :
- (i) **Nom canonique** (en wikilink Obsidian si entité ayant un `.md` source : `[[Nom canonique]]`)
- (ii) **Lien Notion** vers la fiche indexant l'entité (apporte les propriétés sans ouvrir le `.md`)
- (iii) **Lien Drive** vers le `.md` source (au cas où)

Bénéfice : un agent (ou humain) qui lit le doc peut décider sans ouvrir le `.md` si l'entité est pertinente, grâce aux propriétés Notion (statut, version, taxos liées). Et accéder au détail au besoin.

### 3.3 Schéma d'item atomique embarqué dans les docs CATALOGUE (à formaliser en R-XXX)

Tout doc instancié de TPL_META_CATALOGUE déclare en section 1 un sous-titre **« Anatomie d'un item »** qui figé le schéma de ses items atomiques (R-XXX, D-XXX, WF-XXX, PROP-XXX, entrée de codification, etc.). Format : Nom du champ / Type / Obligatoire ? / Description / Exemple. Le schéma est figé après publication v1.0 ; toute évolution = bump version + impact contrôlé sur les items existants.

### 3.4 Auto-suffisance des descriptions (couvert par R-071, à appliquer)

Décrire un doc par lui-même, pas par comparaison à un autre doc. Pas de « 11 sections vs 8 côté Twin/MO », pas de « contrairement à X ». Les distinctions essentielles → caractéristiques intrinsèques.

### 3.5 Pas d'énumération de taxons dans les instructions d'écriture (R-072, à appliquer)

Mentionner uniquement le code de la taxonomie (`Taxo: META.FUNCTION`) et le niveau (`Niveau: taxon`). Jamais énumérer les valeurs.

### 3.6 Wikilinks pour les renvois inter-docs LBP (C-024, à appliquer)

Utiliser systématiquement `[[Nom humain]]` pour citer un autre doc méta. Bénéfice : résilience au rename via Obsidian UI + indexation par recherche Obsidian.

### 3.7 Pas de panorama d'articulations dans les docs méta SoT (anti-asymétrie)

Ne PAS lister en prose dans un doc méta « ce doc cite X / est cité par Y / complète Z » sous forme de tableau panorama. Ce type de section crée un risque d'asymétrie systémique : si un doc cité évolue, les N docs qui le citaient en panorama deviennent silencieusement faux. La cartographie cross-cutting vit dans **3 endroits dédiés** :
- `[[Constitution des docs méta - LBP]]` (Annexe « Cartographie complète » en v1.0)
- **Backlinks Obsidian** (calculés automatiquement, cf. C-025)
- **Relations Notion** (machine-queryable)

Ce qui reste légitime dans un doc méta : (a) section « Périmètre Exclus » qui formalise l'application R-066 (« cet item ne va pas ici, voir [[doc cible]] »), et (b) section « Garde-fous de cohérence » optionnelle limitée à 2-6 règles structurelles concrètes (« si X dans ce doc, alors faire / ne pas faire Y dans le doc voisin ») — supprimable à l'instanciation si aucun garde-fou opérationnel n'existe.

**Découverte** : 03-05-2026, Leonard a flaggé l'anti-pattern dans le 1er jet de TPL_META_CATALOGUE qui contenait une section §3 « Articulation » avec tableau panorama.

### 3.8 Pas d'instructions transitoires dans les templates durables

Un template Brain est un artefact **durable** : il guide la production de docs sur des années, pour des cas d'usage qu'on ne connaît pas encore. Les instructions qu'il embarque doivent rester valides dans le temps.

Anti-pattern : embarquer dans le template une étape spécifique à un chantier en cours (ex. « scanner le doc legacy source » alors que les docs legacy n'existeront plus dans 6 mois). Cette étape doit vivre dans le **doc de chantier transitoire** (ex. ce mapping `MAPPING_DOCS_META.md`).

Règle pratique : pour chaque instruction du template, se demander « cette instruction sera-t-elle encore valide pour générer un doc dans 2 ans ? ». Si non → la déplacer dans le doc de chantier.

**Découverte** : 03-05-2026, Leonard a flaggé l'étape « scanner legacy » dans le 1er jet de TPL_META_CATALOGUE comme non durable.

### 3.9 Bonnes pratiques d'écriture EMBARQUÉES dans le doc canonique (pas dans le doc de chantier)

Les bonnes pratiques de gestion d'un type de doc (stabilité du schéma, traçabilité des items, cycle de vie, anti-patterns) doivent vivre **dans le template ET dans le doc canonique généré** (section dédiée type « Bonnes pratiques d'écriture du catalogue »). Pas seulement dans le doc de chantier (qui est transitoire).

Bénéfice : un consommateur du doc canonique (humain ou agent) trouve sur place les règles d'évolution du doc, sans avoir à consulter un autre doc qui aura disparu.

**Découverte** : 03-05-2026, Leonard a explicité la distinction « MAPPING transitoire vs templates durables ».

### 3.10 Niveau d'explicité attendu dans les templates : référence Manuel BDD Twin v7.0

Le pattern de référence pour le niveau d'explicité d'un template Brain est `Template - Manuel de BDD - Digital Twin.md` v7.0. Ses caractéristiques :
- `cleanup_rules` et `notes` directement dans le frontmatter du template (pas dans un bloc INSTR)
- Multiples blocs INSTR spécialisés en tête : `SETTINGS`, `FRONTMATTER_INSTANCE`, `FRONTMATTER_CONTROLLED_VOCAB`, `FRONTMATTER_DECISION_RULES`, `FRONTMATTER_EXAMPLES` — un bloc par concept structurant
- Plusieurs exemples concrets dans `FRONTMATTER_EXAMPLES` (un par variante d'instanciation)
- Section-by-section : chaque section structurante a son propre bloc INSTR à proximité avec but, règles, vocabulaire contrôlé

Anti-pattern : un seul gros bloc `TEMPLATE_USAGE_GUIDE` qui mélange tout (cas du 1er jet de TPL_META_CATALOGUE, refondu en v1.1).

**Découverte** : 03-05-2026, lors de la refonte de TPL_META_CATALOGUE après lecture du Manuel Twin pour calibrage.

---

## 4. Articulation avec la Constitution des docs méta - LBP

Ce mapping est **transitoire**. Son contenu structurant sera absorbé par `Constitution des docs méta - LBP` en Phase 5 (production v1.0 de la Constitution) :

| Section de ce mapping | Devient dans Constitution v1.0 |
|---|---|
| §1 récap 10 templates | Annexe : « Catalogue des templates META » |
| §2 détail par doc cible | Annexe : « Cartographie complète des docs méta » (24 entrées avec template, scope, propriétaire, fonction systémique) |
| §3 bonnes pratiques | Section dédiée + R-XXX dans `Règles intrinsèques - LBP` |
| §4 (cette section) | Supprimée (devient circulaire) |

Une fois la Phase 4 terminée et Constitution v1.0 publiée → ce mapping est archivé (R-053) dans le repo collab (pas dans le vault, scope Session).

---

## 5. Cycle de vie de ce mapping

- **Création** : 03-05-2026, fin Phase 3 close.
- **Mises à jour fréquentes** : à chaque conversion d'un doc legacy → mettre à jour le statut, ajouter les apprentissages dans §3 si nouvelles bonnes pratiques émergent, ajuster les logiques de conversion si on découvre des nuances.
- **Capture des règles** : quand un template TPL_META_X est produit en Phase 4, les R-XXX correspondantes (3.2, 3.3) sont enregistrées dans `Règles intrinsèques - LBP` (legacy `RULES_LBP.md` jusqu'à conversion N.1, puis `40-Normer/Règles intrinsèques - LBP.md`).
- **Absorption Constitution v1.0** : Phase 5.
- **Archivage** : après Phase 5, ce doc passe en `99-Archives/` du repo collab (ou supprimé).

---

## 6. Stratégie de séquencement (validée 03-05-2026)

### 6.1 Flow par template (interleaved + capture lessons learned)

Pour chaque template (dans l'ordre stratégique) :
1. Produire le template `.md` dans `Templates Brain/`
2. Indexer la fiche dans BDD Notion `Templates Brain`
3. Choisir 1 doc cible représentatif comme **calibrateur**
4. Instancier le template → produire le 1er doc canonique dans le bon dossier `10/20/30/40/50-`
5. Soumettre le doc à Leonard pour validation
6. Si correctif : ajuster le template + bump version + propager au doc
7. Si OK : produire les autres docs de la série (si template réutilisé) sans nouvelle validation lourde
8. **Capture lessons learned** : si une convention transverse aux 10 templates émerge, mettre à jour ce mapping (§3 bonnes pratiques) + appliquer aux templates non encore produits
9. Mettre à jour ECOSYSTEM-STATE + commit + push (vault + collab si besoin)
10. Passer au template suivant

### 6.2 Ordre stratégique des 10 templates

| Ordre | Template | Doc calibrateur | Pourquoi cet ordre |
|---|---|---|---|
| 1 | TPL_META_CATALOGUE | Règles intrinsèques - LBP | **Le plus impactant** : sert 5 docs cibles dont les nouveaux réceptacles de R-XXX, D-XXX, WF-XXX, PROP-XXX, codification. Une fois les 5 catalogues produits → toute capture future va directement vers le nouveau SoT (plus de cul-entre-deux-chaises avec docs legacy). Calibre aussi la convention « Anatomie d'un item ». |
| 2 | TPL_META_PANORAMA | Panorama - LBP | Simple, valide le pattern narratif |
| 3 | TPL_META_CADRE | Cadre - LBP | Réutilisé 4×, valide tôt avant scale |
| 4 | TPL_META_SPECS_ARCHI | Architecture - Brain | Réutilisé 3×, valide pattern pointage croisé enrichi (R-XXX §3.2 du mapping) |
| 5 | TPL_META_PRINCIPES | Principes structurants - LBP | Court, valide variante de catalogue |
| 6 | TPL_META_INTERFACES | Interfaces Brain↔Twin↔MO | Nouveau pattern |
| 7 | TPL_META_CHARTE | Charte rédactionnelle - LBP | Réutilisé 3×, valide pattern guidelines |
| 8 | TPL_META_QC | Quality control - Brain | Réutilisé 3×, valide pattern procédures |
| 9 | TPL_META_MANIFEST | Philosophie - LBP | Court, manifeste |
| 10 | TPL_META_CONSTITUTION | Constitution des docs méta - LBP v1.0 | En dernier : absorbe tout ce qu'on a appris |

### 6.3 Après les 10 templates

Capture d'une `Méthode - Génération d'un template Brain.md` dans `H:\Drive partagés\LBP - shared\Architecture data\Méthodes\` (sur la base de `Template - Méthode LBP.md`), indexée dans la BDD Notion `Méthodes LBP`. Capitalise tout ce qu'on aura appris pour future réplication (Clément, autres).

---

## 7. État du chantier (mis à jour en continu)

| Indicateur | Valeur |
|---|---|
| Docs cibles produits (sur 24) | 1/24 (Constitution v0.3, à raffiner) |
| Templates META produits (sur 10) | 1/10 (TPL_META_CATALOGUE v1.1, en validation) |
| Phase courante | Phase 3 close, Phase 4 à démarrer |
| Dernière mise à jour | 03-05-2026 |
