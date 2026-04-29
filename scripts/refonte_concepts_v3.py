#!/usr/bin/env python3
"""Refonte v3 des champs summary et purpose des notes de concept selon R-060 v3.

- summary corrigé si commence par verbe d'action conjugué (« est », « se », ...)
  ou si dépasse 400 char.
- purpose rédigé from scratch (tous étaient vides avec TODO Phase 6).
- 3 cas test (Brick, Approche systémique, Tension créatrice) déjà appliqués manuellement.
"""

import re
from pathlib import Path

DIR = Path(r"H:\Drive partagés\LBP - shared\Architecture data\Notes de Concept")

# 3 cas test déjà faits manuellement
SKIP = {
    "Concept - Brick.md",
    "Concept - Approche systémique.md",
    "Concept - Tension créatrice.md",
}

MAPPING: dict[str, tuple[str | None, str]] = {
    # None pour summary = ne pas modifier ; sinon nouvelle valeur
    "Concept - 3P (Philosophie, Principes, Pratiques).md": (
        "Cadre de lecture distinguant trois niveaux complémentaires : la Philosophie (croyances et intention), les Principes (règles directrices stables) et les Pratiques (routines concrètes). Sert à diagnostiquer la cohérence d’une organisation et à concevoir des transformations qui alignent sens, règles de décision et exécution.",
        "Diagnostiquer la cohérence d’une organisation sur trois niveaux complémentaires, pour concevoir des transformations qui alignent simultanément sens, règles de décision et exécution.",
    ),
    "Concept - Absorption (capacité motrice).md": (
        "Aptitude collective durable à acquérir, assimiler, transformer et exploiter des connaissances issues de l’expérience interne et externe, puis à les réinjecter dans le système (standards, décisions, formation, pratiques) pour produire du progrès reproductible.",
        "Caractériser l’aptitude d’une organisation à apprendre cumulativement de son expérience, pour expliquer le progrès reproductible et la non-répétition des erreurs dans le temps.",
    ),
    "Concept - Actif.md": (
        "Objet non humain identifiable, susceptible d’être gouverné, mobilisé ou produit par le fonctionnement d’un système, dont l’existence, l’usage ou l’indisponibilité affectent la création de valeur, les capacités, la conformité ou la résilience.",
        "Rendre visibles les dépendances, fragilités et leviers liés aux objets non humains d’une organisation, pour éclairer arbitrages de gouvernance et choix de transformation.",
    ),
    "Concept - Adaptation (capacité motrice).md": (
        None,
        "Caractériser l’aptitude à se reconfigurer sans rupture face au changement, pour analyser comment une organisation tient son cap et maintient sa continuité.",
    ),
    "Concept - Alignement (organisation).md": (
        "Degré de cohérence et de compatibilité entre ce que l’organisation veut être et faire, ce qui guide ses décisions et ce qu’elle fait réellement, ainsi qu’entre les différentes parties du système (équipes, structures, technologies, environnement).",
        "Qualifier la cohérence d’une organisation entre intention, règles et pratiques réelles, pour repérer les désalignements internes et les leviers de réalignement structurel.",
    ),
    "Concept - Apprentissage intégré au travail.md": (
        None,
        "Articuler apprendre et produire dans le même geste, pour réduire la rupture entre formation et action et soutenir l’acquisition de compétences face à l’automatisation.",
    ),
    "Concept - Arbre à capacités organisationnelles.md": (
        "Visualisation structurée représentant les chaînes de contribution entre types de pratiques, modulateurs, capacités habilitantes, capacités motrices et capacités métier spéciales.",
        "Rendre visibles les chaînes de contribution qui consolident ou freinent les capacités d’une organisation, pour identifier les leviers racine et les points d’amélioration.",
    ),
    "Concept - Asymétrie de connaissances.md": (
        None,
        "Nommer les déséquilibres de contexte entre acteurs d’une même interaction, pour expliquer malentendus, re-travail et fragilité des décisions et concevoir leur réduction.",
    ),
    "Concept - Capacité générique.md": (
        "Capacité organisationnelle transverse, commune à la plupart des organisations, décrivant l’aptitude durable à assurer une fonction universelle à une granularité stable et comparable.",
        "Distinguer les fonctions universelles (finance, RH, SI, qualité...) des socles habilitants, capacités motrices ou capacités métier spécifiques, pour produire des diagnostics et plans d’action comparables.",
    ),
    "Concept - Capacité habilitante.md": (
        "Aptitude collective durable de fond, assimilable à un stock de mécanismes stabilisés, qui rend possibles des performances supérieures sur des capacités organisationnelles aval, notamment les capacités motrices.",
        "Expliquer pourquoi certaines transformations plafonnent malgré des actions visibles, pour révéler les conditions de fond qui conditionnent cohérence, reproductibilité et apprentissage collectif.",
    ),
    "Concept - Capacité motrice.md": (
        "Capacité organisationnelle de nature soft appartenant à un noyau stable de cinq, décrivant un moteur collectif qui permet au système de maintenir et transformer sa performance dans la durée.",
        "Lire la dynamique d’évolution d’une organisation au-delà des fonctions universelles et des résultats métier spécifiques, pour comprendre ce qui meut le système dans la durée.",
    ),
    "Concept - Capacité métier.md": (
        "Capacité organisationnelle spécifique à un secteur, un modèle d’affaires ou une contrainte client, décrivant l’aptitude durable à produire un résultat métier identifiable, qualifiée dès l’origine par un niveau de distinctivité (standard ou spéciale).",
        "Caractériser ce qu’une organisation sait faire dans son métier au sens propre, pour distinguer ce qui est nécessaire mais imitable de ce qui est différenciant et créateur de valeur.",
    ),
    "Concept - Capacité organisationnelle.md": (
        None,
        "Expliquer la performance au-delà des individus, pour distinguer ce qui relève du chaos de ce qui est consolidé et structurer un graphe de capacités reliées entre elles.",
    ),
    "Concept - Cohérence (LBP).md": (
        "Degré d’alignement durable et fonctionnel entre le sens d’une organisation, ses règles directrices, ses pratiques réelles et les moyens qui les matérialisent — se manifestant par une réduction des contradictions, une meilleure fluidité et une capacité d’adaptation unifiée.",
        "Qualifier le degré d’alignement durable d’une organisation, pour révéler contradictions, frictions et zones d’incohérence qui freinent fluidité et capacité d’adaptation.",
    ),
    "Concept - Collectif.md": (
        None,
        "Rendre visible la trame réelle du travail, de la coopération et de l’apprentissage dans une organisation, sans la confondre avec l’acteur institutionnel qui l’abrite.",
    ),
    "Concept - Compétence.md": (
        "Capacité individuelle démontrée à mobiliser et appliquer, en contexte, des moyens pertinents (connaissances, savoir-faire, comportements, appuis mobilisables) pour produire un résultat attendu de manière fiable.",
        "Relier connaissance et action chez un individu, pour décrire des exigences de poste et des compétences démontrées, en distinguant compétence individuelle et capacité organisationnelle.",
    ),
    "Concept - Connaissance.md": (
        "Compréhension contextualisée et actionnable qui permet de décider et d’agir avec justesse, construite par intégration d’informations, d’expérience et de modèles mentaux, et qui se dégrade si elle n’est ni testée, ni transmise, ni mise à jour.",
        "Distinguer information, savoir et savoir-faire dans une compréhension actionnable, pour piloter les conditions de sa construction, sa transmission et sa maintenance dans la durée.",
    ),
    "Concept - Contexte.md": (
        None,
        "Caractériser ce qui rend une situation lisible pour un acteur ou un système, pour identifier les conditions de justesse des interprétations, décisions et productions.",
    ),
    "Concept - Digital Twin de l’organisation (LBP).md": (
        None,
        "Représenter une organisation par un graphe d’objets et de relations actionnable, pour produire analyses et scénarios, détecter incohérences et soutenir clarté, alignement et capacité d’action.",
    ),
    "Concept - Découverte d’objets.md": (
        "Opération qui consiste à inférer l’existence plausible d’un objet absent du jumeau numérique à partir de traces convergentes déjà présentes dans l’écosystème, et à produire des propositions de création typées et justifiées soumises à validation humaine.",
        "Inférer la présence plausible d’objets manquants dans le jumeau numérique, pour enrichir la représentation à partir de traces convergentes sans court-circuiter la validation humaine.",
    ),
    "Concept - Dédoublonnage.md": (
        "Opération qui consiste à déterminer si plusieurs représentations renvoient ou non au même objet, puis à organiser leur fusion autour d’un canonique après validation humaine.",
        "Sécuriser l’identité des objets du jumeau numérique, pour réduire les divergences de représentation sans prétendre réécrire le sens des objets fusionnés.",
    ),
    "Concept - Enjeu.md": (
        None,
        "Capturer largement les tensions et opportunités exprimées dans une organisation, pour rendre des sujets comparables et priorisables avant consolidation éventuelle en problématiques ou objectifs.",
    ),
    "Concept - Environnement.md": (
        None,
        "Décrire et comparer les contextes vécus d’une organisation, pour rendre lisible ce qui influence ses conditions d’action sans confondre cadre, ressources, acteurs ou événements.",
    ),
    "Concept - Environnements LBP.md": (
        None,
        "Découper l’écosystème LBP en environnements d’usage distincts, pour clarifier les frontières d’usage, éviter les mélanges (méta, opérationnel, données client, mission) et stabiliser la maintenance.",
    ),
    "Concept - Gestion de la connaissance.md": (
        None,
        "Piloter intentionnellement les conditions qui rendent les connaissances d’un collectif identifiables, accessibles et utilisées, pour améliorer durablement la qualité des décisions et de l’action.",
    ),
    "Concept - Glossaire LBP.md": (
        None,
        "Stabiliser le sens des concepts mobilisés dans l’écosystème LBP, pour réduire les ambiguïtés et soutenir l’outillage humain et IA dans l’analyse, le diagnostic et la conception.",
    ),
    "Concept - Glossaire spécifique.md": (
        None,
        "Stabiliser et expliciter le vocabulaire propre à une organisation cliente, pour réduire les incompréhensions, accélérer l’onboarding et fiabiliser l’interprétation dans son contexte.",
    ),
    "Concept - Hard skill.md": (
        "Compétence individuelle à dominante technique, enseignable et évaluable, permettant d’exécuter ou de concevoir une activité spécifique selon des méthodes, normes, outils ou raisonnements techniques.",
        "Distinguer l’exigence technique d’un poste de la compétence démontrée d’un individu, pour éviter la confusion entre savoir déclaré, usage d’un outil et compétence réellement opératoire.",
    ),
    "Concept - Horizon temporel.md": (
        None,
        "Réduire l’ambiguïté des termes court/moyen/long terme, pour aligner les projections collectives et rendre comparables priorisations, roadmaps et décisions.",
    ),
    "Concept - Indicateur.md": (
        None,
        "Quantifier un phénomène pour le rendre lisible, comparable et pilotable dans le temps, sans le confondre avec données brutes, tableaux de bord ou métriques non définies.",
    ),
    "Concept - Individu.md": (
        None,
        "Décrire de façon traçable les personnes dont l’interaction avec une organisation est significative, pour relier le fonctionnement réel aux décisions de diagnostic, pilotage et transformation.",
    ),
    "Concept - Initiative organisationnelle.md": (
        "Effort intentionnel, temporaire et délimité, porté au sein ou entre une ou plusieurs organisations, visant à transformer, construire, déployer, explorer, coordonner ou résoudre quelque chose au-delà du fonctionnement courant.",
        "Distinguer l’effort structuré dans le temps des groupes humains qui le portent, pour suivre des transformations bornées sans les confondre avec pratiques ou processus récurrents.",
    ),
    "Concept - Innovation (capacité motrice).md": (
        "Aptitude collective durable à convertir des signaux, idées et apprentissages en nouveautés utiles réellement introduites puis diffusées, de manière répétable et soutenable.",
        "Caractériser comment une organisation transforme l’exploration en décisions et déploiements, pour expliquer l’émergence et le maintien de capacités métier différenciantes.",
    ),
    "Concept - Input - Output (LBP).md": (
        "Cadre de définition des entrées et sorties dans le fonctionnement LBP : un input est une information ou un artefact consommé pour produire un résultat, un output est l’information ou l’artefact produit par une transformation.",
        "Standardiser la lecture des transformations dans LBP en distinguant inputs et outputs génériques (natures) et spécifiques (instances en mission), pour maximiser la qualité des productions.",
    ),
    "Concept - Input - Output (Processus).md": (
        None,
        "Clarifier le contrat de transformation d’un processus en explicitant ses interfaces, sa qualité attendue et ses critères de terminé, pour réduire frictions de coordination et re-travail.",
    ),
    "Concept - Instructions d’écriture et clefs de lecture.md": (
        None,
        "Distinguer la règle de production d’une valeur de sa règle d’interprétation, pour aligner extraction, consolidation, lecture analytique et contrôle qualité dans l’écosystème.",
    ),
    "Concept - Intelligence collective (capacité motrice).md": (
        "Aptitude collective durable à faire sens ensemble, juger, décider et résoudre des problèmes de manière coordonnée au-delà des silos, avec une adoption réelle et des effets multi-cycles.",
        "Caractériser la qualité de pensée et de décision d’un collectif au-delà de ses individus, pour expliquer la réduction des frictions d’interface et la soutenabilité des autres capacités motrices.",
    ),
    "Concept - KPI.md": (
        None,
        "Distinguer une mesure réellement décisionnelle d’une métrique de reporting, pour sécuriser le pilotage par indicateurs et éviter la dérive vers les mesures non actionnées.",
    ),
    "Concept - Logic block.md": (
        "Module opératoire de raisonnement, ciblé sur une opération et une cible données, qui complète une instruction générale en apportant une logique locale de traitement, de comparaison, de prudence et de décision.",
        "Augmenter la précision d’un agent sur un cas d’opération précis, pour spécialiser localement un raisonnement sans démultiplier les variantes de prompts.",
    ),
    "Concept - Mad skill.md": (
        None,
        "Révéler les leviers différenciants chez les individus issus de parcours atypiques, pour éviter la sous-exploitation de talents latents et activer ces compétences de façon intentionnelle.",
    ),
    "Concept - Manuel de BDD.md": (
        None,
        "Tenir la spécification stable de la structure et des règles d’une base, pour servir de source de vérité structurelle protégeant la cohérence du modèle dans le temps.",
    ),
    "Concept - Matrice des 5 Dimensions de l’Organisation (5D).md": (
        "Cadre de lecture systémique stable qui qualifie et relie des observations organisationnelles selon 5 dimensions et 10 sous-dimensions (2 sous-dimensions par dimension).",
        "Réduire les angles morts d’une analyse organisationnelle, pour éviter les explications monocausales et raisonner sur des leviers cohérents à l’échelle d’une organisation.",
    ),
    "Concept - Modulateur.md": (
        "Condition observable qui augmente ou diminue l’effectivité d’un type de pratique organisationnelle, sans être ni une pratique ni une ressource — qualifie une « règle du jeu » vécue (clarté, stabilité, disponibilité, discipline, autorisation sociale).",
        "Remonter aux leviers racine d’effectivité d’une pratique, pour expliquer pourquoi une pratique existe mais « ne marche pas » ou plafonne malgré sa présence.",
    ),
    "Concept - Méthode LBP.md": (
        None,
        "Décrire un « comment faire » durable indépendamment des contextes d’exécution, pour stabiliser la cohérence des productions, capitaliser et soutenir l’assistance par IA.",
    ),
    "Concept - OKR.md": (
        None,
        "Traduire des problématiques priorisées en engagements discutables et suivables, pour aligner les acteurs sur des résultats et conserver la traçabilité des décisions de pilotage.",
    ),
    "Concept - Organisation.md": (
        "Acteur collectif institué, reconnu comme entité distincte, avec des frontières, une responsabilité et une capacité de représentation.",
        "Distinguer le cadre institutionnel d’un système des groupes humains opérants qui y agissent, pour cadrer correctement les analyses d’acteurs, de relations et de gouvernance.",
    ),
    "Concept - Partie prenante.md": (
        None,
        "Expliciter les intérêts, attentes, contraintes, pouvoirs et risques relationnels autour d’une organisation, pour cartographier ses interdépendances avec son écosystème.",
    ),
    "Concept - Performance opérationnelle (capacité motrice).md": (
        None,
        "Caractériser la fiabilité de la délivrance malgré la variabilité, pour stabiliser l’exécution, réduire l’héroïsme et rendre adaptation et innovation soutenables dans la durée.",
    ),
    "Concept - Philosophie (LBP).md": (
        "Noyau de sens d’une organisation regroupant Mission, Vision, Valeurs et Raison d’être : ce qu’elle fait et pour qui, où elle veut aller, comment elle entend agir et pourquoi elle existe au-delà de ses activités. Dite « réelle » quand elle se vérifie dans des arbitrages et comportements répétés.",
        "Capturer le noyau de sens d’une organisation au-delà de ses formulations affichées, pour révéler ce qui guide réellement ses arbitrages et orienter les transformations en profondeur.",
    ),
    "Concept - Poste.md": (
        "Position formelle contextualisée, définie indépendamment de la personne qui l’occupe, avec une finalité, un périmètre de responsabilité et des attentes explicites ou durablement stabilisées dans l’organisation.",
        "Distinguer la structure formelle d’une organisation des individus réels qui l’occupent, pour analyser couverture, vacance et adéquation indépendamment des personnes en poste.",
    ),
    "Concept - Pratiques (organisation).md": (
        "Pattern opérant récurrent, identifiable et descriptible (quoi, avec qui, pourquoi, comment), qui produit des effets durables (valeur, robustesse, apprentissage, performance, alignement).",
        "Décrire le « réel » de ce qui est effectivement fait dans une organisation, pour lire la cohérence des pratiques avec les principes et révéler les écarts intention/réalité.",
    ),
    "Concept - Principes (organisation).md": (
        "Intention normative stable qui guide des arbitrages récurrents et oriente durablement des décisions et comportements attendus.",
        "Nommer ce qui doit être vrai dans une organisation au-delà des objectifs datés, pour disposer d’une cible normative stable distincte des pratiques effectives et des objectifs mesurés.",
    ),
    "Concept - Problématique.md": (
        None,
        "Consolider plusieurs enjeux proches en un thème canonique réduit, pour aligner la gouvernance autour de sujets traçables et priorisables avant formalisation en objectifs.",
    ),
    "Concept - Processus.md": (
        "Fonctionnement coordonné et relativement stable qui transforme des inputs en outputs au service d’une finalité explicite, qualifié par un niveau (activité, opération ou étape) afin de rendre lisibles le bon zoom, les interfaces, les critères d’acceptation et la preuve de terminé.",
        "Lire le fonctionnement coordonné d’une organisation par contrats stables de transformation, pour rendre visibles interfaces, qualité attendue et preuves de terminé.",
    ),
    "Concept - Prompt maître.md": (
        "Prompt de cadrage opératoire général qui définit le contrat d’une fonction ou d’une opération dans l’écosystème LBP : mission, protocole, garde-fous, entrées, sorties et articulation avec les logic blocks.",
        "Tenir un contrat fonctionnel partagé pour une opération récurrente, pour disposer d’un point d’autorité commun sans porter toute la logique locale d’un cas particulier.",
    ),
    "Concept - Refactor.md": (
        "Opération qui consiste à proposer un nouveau set d’objets, plus cohérent et plus exploitable, à l’intérieur d’une même base interprétative ou fortement recouvrante, sans résoudre une identité concurrente mais en réorganisant l’ensemble pour qu’il fasse davantage sens.",
        "Réorganiser un ensemble d’objets pour gagner en cohérence et exploitabilité, sans toucher aux identités, pour dissiper le brouillard sémantique d’un domaine documenté de façon hétérogène.",
    ),
    "Concept - Relation inter-organisations.md": (
        "Lien structurant entre deux organisations distinctes, décrivant la nature de leur interaction, leur orientation, leur temporalité et leur périmètre.",
        "Rendre visible ce qui relie les acteurs institutionnels entre eux, sans confondre ce lien avec la hiérarchie interne des organisations ni avec leurs propriétés intrinsèques.",
    ),
    "Concept - Relations Maker.md": (
        "Opération qui consiste à proposer, justifier et faire valider des relations entre objets déjà présents dans le jumeau numérique, selon deux cas : relations entre BDD différentes ou relations au sein d’une même BDD à logique relationnelle interne.",
        "Enrichir le tissu relationnel du jumeau numérique de façon traçable, pour relier les objets pertinents sans court-circuiter la validation humaine ni dupliquer la logique de chaque base.",
    ),
    "Concept - Repères communs.md": (
        None,
        "Stabiliser l’interprétation, la coordination et l’appartenance d’un collectif, pour rendre visibles les attentes communes et réduire les ambiguïtés du fonctionnement quotidien.",
    ),
    "Concept - Soft skill.md": (
        None,
        "Qualifier des comportements concrets et observables transversaux à de nombreux métiers, pour éviter la confusion entre jugements vagues, traits de personnalité et compétences réellement démontrées.",
    ),
    "Concept - Source de vérité.md": (
        None,
        "Désigner une représentation faisant autorité pour chaque information critique, pour réduire divergences, asymétries et conflits d’interprétation entre humains et systèmes.",
    ),
    "Concept - Source d’information.md": (
        None,
        "Garantir la traçabilité des informations utilisées en diagnostic et en pilotage, pour conserver métadonnées, prudence de lecture et preuves indispensables à la qualité d’analyse.",
    ),
    "Concept - System prompt.md": (
        "Cadre d’identité, d’autorité et de comportement stable d’un agent LBP, qui définit sa posture profonde, ses garde-fous globaux, son périmètre de confiance, son rapport aux autres couches de prompting et, le cas échéant, son enveloppe technique d’accès et d’exécution.",
        "Tenir le cadre stable d’un agent au-delà des tâches qu’il exécute, pour assurer une posture, des garde-fous et un périmètre de confiance constants entre runs et entre cas.",
    ),
    "Concept - Taxonomie.md": (
        None,
        "Fixer un vocabulaire canonique pour qualifier des objets de manière comparable dans le temps, pour réduire les ambiguïtés, rendre les données filtrables et servir de contrat commun humains-systèmes.",
    ),
    "Concept - Template de brick.md": (
        None,
        "Standardiser la structure attendue d’une production de brick, pour rendre la qualité plus reproductible et faciliter la réutilisation des bricks dans une chaîne de livrables.",
    ),
    "Concept - Tempo (LBP).md": (
        "Cadence partagée et consciemment régulée à laquelle une organisation observe, décide, apprend et délivre, combinant régularité, synchronisation multi-niveaux et soutenabilité, plutôt que la seule vitesse.",
        "Caractériser la cadence consciemment régulée d’une organisation, pour fluidifier la coordination et accélérer les boucles d’apprentissage sans épuiser le système.",
    ),
    "Concept - Unknown unknown.md": (
        "Facteur, événement ou mécanisme dont l’existence n’est pas identifiée a priori, donc absent des hypothèses et des scénarios.",
        "Penser les angles morts et surprises à fort impact, pour concevoir des organisations robustes et capables d’apprendre face à ce qui n’a pas été anticipé.",
    ),
    "Concept - Vision partagée.md": (
        None,
        "Tenir une image commune et mobilisatrice d’un futur désiré, pour servir de repère de direction et de cohérence dans les arbitrages, la coordination et l’apprentissage collectif.",
    ),
    "Concept - Événement.md": (
        None,
        "Reconstruire des chronologies organisationnelles à partir de jalons concrets, pour relire des dynamiques (structure, pratiques, capacités, résultats) et contextualiser enjeux, problématiques et indicateurs.",
    ),
}


