#!/usr/bin/env python3
"""Refonte v3 des champs summary et purpose des taxonomies LBP selon R-060 v3.

Stratégie:
- Mapping {code_taxo: (summary_v3, purpose_v3)} avec version finale R-060 v3
- Pour chaque fichier .md, regex multilignes qui :
    * trouve le bloc `summary: ...` (chaîne quotée OU bloc multiligne `>`)
    * le remplace par `summary: "<v3>"` sur une ligne
    * idem pour `purpose: ...`
- Sauvegarde en place
- Skip les 3 cas test déjà v3 (ORG.ROLE, SCALE.CRITICALITY, ASSET.SUBTYPE)
"""

import os
import re
import sys
from pathlib import Path

TAXO_DIR = Path(r"H:\Drive partagés\LBP - shared\Architecture data\Taxonomies")

# Skip ces 3 cas test déjà v3 finale
SKIP = {"ORG.ROLE", "SCALE.CRITICALITY", "ASSET.SUBTYPE"}

# Mapping {code: (summary, purpose)} en R-060 v3 strict
MAPPING = {
    "ACT.CONSOLIDATION_TARGET": (
        "Référentiel des cibles d’aval probables vers lesquelles une action détectée peut être consolidée.",
        "Préqualifier l’orientation de consolidation d’une action détectée vers son objet d’aval probable, pour préparer un arbitrage de classement aval sans préjuger de la décision finale.",
    ),
    "ACT.IMPACT_DOMAIN": (
        "Référentiel des grands domaines sur lesquels une action produit principalement ses effets dans une organisation.",
        "Qualifier les domaines principaux d’effet d’une action, pour cartographier de façon homogène la zone d’impact d’un portefeuille d’actions.",
    ),
    "ACT.INTENT": (
        "Référentiel des intentions dominantes d’une action — ce qu’elle cherche à accomplir ici et maintenant.",
        "Qualifier l’intention dominante d’une action, pour rendre lisible et comparable la finalité immédiate poursuivie au sein d’un portefeuille d’actions.",
    ),
    "AGENT.FAMILY": (
        "Référentiel des grandes familles fonctionnelles de profils d’agents LBP, structurées par rôle dominant.",
        "Classer un profil d’agent par sa famille fonctionnelle dominante, pour rendre les profils comparables et faciliter le routage et la recherche au sein du portefeuille d’agents.",
    ),
    "ASSET.LIFECYCLE": (
        "Référentiel des états dominants d’usage et de vie d’un actif, de sa conception à son archivage.",
        "Qualifier l’état d’usage ou de vie dominant d’un actif à un instant donné, pour rendre lisible le cycle de vie du portefeuille d’actifs et le suivre dans le temps.",
    ),
    "ASSET.PROVENANCE": (
        "Référentiel des modes par lesquels un actif est obtenu, mis à disposition ou repris dans une organisation.",
        "Qualifier le mode dominant de provenance d’un actif, pour rendre lisible et comparable l’origine ou le régime de mise à disposition au sein d’un portefeuille d’actifs.",
    ),
    "ASSET.SUBSTITUTABILITY": (
        "Échelle 1-5 du degré auquel un actif peut être remplacé, contourné ou retiré sans rupture majeure pour l’organisation qui en dépend.",
        "Positionner un actif sur une échelle de substituabilité, pour rendre comparable la réversibilité réelle de différents actifs au sein d’un portefeuille.",
    ),
    "BRAIN.LAYER": (
        "Référentiel des couches d’abstraction d’une base de connaissances du Brain LBP.",
        "Classer une base de connaissances du Brain par sa couche d’abstraction, pour orienter l’accès aux ressources sémantiques ou opérationnelles selon le besoin.",
    ),
    "BRAIN.SUBTYPE": (
        "Référentiel des rôles structurels d’une base de connaissances du Brain LBP au sein de l’écosystème.",
        "Identifier le rôle structurel d’une base de connaissances du Brain, pour rendre lisible la doctrine relationnelle attendue et orchestrer correctement les requêtes sur l’écosystème.",
    ),
    "BRICK.FAMILY": (
        "Référentiel des grandes familles fonctionnelles d’une brick LBP.",
        "Classer une brick par sa famille fonctionnelle dominante, pour structurer les vues, faciliter la recherche et homogénéiser le portefeuille de bricks.",
    ),
    "CAP.DISTINCTIVITY": (
        "Référentiel du caractère distinctif d’une capacité métier sur son marché.",
        "Qualifier le caractère distinctif d’une capacité métier, pour identifier les capacités candidates au statut d’avantage concurrentiel au sein d’un portefeuille.",
    ),
    "CAP.FAMILY": (
        "Référentiel des grandes familles ontologiques d’une capacité organisationnelle, classée par son rôle dans le système d’ensemble.",
        "Classer une capacité organisationnelle par son rôle ontologique, pour structurer un portefeuille de capacités et rendre les comparaisons inter-organisations possibles.",
    ),
    "CAP.NATURE": (
        "Référentiel de la nature d’une capacité organisationnelle, opposant capacités collectives transversales et capacités métier d’exécution.",
        "Qualifier la nature d’une capacité organisationnelle, pour rendre lisible l’équilibre entre dynamiques collectives et savoir-faire d’exécution au sein d’un portefeuille.",
    ),
    "COL.DEP_LEVEL": (
        "Échelle 1-5 du niveau de dépendances extérieures qui imposent leur rythme à un collectif.",
        "Positionner un collectif sur une échelle de couplage à son environnement, pour rendre lisible et comparable la part de son rythme conditionnée par des éléments situés hors de lui.",
    ),
    "COL.FORMALITY": (
        "Échelle 1-5 du degré de reconnaissance, de cadrage et d’institutionnalisation d’un collectif.",
        "Positionner un collectif sur une échelle de formalisation, pour rendre lisible et comparable son degré d’inscription dans le cadre organisationnel.",
    ),
    "COL.ORIENTATION": (
        "Référentiel des logiques dominantes selon lesquelles un collectif est structuré.",
        "Identifier la logique dominante qui structure un collectif, pour rendre les modes de découpage comparables au-delà des intitulés.",
    ),
    "COL.TEMPORALITY": (
        "Référentiel des grandes formes de stabilité temporelle d’un collectif.",
        "Qualifier la stabilité temporelle dominante d’un collectif, pour rendre lisible la durée et la continuité de son existence indépendamment de sa forme.",
    ),
    "COL.TEMPO_CLASS": (
        "Échelle 1-5 de la cadence globale d’un collectif, lue à travers ses cycles de coordination, d’action et de feedback.",
        "Positionner un collectif sur une échelle de cadence, pour calibrer les analyses et plans d’action sur le rythme réel du groupe.",
    ),
    "COL.TEMPO_VAR": (
        "Échelle 1-5 de la variabilité du rythme d’un collectif, du très stable au chaotique.",
        "Positionner un collectif sur une échelle de variabilité, pour rendre lisible la stabilité de son rythme indépendamment de sa cadence absolue.",
    ),
    "COL.TYPE": (
        "Cadre hiérarchique des formes que peut prendre un collectif humain opérant et identifiable.",
        "Classer un collectif par sa forme dominante, pour qualifier de façon homogène les groupes humains opérant au sein de l’écosystème observé.",
    ),
    "DBMAN.SCOPE": (
        "Référentiel du scope architectural d’un manuel de base de connaissances dans l’écosystème LBP.",
        "Classer un manuel de base de connaissances par son scope architectural, pour rendre lisible son positionnement dans l’écosystème indépendamment du préfixe de son code.",
    ),
    "DOC.TYPE": (
        "Référentiel des grands types formels de documents produits ou consommés dans l’écosystème LBP.",
        "Classer un document par son type formel, pour orienter le rangement, la lecture et le traitement attendu indépendamment de son contenu spécifique.",
    ),
    "EMO.TYPE": (
        "Cadre hiérarchique des émotions dominantes inférables d’une source verbatim ou textuelle.",
        "Qualifier l’émotion dominante inférée d’une source textuelle, sous condition stricte de présence de marqueurs affectifs explicites, pour enrichir la lecture phénoménologique des signaux.",
    ),
    "ENJ.DOMAIN": (
        "Cadre hiérarchique des domaines d’observation d’un enjeu ou d’une problématique — le langage et le sujet dans lesquels il est formulé.",
        "Qualifier le ou les domaines d’observation d’un enjeu, pour rendre lisible le sujet dans lequel il est formulé indépendamment de ses causes profondes.",
    ),
    "ENJ.EXPRESSION": (
        "Cadre hiérarchique des formes dominantes d’énonciation d’un enjeu.",
        "Qualifier la forme dominante d’énonciation d’un enjeu, pour rendre lisible la valence du matériau collecté et guider la reformulation propre.",
    ),
    "ENJ.HORIZON": (
        "Échelle 1-5 de l’horizon dominant de matérialisation ou de résolution d’un enjeu, exprimé en fenêtres temporelles absolues.",
        "Positionner un enjeu sur une échelle d’horizon temporel borné, pour lever les ambiguïtés du « court/moyen/long terme » par des fenêtres explicites partagées.",
    ),
    "ENV.CONTROLLABILITY": (
        "Échelle 1-5 du degré auquel une organisation peut agir concrètement sur un environnement.",
        "Positionner un environnement sur une échelle de contrôlabilité, pour rendre lisible la marge d’action réelle disponible sur le cadre considéré.",
    ),
    "ENV.PESTEL": (
        "Référentiel PESTEL des dimensions de l’environnement externe d’une organisation.",
        "Qualifier la nature des facteurs externes pesant sur une organisation, pour rendre lisible et comparable l’analyse macro-environnementale.",
    ),
    "ENV.SUBTYPE": (
        "Cadre hiérarchique des environnements perçus dans lesquels évoluent les acteurs d’une organisation.",
        "Classer un environnement perçu par sa nature dominante, pour rendre lisible et comparable le cadre dans lequel s’exerce l’activité.",
    ),
    "ENV.VOLATILITY": (
        "Échelle 1-5 du degré de stabilité ou d’instabilité d’un environnement dans le temps.",
        "Positionner un environnement sur une échelle de volatilité, pour rendre lisible la dynamique du cadre indépendamment de son importance ou de sa contrôlabilité.",
    ),
    "EVT.ORIGIN": (
        "Référentiel de l’origine dominante du déclenchement d’un événement par rapport au périmètre focal d’une mission.",
        "Qualifier l’origine dominante d’un événement, pour rendre lisible la nature du déclencheur indépendamment de ses effets ou des acteurs concernés.",
    ),
    "EVT.RECURRENCE_CLASS": (
        "Référentiel des classes de récurrence dominante d’un événement modélisé.",
        "Qualifier la logique de répétition dominante d’un événement, pour distinguer ce qui revient de ce qui est ponctuel sur le portefeuille d’événements.",
    ),
    "EVT.TIME_GRAIN": (
        "Échelle de granularité temporelle pour caractériser la durée effective d’un événement, du ponctuel au multi-annuel.",
        "Positionner un événement sur une échelle de durée, pour rendre lisible sa granularité temporelle indépendamment de son impact ou de son horizon.",
    ),
    "EVT.TIME_PRECISION": (
        "Échelle 1-5 de la qualité réelle de l’ancrage temporel d’un événement.",
        "Positionner un événement sur une échelle de précision temporelle, pour rendre explicite le niveau de précision disponible et éviter les fausses précisions.",
    ),
    "EVT.TIME_STATUS": (
        "Référentiel du statut temporel d’un événement dans la chronologie d’une organisation.",
        "Qualifier le statut temporel d’un événement, pour rendre lisible sa position chronologique relative au moment d’observation.",
    ),
    "EVT.TYPE": (
        "Cadre hiérarchique des natures principales d’un événement, pour construire une chronologie exploitable.",
        "Classer un événement par sa nature principale, pour construire une chronologie homogène accueillant une large amplitude d’événements de natures différentes.",
    ),
    "GLO.CAT": (
        "Référentiel des natures dominantes d’une entrée de glossaire spécifique.",
        "Qualifier une entrée de glossaire par la nature dominante du terme, pour orienter la rédaction de la définition et éviter les contresens.",
    ),
    "IMPACT.NATURE": (
        "Référentiel des natures d’un lien d’impact entre deux objets, décrivant comment l’un affecte l’autre.",
        "Qualifier la nature d’un lien d’impact entre deux objets, pour rendre lisible la manière dont l’un agit sur l’autre indépendamment de l’intensité de l’effet.",
    ),
    "IND.TYPE": (
        "Cadre hiérarchique des types d’individus selon leur relation à l’organisation focale d’une mission.",
        "Classer un individu par son type de relation à l’organisation, pour garantir la cohérence et l’exploitabilité du portefeuille d’individus.",
    ),
    "INDIC.DOMAIN": (
        "Référentiel des grands domaines métier sur lesquels porte un indicateur.",
        "Qualifier le domaine métier d’un indicateur, pour filtrer, comparer et organiser les indicateurs par familles de sens.",
    ),
    "INDIC.FREQ": (
        "Référentiel des fréquences de mise à jour d’un indicateur.",
        "Qualifier la fréquence de mise à jour d’un indicateur, pour harmoniser la lecture des rythmes de mesure entre indicateurs.",
    ),
    "INDIC.NATURE": (
        "Référentiel des dimensions caractérisant la nature d’un indicateur.",
        "Qualifier la nature d’un indicateur sur plusieurs axes compatibles, pour capturer son profil multi-facette sans démultiplier les taxonomies.",
    ),
    "INDIC.SCOPE_APPLI": (
        "Référentiel des niveaux d’application d’un indicateur dans une organisation.",
        "Qualifier le ou les niveaux d’application d’un indicateur, pour rendre lisible où s’applique la mesure indépendamment de son domaine métier.",
    ),
    "INDIC.TIME_ROLE": (
        "Référentiel du rôle temporel naturel d’un indicateur relativement à un résultat de référence.",
        "Qualifier le rôle temporel naturel d’un indicateur, pour distinguer un indicateur précurseur d’un indicateur de résultat constaté.",
    ),
    "INDIC.UNIT": (
        "Référentiel des familles d’unités de mesure d’un indicateur.",
        "Qualifier le type d’unité d’un indicateur, pour permettre comparaisons et lectures homogènes sans confondre unité, domaine métier et nature.",
    ),
    "INIT.DRIVER": (
        "Référentiel des moteurs dominants qui expliquent l’existence d’une initiative organisationnelle.",
        "Qualifier le moteur dominant d’une initiative organisationnelle, pour rendre lisible la raison d’être de l’effort indépendamment de sa forme et de sa phase.",
    ),
    "INIT.PHASE": (
        "Référentiel des phases ou états d’avancement d’une initiative organisationnelle.",
        "Qualifier la phase d’avancement d’une initiative organisationnelle, pour rendre lisible sa position dans sa trajectoire de vie.",
    ),
    "INIT.TYPE": (
        "Référentiel des formes dominantes d’une initiative organisationnelle.",
        "Qualifier la forme dominante d’une initiative organisationnelle, pour rendre lisible le type d’effort temporaire indépendamment de son moteur et de sa phase.",
    ),
    "INS.TYPE": (
        "Référentiel des formes principales du pattern observé dans un insight.",
        "Classer un insight par la forme principale du pattern observé, pour faciliter tri, clustering et déduplication indépendamment du degré de preuve.",
    ),
    "JOB.COVERAGE": (
        "Référentiel des situations de couverture d’un poste à un instant donné.",
        "Qualifier la situation réelle de couverture d’un poste, pour rendre lisible et comparable l’état d’occupation du portefeuille de postes au cours du temps.",
    ),
    "JOB.FAMILLE": (
        "Cadre hiérarchique des familles métier d’un poste, organisé par catégorie puis par famille.",
        "Classer un poste par sa famille métier dominante, pour qualifier le portefeuille de postes indépendamment des intitulés locaux.",
    ),
    "JOB.SENIORITE": (
        "Échelle 1-5 de séniorité d’un rôle, définie par les axes d’autonomie, de complexité et de responsabilité.",
        "Positionner un rôle sur une échelle de séniorité, pour harmoniser la lecture des niveaux indépendamment des intitulés locaux.",
    ),
    "LGBLK.FAMILY": (
        "Référentiel des natures d’opération réalisée par un logic block LBP.",
        "Classer un logic block par sa nature d’opération, pour rendre lisible la fonction du bloc dans l’orchestration et faciliter sa découverte.",
    ),
    "MET.FAMILY": (
        "Référentiel des grandes familles fonctionnelles d’une méthode LBP.",
        "Classer une méthode par sa famille fonctionnelle dominante, pour structurer les vues, faciliter la recherche et orienter le choix méthodologique.",
    ),
    "META.FAMILY": (
        "Référentiel des grandes familles fonctionnelles d’un document méta LBP.",
        "Classer un document méta par sa famille fonctionnelle dominante, pour faciliter rangement, recherche et sélection contextuelle au sein du portefeuille de doctrines.",
    ),
    "MTG.EXEC_STATUS": (
        "Référentiel des états opérationnels d’un meeting dans son cycle de vie.",
        "Qualifier l’état opérationnel d’un meeting, pour rendre lisible son avancement de planification et de tenue indépendamment de la maturité documentaire de la fiche.",
    ),
    "MTG.FORMAT": (
        "Référentiel des formats logistiques selon lesquels se tient un meeting.",
        "Qualifier le format logistique d’un meeting, pour piloter la logistique sans préjuger de la nature du meeting ni de son état d’exécution.",
    ),
    "MTG.TYPE": (
        "Référentiel des archétypes selon lesquels se tient un meeting de mission.",
        "Classer un meeting par son archétype dominant, pour activer les bons supports d’animation et homogénéiser les attendus de préparation, de tenue et de restitution.",
    ),
    "OBJ.CONFIDENTIALITE": (
        "Référentiel des niveaux de confidentialité applicables à un objet documentaire.",
        "Qualifier le niveau de confidentialité d’un objet, pour guider sa diffusion et son partage de façon homogène.",
    ),
    "OBJ.STATUT": (
        "Référentiel des états documentaires d’une fiche dans son cycle de remplissage et de validation.",
        "Qualifier l’état documentaire d’une fiche, pour rendre lisible sa maturité de remplissage et orienter les filtres et routines de complétude.",
    ),
    "OPS.ACTION_FAMILY": (
        "Référentiel des grandes familles fonctionnelles d’une action de mission opérationnelle.",
        "Classer une action de mission par sa famille fonctionnelle dominante, pour structurer les vues et faciliter la lecture du portefeuille d’actions.",
    ),
    "OPS.ACTION_ITEM_TYPE": (
        "Référentiel distinguant les niveaux parent et enfant des entrées d’un backlog d’actions.",
        "Distinguer un regroupement parent d’une entrée enfant exécutable dans un backlog, pour appliquer des règles de remplissage cohérentes et préserver la lisibilité du suivi.",
    ),
    "OPS.RESPONSIBLE_MAIN": (
        "Référentiel des principales catégories de portage de la responsabilité d’exécution sur une action ou activité de mission.",
        "Qualifier qui porte principalement la responsabilité d’exécution, pour piloter charge et coordination sans remplacer l’assignation à des individus.",
    ),
    "OPS.STATUS": (
        "Référentiel transversal de l’avancement d’exécution d’un objet de mission opérationnelle.",
        "Qualifier l’avancement d’exécution d’un objet opérationnel de façon homogène, pour piloter vues, filtres et routines sans confondre maturité de la fiche et avancement opérationnel.",
    ),
    "ORG.CONTEXTE": (
        "Référentiel des niveaux de périmètre organisationnel dans lesquels s’exerce un poste.",
        "Qualifier le périmètre organisationnel d’un poste, pour rendre lisible son ancrage dans la structure indépendamment de sa famille métier.",
    ),
    "ORG.JURISDICTION": (
        "Référentiel hiérarchique des juridictions de référence d’une organisation, codifiées au standard ISO 3166-1 alpha-2.",
        "Qualifier la juridiction d’une organisation, pour rendre lisible son pays de droit applicable indépendamment de ses pays de présence commerciale.",
    ),
    "ORG.SECTEUR": (
        "Référentiel hiérarchique des secteurs ou domaines d’activité d’une organisation.",
        "Qualifier le secteur d’activité d’une organisation, pour rendre lisible son positionnement filière et alimenter les analyses sectorielles.",
    ),
    "ORG.TYPE": (
        "Cadre hiérarchique des formes institutionnelles d’une organisation reconnue comme entité distincte.",
        "Qualifier la forme institutionnelle d’une organisation, pour rendre lisibles les acteurs reconnus indépendamment des collectifs humains qui les composent.",
    ),
    "ORG5D.DIM": (
        "Référentiel des cinq dimensions du modèle ORG5D pour qualifier le « où dans le système » d’un objet observé.",
        "Qualifier la dimension systémique principale d’un objet observé, pour structurer les analyses transverses et organiser les portefeuilles selon une grille commune.",
    ),
    "ORG_REL.TYPE": (
        "Cadre hiérarchique des natures dominantes d’un lien structurant entre deux organisations distinctes.",
        "Qualifier la nature dominante d’un lien inter-organisations, pour rendre lisible le type de relation indépendamment de son statut, sa durée ou sa criticité.",
    ),
    "OUT.FAMILY": (
        "Référentiel des familles d’usage principal des outils logiciels et formats standards externes.",
        "Classer un outil ou format externe par sa famille d’usage principal, pour faciliter le filtrage et la recommandation dans le bon contexte.",
    ),
    "PLATFORM.ENV": (
        "Référentiel des environnements de déploiement utilisés par la plateforme LBP.",
        "Normaliser l’environnement de déploiement d’un objet de la plateforme, pour fiabiliser les vues multi-environnements et éviter les variantes de libellés.",
    ),
    "PRA.TYPE": (
        "Cadre hiérarchique des types de pratiques organisationnelles, classées par mécanisme de valeur dominant.",
        "Classer une pratique par son mécanisme de valeur dominant, pour organiser un portefeuille de pratiques indépendamment des capacités organisationnelles qu’elles renforcent.",
    ),
    "PROC.NIVEAU": (
        "Référentiel des niveaux d’emboîtement d’un item dans la base des processus.",
        "Qualifier le niveau d’un item dans la structure des processus, pour appliquer des exigences de remplissage adaptées au niveau.",
    ),
    "PROMPT.ARCH_ROLE": (
        "Référentiel des rôles architecturaux d’un prompt LBP dans l’orchestration agentique.",
        "Classer un prompt par son rôle architectural, pour rendre lisible sa place dans l’orchestration indépendamment de son type dominant et de son statut de déploiement.",
    ),
    "PROMPT.DEPLOY_STATUS": (
        "Référentiel des statuts de déploiement d’un prompt LBP dans son cycle de vie.",
        "Qualifier le statut de déploiement d’un prompt, pour distinguer ce qui est en production de ce qui est en test ou retiré, et fiabiliser les vues d’usage.",
    ),
    "PROMPT.TYPE": (
        "Référentiel des types dominants d’un prompt LBP par intention de production.",
        "Classer un prompt par son type dominant, pour filtrer, construire des vues qualité et router les usages au sein du portefeuille de prompts.",
    ),
    "SCALE.ALIGNMENT": (
        "Échelle 1-5 du degré d’alignement entre une intention-cible et les pratiques réelles observées.",
        "Positionner un objet sur une échelle d’alignement, pour rendre comparable l’écart entre intention et pratique réelle entre objets ou dans le temps.",
    ),
    "SCALE.COLLAB_INTENSITY": (
        "Échelle 1-5 du niveau d’interaction effectivement déployé pour réaliser une action, du travail autonome à l’intelligence collective.",
        "Positionner une action sur une échelle d’intensité collaborative, pour rendre lisible le mode de travail mobilisé indépendamment du résultat obtenu.",
    ),
    "SCALE.CONFIDENCE": (
        "Échelle 0-5 de la confiance accordée à une information ou un extrait au regard des preuves disponibles.",
        "Positionner une information sur une échelle de confiance, pour rendre lisible et comparable son degré de fiabilité au sein d’un corpus.",
    ),
    "SCALE.COVERAGE": (
        "Échelle de la directivité d’une mesure par rapport au phénomène qu’elle prétend éclairer.",
        "Positionner une mesure sur une échelle de couverture, pour rendre explicite la qualité du lien entre la mesure et le phénomène observé.",
    ),
    "SCALE.GRANULARITY": (
        "Échelle 1-5 de la granularité d’une action, de la tâche élémentaire à la macro-fonction.",
        "Positionner une action sur une échelle de granularité, pour qualifier de façon homogène le niveau de découpage retenu pour la modélisation.",
    ),
    "SCALE.IMPACT_INTENSITY": (
        "Échelle 0-5 de l’intensité d’un lien d’impact entre deux objets.",
        "Positionner un lien d’impact sur une échelle d’intensité, pour rendre comparable la force des effets indépendamment de leur nature ou de leur horizon.",
    ),
    "SCALE.INFLUENCE": (
        "Échelle 1-5 du poids structurel et de la centralité d’un objet dans le système qu’il habite.",
        "Positionner un objet sur une échelle d’influence, pour rendre comparable son poids structurel indépendamment de sa criticité ou de son pouvoir hiérarchique.",
    ),
    "SCALE.MATURITY": (
        "Échelle 0-5 du degré de maturité d’un objet observé sur un axe ordinal stable.",
        "Positionner un objet sur une échelle de maturité, pour rendre comparable son degré de développement entre objets ou dans le temps.",
    ),
    "SCALE.NECESSITY_TODAY": (
        "Échelle 1-5 du caractère indispensable d’une action pour assurer la production du jour J.",
        "Positionner une action sur une échelle de nécessité quotidienne, pour distinguer le strictement indispensable du contournable au sein d’un backlog.",
    ),
    "SCALE.PROCESSISATION": (
        "Échelle 1-5 du degré de formalisation et de maîtrise d’une action ou d’un flux.",
        "Positionner une action sur une échelle de processisation, pour rendre lisible son niveau de standardisation et de pilotage indépendamment de sa performance.",
    ),
    "SCALE.RECURRENCE": (
        "Échelle 1-5 de la fréquence d’occurrence d’une action, de l’événement unique au flux continu.",
        "Positionner une action sur une échelle de récurrence, pour soutenir les heuristiques de typage en distinguant ce qui revient de ce qui est ponctuel.",
    ),
    "SCALE.SAILLANCE": (
        "Échelle 1-5 de la saillance perçue d’un signal, combinant récurrence, portée et impact potentiel.",
        "Positionner un signal sur une échelle de saillance, pour rendre comparable son importance perçue et orienter la priorisation de l’investigation.",
    ),
    "SCALE.SCOPE": (
        "Échelle 0-5 de l’étendue d’interaction d’un objet selon le périmètre relationnel concerné.",
        "Positionner un objet sur une échelle de scope d’interaction, pour rendre comparable la portée relationnelle indépendamment de l’importance ou de la criticité.",
    ),
    "SCALE.VALUE_HORIZON": (
        "Échelle 1-5 de l’horizon auquel la valeur principale d’une action se matérialise par nature.",
        "Positionner une action sur une échelle d’horizon de valeur, pour décorréler le moment d’observation du délai naturel de matérialisation de la valeur.",
    ),
    "SIG.NATURE": (
        "Référentiel des formes phénoménologiques dominantes d’un signal.",
        "Qualifier la forme phénoménologique dominante d’un signal, pour guider l’extraction et la lecture du matériau qualitatif collecté.",
    ),
    "SIG.REGISTRE": (
        "Référentiel des registres ou loci où se situe le mécanisme principal qui produit un signal.",
        "Qualifier le locus d’un signal — où se situe le mécanisme qui le produit — pour rendre lisible la nature du phénomène indépendamment de son sujet.",
    ),
    "SKILL.HARD": (
        "Cadre de normalisation des compétences techniques, outillées ou normatives d’un poste ou d’un individu.",
        "Qualifier les compétences techniques d’un poste ou d’un individu, pour homogénéiser la lecture des savoir-faire avec un vocabulaire stable au niveau des familles.",
    ),
    "SKILL.SOFT": (
        "Cadre fermé des compétences comportementales d’un individu, structuré en blocs et sous-domaines.",
        "Qualifier les comportements observables d’un individu, pour rendre lisibles les savoir-être avec un vocabulaire commun.",
    ),
    "SRC.EXTRACT_TARGET": (
        "Référentiel des cibles d’extraction recommandées pour une source d’information.",
        "Qualifier les cibles d’extraction d’une source, pour orienter le pipeline d’extraction et homogénéiser les attendus en aval.",
    ),
    "SRC.FORMAT": (
        "Référentiel des formats d’origine d’une source d’information avant conversion en Markdown.",
        "Qualifier le format d’origine d’une source, pour choisir le bon pipeline de conversion et anticiper la qualité d’extraction.",
    ),
    "SRC.PROVENANCE": (
        "Référentiel des modes de provenance d’une source d’information dans son régime épistémique.",
        "Qualifier la provenance d’une source, pour adapter son traitement en termes d’officialité, de prudence d’interprétation et de confidentialité.",
    ),
    "STAKEHOLDER.ROLE": (
        "Référentiel des rôles relationnels d’une organisation vis-à-vis de l’organisation focale.",
        "Qualifier le rôle relationnel d’une organisation, pour cartographier les parties prenantes indépendamment des liens structurels.",
    ),
}


