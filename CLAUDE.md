# CLAUDE.md

> Ce fichier regit le comportement de Claude et le cadre de notre collaboration.
> Les regles intrinseques a l'ecosysteme Brain/Twin sont dans `refs/RULES_LBP.md` (IDs `R-XXX`).
> Ici, les IDs sont `C-XXX` (C pour collaboration/Claude).

---

## 1. Regles absolues

### C-001 : Confirmation humaine obligatoire

- **Statut** : Actif (absolue, aucune exception)
- **Why** : L'ecosysteme est critique. Une modification non validee peut casser relations, conventions, references.
- **How to apply** : Aucune creation, edition, suppression, renommage sur le vault Obsidian ou Notion sans validation explicite de Leonard. Toujours presenter le changement prevu et attendre un "oui" / "go".

### C-002 : Vault unique = Architecture data

- **Statut** : Actif (absolue)
- **Why** : Eviter toute contamination avec d'autres vaults Obsidian de Leonard.
- **How to apply** : On ne travaille que sur le vault Obsidian **"Architecture data"**. Ne jamais toucher aux autres vaults (LEO SECOND BRAIN, LBP CLIENTS VAULT, CONTEXT BRAIN, etc.). Un doute = on demande.

### C-003 : Git comme filet de securite

- **Statut** : Actif
- **Why** : Reversibilite de toute modification + historique + backup externe sur GitHub.
- **How to apply** : Chaque milestone (nouveau doc, mise a jour de regles, changement d'etat) declenche une suggestion de commit. Message clair qui resume le changement et son motif. Format : resume + detail si necessaire + `Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>`.

---

## 2. Acces ecosysteme

- **Vault Obsidian** : `Architecture data` — accessible via Obsidian CLI (`Obsidian.exe`) et en lecture directe fichiers
- **Drive** : `H:\Drive partagés\LBP - shared\Architecture data\` (synchronise avec le vault)
- **Notion** : Page maitre Brain = `20be1a18653c8079aeb1e01047fddddd` — 11 BDD officielles (ignorer les BDD prefixees "XXX")
- **Repo git** : Ce dossier (`Claude - Brain architect temporaire`) — pour versionner le travail

---

## 3. Documentation de reference

A consulter selon le besoin ; `refs/PANORAMA_LBP.md` a relire au debut de chaque conversation pour se recontextualiser.

**🟦 Scope LBP (bundle ecosysteme — 11 docs `*_LBP.md`)**
- `refs/PANORAMA_LBP.md` — Doc d'entree, vue macro 3 ensembles (Brain/Twin/MO)
- `refs/DOCTRINE_LBP.md` — 9 doctrines transverses (pourquoi structurel)
- `refs/DOCTRINE_TWIN_LBP.md` — Doctrine detaillee Twin (regimes, chaines, gouvernance)
- `refs/RULES_LBP.md` — Regles intrinseques a l'ecosysteme (IDs R-XXX)
- `refs/DECISIONS_LBP.md` — Decisions architecturales (IDs D-XXX)
- `refs/WORKFLOWS_LBP.md` — Workflows operationnels LBP (IDs WF-XXX)
- `refs/SPECS_ARCHITECTURE_BRAIN_LBP.md` — Modele conceptuel 11 BDDs Brain
- `refs/SPECS_ARCHITECTURE_TWIN_LBP.md` — Modele conceptuel 28 BDDs Twin
- `refs/SPECS_ARCHITECTURE_MISSION_OPS_LBP.md` — Modele conceptuel 4 BDDs Mission Ops
- `refs/CODIFICATION_LBP.md` — Grammaire de tous les codes LBP
- `refs/PROPAGATION_RULES_LBP.md` — Cheat sheet propagation
- `refs/RULES_BRAIN_TWIN-backlog.md` — Regles pressenties (Scope Session, hors bundle)

**🟪 Scope Session (hors bundle, collaboration Claude/Leonard)**
- `refs/SESSION_WORKFLOWS.md` — Workflows propres a notre collaboration en session (re-contextualisation, etc.)
- `refs/ECOSYSTEM-STATE.md` — Journal de session + etat courant (a mettre a jour apres chaque changement)

---

## 4. Habitudes de travail

- **C-004 — TodoWrite** : Maintenir une liste de taches a jour pendant chaque session des qu'il y a 3+ etapes.
- **C-005 — Memoire** : Sauvegarder en memoire les decisions importantes, preferences utilisateur, pointeurs de contexte.
- **C-006 — Relecture avant modif** : Avant de modifier un doc, toujours le lire d'abord. Avant de creer un doc, verifier qu'il n'existe pas deja.
- **C-007 — Pointer vers les docs de ref** : Quand une question est deja traitee dans les docs refs/, y renvoyer plutot que de parapher.
- **C-008 — Separer scope LBP et scope Session dans `refs/`** : Tout doc dans `refs/` a un scope explicite : 🟦 **LBP** (bundle ecosysteme, vocation a etre publie/consomme par les agents et humains LBP) ou 🟪 **Session** (collaboration Claude/Leonard, hors bundle final). Les workflows LBP vont dans `WORKFLOWS_LBP.md` ; les workflows de session vont dans `SESSION_WORKFLOWS.md`. A terme, les fichiers du bundle LBP seront suffixes en `_LBP.md` pour permettre l'extraction propre du bundle. Tout nouveau doc dans `refs/` doit indiquer son scope dans son intro ou son frontmatter (ligne `> **Scope** : LBP` ou `> **Scope** : Session`).
- **C-009 — Annonce explicite de la propagation Manuel ↔ WR-RD** : R-041 / R-042 imposent la propagation Manuel → WR-RD à chaque modification de propriété. Ne pas la faire en silence (même si correctement effectuée par script) ; **annoncer dans la même réponse** : "✓ Manuel modifié : X manuel(s) · ✓ Propagation WR-RD : Y WR-RD mis à jour" (ou explicitement "WR-RD non concerné car ..."). Sans cette annonce explicite, considérer la propagation comme **non vérifiable** par Leonard, donc à risque. Découverte : 27-04-2026 (modification `Lien vers la note avancée` faite correctement mais non annoncée, signalée par Leonard).
- **C-010 — Numérotation des options dans mes propositions** : Quand je propose à Leonard plusieurs options à arbitrer (multi-choix), j'utilise des **lettres latines** `(a)/(b)/(c)` ou des **chiffres simples** `1./2./3.`. **Jamais** de caractères grecs (α/β/γ), symboles spéciaux ou autres caractères peu accessibles au clavier. Permet à Leonard de répondre rapidement sans chercher la touche. Découverte : 27-04-2026 (Leonard m'a signalé qu'il ne savait pas où se trouvait la touche `β` sur son clavier).
- **C-011 — Mise à jour systématique de `ECOSYSTEM-STATE.md` à chaque fin de phase** : Après toute phase notable (migration, audit, sync, refonte structurelle), mettre à jour `refs/ECOSYSTEM-STATE.md` **avant** le commit de la phase. Cette mise à jour est non négociable car ECOSYSTEM-STATE est le journal vivant qui sert à la re-contextualisation au démarrage de session (cf. WF-010). Sections à rafraîchir : « Dernière mise à jour », « Phase actuelle », « État du Brain », « À faire ». Ne pas batch ces mises à jour (= ne pas attendre la fin de plusieurs phases pour rafraîchir d'un coup, on perd la traçabilité incrémentale). Découverte : 28-04-2026 (Leonard a constaté que ECOSYSTEM-STATE était resté figé sur Phase 5 Twin v2 / mini-batch 0 alors que les Phases 4-7 + sync DDL Brain s'étaient empilées dessus ; risque de re-contextualisation sur des bases obsolètes à la prochaine session).
- **C-012 — Calibration explicite avant production en série** : Avant de lancer une production répétitive sur N items (≥10) qui appliquent une règle ou un pattern (ex. remplir un champ dans 100 fichiers, refondre 30 manuels, etc.), **arrêter au cas n°2 ou 3** et soumettre les sorties à Leonard pour validation explicite du pattern, **avant** de relancer à l'échelle. Critère cible à écrire à voix haute : « Voici le pattern attendu. Voici 2-3 sorties. Tu valides ? ». Si je tourne directement en mode mécanique sur 100 items sans cette pause, le risque est qu'une asymétrie systémique se révèle seulement à la fin (Leonard ouvre un fichier au hasard et détecte une faute sur les 100). Le coût de la pause est de 5 min ; le coût d'un repassage complet est de plusieurs heures. Découverte : 29-04-2026 (Phase 0a, 102 taxos refondues d'un trait avec un pattern défaillant : doublon summary↔purpose, énumération des valeurs en prose, citation de codes externes ; Leonard a signalé l'asymétrie sur ORG.ROLE après que tout était déjà produit, imposant une refonte complète et un durcissement de R-060).
- **C-013 — Push systématique après chaque commit de fin de phase** : Après chaque `git commit` qui clôture une phase notable (Phase 0, 0a, 0b, A1.x, etc.), enchaîner immédiatement avec `git push origin master` **dans la même réponse**, sans attendre une session ultérieure. Le commit local ne suffit pas — C-003 exige le filet de sécurité GitHub (backup externe + traçabilité publique). Sans push, en cas de crash machine ou de perte de session, le repo distant est désynchronisé et le filet de sécurité n'opère plus. Annoncer le push dans la même réponse : « ✓ Push : N commits poussés sur origin/master ». Découverte : 29-04-2026 (Leonard a constaté que 11 commits étaient en local sans push après les Phases 0 v3 + A1 + A2 — ~2h de travail entièrement non sauvegardé sur GitHub. Capture immédiate avec correctif rétroactif).
- **C-014 — Quirk wrapper MCP Notion : apostrophes ASCII dans les payloads `query-database-view`** : Le wrapper MCP Notion renvoie les noms de propriétés contenant une apostrophe en **ASCII** (`'`, U+0027) dans les payloads de `notion-query-database-view`, alors qu'ils sont en **typographique** (`'`, U+2019) dans le schéma (`notion-fetch`), dans l'UI Notion, et dans les manuels Drive (R-052). C'est un défaut connu du wrapper, **pas** une divergence de nos données. Conséquence pratique : tout script Python qui parse ces payloads doit utiliser le helper `scripts/lib/notion_keys.py` (`get()` ou `normalize_keys()`), ou tester systématiquement les 2 variantes via `repr(list(entry.keys()))` en début d'audit. **Ne pas modifier** les manuels, WR-RD ou Notion en réaction — l'asymétrie est uniquement dans le pipeline MCP en lecture. Découverte : 29-04-2026 (Phase A3.0, audit Glossaire LBP : 100 entrées comptées vides à tort sur `Statut de l'objet` à cause de la clé typographique côté Python alors que le payload renvoie ASCII).
- **C-015 — Vocabulaire : éviter « Drive » pour désigner les fichiers Markdown du vault** : Les fichiers Markdown du vault Obsidian `Architecture data` sont stockés sous `H:\Drive partagés\` parce que Google Drive Desktop synchronise le dossier — mais ce sont des `.md` purs, source de vérité LBP, **pas** des fichiers Google Drive natifs (Docs, Sheets, etc.). Termes corrects : « notes de concept », « manuels de BDD », « WR-RD », « taxonomies », ou plus génériquement « source de vérité Markdown » / « vault Architecture data ». Termes à proscrire : « notes Drive », « fichiers Drive », « doc Drive » — ils suggèrent à tort un format Google natif et brouillent la distinction Markdown ↔ Notion. Les **liens** vers Google Drive (URLs `drive.google.com`) restent eux légitimement nommés ainsi car ils pointent l'API Drive. Découverte : 29-04-2026 (Phase A3.2, Leonard a flaggé l'imprécision « notes Drive »).
- **C-016 — Mettre à jour les plans JSON après ajouts inline en sous-phase** : Quand on étend une sous-phase par des ajouts inline (entrées non prévues au plan initial, ex. concepts trouvés via search ad hoc et traités directement par tool calls sans repasser par le plan), **mettre à jour le JSON de plan** dans `scripts/.../output/` **dans la même unité de travail**. Sinon, les scripts de migration ultérieurs (qui consomment ce JSON comme source de vérité) vont consommer un plan obsolète et **manquer les ajouts**. Symptôme typique : audit final révèle que des entries n'ont pas reçu un traitement censé être systémique (ex. migration de code), parce qu'invisibles pour le script. Découverte : 29-04-2026 (Phase A3.6, 5 entrées Glossaire ratées par script `a3_6_migration.py` car `a3bis_plan.json` n'avait pas capté les ajouts inline de sub-phase A3.bis.e — détecté par Leonard via spot-check manuel).
- **C-017 — Lire le WR-RD (et les `.md` taxos référencées) avant chaque vague de remplissage de BDD Notion** : Avant de remplir des fiches dans une BDD Notion (Twin, Mission Ops ou Brain), lire systématiquement le WR-RD correspondant (`Manuels de BDD/<Domain>/WR-RD/WR-RD - <Nom BDD>.md`) pour absorber les **Instructions d'écriture** champ par champ + les contraintes de format (longueur, anti-patterns documentés, valeurs canoniques de taxons attendues, format des Noms type `Nom (Type)` pour Collectifs / `Nom (Sous-type)` pour Actifs, etc.). **Lire aussi les `.md` des taxonomies référencées** (`Taxonomies/*.md`) pour vérifier les libellés canoniques exacts. **Sans cette double lecture, le remplissage devient un best-guess** depuis le seul schéma Notion (data-source-state) qui produit des asymétries systémiques (taxons mal choisis, formats de Nom non conformes, mauvaise lecture du niveau category vs taxon, dimensions 5D dispatchées à l'instinct). Articulation avec C-012 : la lecture WR-RD/taxo doit avoir lieu **avant** la calibration de la fiche n°1 ; la calibration valide ensuite l'application correcte des contraintes lues. Découverte : 30-04-2026 (Phase B test Twin DeepSecAI v0, 25 fiches créées en best-guess depuis schéma Notion + json deepsecai_v0 sans lecture WR-RD/taxos ; audit a posteriori a révélé 6 fiches au format Nom non conforme et plusieurs anti-patterns documentés ignorés).
- **C-018 — Avant de juger une absence de relation comme anomalie : vérifier les chaînes de transformation (D-009) et le régime de la BDD** : Une BDD Twin/MO peut légitimement ne pas avoir de relation directe vers `Sources d'informations` si elle est de **régime « consolidé/dérivé »** plutôt que « extraction directe ». Les BDDs analytiques (Processus, Pratiques organisationnelles, Principes organisationnels, Capacités organisationnelles, Modulateurs, etc.) sont alimentées par d'autres BDDs amont (Actions détectées, Processus candidats sandbox, Enjeux, etc.) selon les chaînes de transformation **D-009**. La traçabilité vers les sources est donc **indirecte / transitive** via les BDDs amont, pas directe. **Avant de signaler une « anomalie DDL »** sur l'absence d'une relation `Source(s) d'information`, lire : (i) le WR-RD complet de la BDD pour comprendre son régime, (ii) les chaînes de transformation D-009 dans `refs/DECISIONS_LBP.md` et `refs/SPECS_ARCHITECTURE_TWIN_LBP.md`, (iii) **R-012** (séparation des 4 régimes de connaissance). Articulation avec C-017 : c'est l'extension du principe « lire le WR-RD avant remplissage » — la doctrine architecturale de la BDD doit être absorbée avant de juger ce qui manque. Découverte : 30-04-2026, Phase B Vague 7.1, lors de la création des 2 fiches Processus j'ai initialement signalé comme « anomalie DDL » l'absence de relation `Source(s) d'information` côté Processus, alors que c'est intentionnel et conforme à la doctrine LBP (régime consolidé, alimentation amont via Process candidats / Actions détectées). Leonard a corrigé.

- **C-020 — Ne JAMAIS utiliser `obsidian_patch_content` sur `target_type: frontmatter` pour les docs Brain au canon R-055** : L'outil MCP Obsidian `obsidian_patch_content` (qui appelle l'endpoint Local REST API `PATCH` sur le frontmatter) **parse le YAML, modifie le champ ciblé, puis re-sérialise** avec son propre formatter. Conséquences destructrices sur les docs au canon R-055 : (i) commentaires YAML perdus (`# === Identité ===`, `# === Méta-gouvernance ===`, `# === Spec d'usage ===`) ; (ii) quotes sur strings supprimées ; (iii) structure 3 zones balisées détruite ; (iv) style de sérialisation YAML modifié (compact / line-folded selon humeur du serializer). **Règle** : pour modifier un champ frontmatter d'un doc Brain R-055, **toujours utiliser `Edit`** (remplacement textuel exact qui préserve commentaires et structure). `obsidian_patch_content` reste utilisable pour `target_type: heading` ou `block` sur le corps Markdown. **Articulation** : R-055 (frontmatter en 3 zones balisées) + C-001 (validation avant modif vault). Sans cette règle, toute opération MCP innocente sur frontmatter casse silencieusement le canon. **Découverte** : 02-05-2026 (Test C `patch_content` sur PANORAMA_LBP pour bump version 1.0→1.1 ; succès technique mais corruption complète du frontmatter R-055 ; restauration manuelle via Edit).

- **C-019 — Push systématique sur TOUS les repos git impactés (extension de C-013)** : L'écosystème LBP comporte plusieurs repos git distincts qui doivent être commit + push **chacun** dans leur propre cadence : (1) `Claude - Brain architect temporaire` (collab Claude/Leonard, scripts, refs/, Transmission Clément/) ; (2) `lbp-architecture-data-vault` (vault Markdown source de vérité R-001 — manuels, WR-RD, taxos, bundle docs méta, taxonomies, notes de concept, templates, etc.) ; (3) tout futur repo (app LBP, scripts dédiés, etc.). À chaque fin de phase notable, **vérifier `git status` dans chaque repo pertinent** et committer + pousser séparément. Une cascade WF-008 qui touche le vault doit générer un commit dans le vault, pas seulement dans le repo collab. Annoncer explicitement : « ✓ Push : N commits sur repo-A · ✓ Push : M commits sur repo-B ». **Articulation avec C-013** : C-013 disait « push après commit », C-019 dit « vérifier que TOUS les repos pertinents ont leurs commits à jour avant la fin de phase ». **Articulation avec WF-008** : la phase 7 du workflow (commit + push) s'applique à chaque repo touché par la propagation, pas à un seul. **Découverte** : 02-05-2026 — Leonard signale que 5 jours de modifs sur le vault `Architecture data` (227 fichiers : Phases A4 + B + Bundle docs méta + Cleanup + Cascades WF-008) étaient restés uncommitted sur le repo `lbp-architecture-data-vault`, alors que le repo collab `Claude - Brain architect temporaire` était à jour. Risque concret : crash machine ou bug Drive desktop = 2+ jours de travail perdus. Correctif rétroactif : commit massif `66547c7` poussé immédiatement.

---

## 5. Protocole de capture proactive des regles

A chaque fois qu'une regle, convention ou decision emerge, je prends l'initiative de proposer sa capture.

### 5.1 Declencheurs

Je propose une capture dans ces situations :

- **Succes non-trivial** : on vient de reussir une action qui a demande un choix de methode → je propose de retenir comment on a fait.
- **Decision orientante** : tu prends une decision qui va influencer des pratiques futures → je propose capture immediate.
- **Convention implicite detectee** : je constate qu'on a applique une convention sans l'avoir formalisee → je propose de la rendre explicite.
- **Anti-pattern identifie** : on decouvre qu'une approche ne marche pas → je capture la regle negative (ce qu'il ne faut pas faire).
- **Conflit / contradiction** : deux regles existantes se marchent dessus → je signale.

### 5.2 Format de proposition

Je te presente :
- **Enonce propose** de la regle (titre + 2-3 lignes)
- **Portee** pressentie (Brain / Twin / Transverse / Contextuel a notre collab)
- **Nature** : "Regle fixe", "Hypothese a confirmer", ou "Decision archi"

### 5.3 Routage selon ton arbitrage

| Ton arbitrage | Destination |
|---|---|
| "Regle fixe" intrinseque a l'ecosysteme | `refs/RULES_LBP.md` avec ID R-XXX |
| "Hypothese a confirmer" | `refs/RULES_BRAIN_TWIN-backlog.md` |
| "Contextuel a notre collab" (comportement Claude, outillage) | `CLAUDE.md` avec ID C-XXX |
| "Decision archi" (choix structurant) | `refs/DECISIONS_LBP.md` avec ID D-XXX |
| "Laisser pour plus tard" | rien, on avance |

### 5.4 Apres capture

Je suggere un commit. Je mets a jour `refs/ECOSYSTEM-STATE.md` si l'etat a change.
