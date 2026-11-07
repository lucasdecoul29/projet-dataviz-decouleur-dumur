
from pathlib import Path
from urllib.request import urlopen
from zipfile import ZipFile
import shutil

# Dossier principal du projet
PROJECT_DIR = Path(__file__).resolve().parents[1]

# Dossier dans lequel seront enregistrés les CSV
RAW_DIR = PROJECT_DIR / "data" / "raw"

# Adresse de l'archive Divvy
BASE_URL = "https://divvy-tripdata.s3.amazonaws.com"

# Période à télécharger : janvier 2024 à décembre 2025
START_YEAR = 2024
END_YEAR = 2025


def download_month(year, month):
    """Télécharge et extrait le fichier CSV d'un mois."""

    filename = f"{year}{month:02d}-divvy-tripdata"
    csv_path = RAW_DIR / f"{filename}.csv"
    zip_path = RAW_DIR / f"{filename}.zip"

    # Ne pas télécharger un fichier déjà présent
    if csv_path.exists():
        print(f"[DEJA PRESENT] {filename}.csv")
        return

    url = f"{BASE_URL}/{filename}.zip"

    print(f"[TELECHARGEMENT] {filename}.zip")

    try:
        # Télécharger le fichier ZIP
        with urlopen(url) as response:
            with open(zip_path, "wb") as file:
                shutil.copyfileobj(response, file)

        # Extraire le fichier CSV du ZIP
        with ZipFile(zip_path, "r") as archive:
            csv_files = [
                name for name in archive.namelist()
                if name.lower().endswith(".csv")
                and not name.startswith("__MACOSX/")
            ]

            if not csv_files:
                raise ValueError("Aucun fichier CSV trouvé dans l'archive.")

            with archive.open(csv_files[0]) as source:
                with open(csv_path, "wb") as destination:
                    shutil.copyfileobj(source, destination)

        # Supprimer le ZIP après extraction
        zip_path.unlink()

        print(f"[OK] {filename}.csv")

    except Exception as error:
        print(f"[ERREUR] {filename} : {error}")


def main():
    # Créer le dossier de destination s'il n'existe pas
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    total_files = 0

    for year in range(START_YEAR, END_YEAR + 1):
        for month in range(1, 13):
            download_month(year, month)
            total_files += 1

    print("\nTéléchargement terminé.")
    print(f"Nombre de fichiers mensuels traités : {total_files}")
    print(f"Dossier de destination : {RAW_DIR}")


if __name__ == "__main__":
    main()