def replace_field(content, field, new_value):
    pat_block = re.compile(rf"^{field}: >[^\S\n]*\n((?:[ \t]+.*\n)+)", re.MULTILINE)
    pat_line = re.compile(rf'^{field}:[ \t]+.*$', re.MULTILINE)
    new_line = f'{field}: "{new_value}"'
    if pat_block.search(content):
        return pat_block.sub(new_line + "\n", content, count=1), True
    if pat_line.search(content):
        return pat_line.sub(new_line, content, count=1), True
    return content, False


def main():
    stats = {"ok": 0, "skipped": 0, "missing": [], "too_long": [], "partial": []}
    files = sorted(DIR.glob("Concept - *.md"))
    for p in files:
        if p.name in SKIP:
            stats["skipped"] += 1
            continue
        if p.name not in MAPPING:
            stats["missing"].append(p.name)
            continue
        new_sum, new_pur = MAPPING[p.name]
        if new_sum is not None and len(new_sum) > 400:
            stats["too_long"].append(f"{p.name} sum={len(new_sum)}")
            continue
        if len(new_pur) > 400:
            stats["too_long"].append(f"{p.name} pur={len(new_pur)}")
            continue
        c = p.read_text(encoding="utf-8")
        sok = True
        if new_sum is not None:
            c, sok = replace_field(c, "summary", new_sum)
        c, pok = replace_field(c, "purpose", new_pur)
        if sok and pok:
            p.write_text(c, encoding="utf-8")
            stats["ok"] += 1
        else:
            stats["partial"].append(f"{p.name} sum={sok} pur={pok}")

    print(f"OK: {stats['ok']} / {len(files) - stats['skipped']}")
    print(f"Skipped: {stats['skipped']}")
    if stats["missing"]:
        print(f"\nMissing mapping ({len(stats['missing'])}):")
        for n in stats["missing"]: print(f"  {n}")
    if stats["too_long"]:
        print(f"\nToo long ({len(stats['too_long'])}):")
        for n in stats["too_long"]: print(f"  {n}")
    if stats["partial"]:
        print(f"\nPartial ({len(stats['partial'])}):")
        for n in stats["partial"]: print(f"  {n}")


if __name__ == "__main__":
    main()
