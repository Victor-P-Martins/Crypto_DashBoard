from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator

from crypto.classes.class_save_data import Save_data_coin
from crypto.classes.class_get_all_data_history_coin import Get_all_data_coins

from datetime import timedelta, datetime


def save_data_coin_parquet(path: str = r"./") -> None:
    Save_data_coin_var = Save_data_coin(Get_all_data_coins.get_all_data())
    Save_data_coin_var.save_data_parquet(path)
    return None


default_args = {
    "owner": "Victor Pinheiro Martins",
    "email": ["victorpinheiromartins@hotmail.com"],
    "email_on_failure": True,
    "email_on_retry": False,
    "retry_delay": timedelta(seconds=300),
    "retries": 2,
    "start_date": datetime.now(),
}

with DAG(
    "data_history_coin",
    description="Return all historical data from all coins with d-1 and save to parquet",
    default_args=default_args,
) as dag:

    save_parquet_data = PythonOperator(
        task_id="save_parquet_data", python_callable=save_data_coin_parquet
    )
