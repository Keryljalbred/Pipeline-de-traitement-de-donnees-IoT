from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
from cassandra.policies import DCAwareRoundRobinPolicy
import logging
import sys
import time

# Configuration de logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

def store_data_in_cassandra(**kwargs):
    logging.info("Début de l'exécution du script.")
    ti = kwargs['ti']

    try:
        data = ti.xcom_pull(task_ids='process_data')
        logging.info(f"Données récupérées : {data}")
    except Exception as e:
        logging.error(f"Erreur lors de la récupération des données : {e}")
        return

    if not data:
        logging.warning("Aucune donnée à stocker.")
        return

    # Ajout d'un device_id si nécessaire
    for i, record in enumerate(data):
        record['device_id'] = f'device_{i}'  # Ajout d'un identifiant unique

    cluster = None
    session = None

    try:
        cluster = Cluster(['cassandra_db'], load_balancing_policy=DCAwareRoundRobinPolicy(local_dc='datacenter1'))
        for attempt in range(5):
            try:
                session = cluster.connect()
                logging.info("Connexion à Cassandra réussie.")
                break
            except Exception as e:
                logging.warning(f"Échec de la connexion, tentative {attempt + 1} : {e}")
                time.sleep(2)

        session.execute("""
            CREATE KEYSPACE IF NOT EXISTS airflow 
            WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 1}
        """)
        logging.info("Keyspace 'airflow' vérifié ou créé.")
        session.set_keyspace('airflow')

        # Création de la table si elle n'existe pas
        session.execute("""
            CREATE TABLE IF NOT EXISTS iot_data (
                device_id TEXT,
                timestamp TIMESTAMP,
                battery_level INT,
                status TEXT,
                PRIMARY KEY (device_id, timestamp)
            )
        """)
        logging.info("Table 'iot_data' vérifiée ou créée.")

        for record in data:
            logging.info(f"Tentative d'insertion des données : {record}")
            try:
                query = SimpleStatement("""
                    INSERT INTO iot_data (device_id, timestamp, battery_level, status)
                    VALUES (%s, %s, %s, %s)
                """)
                session.execute(query, (
                    record['device_id'],
                    record['timestamp'],
                    record['battery_level'],
                    record['status']
                ))
                logging.info(f"Données insérées : {record}")
            except Exception as e:
                logging.error(f"Erreur lors de l'insertion des données : {record} - Erreur : {e}")

        logging.info("Données stockées dans Cassandra avec succès.")
    except Exception as e:
        logging.error(f"Erreur lors du stockage des données : {e}")
    finally:
        if session:
            session.shutdown()
            logging.info("Session Cassandra fermée.")
        if cluster:
            cluster.shutdown()
            logging.info("Cluster Cassandra fermé.")