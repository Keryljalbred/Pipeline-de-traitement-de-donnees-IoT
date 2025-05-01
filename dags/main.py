from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from ingest import ingest_data
from process import process_data
from storage import store_data_in_cassandra

# Arguments par défaut pour le DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

# Définition du DAG
dag = DAG(
    'ingest_iot_data',
    default_args=default_args,
    description='Un DAG pour ingérer et traiter des données IoT',
    schedule_interval='@daily',
)

# Tâches
ingest_task = PythonOperator(
    task_id='ingest_data',
    python_callable=ingest_data,
    provide_context=True,
    dag=dag,
)

process_task = PythonOperator(
    task_id='process_data',
    python_callable=process_data,
    provide_context=True,
    dag=dag,
)

store_task = PythonOperator(
    task_id='store_data',
    python_callable=store_data_in_cassandra,
    provide_context=True,
    dag=dag,
)

# Dépendances
ingest_task >> process_task >> store_task