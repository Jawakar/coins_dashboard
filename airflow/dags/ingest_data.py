from datetime import datetime, timedelta
import json
import time
import requests
from google.cloud import storage

from airflow import DAG
from airflow.models import Variable
from airflow.operators.python_operator import PythonOperator
# from airflow.providers.google.cloud.operators.gcs import GCSUploadOperator
# from airflow.providers.google.cloud.hooks.gcs import GoogleCloudStorageHook


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 3, 31),
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

def get_data():
    url = "https://api.coincap.io/v2/assets?limit=2000"
    response = requests.get(url)
    data = response.json()
    return data

def upload_to_gcs(response_data):
    timestamp = response_data["timestamp"]
    dt_object = datetime.fromtimestamp(timestamp/1000)
    created_date = dt_object
    storage_client = storage.Client("jawa-378700")
    bucket_name = "coin_data_raw"
    bucket = storage_client.get_bucket(bucket_name)
    destination_blob_name = f'{created_date}.json'
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_string(json.dumps(response_data))

def ingest_data():
    response_data = get_data()
    upload_to_gcs(response_data)

dag = DAG(
    'ingest_data',
    default_args=default_args,
    description='Ingest data to GCP bucket',
    schedule_interval=timedelta(minutes=1),
)

ingest_task = PythonOperator(
    task_id='ingest_data_task',
    python_callable=ingest_data,
    dag=dag,
)

ingest_task