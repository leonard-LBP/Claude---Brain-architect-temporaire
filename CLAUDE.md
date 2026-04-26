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
