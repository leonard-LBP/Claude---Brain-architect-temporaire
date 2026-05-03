# Etat courant de l'ecosysteme LBP

> Snapshot dynamique — mis à jour après chaque changement.
> Dernière mise à jour : 03-05-2026 — **Phase 4.4 close intégralement.** Catalogue `Workflows opérationnels - LBP v1.1` actif (4e catalogue fondateur, 13 WF en 4 sous-sections + §5.5 anticipée). Sync Notion fait (fiche `Workflows opérationnels - LBP` créée dans BDD `Docs méta LBP`, ID `355e1a18-653c-8133-8fb1-e509021239d3`, fonction Opérer). Fiche Notion legacy `Workflows opérationnels LBP` (ID `353e1a18...`) → Statut Archivé. Legacy `WORKFLOWS_LBP.md` archivé sous R-053 dans `00 - archives/` + suppression mirror `refs/WORKFLOWS_LBP.md`. **Convention transverse archives unifiée** (décision Leonard) : `99-Archives/` → `00 - archives/` pour cohérence avec les autres types d'objet (Manuels, Taxos, Notes, Templates). 5 fichiers archivés conservés, cascade docs référents : Règles intrinsèques v1.3 → v1.4 (R-026 reformulée), Constitution des docs méta v0.3 → v0.4. **Triptyque + WF complet** : R + PROP + D + WF tous actifs comme catalogues fondateurs. **Prochaine étape** : Phase 4.5 = `Codification - LBP` + nouveau template `TPL_META_GRAMMAR` (mode référentiel statique distinct des modes log/substitution).

> _Précédent_ : 03-05-2026 — **Phase 4.4 produite (commit + push faits sur Markdown ; sync Notion + archivage legacy en attente validation Leonard).** Catalogue `Workflows opérationnels - LBP v1.0` produit dans `50-Opérer/` (598 lignes, 12 WF en 4 sous-sections). Découpage révisé vs plan initial : (a) §5.1 Cycle de vie d'une BDD (4 WF : 013/014/012/017) ; (b) §5.2 Cycle de vie d'un catalogue doc méta (4 WF : 022/019/021/020) ; (c) §5.3 Audits & migrations transverses (2 WF : 016/015) ; (d) §5.4 Cascades, utilitaires & sync transverses (2 WF : 008/011). §5.5 « Production des autres docs canoniques » anticipée mais non créée à v1.0 (à créer dès le 1er WF émergent par bump MINOR). Schéma item figé : 9 obligatoires + 1 optionnel (Garde-fous & anti-patterns), avec verbe d'action en tête du Nom et étapes numérotées imposées. Champ Acteur explicitement rejeté (R-070 étendue : WF agent-agnostique, l'attribution est faite dans les system prompts/prompts maîtres/logic blocks/méthodes). §1.4 du catalogue formalise cette agnosticité. Audit grep clean (YAML OK, 12 items H2, 12 entrées récap §4, 0 ref CLAUDE.md, marqueurs temporels uniquement en citations canoniques légitimes). Capture proactive en parallèle à proposer post-Phase : extension explicite de R-070 ou nouvelle R-076 « Catalogues opérationnels agnostiques de l'exécutant ». **À faire en suite** : (a) sync Notion = créer fiche `Workflows opérationnels - LBP` dans BDD `Docs méta LBP` (fonction Opérer) ; (b) archiver legacy `WORKFLOWS_LBP.md` sous R-053 dans `Doctrines & playbooks/00 - archives/` + supprimer mirror `refs/WORKFLOWS_LBP.md`. Puis Phase 4.5 = `Codification - LBP` + nouveau template TPL_META_GRAMMAR.

> _Précédent_ : 03-05-2026 — **Phase 4.4 préparée + Phase 4.3 close + 2 décisions structurelles capturées avant pause.** (1) Plan validé pour Workflows opérationnels - LBP : Option B 3 sous-sections par cycle de vie (Production initiale 4 WF / Maintenance et propagation 2 WF / Audit et migration 2 WF) + schéma item WF-XXX 10 champs (Trigger, Préconditions, Étapes, Sortie obligatoires en plus des 4 génériques). Production reportée à prochaine session (volume ~700-900 lignes, risque de coupure mid-doc en fin de contexte actuel). (2) Décision capturée : créer un template **TPL_META_GRAMMAR** dédié pour Codification - LBP (et futures grammaires SQL/Supabase, naming bricks MO, etc.) car le pattern catalogue colle « limite » au mode « référentiel statique » des conventions de format. Mapping mis à jour de 10 → 11 templates. Phase 4.5 = Codification + TPL_META_GRAMMAR (post-Workflows). (3) Note de maintenance intelligente des catalogues : principes d'évolution des sous-sections thématiques (ajout/split/fusion/renommage par bump MINOR si croissance le justifie) capturés dans MAPPING §6.2sexies — à formaliser dans la future Méthode de maintenance. (4) Fix R-068 sur fiche Notion `Template - META Catalogue` : retrait de TPL_META_CATALOGUE des aliases. (5) Fiche Notion `Décisions architecturales - LBP` créée dans BDD `Docs méta LBP` (ID `355e1a18-653c-81da-8654-d2958a4c1a8d`). **À faire en début de prochaine session** : production complète Workflows opérationnels - LBP v1.0 selon plan validé en MAPPING §6.2quinquies + audit + sync Notion + archivage legacy WORKFLOWS_LBP. Puis Phase 4.5 Codification + TPL_META_GRAMMAR.

