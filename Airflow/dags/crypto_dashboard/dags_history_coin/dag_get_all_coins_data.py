from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
from crypto_dashboard.classes.class_save_data import Save_data_coin

from datetime import timedelta

Save_data_coin_historical = Save_data_coin()

default_args = {
    "owner": "Victor Pinheiro",
    "email": ["victorpinheiromartins@hotmail.com"],
    "email_on_failure": True,
    "email_on_retry": False,
    "retry_delay": timedelta(seconds=300),
    "retries": 2,
}

with DAG(
    "data_history_coin",
    description="Return all historical data from all coins with d-1 and save to parquet",
    default_args=default_args,
) as dag:

    save_parquet_data = PythonOperator(
        task_id="save_parquet_data", python_callable=Save_data_coin_historical(r"/.")
    )
