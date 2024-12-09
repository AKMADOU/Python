##  BI Tools

  ![Data_warehouse_architecture](https://github.com/sanogotech/kidprogrammingstarter/blob/main/images/Data_warehouse_architecture.jpg)

## Architecture Three Tier
![ Architecture Three Tier 1 ](https://github.com/sanogotech/kidprogrammingstarter/blob/main/images/three-tier-data-warehouse-architecturefull.png)

##  Composants BI

![ Architecture Three Tier 2 ](https://github.com/sanogotech/kidprogrammingstarter/blob/main/images/three-tier-data-warehouse-architecture.png)

## ETL
![ETL ](https://github.com/sanogotech/kidprogrammingstarter/blob/main/images/ETLBI.jpg)

## Principles of Data Warehousing

![Principles of Data Warehousing](https://github.com/sanogotech/kidprogrammingstarter/blob/main/images/data-warehouseprinciples.png )
## Qu’est ce que les métadonnées ?

“Les métadonnées sont de l’information structurée qui décrit, explique, localise ou facilite autrement l’obtention, l’utilisation ou la gestion d’une ressource d’information. Les métadonnées sont souvent appelées données des données ou information sur l’information.” — National Information Standards Organization.
Les métadonnées fournissent des informations permettant de comprendre des données (documents, images, bases de données), des concepts (par exemple, les systèmes de classification) et des entités du monde réel (par exemple, les personnes, les organisations, les lieux, peintures, produits).

Types de métadonnées :
Il existe trois type de métadonnées :

Métadonnées descriptives, décrivent une ressource à des fins de découverte et d’identification.
Métadonnées structurelles, par ex. des modèles de données et des données de référence.
Métadonnées administratives, renseignent afin d’aider à la gestion d’une ressource.
Exemple de métadonnées :
L’image suivante (source : Open Data Support) fournit quelques exemples de métadonnées :


Figure : Exemple de métadonnées (source : Open Data Support)
Métadonnées dans le domaine de la BI :
Dans le cas du domaine de la Business Intelligence, les différentes phases de mise en place d’un projet BI, de la planification à la maintenance, générent un grand volume de métadonnées. Un rapport, par exemple, présente un certain nombre d’indicateurs dans un format bien spécifique (Liste, graphique…), mais ne donne aucune information sur la formule de calcul de chaque indicateur, sa source de donnée, les aggrégations qu’il a subit… toutes ces informations représentent les métadonnées associées à ce rapport.

Exemple de métadonnées BI :
Nous allons donner quelques exemples de métadonnées pour chacune des composantes clés d’une solution BI :

Rapport : Date de dernière exécution, fréquence d’éxécution, formule de calcul des indicateurs calculés dans le rapport, définition de chaque colonne/axe.. du rapport
Cube : Date dernier raffraichissement des données, date de publication, méthode d’aggrégation des indicateurs (somme, moyenne…)
Traitement ETL : Date dernière exécution, nombre d’enregistrements mis à jour par table par traitement, nombre d’enregistrements ajoutés…
Les métadonnées ne sont pas seulement utiles pour les utilisateurs finaux, mais aussi pour l’équipe IT et surtout l’équipe support BI.

## Fact/Dimension Constellation in Data Warehouse modelling


![Facts Constellation](https://github.com/sanogotech/kidprogrammingstarter/blob/main/images/factGalaxy-Schema.jpg)

La table de faits et la table de dimensions sont utilisées pour créer des schémas. L’enregistrement d’une table de faits est une combinaison d’attributs de différentes tables de dimension. La table des faits aide l’utilisateur à analyser les dimensions de l’entreprise, ce qui aide à prendre des décisions pour améliorer son activité. D’ailleurs, les tables de dimensions aident à rassembler les dimensions avec lesquels les mesures doivent être prises.
 
 
La différence clé entre la table de faits et la table de dimension est que la table de dimension contient des attributs avec lesquels les mesures sont prises dans la table de faits.

![Exemple Faits / Dimensions](https://github.com/sanogotech/kidprogrammingstarter/blob/main/images/TabledesfaitsetDimensions.png)

![Comparaision table faits et dimensions ](https://github.com/sanogotech/kidprogrammingstarter/blob/main/images/comparaisontablefaitsdimensions.png)