> _Précédent_ : 03-05-2026 — **Phase 4.3 close intégralement : 3e catalogue produit (Décisions architecturales - LBP v1.0, 26 D en 5 sous-sections, 766 lignes) + audit complet clean (26/26 D, 0 champ manquant) + sync Notion (fiche `Décisions architecturales - LBP` créée dans BDD `Docs méta LBP`, ID `355e1a18-653c-81da-8654-d2958a4c1a8d`, fonction Expliquer) + archivage legacy `DECISIONS_LBP.md` sous R-053 + suppression mirror `refs/DECISIONS_LBP.md`.** Schéma D-XXX inclut champ dédié `Date de décision` (chronologie) distinct de `Origine` (contexte de capture). Triptyque doctrinal des catalogues fondateurs (R + PROP + D) maintenant complet et actif. **Prochaine étape** : Phase 4.4 — `Codification - LBP` (catalogue le plus court restant, ~10-15 entrées) ou directement `Workflows opérationnels - LBP` (catalogue orchestrateur qui invoque R + PROP).

> _Précédent_ : 03-05-2026 — **Phase 4.3 produit (Décisions architecturales - LBP v1.0, 26 D en 5 sous-sections), commit + push faits, mais clôture INCOMPLÈTE (sync Notion + archivage legacy DECISIONS_LBP non encore faits — à enchaîner en début de prochaine session).** Catalogue placé dans 20-Expliquer/. Schéma D-XXX inclut un champ dédié `Date de décision` (chrono) + `Origine` (contexte de capture, sans date). Découpage 5 sous-sections : Décisions fondatrices d'écosystème (3) ; Ontologie des objets et frontières (6) ; Architecture transverse et lecture analytique (5) ; Conventions de docs et lifecycle documentaire (6) ; Codification, templates et migrations docs méta (6). **À faire en début de prochaine session** : (a) audit complet du nouveau doc (vérifier 26/26 D migrées, articulations, cohérence) ; (b) sync Notion (créer fiche `Décisions architecturales - LBP` dans BDD `Docs méta LBP`) ; (c) archivage legacy `DECISIONS_LBP.md` sous R-053 dans `Doctrines & playbooks/00 - archives/` + suppression mirror `refs/DECISIONS_LBP.md` ; (d) ECOSYSTEM-STATE rafraîchi avec Phase 4.3 close. **Commits poussés** : vault `153e170`, collab `a21a1a4`.

> _Précédent_ : 03-05-2026 — **Phase 4.2 close : 2e catalogue produit (Règles de propagation - LBP v1.0, 11 PROP en 5 sous-sections) + cascade Règles intrinsèques v1.2 → v1.3 (4 R archivées : R-028, R-041, R-042, R-075 → migrées en PROP-001 ou PROP-011).** Catalogue PROP placé dans 40-Normer/ (PROP = norme contraignante événementielle, donc Normer pas Opérer — observation Leonard). Sync Notion : fiche Règles intrinsèques mise à jour à v1.3, fiche Règles de propagation créée dans BDD `Docs méta LBP` (ID `355e1a18-653c-81e0-8d10-ef4b24301741`, fonction Normer). Ancien `PROPAGATION_RULES_LBP.md` archivé sous R-053. Mirror `refs/PROPAGATION_RULES_LBP.md` supprimé. Observation transverse capturée dans MAPPING_DOCS_META §6.2ter : le template TPL_META_CATALOGUE est trans-fonction (5 catalogues prévus dans 3 fonctions différentes). **Prochaine étape** : Phase 4.3 — au choix entre `Décisions architecturales - LBP` (D-XXX, fonction Expliquer), `Codification - LBP` (code, Normer), ou `Workflows opérationnels - LBP` (WF-XXX, Opérer).

