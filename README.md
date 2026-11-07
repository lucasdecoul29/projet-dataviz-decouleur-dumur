# Projet DataViz – Divvy Bike Sharing

**Mastère Big Data & IA – M1**  
**Projet : De la donnée massive au tableau de bord décisionnel**

## 1. Présentation du jeu de données

### 1.1 Contexte

Pour ce projet, nous avons choisi d'étudier les données de déplacements du système de vélos en libre-service **Divvy**, situé à Chicago, aux États-Unis.

Divvy est un service de vélos partagés permettant aux habitants et aux visiteurs d'effectuer des déplacements dans la ville à partir de différentes stations.

Les données historiques sont mises à disposition publiquement par Divvy et sont téléchargeables sous forme de fichiers CSV mensuels.

**Sources des données :**
- [Divvy – System Data](https://divvybikes.com/system-data)
- [Divvy Trip Data – Archive des fichiers](https://divvy-tripdata.s3.amazonaws.com/index.html)

### 1.2 Description du jeu de données

Chaque enregistrement correspond à un trajet effectué par un utilisateur.

Les principales variables disponibles sont :

| Variable | Description |
|---|---|
| `ride_id` | Identifiant unique du trajet |
| `rideable_type` | Type de vélo utilisé |
| `started_at` | Date et heure de départ |
| `ended_at` | Date et heure d'arrivée |
| `start_station_name` | Nom de la station de départ |
| `end_station_name` | Nom de la station d'arrivée |
| `start_lat` / `start_lng` | Coordonnées géographiques du départ |
| `end_lat` / `end_lng` | Coordonnées géographiques de l'arrivée |
| `member_casual` | Catégorie de l'utilisateur : abonné ou occasionnel |

### 1.3 Dimensions d'analyse

Ce jeu de données présente plusieurs dimensions intéressantes :

- **Dimension temporelle :** analyse des déplacements par heure, jour, mois et saison.
- **Dimension géographique :** localisation des stations et répartition des déplacements dans la ville de Chicago.
- **Dimension comportementale :** comparaison des habitudes des abonnés et des utilisateurs occasionnels.

### 1.4 Volume des données

Nous prévoyons d'utiliser les données mensuelles couvrant les années 2024 et 2025, soit une période de 24 mois.

L'objectif est de constituer un jeu de données de plus de 2 millions de trajets, conformément aux exigences du projet.

Le volume exact sera vérifié après le téléchargement et la consolidation des fichiers mensuels.

## 2. Présentation du persona

### 2.1 Profil du décideur

Notre persona est un **responsable marketing et fidélisation de Divvy**, travaillant pour le service de vélos partagés de Chicago.

Son objectif principal est de développer le nombre d'abonnements annuels en comprenant les habitudes des utilisateurs occasionnels.

### 2.2 Responsabilités et décisions

Dans le cadre de ses fonctions, il doit notamment :

- Analyser les différences de comportement entre les abonnés et les utilisateurs occasionnels.
- Identifier les stations et les zones géographiques présentant une forte fréquentation d'utilisateurs occasionnels.
- Repérer les périodes de forte activité afin d'adapter les campagnes marketing.
- Proposer des actions commerciales pour encourager les utilisateurs occasionnels à souscrire un abonnement annuel.

### 2.3 Fréquence de consultation

Le responsable consulte les indicateurs chaque semaine afin de suivre l'évolution de l'activité.

Une analyse plus approfondie est réalisée chaque mois afin d'adapter les campagnes marketing et les actions de fidélisation.

### 2.4 Question principale du tableau de bord

**Dans quelles stations et à quelles périodes concentrer les campagnes de conversion des utilisateurs occasionnels ?**

Le futur tableau de bord devra permettre de comparer les différents profils d'utilisateurs, d'identifier les périodes et les zones géographiques les plus fréquentées et de fournir des indicateurs utiles à la prise de décision.

---

## 3. Sources

- [Divvy System Data](https://divvybikes.com/system-data)
- [Divvy Historical Trip Data](https://divvy-tripdata.s3.amazonaws.com/index.html)
- [Divvy – Informations sur le service](https://divvybikes.com/)

## Qualité et nettoyage des données (Silver)

La couche Silver transforme les données brutes Bronze en données typées
et exploitables.

Les principales règles appliquées sont :

- Suppression des identifiants de trajets dupliqués.
  Les 211 doublons détectés correspondaient à des trajets identiques
  après normalisation des horodatages à la seconde près.

- Suppression des trajets présentant une durée nulle ou négative,
  à l'exception de 72 trajets concernés par le changement d'heure
  (passage à l'heure d'hiver), conservés avec une durée NULL.

- Conservation des trajets dont les stations de départ ou d'arrivée
  sont manquantes, car ils restent exploitables pour les analyses
  temporelles et par type d'utilisateur.

- Conservation des coordonnées d'arrivée manquantes.

- Conversion des dates en timestamps et des coordonnées géographiques
  en valeurs numériques.

Au total, 891 lignes ont été supprimées :
211 doublons et 680 trajets présentant une durée invalide.
La couche Silver contient 11 412 671 trajets.