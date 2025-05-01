import pandas as pd
import logging

# Fonction pour ingérer les données
def ingest_data(**kwargs):
    try:
        # Lire le fichier CSV
        df = pd.read_csv('/opt/airflow/dags/MOCK_DATA.csv')
        logging.info("Données ingérées avec succès.")
        logging.info(f"Voici un aperçu des données :\n{df.head()}")
        return df.to_dict(orient='records')
    except Exception as e:
        logging.error(f"Erreur lors de l'ingestion des données : {e}")
        raise