> _Précédent_ : 03-05-2026 — **Phase 4.1 close : 1er catalogue produit (Règles intrinsèques - LBP v1.2) + template TPL_META_CATALOGUE v1.6 stabilisé + R-072, R-073, R-074, R-075 + C-028 capturés.** Premier doc méta canonique converti depuis le legacy `RULES_LBP.md` au nouveau format catalogue. 73 règles R-XXX migrées en 8 sous-sections thématiques. Schéma item figé. Récap tabulaire en tête. Section §6 Archives placeholder. Champ `Origine` (renommé depuis `Découverte` pour élargir au-delà de l'observation dans un doc). 4 PROP « déguisées » identifiées dans Règles (R-028, R-041, R-042, R-075) — migreront vers `Règles de propagation - LBP` en Phase 4.2 (prochain catalogue à produire). Sync Notion : fiche Template-META-Catalogue v1.6 mise à jour, fiche Règles intrinsèques créée dans BDD `Docs méta LBP` (ID `355e1a18-653c-8111-bd4a-e80a8f56a0ad`, fonction `Normer`, statut Validé). Ancien `RULES_LBP.md` archivé sous R-053 dans `Doctrines & playbooks/00 - archives/RULES_LBP (archivé v1.9 le 03-05-2026).md`. Mirror `refs/RULES_LBP.md` supprimé (remplacé par `refs/Règles intrinsèques - LBP.md`). MAPPING_DOCS_META enrichi de 12 bonnes pratiques (§3.1 à §3.12) dont la chaîne intuition Leonard : Catalogues atomiques (R/PROP/D/code) → Catalogue orchestré (WF) → Méthodes futures. **Prochaine étape** : Phase 4.2 — produire `Règles de propagation - LBP` + migrer R-028, R-041, R-042, R-075.

> _Précédent_ : 03-05-2026 — **Phase 3 close intégralement (E + B + C).** Phase 3.C : création de l'arborescence cible des docs méta sous `00 - Docs méta/` — 5 dossiers fonctionnels reflétant la taxo META.FUNCTION (`10-Orienter/`, `20-Expliquer/`, `30-Structurer/`, `40-Normer/`, `50-Opérer/`) + 2 transverses (`90-États & audits/`, `99-Archives/`). Tous vides à ce stade, seront peuplés organiquement en Phase 4 par les nouveaux docs canoniques produits depuis les 10 templates META. Le dossier `Doctrines & playbooks/` reste en place avec les 12 docs legacy `*_LBP.md` (à convertir/réactualiser dans un chantier ultérieur, après réactualisation prompts/logic blocks — séquence arbitrée par Leonard 03-05-2026). **Prochaine phase** : Phase 4 — produire les 10 templates META + convertir progressivement les 12 docs legacy. **Phases passées** : 

> _Précédent_ : 03-05-2026 — **Phase 3.E + Phase 3.B closes intégralement + capture C-028.** Phase 3.B Notion finale : (a) fiche `Manuel de BDD - Templates Brain` créée dans BDD canonique `Manuels de BDD` (ID `355e1a18-653c-8137-8c2b-f310cc1d339a`, code `DBMAN_BR_TEMPLATES_BRAIN`, version template 1.1, statut Validé, domaine Motor, taxos OBJ.STATUT + TPL.SCOPE liées, liens Drive Manuel + WR-RD + BDD Notion `Templates Brain` posés) ; (b) opération `replace_content` body de fiche `Manuel de BDD - Docs méta LBP` ABANDONNÉE après vérification : la fiche active `6257523b...` (sous DB NOTES BRAIN) a un body vide conforme à la convention LBP — l'erreur initiale venait du fetch d'un doublon legacy `317e1a18...` sous `Source of truth` (page hors canon). Capture **C-028** dans CLAUDE.md (« Ne consulter QUE DB NOTES BRAIN pour les BDDs Notion du Brain ; ignorer absolument Source of truth ») pour prévenir la récidive. **Reste à arbitrer** : (option) archiver les fiches legacy sous `Source of truth → Manuels de BDD - 02/03/2026` (hors scope Phase 3.B). **Prochaine phase** : 3.C (réorganisation arborescence Markdown 5 sous-dossiers fonctionnels Orienter/Expliquer/Structurer/Normer/Opérer).

> _Précédent_ : 03-05-2026 — **Phase 3.E + Phase 3.B partielle closes (checkpoint intermédiaire).** Phase 3.E : 12 docs `*_LBP.md` du bundle déplacés à plat dans `00 - Docs méta/Doctrines & playbooks/` + dossier `Bundle écosystème LBP/` supprimé (nom contextuel obsolète) + script `scripts/bundle_docs_meta/get_bundle_urls.py` patché. Phase 3.B Markdown : Manuel `Docs méta LBP.md` bumped 0.2→0.3 (10 occurrences `Famille (Doc méta)/META.FAMILY` → `Fonction systémique/META.FUNCTION` + suppression de l'énumération des taxons dans description ≤280 par R-072) ; WR-RD `Docs méta LBP.md` cascadé bumped 1.0→1.1 (R-042 strict) ; capture **R-072** dans RULES_LBP (« Pas d'énumération de taxons dans les instructions d'écriture / descriptions ≤280 ») bumped 1.6→1.7. Phase 3.B Notion : relation `utilise (taxonomies)` sur fiche `Manuel de BDD - Docs méta LBP` (ID `6257523b-2511-4dd4-ac76-fd8f331a4a58`) mise à jour : META.FAMILY (`b859bcd6...`) supprimée, META.FUNCTION (`355e1a18-653c-8196-99ea-fa96944e9013`) ajoutée. **Restant Phase 3.B** : (a) replace_content body fiche `6257523b...` avec contenu .md à jour ; (b) création fiche `Manuel de BDD - Templates Brain` dans BDD `Manuels de BDD` (n'existe pas encore). ~~Dette WF-008 globale identifiée~~ → **Faux positif rétracté 03-05-2026** : les ~80 taxos en `.LBP` que je voyais étaient sous la page legacy `Source of truth → Docs de Taxonomies`, hors canon (cf. C-028). La BDD canonique `Registre des taxonomies` (sous `DB NOTES BRAIN`) est bien migrée sans suffixe — la propagation A4.A est complète.

> _Précédent_ : 03-05-2026 — **Phase 3.A du chantier d'architecture des docs méta close (sync Notion Phase 1.0 différée).** Livrables : (1) Fiche `META.FUNCTION` indexée dans BDD `Registre des taxonomies` (`355e1a18-653c-8196-99ea-fa96944e9013`) ; (2) Fiche `TPL.SCOPE` indexée dans BDD `Registre des taxonomies` (`355e1a18-653c-81b1-9428-e54273713df9`) ; (3) Fiche existante `Taxonomie - Famille de doc méta (LBP)` (META.FAMILY) marquée **Archivé** dans `Registre des taxonomies` avec note d'archivage dans aliases (« remplacée par META.FUNCTION le 03-05-2026 ») ; (4) Propriété `Fonction systémique` (select META.FUNCTION : Orienter/Expliquer/Structurer/Normer/Opérer) ajoutée sur BDD Notion `Docs méta LBP` ; (5) Fiche `Constitution des docs méta - LBP` créée dans BDD `Docs méta LBP` (`355e1a18-653c-8171-a1f6-ceeb0c47dbd9`, code `META_DOC_MAP_LBP`, fonction Orienter, version 0.2) ; (6) 11 fiches existantes migrées avec leur `Fonction systémique` (Panorama/Constitution=Orienter ; Doctrine LBP/Doctrine Twin/Décisions=Expliquer ; Architecture Brain/Twin/MO=Structurer ; Règles intrinsèques/Codification=Normer ; Workflows/Propagation Rules=Opérer) ; (7) Propriété `Famille (Doc méta)` SUPPRIMÉE de BDD `Docs méta LBP` (D-025). **Restant Phase 3** : 3.D nouveau (déplacer dossier `Templates d'instanciation/` vers `Templates Brain/` racine vault — proposé par Leonard, pour cohérence avec BDD Notion séparée), puis 3.B (refonte manuel + WR-RD Docs méta LBP), puis 3.C (réorganisation arborescence Markdown 5 sous-dossiers fonctionnels).

> _Précédent_ : 03-05-2026 — **Phase 2 du chantier d'architecture des docs méta close (BDD `Templates Brain` créée + indexée).** Livrables : (1) BDD Notion `Templates Brain` créée sous DB NOTES BRAIN avec 16 propriétés (5 strict + 4 quasi-génériques + 6 spécifiques + 1 relation bidir vers Prompts LBP) ; (2) 15 fiches templates indexées (TPL_NOTE_CONCEPT, TPL_DBMAN_BR/TW/MO, TPL_WRRD_BR/TW/MO, TPL_TAXO, TPL_METH, TPL_OUT, TPL_BRICK_META, TPL_PROMPT, TPL_PROMPT_MAITRE, TPL_SYSTEM_PROMPT, TPL_LOGIC_BLOCK) — toutes avec Lien Drive récupéré via SQLite Drive Desktop locale (compte LBP `101486418960336612156`) ; (3) Manuel + WR-RD `Templates Brain` au canon Brain (Descriptions ≤280 en instructions d'écriture verbe à l'infinitif, R-042 cascade) ; (4) Refonte des 15 fiches en mode auto-suffisant (sans noms d'agents, sans comparaisons relatives) suite à 2 itérations de calibration C-012 ; (5) RULES_LBP bumpée 1.4→1.5→1.6 avec **5 nouvelles règles capturées** : R-067 (libellés humains pour valeurs select Notion), R-068 (aliases ne contiennent pas le code unique ni le nom canonique), R-069 (lecture complète du doc avant indexation, pas seulement le frontmatter), R-070 (ban des noms d'agents dans les SoT), R-071 (auto-suffisance des descriptions dans les SoT — pas de comparaisons relatives). **À faire en ouverture Phase 3** : (a) suppression manuelle (UI Notion) des ~11 fiches templates legacy obsolètes dans BDD Docs méta LBP (le wrapper MCP n'expose pas l'option in_trash) ; (b) sync Notion Phase 1.0 différée (statut META.FAMILY archivé + indexer META.FUNCTION + créer fiche Constitution + ajouter propriété Fonction systémique sur BDD Docs méta LBP).

> _Précédent_ : 03-05-2026 — **Phase 2.1 du chantier d'architecture des docs méta close (production Markdown).** Livrables : (1) `Manuel de BDD - Templates Brain.md` v1.0 créé (code DBMAN_BR_TEMPLATES_BRAIN, brain_layer MOTOR, brain_subtype SPOKE_MOTOR, 11 sections canon Brain, 6 propriétés spécifiques + relation `est utilisé dans (Prompts LBP)`). (2) `WR-RD - Templates Brain.md` v1.0 dérivé strictement de la section 3.2 du manuel parent (R-041/R-042). (3) Taxo `TPL.SCOPE.md` créée (12 valeurs : NOTE_CONCEPT, MANUEL_BDD, WR_RD, TAXONOMIE, METHODE, OUTIL, BRICK, PROMPT, PROMPT_MAITRE, SYSTEM_PROMPT, LOGIC_BLOCK, DOC_META). (4) Constitution des docs méta - LBP bumpée 0.1→0.2 : nettoyage de TOUS les marqueurs temporels (« à créer Phase X », « à venir », « D-XXX à capturer », etc.) + renommage `Templates méta Brain` → `Templates Brain` partout + intégration des IDs réels (R-064, R-065, R-066, D-024, D-025, D-026). (5) Manuel `Manuel de BDD - Templates Brain.md` également nettoyé des marqueurs temporels. (6) Capture **C-027** dans CLAUDE.md : « pas d'infos temporaires ou de marqueurs de log dans une source de vérité Markdown à un instant t » (proscrit « à créer Phase X », « à venir », « remplace », « D-XXX à capturer », etc. — règle de discipline rédactionnelle SoT, articulée avec C-011 ECOSYSTEM-STATE). **Sync Notion DIFFÉRÉE Phase 2.2-2.3** : (i) génération BDD Notion `Templates Brain` via WF-014 (3 passes : natives → relations → rollups), (ii) indexation des 15 templates existants dans la nouvelle BDD, (iii) suppression / archivage des fiches templates actuellement dans BDD `Docs méta LBP`, (iv) statut `META.FAMILY` → archivé sur Notion + indexer `META.FUNCTION` + créer fiche Constitution + ajouter propriété `Fonction systémique` sur BDD Docs méta LBP. **Avant Phase 2.1** : Phase 1.0 close (constitution v0.1, taxo META.FUNCTION, archivage META.FAMILY, R-064 + R-065 + R-066, D-024 + D-025 + D-026).

> _Précédent_ : 03-05-2026 — **Phase 1.0 du chantier d'architecture des docs méta close.** Livrables : (1) nouvelle taxo `META.FUNCTION` (5 fonctions systémiques : Orienter / Expliquer / Structurer / Normer / Opérer) créée dans `Taxonomies/`. (2) Ancienne taxo `META.FAMILY` archivée selon R-053 (suffixe `(archivé v1.0 le 03-05-2026)`) avec note d'archivage explicite. (3) Doc constitution `Constitution des docs méta - LBP.md` v0.1 créé (code `META_DOC_MAP_LBP`, 8 sections + 3 annexes incluant arborescence cible et trajectoire workflows → agents). (4) 3 nouvelles règles dans `RULES_LBP` (section 5.8 « Architecture des docs méta du Brain LBP ») : R-064 (naming filename humain + code `META_*` + scope), R-065 (définition opérationnelle « gouverne plusieurs objets »), R-066 (propriétaire canonique unique). (5) 3 nouvelles décisions dans `DECISIONS_LBP` : D-024 (préfixe `META_` remplace `CHRT_`), D-025 (5 fonctions systémiques `META.FUNCTION` remplacent `META.FAMILY`), D-026 (BDD `Templates méta Brain` séparée + `Templates de Bricks` reste séparée par scope agent kontext). RULES_LBP bumpée 1.1→1.2, DECISIONS_LBP bumpée 1.0→1.1, miroirs `refs/` rafraîchis. **Sync Notion DIFFÉRÉE** (Phase 2-3) : statut `META.FAMILY` → archivé sur Notion + indexer `META.FUNCTION` dans Registre des taxonomies + créer fiche `Constitution des docs méta - LBP` dans BDD `Docs méta LBP` + ajouter propriété `Fonction systémique` sur BDD `Docs méta LBP`. **Avant Phase 1.0** : Phase B (test Twin DeepSecAI v0) close + investigation MCP Obsidian Q1-Q4 close avec 7 règles capturées (C-020 à C-026).

> _Précédent_ : 30-04-2026 — **Phase B (test Twin DeepSecAI v0) close.** 51 fiches sur 17 BDDs Twin/MO mobilisées sur la page test `352e1a18653c8079b1b6edd1c456aaeb`. Vague 9 Mission Ops complète (2 Meetings + 2 Actions LBP + 2 Bricks). Vague 10 vérifs transverses : ✓ bidir auto-propagation Notion (Meeting↔Action, Action↔Brick, Source↔Brick), ✓ chaînes D-009 indicateurs (5 relations + correctif `mesure (problématiques)` post-audit). Playbook stabilisé : `refs/TEST_TWIN_PLAYBOOK.md`. Captures session : C-017 (lecture WR-RD obligatoire avant remplissage) + C-018 (vérifier régime BDD avant signaler anomalie). Reste post-test : (a) cogitation propriété 'Régime de l'entité', (b) Phase C audit final + figement Brain, (c) Phases D/E chantiers M et P.

## Phase actuelle

**Phase A4 close + Phase B en cours (test Twin DeepSecAI v0, ~75% close).** Cumul A1+A2+A3+A4 : **447 actions Notion**. **Phase B Vagues 1-7 close** sur la nouvelle page : 41 entités Twin/MO (3 Sources + 1 Org + 4 Coll + 7 Ind + 2 Postes + 2 Env + 2 Actifs + 2 Évén + 2 Glossaire + 2 JdS + 2 AD + 2 Enjeux + 2 Process candidats sandbox + 2 Process officiels + 2 Pratiques + 2 Principes + 2 Capacités métier candidates sandbox). Captures règles : C-017 (lecture WR-RD obligatoire), C-018 (vérifier régime BDD avant signaler une anomalie de relation absente). Reste : Vague 8 (6 fiches Pilotage) + Vague 9 (6 fiches Mission Ops final) + Vague 10 (vérifs) + post-test : créer `refs/TEST_TWIN_PLAYBOOK.md` + cogitation propriété 'Régime de l'entité'. **Phase A4.B** (relations Manuels ↔ Taxonomies) : 43 manuels mis à jour avec `utilise (taxonomies)` peuplé depuis le parsing de leur section « Usages des taxonomies ». 87+ codes uniques référencés transverse, 100% mappables. **Phase A4.A** (Taxonomies) : 102 taxos Markdown synchronisées avec BDD `Registre des taxonomies` Notion. 96 updates (codes `<X>.<Y>.LBP` migrés vers `<X>.<Y>` per R-054, props complètes : Aliases, Descriptions, Lien Drive, Nature sémantique, Mode de sélection, Ouverture, Statut Validé, Version 2.0) + 6 creates (BRAIN.LAYER, BRAIN.SUBTYPE, DBMAN.SCOPE, DOC.TYPE, JOB.COVERAGE, LGBLK.FAMILY). Architecture Glossaire / Registre stabilisée : Glossaire = identité + sémantique du concept (Code, Aliases, Mots clés, Type, Définition, Valeur ajoutée, Règles d'usage, Usages IA, Équivalent langage courant) ; Registre = méta du fichier source (Code `CPT_*`, Version du template, Statut, Lien Drive). Captures règles : C-013, C-014, C-015 + amendement R-054 (paire `CPT/GLO`). Outils : `scripts/lib/notion_keys.py`, `scripts/phase_a3/build_drive_url_resolver.py`, `scripts/phase_a3/a3bis_plan.py`, `scripts/phase_a3/a3_6_migration.py`. Prochaine étape : **Phase A4** (Taxonomies, 102 taxos) + relations utilise (taxonomies) cross-BDDs.

