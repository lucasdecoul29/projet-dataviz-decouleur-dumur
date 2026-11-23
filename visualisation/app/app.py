
import os

import pandas as pd
import sqlalchemy
import streamlit as st


# --------------------------------------------------
# 1. Configuration de la page
# --------------------------------------------------

st.set_page_config(
    page_title="Divvy - Analyse des trajets",
    page_icon="🚲",
    layout="wide"
)


# --------------------------------------------------
# 2. Connexion à PostgreSQL
# --------------------------------------------------

PG = (
    f"postgresql+psycopg2://"
    f"{os.getenv('PG_USER', 'divvy')}:"
    f"{os.getenv('PG_PASSWORD', 'divvy')}"
    f"@{os.getenv('PG_HOST', 'postgres')}:5432/"
    f"{os.getenv('PG_DB', 'divvy')}"
)


# --------------------------------------------------
# 3. Chargement des données Gold
# --------------------------------------------------

@st.cache_data(ttl=600)
def charger_donnees():
    moteur = sqlalchemy.create_engine(PG)

    station_period = pd.read_sql(
        "SELECT * FROM gold_station_period",
        moteur
    )

    monthly_overview = pd.read_sql(
        "SELECT * FROM gold_monthly_overview",
        moteur
    )

    station_ranking = pd.read_sql(
        "SELECT * FROM gold_station_ranking",
        moteur
    )

    moteur.dispose()

    return station_period, monthly_overview, station_ranking


# --------------------------------------------------
# 4. Calcul et affichage des KPI
# --------------------------------------------------

def afficher_kpi(monthly_overview):

    # Données des utilisateurs occasionnels
    casual_data = monthly_overview[
        monthly_overview["member_casual"] == "casual"
    ]

    # KPI 1 : Part des trajets occasionnels
    total_trajets = monthly_overview["total_trips"].sum()
    trajets_casual = casual_data["total_trips"].sum()

    part_casual = trajets_casual / total_trajets * 100

    # KPI 2 : Nombre de trajets occasionnels
    # KPI 3 : Durée moyenne des trajets occasionnels
    duree_moyenne_casual = (
        (casual_data["avg_duration_minutes"] * casual_data["total_trips"]).sum()
        / trajets_casual
    )

    # Affichage des trois premiers KPI
    col1, col2, col3 = st.columns(3)

    col1.metric(
        label="Part des trajets occasionnels",
        value=f"{part_casual:.1f}%"
    )

    col2.metric(
        label="Nombre de trajets occasionnels",
        value=f"{int(trajets_casual):,}".replace(",", " ")
    )

    col3.metric(
        label="Durée moyenne des trajets occasionnels",
        value=f"{duree_moyenne_casual:.1f} min"
    )

    # KPI 4 : Répartition des trajets occasionnels par véhicule
    repartition_vehicules = (
        casual_data.groupby("rideable_type")["total_trips"].sum()
    )

    part_vehicules = repartition_vehicules / trajets_casual * 100

    st.subheader("Répartition des trajets occasionnels par véhicule")

    for vehicule, pourcentage in part_vehicules.items():
        st.write(f"{vehicule} : {pourcentage:.1f} %")


# --------------------------------------------------
# 5. Interface du tableau de bord
# --------------------------------------------------

st.title("Analyse des trajets Divvy")

st.write(
    "Tableau de bord consacré à l'analyse des utilisateurs "
    "occasionnels et abonnés du service Divvy."
)


# --------------------------------------------------
# 6. Exécution de l'application
# --------------------------------------------------

try:
    station_period, monthly_overview, station_ranking = charger_donnees()

    st.success("Connexion à PostgreSQL réussie.")

    afficher_kpi(monthly_overview)

    # Informations provisoires sur les données chargées
    st.subheader("Données disponibles")

    st.write(f"Gold station period : {len(station_period):,} lignes")
    st.write(f"Gold monthly overview : {len(monthly_overview):,} lignes")
    st.write(f"Gold station ranking : {len(station_ranking):,} lignes")

except Exception as e:
    st.error(f"Erreur lors du chargement des données : {e}")
