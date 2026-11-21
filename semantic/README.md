# Couche sémantique — Divvy Bike Sharing

## 1. Objectif

La couche sémantique complète les traitements analytiques réalisés dans les couches Bronze, Silver et Gold. Elle permet de représenter les principales notions du domaine Divvy Bike Sharing sous forme d'une ontologie, puis de les interroger à l'aide du langage SPARQL.

L'objectif est de faciliter l'exploitation des données et de répondre à la problématique du projet :

**Dans quelles stations et à quelles périodes concentrer les campagnes de conversion des utilisateurs occasionnels ?**

## 2. Ontologie

L'ontologie est définie dans le fichier `ontologie-divvy.ttl`, au format Turtle.

Elle décrit six classes principales :

- `Station` : station de départ d'un trajet.
- `Periode` : période temporelle caractérisée par une année, un mois, un jour de la semaine et une heure.
- `TypeVehicule` : type de véhicule utilisé.
- `CategorieUtilisateur` : catégorie d'utilisateur, occasionnel ou abonné.
- `ObservationTrajets` : agrégation de trajets associée à une station, une période ou un type de véhicule.
- `RepartitionCategorie` : répartition des trajets entre les catégories d'utilisateurs.

Des propriétés définissent les relations entre ces concepts ainsi que leurs caractéristiques.

Les catégories d'utilisateurs et les types de véhicules sont représentés par des individus contrôlés afin d'assurer une représentation cohérente des données.

## 3. Construction du graphe RDF

Le graphe RDF est construit à partir des tables Gold stockées dans le Data Lake.

Trois ensembles d'informations sont intégrés :

- Les statistiques par station, issues de `gold_station_ranking`.
- Les statistiques par jour de la semaine et heure, calculées à partir de `gold_station_period`.
- La répartition par type de véhicule et catégorie d'utilisateur, calculée à partir de `gold_monthly_overview`.

Les identifiants et les noms des stations sont utilisés conjointement pour construire les ressources RDF. Ce choix permet de conserver distinctes les stations qui possèdent un même nom mais des identifiants différents.

Le graphe généré est enregistré dans `graphe-divvy.ttl`.

## 4. Requêtes SPARQL

Trois requêtes ont été développées pour répondre aux besoins de la persona.

### Requête 1 — Stations générant le plus de trajets occasionnels

Fichier : `requetes/01_stations_occasionnels.rq`

Cette requête classe les dix stations ayant le plus grand volume de trajets occasionnels. Elle affiche également le nombre total de trajets et la part des trajets occasionnels.

Elle permet d'identifier les stations présentant le plus fort potentiel d'exposition aux campagnes de communication.

### Requête 2 — Périodes concentrant les trajets occasionnels

Fichier : `requetes/02_periodes_prioritaires.rq`

Cette requête identifie les dix combinaisons jour de la semaine et heure présentant le plus grand volume de trajets occasionnels.

Elle permet de repérer les périodes durant lesquelles les utilisateurs occasionnels sont les plus présents.

### Requête 3 — Répartition selon le type de véhicule

Fichier : `requetes/03_repartition_vehicules.rq`

Cette requête compare le nombre de trajets occasionnels et abonnés selon le type de véhicule utilisé.

Elle permet d'étudier les différences d'utilisation entre vélos classiques, vélos électriques et scooters électriques.

## 5. Principaux résultats

Les résultats obtenus mettent en évidence plusieurs tendances :

- La station Streeter Dr & Grand Ave arrive en première position en volume de trajets occasionnels, avec 59 513 trajets sur la période étudiée.
- Le samedi entre 10 h et 15 h concentre une forte activité des utilisateurs occasionnels. Le pic observé est atteint le samedi à 14 h, avec 58 566 trajets.
- Les vélos électriques représentent le type de véhicule ayant le plus grand volume de trajets, aussi bien chez les utilisateurs occasionnels que chez les abonnés.

Ces résultats peuvent orienter le ciblage géographique et temporel des campagnes marketing.

## 6. Limites et précautions d'interprétation

La part des trajets occasionnels correspond à la proportion de trajets réalisés par cette catégorie d'utilisateurs. Elle ne représente pas un taux de conversion en abonnement.

Les données disponibles ne permettent pas de savoir si un utilisateur occasionnel a souscrit un abonnement à la suite d'une campagne.

Les résultats décrivent donc des comportements d'utilisation et des zones de concentration, mais ne démontrent pas directement l'efficacité d'une campagne marketing.

Enfin, les analyses temporelles et par station portent sur les années 2024 et 2025.