### Phases terminées (chronologie)

| Phase | Volume | Notes |
|---|---|---|
| Mini-phase 1f-g | 2 taxos (`BRAIN.SUBTYPE`, `BRAIN.LAYER`) + `Template - Manuel de BDD - Brain.md` v1.1 | Pattern v1.1 inauguré |
| Phase 4 | 43 manuels de BDD migrés au canon | Frontmatter R-054 / R-055 / R-056 |
| Phase 5 | 32 WR-RD migrés au canon | idem |
| Phase 6 | 72 notes de concept migrées au canon | Split anti-pattern `version: "DATE vX.Y.Z"` → `version` + `created_at` |
| Phase 6.5 | Refonte de 4 templates secondaires en v2.0 + MAJ 5 manuels Brain | Voir détail ci-dessous |
| Audit transverse Notion ↔ Manuels Brain | Rapport `scripts/notion_brain_audit/audit_notion_brain.md` | A déclenché la sync DDL |
| Sync DDL Notion BDDs Brain | ~26 actions sur les 11 BDDs Brain | Voir détail ci-dessous |
| Phase 7 | 24 instances migrées au canon (20 Templates de Bricks + 3 Méthodes + 1 Doc méta playbook) | Codes `TPL_BRICK_*`, `METH_*`, `CHRT_*` (conformes R-054 ; à vérifier dans le vault si certains fichiers utilisent encore les préfixes ad hoc `TPL_BRK_/MET_`) |
| Création `Template - WR-RD - Brain.md` v1.0 | 1 template `TPL_WRRD_BR` | Aligné sur templates Twin et Mission Ops, adapté aux spécificités Brain (pas de couche 5D, pas de jumelles texte R-058) |
| Génération des 11 WR-RD Brain | 11 fichiers `WR-RD - X.md` dans `Manuels de BDD/Brain/WR-RD/` | Extraction stricte depuis manuels parents (R-041/R-042). Section couche calculée supprimée partout (rollups Brain tous relationnels). |
| Audit transverse taxonomies | 87/87 référencées présentes ; 1 manquante détectée (`JOB.COVERAGE`) ; 14 orphelines à arbitrer plus tard | Rapport via agent + grep cross-manuels |
| Création `JOB.COVERAGE` | 1 taxo (BDD Postes Twin) — 6 valeurs (Couvert / Partiellement couvert / Vacant / Sur-couvert (doublon) / En transition / Gelé) | Au canon R-054 + ALTER Notion `État de couverture du poste` SET SELECT |
| 11 `Lien WR-RD` posés sur Notion | 11 fiches BDD `Manuels de BDD` mises à jour avec URL Drive du WR-RD Brain correspondant | Via WF-011 (lecture SQLite Drive locale) + notion-update-page |
| Capture **D-020** + Lot 1 DDL | ADD `Version du template` (RICH_TEXT) sur 10 BDDs Brain + ALTER Manuels de BDD (select→text) + RENAME `Lien vers le doc du manuel` → `Lien vers le manuel de BDD (.md)` + RENAME apostrophe Logic blocks (typo U+2019) | 14 actions DDL Notion réussies |
| Lot 2 (manuels + WR-RD) | Documentation `Version du template` ajoutée à 10 manuels Brain + propagée à 11 WR-RD Brain. 3 props Méthodes (`Erreurs fréquentes / anti-patterns`, `Quand l'utiliser`, `Variantes & adaptations`) documentées dans Manuel + WR-RD Méthodes. | 22 fichiers Markdown enrichis |
| Lot 3 (audit-correction Lien manuel) | 21 entrées Notion `Manuels de BDD` désynchronisées corrigées (URL Drive posée, 7 renames de Nom canonique) + 7 archivages V1 orphelins (Insights, Impacts de Modulateurs, Rôles officiels, Ressources, Unités Organisationnelles, Appartenances, Edges) | Script réutilisable `scripts/get_manuels_urls.py` |