# Regex multilignes pour matcher summary et purpose dans le frontmatter YAML
# Le bloc summary ou purpose peut être :
#   summary: "..."
#   summary: '...'
#   summary: texte sans guillemets sur une ligne
#   summary: >
#     ligne 1
#     ligne 2
# (et idem pour purpose)

def replace_field(content: str, field_name: str, new_value: str) -> tuple[str, bool]:
    """Remplace le champ field_name dans le frontmatter par la nouvelle valeur (chaîne quotée).

    Retourne (nouveau_contenu, bool: a-t-on trouvé et remplacé).
    """
    # Pattern pour bloc multiligne `field: >` puis indentation
    pat_block = re.compile(
        rf"^{field_name}: >[^\S\n]*\n((?:[ \t]+.*\n)+)",
        flags=re.MULTILINE,
    )
    # Pattern pour ligne simple : `field: ...` (avec ou sans guillemets, jusqu'à fin de ligne)
    pat_line = re.compile(
        rf'^{field_name}:[ \t]+.*$',
        flags=re.MULTILINE,
    )

    new_line = f'{field_name}: "{new_value}"'

    if pat_block.search(content):
        new_content = pat_block.sub(new_line + "\n", content, count=1)
        return new_content, True

    if pat_line.search(content):
        new_content = pat_line.sub(new_line, content, count=1)
        return new_content, True

    return content, False


