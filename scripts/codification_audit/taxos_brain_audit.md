# Audit ciblé — Taxonomies qui régissent les types d'objets du Brain

> **Date** : 27-04-2026
> **Scope** : 🟪 Session (préparation codification universelle des objets LBP)
> **Méthode** : lecture seule du dossier `Taxonomies/` (hors `00 - archives/`) + croisement avec les manuels Brain (`Manuels de BDD/Brain/`).
> **Périmètre** : taxos « Brain-related » uniquement (méta-objets de l'écosystème). Taxos Twin métier (CAP/ENJ/ORG5D/ACT/EVT/INDIC/SCALE/SIG/SRC/STAKEHOLDER…) explicitement exclues.

---

## 1) Inventaire des taxos Brain-related

| # | namespace_code | canonical_name | Statut | Sélection | Nb taxons | Manuel(s) Brain consommateur(s) |
|---|---|---|---|---|---:|---|
| 1 | `OBJ.STATUT.LBP` | Statut de l'objet | Actif (fermée, 4 v.) | mono | 4 | **Tous les 11 manuels Brain** (transverse) |
| 2 | `OBJ.CONFIDENTIALITE.LBP` | Niveau de confidentialité | Actif (fermée, 4 v.) | mono | 4 | Aucun manuel Brain ne le consomme actuellement (pas trouvé) — orphelin |
| 3 | `META.FAMILY.LBP` | Famille de doc méta | Actif (fermée, 8 v.) | mono | 8 | `Manuel de BDD - Docs méta LBP.md` |
| 4 | `BRICK.FAMILY.LBP` | Famille de Brick | Actif (fermée, 10 v.) | mono | 10 | `Manuel de BDD - Templates de bricks.md` |
| 5 | `MET.FAMILY.LBP` | Famille de méthode | Actif (fermée, 9 v.) | multi | 9 | `Manuel de BDD - Méthodes LBP.md` |
| 6 | `OUT.FAMILY.LBP` | Famille d'outil externe | Actif (fermée, 7 v.) | multi | 7 | `Manuel de BDD - Outils externes.md` |
| 7 | `AGENT.FAMILY.LBP` | Famille d'agent | Actif (fermée, 6 v.) | mono | 6 | `Manuel de BDD - Agents LBP.md` |
| 8 | `PROMPT.TYPE.LBP` | Type de prompt | Actif (fermée, 8 v.) | mono | 8 | `Manuel de BDD - Prompts LBP.md` |
| 9 | `PROMPT.ARCH_ROLE.LBP` | Rôle architectural des prompts | Actif (fermée, 4 v.) | mono | 4 | `Manuel de BDD - Prompts LBP.md` |
| 10 | `PROMPT.DEPLOY_STATUS.LBP` | Statut de déploiement des prompts | Actif (fermée, 4 v.) | mono | 4 | `Manuel de BDD - Prompts LBP.md` |
| 11 | `PLATFORM.ENV.LBP` | Environnement de déploiement plateforme | Actif (fermée, 5 v.) | multi | 5 | `Manuel de BDD - Prompts LBP.md` |

**Détail des valeurs (taxons)** :

- `OBJ.STATUT.LBP` : `BROUILLON`, `VALIDE`, `A_REVOIR`, `ARCHIVE`
- `OBJ.CONFIDENTIALITE.LBP` : `PUBLIC`, `INTERNE`, `INTERNE_RESTREINT`, `TRES_SENSIBLE`
- `META.FAMILY.LBP` : `NAMING_CONVENTIONS`, `QUALITY_QA`, `CHARTS`, `WORKFLOWS_PLAYBOOKS`, `TOOLING_RULES`, `TEMPLATE_RULES`, `DATA_MODEL_RULES`, `SECURITY_PRIVACY`
- `BRICK.FAMILY.LBP` : `PROFIL`, `MEETING`, `COMPTE_RENDU`, `ANALYSE`, `LIVRABLE`, `CORRESPONDANCE`, `SOURCES`, `GLOSSAIRE`, `SOCLE_CLIENT`, `SOCLE_MISSION`
- `MET.FAMILY.LBP` : `COLLECTE_ENTRETIEN`, `STRUCTURATION_MODELE`, `ANALYSE_DIAGNOSTIC`, `SYNTHESE_FORMALISATION`, `RECOMMANDATION_DECISION`, `PLANIFICATION_ROADMAP`, `QUALITE_QA`, `GOUVERNANCE_ECOSYSTEME`, `PUBLICATION_COMMUNICATION`
- `OUT.FAMILY.LBP` : `DOCUMENT`, `PRESENTATION`, `DATA`, `VISUALISATION`, `COLLABORATION`, `COMMUNICATION`, `AUTOMATION`
- `AGENT.FAMILY.LBP` : `ANALYSE`, `GENERATION_BRICKS`, `MISSION_OPS`, `GESTION_DIGITAL_TWIN`, `MARKETING_COMMUNICATION`, `ADMIN_LBP`
- `PROMPT.TYPE.LBP` : `GENERATION_BRICK`, `GESTION_DIGITAL_TWIN`, `CREATION_RELATIONS`, `DEDUP_CONSOLIDATION`, `CONTROLE_QUALITE`, `IDEATION_ASSISTEE`, `CONVERSION_RENDU`, `ROUTAGE_SELECTION`
- `PROMPT.ARCH_ROLE.LBP` : `SYSTEM_PROMPT`, `PROMPT_EXECUTION`, `PROMPT_MAITRE`, `TEMPLATE_PROMPT`
- `PROMPT.DEPLOY_STATUS.LBP` : `NOT_DEPLOYED`, `DEPLOYED`, `SUSPENDED`, `RETIRED`
- `PLATFORM.ENV.LBP` : `DEV`, `TEST`, `STAGING`, `PROD`, `SANDBOX`

**Note d'archives** : `PROMPT.ARCH_ROLE.LBP`, `PROMPT.DEPLOY_STATUS.LBP`, `PLATFORM.ENV.LBP`, `OBJ.CONFIDENTIALITE.LBP` ont chacune une copie « archivée le 26-04-2026 » dans `00 - archives/`. La version active porte le même nom et le même contenu (refonte récente, frontmatter modernisé). Cohérent.

---

## 2) Cas spécifique — la taxo "type de doc Brain" : **N'EXISTE PAS**

**Constat clé** : il n'existe **aucune taxonomie unique** type `DOC.TYPE.LBP` ou `OBJ.TYPE.LBP` qui discriminerait l'ensemble des types de docs/objets Brain (manuel BDD, taxo, prompt, template, logic block, méthode, doctrine, charte, etc.).

À la place, la classification s'opère **implicitement par BDD d'appartenance** : chaque manuel Brain a sa propre BDD (Manuels, Taxonomies, Prompts, Templates de bricks, Méthodes, Outils externes, Docs méta, Agents, Logic blocks, Notes de concept, Glossaire) et le « type de doc » est porté par le **fait d'être dans telle BDD** + une famille interne (`META.FAMILY`, `BRICK.FAMILY`, etc.).

**Conséquence pour la codification** : la table de préfixes proposée (`DBMAN_TW`, `CPT`, `TAXO`, `TPL`, `PRMPT_M/S/U/F`, `LGBLK`, `METH`, `DOCT`, `CHRT`…) est aujourd'hui **non adossée à une taxonomie formelle** côté Brain. Elle est cohérente avec la **partition par BDD**, mais n'a pas de référent contrôlé exploitable par les agents.

---

## 3) Cohérence préfixes proposés ↔ taxos existantes

| Préfixe proposé | Type de doc Brain | Taxo Brain qui l'encadre | Sous-typage interne | Aligné ? |
|---|---|---|---|---|
| `DBMAN_TW` / `DBMAN_MO` / `DBMAN_BR` | Manuel de BDD (Twin / Mission Ops / Brain) | **aucune** (BDD « Manuels de BDD » + scope implicite) | — | ⚠️ Pas de taxo de scope (Twin/MO/Brain) |
| `WRRD_TW` / `WRRD_MO` | WR-RD (Twin / Mission Ops) | aucune (BDD séparée + suffixe) | — | ⚠️ idem |
| `CPT` | Note de concept | aucune (BDD « Registre des notes de concept ») | — | ⚠️ Pas de famille |
| `TAXO` | Taxonomie | aucune (BDD « Registre des taxonomies ») — code = `NAMESPACE.FAMILLE.LBP` lui-même | namespace + suffixe `.LBP` | ✅ Codification taxo déjà figée par convention propre |
| `TPL` | Template d'instanciation / template de Brick | `BRICK.FAMILY.LBP` (10 valeurs) pour les templates de bricks | sous-typage par famille de brick | ✅ partiellement — TPL générique vs TPL_BRICK à clarifier |
| `PRMPT_M / PRMPT_S / PRMPT_U / PRMPT_F` | Prompt maître / system / user / function | `PROMPT.ARCH_ROLE.LBP` (`PROMPT_MAITRE`, `SYSTEM_PROMPT`, `PROMPT_EXECUTION`, `TEMPLATE_PROMPT`) + `PROMPT.TYPE.LBP` (8 v.) | rôle archi + type fonctionnel | ✅ Bonne couverture, MAIS écart : `PROMPT_U` (user) ↔ `PROMPT_EXECUTION` ; `PRMPT_F` (function) ≠ `TEMPLATE_PROMPT`. Pas d'équivalent direct « function » dans `PROMPT.ARCH_ROLE.LBP` |
| `LGBLK` | Logic block | aucune (BDD « Registre des logic blocks ») | — | ❌ Pas de taxo famille des logic blocks |
| `METH` | Méthode | `MET.FAMILY.LBP` (9 v.) | famille opératoire | ✅ Aligné |
| `DOCT` | Doctrine / Playbook | `META.FAMILY.LBP` (8 v.) — `WORKFLOWS_PLAYBOOKS`, `TOOLING_RULES`, `DATA_MODEL_RULES`… | famille doctrinale | ✅ Aligné (Doctrine = Doc méta) |
| `CHRT` | Charte | `META.FAMILY.LBP.CHARTS` (1 valeur sur 8) | sous-cas de meta family | ⚠️ « Charte » est un **taxon dans META.FAMILY**, pas un type de doc autonome. Question de granularité : `DOCT` couvre déjà toutes les META.FAMILY. |
| (manquant) | Agent LBP | `AGENT.FAMILY.LBP` (6 v.) | famille | ⚠️ Pas de préfixe proposé pour les agents |
| (manquant) | Outil externe | `OUT.FAMILY.LBP` (7 v.) | famille | ⚠️ Pas de préfixe proposé pour les outils |
| (manquant) | Glossaire entry | aucune | — | ⚠️ Hors scope ? |

**Écarts notables** :
- **`CHRT` vs `DOCT`** : redondance potentielle. La charte est une famille parmi d'autres dans `META.FAMILY.LBP`. Soit on aligne `DOCT` sur Doc méta entier et on supprime `CHRT` (et alors les 8 META.FAMILY deviennent du sous-typage interne), soit on dérive 8 préfixes (1 par META.FAMILY) — pas pratique.
- **`PRMPT_F` (function)** n'a pas d'équivalent dans `PROMPT.ARCH_ROLE.LBP`. Soit Leonard veut enrichir la taxo (ajouter `FUNCTION_PROMPT`), soit `PRMPT_F` recouvre une autre dimension (ex. `PROMPT.TYPE.LBP.ROUTAGE_SELECTION` ou `CONVERSION_RENDU`).
- **Aucune taxo ne porte le scope Twin/MissionOps/Brain pour les manuels** — c'est implicite côté chemin/BDD.

---

## 4) Trous identifiés

| Trou | Description | Criticité | Recommandation |
|---|---|---|---|
| **T1 — `DOC.TYPE.LBP`** | Pas de taxonomie unique listant les types de docs Brain (manuel, taxo, prompt, template, logic block, méthode, doc méta, agent, outil, note de concept, entry de glossaire) | 🔴 Haute | Créer cette taxo comme **socle de la codification universelle**. Elle sera la référence des préfixes. |
| **T2 — Scope BDD (Twin/MO/Brain)** | Préfixes `DBMAN_TW/MO/BR`, `WRRD_TW/MO` reposent sur un découpage non taxonomisé | 🟠 Moyenne | Créer `DBMAN.SCOPE.LBP` ou `MAN.SCOPE.LBP` à 3 valeurs (`TWIN`, `MISSION_OPS`, `BRAIN`) |
| **T3 — Famille de logic block** | Aucune taxo `LGBLK.FAMILY.LBP` ; tous les logic blocks sont indifférenciés | 🟠 Moyenne | Créer `LGBLK.FAMILY.LBP` (op de validation, op de transformation, op de routage, op de calcul…). À cadrer avec Leonard. |
| **T4 — Famille de note de concept** | Aucune taxo `CPT.FAMILY.LBP` (concept, principe, hypothèse, modèle théorique…) | 🟡 Faible | Optionnel : à créer si la BDD se densifie |
| **T5 — `PROMPT.ARCH_ROLE.LBP.FUNCTION_PROMPT`** | Si `PRMPT_F` est retenu, le taxon manque dans `PROMPT.ARCH_ROLE.LBP` | 🟠 Moyenne | Ajouter le taxon ou clarifier l'intention de `PRMPT_F` |
| **T6 — `OBJ.CONFIDENTIALITE.LBP` orpheline** | La taxo existe et est active, mais aucun manuel Brain ne la déclare en spec d'usage | 🟡 Faible | Soit ajouter la propriété aux manuels concernés (Prompts, Docs méta…), soit archiver |

---

## 5) Recommandations — par où commencer

### 5.1 Priorité 1 — Créer `DOC.TYPE.LBP` comme socle de la codification

C'est **la** taxo manquante qui donnerait un référent contrôlé à toute la table de préfixes. Proposition de valeurs (à arbitrer avec Leonard) :

```
DOC.TYPE.LBP.MANUEL_BDD          (préfixe DBMAN_*)
DOC.TYPE.LBP.WR_RD               (préfixe WRRD_*)
DOC.TYPE.LBP.NOTE_CONCEPT        (préfixe CPT)
DOC.TYPE.LBP.TAXONOMIE           (préfixe TAXO — code = namespace_code lui-même)
DOC.TYPE.LBP.TEMPLATE_BRICK      (préfixe TPL_BRICK)
DOC.TYPE.LBP.TEMPLATE_INSTANCIATION  (préfixe TPL)
DOC.TYPE.LBP.PROMPT              (préfixe PRMPT_*, sous-typé par PROMPT.ARCH_ROLE.LBP)
DOC.TYPE.LBP.LOGIC_BLOCK         (préfixe LGBLK)
DOC.TYPE.LBP.METHODE             (préfixe METH, sous-typé par MET.FAMILY.LBP)
DOC.TYPE.LBP.DOC_META            (préfixe DOCT, sous-typé par META.FAMILY.LBP — couvre doctrine, charte, playbook)
DOC.TYPE.LBP.AGENT               (préfixe AGT, sous-typé par AGENT.FAMILY.LBP)
DOC.TYPE.LBP.OUTIL_EXTERNE       (préfixe OUT, sous-typé par OUT.FAMILY.LBP)
DOC.TYPE.LBP.GLOSSAIRE_ENTRY     (préfixe GLO)
```

→ Cela règle T1 et clarifie d'un coup les ambiguïtés `CHRT` vs `DOCT` et la place des agents/outils dans la grammaire.

### 5.2 Priorité 2 — Créer `DBMAN.SCOPE.LBP` (3 valeurs)

Pour rendre le scope `_TW` / `_MO` / `_BR` adossé à un référent contrôlé.

### 5.3 Priorité 3 — Décisions à prendre avec Leonard

1. Garde-t-on `CHRT` distinct ou bien fusion dans `DOCT` (avec sous-typage `META.FAMILY.LBP.CHARTS`) ? **Recommandation : fusion**.
2. Que recouvre `PRMPT_F` (function) ? Si c'est un rôle archi, ajouter `FUNCTION_PROMPT` à `PROMPT.ARCH_ROLE.LBP`.
3. Crée-t-on `LGBLK.FAMILY.LBP` maintenant ou plus tard ?
4. `OBJ.CONFIDENTIALITE.LBP` : on l'active dans les manuels ou on l'archive ?

### 5.4 Sources à utiliser pour rédiger la codification

- **Référentiel pivot** (à créer) : `Taxonomies/DOC.TYPE.LBP.md` — sera le source-of-truth.
- **Référentiels existants à citer dans la table de préfixes** :
  - `BRICK.FAMILY.LBP` pour le sous-typage des templates de bricks
  - `META.FAMILY.LBP` pour le sous-typage des docs méta (doctrine/charte/playbook)
  - `MET.FAMILY.LBP` pour le sous-typage des méthodes
  - `PROMPT.ARCH_ROLE.LBP` + `PROMPT.TYPE.LBP` pour le sous-typage des prompts
  - `AGENT.FAMILY.LBP` pour les agents
  - `OUT.FAMILY.LBP` pour les outils externes
  - `OBJ.STATUT.LBP` (transverse, déjà universellement consommé)

---

## 6) Annexe — Pointeurs fichiers

**Taxonomies Brain-related actives** :
- `H:\Drive partagés\LBP - shared\Architecture data\Taxonomies\OBJ.STATUT.LBP.md`
- `H:\Drive partagés\LBP - shared\Architecture data\Taxonomies\OBJ.CONFIDENTIALITE.LBP.md`
- `H:\Drive partagés\LBP - shared\Architecture data\Taxonomies\META.FAMILY.LBP.md`
- `H:\Drive partagés\LBP - shared\Architecture data\Taxonomies\BRICK.FAMILY.LBP.md`
- `H:\Drive partagés\LBP - shared\Architecture data\Taxonomies\MET.FAMILY.LBP.md`
- `H:\Drive partagés\LBP - shared\Architecture data\Taxonomies\OUT.FAMILY.LBP.md`
- `H:\Drive partagés\LBP - shared\Architecture data\Taxonomies\AGENT.FAMILY.LBP.md`
- `H:\Drive partagés\LBP - shared\Architecture data\Taxonomies\PROMPT.TYPE.LBP.md`
- `H:\Drive partagés\LBP - shared\Architecture data\Taxonomies\PROMPT.ARCH_ROLE.LBP.md`
- `H:\Drive partagés\LBP - shared\Architecture data\Taxonomies\PROMPT.DEPLOY_STATUS.LBP.md`
- `H:\Drive partagés\LBP - shared\Architecture data\Taxonomies\PLATFORM.ENV.LBP.md`

**Manuels Brain (BDD)** :
- `H:\Drive partagés\LBP - shared\Architecture data\Manuels de BDD\Brain\Manuel de BDD - Manuels de BDD.md`
- `H:\Drive partagés\LBP - shared\Architecture data\Manuels de BDD\Brain\Manuel de BDD - Registre des taxonomies.md`
- `H:\Drive partagés\LBP - shared\Architecture data\Manuels de BDD\Brain\Manuel de BDD - Prompts LBP.md`
- `H:\Drive partagés\LBP - shared\Architecture data\Manuels de BDD\Brain\Manuel de BDD - Templates de bricks.md`
- `H:\Drive partagés\LBP - shared\Architecture data\Manuels de BDD\Brain\Manuel de BDD - Méthodes LBP.md`
- `H:\Drive partagés\LBP - shared\Architecture data\Manuels de BDD\Brain\Manuel de BDD - Outils externes.md`
- `H:\Drive partagés\LBP - shared\Architecture data\Manuels de BDD\Brain\Manuel de BDD - Docs méta LBP.md`
- `H:\Drive partagés\LBP - shared\Architecture data\Manuels de BDD\Brain\Manuel de BDD - Agents LBP.md`
- `H:\Drive partagés\LBP - shared\Architecture data\Manuels de BDD\Brain\Manuel de BDD - Registre des logic blocks.md`
- `H:\Drive partagés\LBP - shared\Architecture data\Manuels de BDD\Brain\Manuel de BDD - Registre des notes de concept.md`
- `H:\Drive partagés\LBP - shared\Architecture data\Manuels de BDD\Brain\Manuel de BDD - Glossaire LBP.md`