#### Détail Phase 6.5 (refonte templates secondaires)

- `template-db-manual-mission_ops.md` v0.3 → archivé (doublon)
- `template-methode_lbp.md` → `Template - Méthode LBP.md` v2.0 (canon, pattern v1.1)
- `Template-Fiche_outil_LBP.md` → `Template - Outil externe.md` v2.0
- `Template méta de Brick.md` → `Template - Template de Brick.md` v2.0 (méta-template mince)
- MAJ des 5 manuels Brain : Glossaire LBP, Manuels de BDD, Méthodes LBP, Agents LBP, Prompts LBP (suite à audit transverse)

#### Détail sync DDL Notion Brain (~26 actions)

- DROP `actif` (Prompts LBP)
- ADD `Domaine(s) d'usage` multi-select (4 BDDs Motor : Méthodes, Templates, Agents, Outils)
- ADD `System prompt (lien source)` URL (Agents LBP)
- DROP `Type fonctionnel (BDD décrite)` (Manuels de BDD) — application D-019
- DROP 2 jumelles texte (Logic blocks) — application R-058
- DROP `Entrées attendues` (ancien champ, Méthodes) ; DROP `actif` (Prompts)
- ALTER options `Statut de déploiement` (5 valeurs PROMPT.DEPLOY_STATUS), `Environnement(s) de déploiement` (5 valeurs PLATFORM.ENV), harmonisation casse `Domaine(s) d'usage` (Prompts)
- RENAME apostrophes ASCII → typographiques (Logic blocks `Statut de l’objet`) — R-052
- RENAME accents (Outils : `Valeur ajoutée`, `Entrées attendues`)
- CONVERT 8 propriétés `text` → `rollup` (Méthodes 2, Templates 2, Agents 4)
- CREATE 3 rollups manquants (Outils externes : Agents/Méthodes/Templates mobilisés via prompts)