def process_file(path: Path) -> dict:
    """Process un fichier .md de taxonomie. Retourne un dict de stats."""
    code = path.stem  # ex. "ACT.INTENT"

    if code in SKIP:
        return {"file": code, "status": "skipped (cas test)", "summary_changed": False, "purpose_changed": False}

    if code not in MAPPING:
        return {"file": code, "status": "MISSING_MAPPING", "summary_changed": False, "purpose_changed": False}

    summary, purpose = MAPPING[code]

    # Vérification longueur
    if len(summary) > 400:
        return {"file": code, "status": f"summary >400 ({len(summary)})", "summary_changed": False, "purpose_changed": False}
    if len(purpose) > 400:
        return {"file": code, "status": f"purpose >400 ({len(purpose)})", "summary_changed": False, "purpose_changed": False}

    content = path.read_text(encoding="utf-8")
    content, sum_ok = replace_field(content, "summary", summary)
    content, pur_ok = replace_field(content, "purpose", purpose)

    if sum_ok or pur_ok:
        path.write_text(content, encoding="utf-8")

    return {
        "file": code,
        "status": "ok" if (sum_ok and pur_ok) else f"partial (sum={sum_ok}, pur={pur_ok})",
        "summary_changed": sum_ok,
        "purpose_changed": pur_ok,
        "summary_len": len(summary),
        "purpose_len": len(purpose),
    }


