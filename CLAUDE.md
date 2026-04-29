# CLAUDE.md

> Ce fichier regit le comportement de Claude et le cadre de notre collaboration.
> Les regles intrinseques a l'ecosysteme Brain/Twin sont dans `refs/RULES_BRAIN_TWIN.md` (IDs `R-XXX`).
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

A consulter selon le besoin ; `refs/ARCHITECTURE-DIGEST.md` a relire au debut de chaque conversation pour se recontextualiser.

**🟦 Scope LBP (bundle ecosysteme)**
- `refs/ARCHITECTURE-DIGEST.md` — Synthese de l'architecture LBP
- `refs/RULES_BRAIN_TWIN.md` — Regles intrinseques a l'ecosysteme (IDs R-XXX)
- `refs/RULES_BRAIN_TWIN-backlog.md` — Regles pressenties a formaliser plus tard
- `refs/DECISIONS.md` — Decisions architecturales (le pourquoi des choix, IDs D-XXX)
- `refs/WORKFLOWS_LBP.md` — Workflows operationnels LBP (IDs WF-XXX)
- `refs/SPECS_ARCHITECTURE_BRAIN.md` — Specs detaillees des 11 BDD Brain (schemas Notion)

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
| "Regle fixe" intrinseque a l'ecosysteme | `refs/RULES_BRAIN_TWIN.md` avec ID R-XXX |
| "Hypothese a confirmer" | `refs/RULES_BRAIN_TWIN-backlog.md` |
| "Contextuel a notre collab" (comportement Claude, outillage) | `CLAUDE.md` avec ID C-XXX |
| "Decision archi" (choix structurant) | `refs/DECISIONS.md` avec ID D-XXX |
| "Laisser pour plus tard" | rien, on avance |

### 5.4 Apres capture

Je suggere un commit. Je mets a jour `refs/ECOSYSTEM-STATE.md` si l'etat a change.
