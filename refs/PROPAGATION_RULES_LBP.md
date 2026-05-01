# PROPAGATION RULES — Cheat sheet de propagation des modifications LBP

> **Scope** : 🟦 LBP — Bundle écosystème (durable, indexé dans BDD `Docs méta` du Brain).
> **Format** : cheat sheet 1-pager actionnable. Pour le détail procédural complet en 7 phases, voir `WORKFLOWS_LBP.md` → **WF-008**.
> **Public visé** : tout intervenant (humain, agent, dev) qui modifie un objet de l'écosystème LBP et doit savoir où propager. À garder à portée de main avant chaque modification structurante.
> Dernière mise à jour : 01-05-2026 — création post-WF-008.

---

## 1. La règle d'or (R-001)

> **Markdown = source de vérité. Notion = miroir d'application. Jamais l'inverse.**

Pour modifier un objet :
1. Modifier d'abord le doc Markdown (vault `Architecture data/`)
2. Aligner ensuite Notion (DDL si schéma, propriétés si contenu)
3. Annoncer explicitement la propagation (C-009)
4. Tracer dans `ECOSYSTEM-STATE.md` (C-011)
5. Commit + push (C-013)

---

## 2. Matrice de propagation — « Si tu modifies X → tu propages dans Y »

| Doc source modifié | Dérivés directs | Règles | Workflow |
|---|---|---|---|
| **Manuel de BDD** (section 4 — schéma) | WR-RD du même nom + fiche Notion `Manuels de BDD` | R-041, R-042 | WF-013 + WF-008 |
| **Manuel de BDD** (frontmatter / autres sections) | Fiche Notion `Manuels de BDD` (lien Drive, version, statut) | R-029, D-020 | WF-012 |
| **WR-RD** (corriger un bug d'écriture) | ⚠️ INTERDIT — repasser par le manuel parent | R-041 (interdiction propagation remontante) | — |
| **Taxonomie .md** (valeurs canoniques) | Manuels qui la référencent (section "Usages") + Notion DDL options select sur N BDDs + WR-RD si valeurs impactent instructions d'écriture | R-049 | WF-017 |
| **Template d'instanciation** (bump majeur) | Marquage instances stale (`Version du template` < cible) + planification migration WF-015 | R-056, D-020 | WF-015 |
| **Note de concept** (frontmatter) | Glossaire LBP Notion + Registre des notes de concept Notion (paire CPT/GLO synchronisée) | R-029, R-031 | WF-012 |
| **Note de concept** (corps Markdown) | Lien Drive Notion uniquement (Notion = miroir, pas le contenu) | R-001, R-029 | WF-011 |
| **Règle R-XXX** (création / modification format-impactante) | RULES_LBP.md + ECOSYSTEM-STATE + audit/migration des docs concernés | R-001, C-007 | WF-015 si massif |
| **Décision D-XXX** | DECISIONS_LBP.md + RULES_LBP si dérivation R + ECOSYSTEM-STATE | R-001, C-007 | — |
| **Convention C-XXX** | CLAUDE.md + ECOSYSTEM-STATE | C-006 | — |
| **Code de codification** (R-054 préfixes) | Bundle `*_LBP.md` qui mentionne les codes + scripts d'audit | R-054 | WF-008 cascade |

---

## 3. Checklist actionnable (7 étapes WF-008)

À cocher pour chaque modification structurante :

```
[ ] 1. Identifier le TYPE de modification (format / contenu / codification / archivage)
[ ] 2. Cartographier les DÉRIVÉS DIRECTS (cf. matrice §2)
[ ] 3. Propager dans l'ORDRE STRICT :
       a) Markdown source de vérité (R-001)
       b) Bumper version du dérivé si structurant (R-056)
       c) Aligner Notion (DDL si schéma, propriétés si contenu)
       d) Grep + remplacement des renvois croisés
[ ] 4. QA :
       - WR-RD : R-042 égalité mot pour mot avec section 4 du manuel
       - Notion : re-fetch et compare avec manuel (WF-016)
       - Renvois : grep ancien_nom -> 0 match (sauf archives)
       - Cohérence narrative
[ ] 5. ANNONCE EXPLICITE C-009 :
       "✓ Manuel modifié : X manuel(s) · ✓ Propagation WR-RD : Y WR-RD mis à jour"
       (ou "WR-RD non concerné car ...")
[ ] 6. Trace ECOSYSTEM-STATE.md (C-011) :
       - "Dernière mise à jour" du jour
       - Section "Phase actuelle" si phase notable
       - Section "État du Brain" si volumétrie change
       - PAS DE BATCH (un commit ECOSYSTEM-STATE par phase)
[ ] 7. Commit + push (C-013) :
       - Message explicite : [Domain] [Action] [Volume] — propagation [source] → [dérivés]
       - Push immédiat dans la même réponse
       - Annoncer : "✓ Push : N commit(s) poussé(s) sur origin/master"
```

---

## 4. Anti-patterns à NE JAMAIS faire

| ❌ Anti-pattern | Pourquoi c'est interdit |
|---|---|
| Propager Notion → Markdown | Viole R-001 (Markdown = source de vérité unique) |
| Modifier un WR-RD pour corriger une coquille | Viole R-041 — toute amélioration repasse par le manuel parent |
| Sauter la phase ECOSYSTEM-STATE | Viole C-011 — perte de traçabilité incrémentale |
| Propagation silencieuse sans annonce C-009 | Manuel ↔ WR-RD considérés non vérifiables |
| Commit local sans push | Viole C-013 — filet de sécurité GitHub absent |
| Batch de plusieurs phases en un seul commit ECOSYSTEM-STATE | Perte de traçabilité incrémentale |
| Inventer un préfixe de code sans vérifier R-054 | Crée des asymétries silencieuses dans le bundle (cf. CODIFICATION_LBP §9) |
| Modifier un manuel sans propager au WR-RD | Viole R-041 — divergence fatale entre source et précis agent |
| Toucher une fiche Notion sans modifier le Markdown amont | Désync fatal — au prochain audit transverse, l'écart devra être nettoyé |

---

## 5. Cas particuliers fréquents

### 5.1 Modification de codification (R-054)

Un changement de code stable n'est **jamais** une modification simple — c'est **archivage de l'ancien + création du nouveau** (R-053) :
1. Archiver l'ancienne entrée Notion (`Statut → Archivé`), pas de suppression
2. Créer la nouvelle entrée avec le nouveau code
3. Propager les renvois (grep + remplacement transverse)
4. Si paire `CPT/GLO` (R-031), propager aux 2 entrées en miroir

### 5.2 Modification d'une taxonomie (cascade large)

Une taxo est référencée par N manuels et M propriétés Notion. Cascade :
1. Mettre à jour la taxo `.md` + Notion BDD `Registre des taxonomies`
2. Identifier les manuels qui la référencent (relation `utilise (taxonomies)`)
3. Pour chaque manuel : section "Usages des taxonomies" + WR-RD si applicable
4. Pour chaque BDD Notion concernée : ALTER options select (WF-017)
5. Annoncer le volume total : « Taxo X mise à jour → N manuels + M BDDs Notion alignés »

### 5.3 Modification d'un template d'instanciation

Un bump majeur de template (X.Y → (X+1).0) **ne propage pas automatiquement** :
1. Mettre à jour le template (source de vérité)
2. Mettre à jour la propriété Notion `Version du template` (D-020)
3. **Marquer les instances stale** (audit mécanique sur `template_version` < cible)
4. Planifier une phase de migration des instances (WF-015 si applicable)
5. **Ne pas propager dans l'urgence** — c'est un chantier dédié

### 5.4 Modification d'une règle format-impactante (ex. R-052 apostrophes)

Cas le plus délicat — peut concerner des dizaines de docs :
1. Mettre à jour la règle dans RULES_LBP.md
2. Identifier l'ensemble impacté (grep sur les caractères concernés)
3. Si pattern massif : lancer un WF-015 (migration au canon)
4. Si pattern ciblé : propagation manuelle doc par doc avec QA

---

## 6. Renvois

- **`refs/WORKFLOWS_LBP.md` § WF-008** — détail procédural complet en 7 phases (cartographie, propagation, QA, annonce, trace, commit)
- **`refs/RULES_LBP.md`** — R-001 (Markdown source de vérité), R-029 (indexation Notion), R-031 (paire CPT/GLO), R-038 (identifiant pivot), R-041 (propagation Manuel→WR-RD), R-042 (QA stricte), R-049 (taxonomies), R-053 (archivage), R-054 (codification), R-056 (versioning)
- **`refs/CODIFICATION_LBP.md`** — grammaire des codes (à consulter avant toute modification de codification)
- **`refs/DECISIONS_LBP.md`** — D-020 (Version du template propagée Brain)
- **`CLAUDE.md`** — C-007 (pointer vers refs/), C-009 (annonce propagation), C-011 (ECOSYSTEM-STATE), C-013 (push systématique)

---

> Cheat sheet à garder à portée de main. Pour chaque modification structurante, dérouler la checklist §3 et vérifier la matrice §2.