def main():
    if not TAXO_DIR.exists():
        print(f"ERROR: directory not found: {TAXO_DIR}", file=sys.stderr)
        sys.exit(1)

    md_files = sorted([p for p in TAXO_DIR.glob("*.md") if p.is_file()])
    print(f"Found {len(md_files)} taxonomies. Mapping has {len(MAPPING)} entries. Skip set: {SKIP}")

    stats = []
    for p in md_files:
        stat = process_file(p)
        stats.append(stat)

    # Récap
    ok = sum(1 for s in stats if s["status"] == "ok")
    skipped = sum(1 for s in stats if s["status"].startswith("skipped"))
    missing = sum(1 for s in stats if s["status"] == "MISSING_MAPPING")
    partial = sum(1 for s in stats if s["status"].startswith("partial"))
    too_long = sum(1 for s in stats if ">400" in s["status"])

    print(f"\n=== RECAP ===")
    print(f"OK: {ok} / {len(md_files)}")
    print(f"Skipped (cas test): {skipped}")
    print(f"Missing mapping: {missing}")
    print(f"Partial replacements: {partial}")
    print(f"Too long: {too_long}")

    if missing > 0:
        print("\nMISSING:")
        for s in stats:
            if s["status"] == "MISSING_MAPPING":
                print(f"  - {s['file']}")

    if partial > 0:
        print("\nPARTIAL:")
        for s in stats:
            if s["status"].startswith("partial"):
                print(f"  - {s['file']}: {s['status']}")

    if too_long > 0:
        print("\nTOO LONG:")
        for s in stats:
            if ">400" in s["status"]:
                print(f"  - {s['file']}: {s['status']}")


if __name__ == "__main__":
    main()
