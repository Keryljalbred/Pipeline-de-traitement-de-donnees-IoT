import pandas as pd
import logging

# Fonction pour nettoyer et transformer les données
def process_data(**kwargs):
    ti = kwargs['ti']
    data = ti.xcom_pull(task_ids='ingest_data')

    if not data:
        logging.warning("Aucune donnée à traiter.")
        return

    df = pd.DataFrame(data)

    # Nettoyage des données
    df = df.drop(columns=['id'], errors='ignore')
    df.fillna({'battery_level': 0, 'status': 'unknown'}, inplace=True)
    df = df[df['status'] == 'active']

    logging.info(f"Données nettoyées :\n{df.head()}")
    return df.to_dict(orient='records')