#### Out of scope Phase 7 (différé)

- **Logic Blocks (101)** + **Prompts (76)** : obsolètes vs Twin v2, refonte/regen ultérieure → **Phase 7 bis**.

### Règles et décisions captées dans cette série

- **R-053** — convention de renaming des docs archivés (suffix `(archivé v<X> le JJ-MM-YYYY)`)
- **R-054** — codification universelle des objets Brain (table de préfixes officielle : `CPT_`, `GLO_`, `METH_`, `TPL_BRICK_`, `CHRT_`, `DBMAN_TW/MO/BR_`, `WRRD_TW/MO/BR_`, `LGBLK_`, `PRMPT_M/S/U/T_`, `OUT_`, `AGT_`, etc. — cf. `CODIFICATION_LBP.md`)
- **R-055** — frontmatter canon Brain en 3 zones balisées (Identité / Méta-gouvernance / Spec d’usage)
- **R-056** — versioning `X.Y` (sans PATCH)
- **R-057** — discipline d’usage des backticks Markdown
- **R-058** — interdiction des jumelles texte sur les BDDs Brain
- **R-059** — hygiène d’écriture des docs Brain (pas de bruit historique ni de spéculation future)
- **D-019** — Brain = environnement documentaire en évolution ; Core+Motor unifié au niveau modèle de données ; isolation stricte Brain ↔ MO/Twin
- **C-011** (CLAUDE.md) — mise à jour systématique de `ECOSYSTEM-STATE.md` à chaque fin de phase, avant le commit de la phase
- **D-020** (DECISIONS_LBP.md) — propagation de la propriété `Version du template` (RICH_TEXT, type texte libre format X.Y) à toutes les BDDs Brain ; permet l'audit mécanique des docs stale lors de bumps majeurs de templates
- **D-021** (DECISIONS_LBP.md) — Architecture des 3 agents LBP : Brain architect (évolution du Brain) / Twin architect (modélisation Twin client) / KONTEXT (Mission Ops, agent central consultant). Frontière d'isolation infranchissable : KONTEXT ⊥ Brain architect (le Brain est utilisé pendant les missions mais n'évolue pas). 3 fiches `Agents LBP` à créer post-Chantier P.

