from cassandra.cluster import Cluster
import pandas as pd
import matplotlib.pyplot as plt

def analyze_data():
    # Connexion à Cassandra
    cluster = Cluster(['cassandra_db'])  # Remplacez par votre adresse
    session = cluster.connect('airflow')  # Nom du keyspace

    # Récupération des données
    query = "SELECT * FROM iot_data"
    rows = session.execute(query)

    # Conversion des données en DataFrame
    df = pd.DataFrame(rows)

    # Analyse des données : exemple - moyenne du niveau de batterie
    avg_battery_level = df['battery_level'].mean()
    print(f"Average Battery Level: {avg_battery_level}")

    # Visualisation : exemple - histogramme des niveaux de batterie
    plt.hist(df['battery_level'], bins=10, alpha=0.7)
    plt.title('Distribution of Battery Levels')
    plt.xlabel('Battery Level')
    plt.ylabel('Frequency')
    plt.show()

    # Fermeture de la session
    session.shutdown()
    cluster.shutdown()

# Appel de la fonction d'analyse
analyze_data()