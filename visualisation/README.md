# Documentation des KPI — Tableau de bord Divvy

## KPI 1 — Part des trajets occasionnels

**Définition :**

Proportion des trajets réalisés par les utilisateurs occasionnels (`casual`) par rapport à l'ensemble des trajets effectués sur la période étudiée.

**Calcul :**

\[
\text{Part casual} =
\frac{\text{Nombre de trajets casual}}{\text{Nombre total de trajets}} \times 100
\]

**Résultat :** 36,4 %

**Source :** `gold_monthly_overview` (PostgreSQL).

**Intérêt pour le persona :**

Cet indicateur permet de mesurer le poids des utilisateurs occasionnels dans l'activité globale de Divvy. Il donne une première estimation du potentiel de conversion vers des abonnements et aide à déterminer l'importance à accorder aux campagnes marketing ciblant cette catégorie d'utilisateurs.

---

## KPI 2 — Nombre total de trajets occasionnels

**Définition :**

Nombre total de trajets effectués par les utilisateurs occasionnels (`casual`) sur l'ensemble de la période étudiée.

**Calcul :**

Somme de la colonne `total_trips` pour les lignes correspondant aux utilisateurs `casual`.

**Résultat :** 4 150 785 trajets.

**Source :** `gold_monthly_overview` (PostgreSQL).

**Intérêt pour le persona :**

Cet indicateur permet de mesurer le volume d'activité généré par les utilisateurs occasionnels. Il aide le persona à évaluer l'ampleur du public susceptible d'être ciblé par les campagnes de conversion et à dimensionner les actions marketing en fonction du volume d'utilisation observé.

---

## KPI 3 — Durée moyenne des trajets occasionnels

**Définition :**

Durée moyenne des trajets effectués par les utilisateurs occasionnels (`casual`), exprimée en minutes.

**Calcul :**

Moyenne pondérée des durées moyennes mensuelles par le nombre de trajets :

\[
\text{Durée moyenne} =
\frac{\sum(\text{Durée moyenne} \times \text{Nombre de trajets})}
{\sum(\text{Nombre de trajets})}
\]

**Résultat :** 23,9 minutes.

**Source :** `gold_monthly_overview` (PostgreSQL).

**Intérêt pour le persona :**

Cet indicateur permet de mieux comprendre les habitudes d'utilisation des utilisateurs occasionnels. Il peut aider le persona à adapter les messages des campagnes marketing en fonction de la durée moyenne de leurs déplacements et à identifier des offres susceptibles de correspondre à leurs usages.

---

## KPI 4 — Répartition des trajets occasionnels par type de véhicule

**Définition :**

Répartition des trajets effectués par les utilisateurs occasionnels (`casual`) selon le type de véhicule utilisé : vélo classique, vélo électrique ou trottinette électrique.

**Calcul :**

Pour chaque type de véhicule :

\[
\text{Part du véhicule} =
\frac{\text{Nombre de trajets casual avec ce véhicule}}
{\text{Nombre total de trajets casual}} \times 100
\]

**Résultats :**

- Vélo classique : 39,7 % (1 647 524 trajets).
- Vélo électrique : 58,3 % (2 418 046 trajets).
- Trottinette électrique : 2,1 % (85 215 trajets).

**Source :** `gold_monthly_overview` (PostgreSQL).

**Intérêt pour le persona :**

Cet indicateur permet d'identifier les types de véhicules privilégiés par les utilisateurs occasionnels. Le persona peut ainsi adapter ses campagnes de conversion aux habitudes observées, notamment en mettant en avant les avantages des vélos électriques, qui représentent la majorité des trajets occasionnels.