**Backlog enrichi** (28-04-2026) :
- **Chantier P** — Tri massif `Prompts/` + `Logic Blocks/` + création des 3 fiches `Agents LBP` (Brain architect, Twin architect, KONTEXT) ; mise à jour des system prompts/prompts maîtres/logic blocks pour cohérence Twin v2 + D-019 + D-021. À traiter avant indexation Notion de ces 3 BDDs.
- **Chantier M** — Réactualisation PLAYBOOK macro-archi v2 + tri des entrées Notion `Docs méta LBP` sans Markdown actif. **Réflexion bundle** : produire un bundle de docs méta dédiés à chaque ensemble de doctrines/règles/chartes avec périmètre bien défini par doc (maintenable, améliorable, durable).
- **Convention** : "Statut de l'objet vide = à créer" (induction Méthodes LBP, à confirmer transverse).
- **Patterns techniques DDL Notion** : multi-select string JSON-encoded, types `CREATED_TIME`/`LAST_EDITED_TIME` (DDL fonctionnels mais non documentés), statements séquentiels en API séparés.
- **Propriété "Maître"** — figement d'une entité avérée Twin pour gouvernance dédoublonnage : entité maître = entité d'accueil en cas de fusion (les autres sont archivées dedans). À cogiter pendant Phase B.

---

## Plan global — vue d'ensemble (28-04-2026, ré-ordonné)

### Phase 0 (préalable) — Remplissage `summary` / `purpose` AVANT indexation

**Doctrine Leonard 28-04-2026** : remplir les `summary` / `purpose` des docs au canon **avant** d'indexer Notion (sinon on indexe des champs vides). Sous-étapes en miroir des BDDs à indexer ensuite :

0a. **Taxonomies** (96-102 docs) — `purpose` à écrire pour chaque taxo (les `summary` sont déjà partiellement présents)
0b. **Manuels de BDD** (43 docs) — `summary` à écrire (pour compléter avant Phase A1)
0c. **WR-RD** (32 docs Twin + 4 MO + 11 Brain = 47 docs) — `summary` à écrire si vide
0d. **Notes de concept** (72 docs) — `purpose` à écrire si vide
0e. **Templates de bricks** (20 docs) — `summary` à écrire si vide

→ **Markdown-only**, aucun coût Notion. Peut être fait pendant les pauses Notion.

### Phase A — Indexation Brain restante (4 BDDs, ~270 entrées)

A1. **Manuels de BDD** (43 entrées) — partiellement fait au Lot 3, reste les autres propriétés à dériver des manuels (préalable 0b)
A2. **Templates de bricks** (20 entrées) (préalable 0e)
A3. **Glossaire LBP + Registre des notes de concept** (72 + 72, double indexation cohérente) (préalable 0d)
A4. **Registre des taxonomies** (102 entrées) (préalable 0a)

→ **Out of scope court terme** : Prompts LBP (Chantier P), Registre des logic blocks (Chantier P), Agents LBP (Chantier P + D-021), Docs méta LBP (Chantier M).

### Phase B — Tests fonctionnels Twin + Mission Ops

