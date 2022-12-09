from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
from datetime import timedelta, datetime
import requests
import boto3
from crypto.utils.dict_coins import dict_coins
from crypto.classes.class_get_all_current_data_coin import Get_current_data_coins
from crypto.classes.class_save_data import Save_data_coin
from datetime import datetime

bucket_name = "crypto-dash-bucket-app"


def verify_api():
    for coin_code in dict_coins:
        url_verify = f"https://www.mercadobitcoin.net/api/{coin_code}/ticker"
        if requests.get(url_verify).ok:
            print(coin_code + " OK")
        else:
            raise ConnectionError(f"Connection API Error! {coin_code}")


def get_current_data_coins_func() -> None:
    data = Get_current_data_coins.get_current_data()

    Save_data_coin(data).save_data_parquet_to_s3(
        bucket_name,
        f'{datetime.now().date().strftime(format="%d-%m-%Y")}-Crypto_Currency.parquet',
    )
    return None


default_args = {
    "owner": "Victor Pinheiro Martins",
    "email": ["victorpinheiromartins@hotmail.com"],
    "email_on_failure": True,
    "email_on_retry": False,
    "retry_delay": timedelta(seconds=300),
    "retries": 2,
    "start_date": datetime(2022, 12, 6),
    "schedule_interval": "@daily",
}

with DAG(
    "data_current_coin",
    description="Return the current data coins and save to parquet",
    default_args=default_args,
    catchup=False,
) as dag:

    verify_api_connection = PythonOperator(
        task_id="verify_api_conn", python_callable=verify_api
    )

    get_current_data_coins = PythonOperator(
        task_id="get_current_data_coins", python_callable=get_current_data_coins_func
    )

verify_api_connection >> get_current_data_coins
