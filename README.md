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

**Comment identifier les comportements et les habitudes de déplacement des utilisateurs occasionnels afin de mieux cibler les campagnes marketing et d'encourager la souscription d'abonnements annuels ?**

Le futur tableau de bord devra permettre de comparer les différents profils d'utilisateurs, d'identifier les périodes et les zones géographiques les plus fréquentées et de fournir des indicateurs utiles à la prise de décision.

---

## 3. Sources

- [Divvy System Data](https://divvybikes.com/system-data)
- [Divvy Historical Trip Data](https://divvy-tripdata.s3.amazonaws.com/index.html)
- [Divvy – Informations sur le service](https://divvybikes.com/)