B1. Création **fausses entités test** sur les 28 BDDs Twin
B2. Création **fausses entités test** sur les 4 BDDs Mission Ops
B3. **Validation combo Twin + Mission Ops** : instanciation actions de mission, fixation RDV, génération bricks, mise à jour Twin
B4. **Réflexion ordonnancement de remplissage** : intra-BDD (dans quel ordre remplir les propriétés d'une fiche ?) + inter-BDD (qu'est-ce qu'on remplit d'abord quand on extrait des infos d'un document ?)
B5. **Cogitation propriété "Maître"** (cf. backlog) : si elle se révèle utile pendant les tests, formaliser en R-XXX ou D-XXX

### Phase C — Audit final symétrie + figement Brain

C1. Audit ultime symétrie manuels Brain ↔ BDDs Notion (dernier passage)
C2. Correction des écarts résiduels éventuels
C3. **Figement / freeze** du Brain (état stable de référence)

### Phase D — Chantier M (Docs méta — bundle réfléchi)

D1. Réflexion bundle docs méta : recensement des ensembles thématiques (architecture macro, codification, cycle de vie docs, doctrine isolation agents, gouvernance, etc.) + définition du périmètre de chaque doc
D2. Production du **bundle de docs méta** (un doc par périmètre, au canon, articulés sans recouvrement)
D3. Tri des entrées Notion `Docs méta LBP` (refondre ou archiver)
D4. Indexation Notion BDD Docs méta LBP

### Phase E — Chantier P (Prompts / Logic Blocks / Agents)

E1. Tri massif des dossiers `Prompts/` et `Logic Blocks/` (séparer ancien du code app vs docs de travail)
E2. Mise à jour des system prompts / prompts maîtres / logic blocks (cohérence Twin v2 + D-019 + D-021)
E3. Création des 3 fiches Agents LBP (Brain architect, Twin architect, KONTEXT) au canon
E4. Indexation Notion BDDs Prompts + Logic Blocks + Agents

### Phase F — Hors-scope ponctuel (à programmer)

F1. Remplissage `summary` / `purpose` TODO (~275 docs : 43 manuels + 64 WR-RD + 72 notes + 96 taxos)
F2. Audit nettoyage backticks abusifs (R-057)
F3. Phase 7 bis : refonte structurelle des 101 logic blocks + 76 prompts (post-Chantier P)

## Etat du Brain (11 BDD) — post-sync DDL

| BDD | Score audit | Manuel à jour ? | Notion à jour ? |
|---|---|---|---|
| Docs méta LBP | Conforme | OK | OK (au canon) |
| Glossaire LBP | Conforme (post-MAJ) | MAJ 28-04-2026 (`Notes` documenté + dates auto) | OK |
| Registre des notes de concept | Conforme | OK | OK |
| Registre des taxonomies | Conforme | OK | OK |
| Manuels de BDD | Conforme (Type fonctionnel retiré) | MAJ 28-04-2026 | DROP Type fonctionnel appliqué |
| Prompts LBP | Conforme (post-sync) | OK | DROP `actif`, taxos alimentées, casse harmonisée |
| Logic blocks | Conforme (post-sync) | OK | DROP 2 jumelles texte, apostrophe alignée |
| Méthodes LBP | Conforme (post-sync) | MAJ 28-04-2026 (Entrées MUST/SHOULD/NICE) | DROP ancien Entrées + 2 rollups corrects |
| Templates de bricks | Conforme (post-sync) | OK | + Domaine(s) d’usage, 2 rollups corrects |
| Agents LBP | Conforme (post-sync) | MAJ 28-04-2026 (relation §7 corrigée) | + Domaine(s) d’usage + System prompt + 4 rollups |
| Outils externes | Conforme (post-sync) | OK | + Domaine(s) d’usage + 3 rollups + accents corrigés |

## A faire (prochaines étapes)

**Dette technique — citations placeholders à résoudre après Phase 4.5** :

- **Audit + remplacement de toutes les citations vers docs « futurs »** dans les catalogues docs méta produits (R / PROP / D / WF actuellement, codification + grammaires + méthodes à venir). Exemples connus : `[[Codification - LBP]]` cité dans WF-019 (futur Phase 4.5), `Méthodes LBP` cité dans WF (futur post-Phase 4) — à transformer en wikilinks valides dès production des docs cibles. Lancer un grep pattern `\[\[(Codification - LBP|Méthodes LBP|...)\]\]` dans tous les catalogues une fois Phase 4 close pour détection exhaustive et résolution. Dette à porter jusqu'à la fin de Phase 4 inclus.

**Court terme — chantier Brain au canon Notion** :

1. **Indexation des Markdown au canon dans les BDDs Notion Brain** — **mise à jour des entrées existantes** plutôt qu’archivage+recréation (préservation des relations Notion existantes).
2. **Renseigner les `Lien vers le doc WR-RD (.md)`** dans la BDD Manuels de BDD pour les 11 manuels Brain (chaque manuel pointera vers son WR-RD).

**Moyen terme** :

5. **Remplissage `summary` / `purpose`** sur ~275 docs où ces champs sont en TODO (par moi avec vision globale).
6. **Audit nettoyage backticks abusifs** (R-057).

**Out of scope court terme (différé)** :

- **Phase 7 bis** : refonte/regen des Logic Blocks + Prompts (obsolètes vs Twin v2).
- **Phases 9-12** : taxos manquantes (JOB.COVERAGE, etc.), audit cross-éco, audit final, indexation Brain Notion étendue.

## Notes diverses

- **R-052** : apostrophes typographiques `’` (U+2019) appliquées partout (vault + Notion).
- **R-044** : dates au format `JJ-MM-YYYY` partout dans les sections vivantes.
- **D-019** : la distinction Core/Motor est conservée comme étiquette de discours et matérialisée dans la propriété `Domaine(s) d’usage` (5 BDDs Motor), mais elle n’est plus une partition stricte du modèle de données.
- **R-058** : les jumelles texte sont **interdites sur Brain**, autorisées Twin, expérimentales Mission Ops.
