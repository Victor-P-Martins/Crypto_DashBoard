from Airflow.dags.crypto_dashboard.classes.class_coin import Coin
from Airflow.dags.crypto_dashboard.classes.class_data_transformation import (
    Data_transformation,
)
from Airflow.dags.crypto_dashboard.utils.dict_coins import dict_coins

import pandas as pd


class Get_all_data_coins:
    def get_all_data() -> pd.DataFrame:
        num_complete = 1
        df_final = pd.DataFrame()
        for coin in dict_coins:
            print(coin, " Iniciando Extração")
            dinamyc_temp_coin = Coin(coin, dict_coins[coin])
            dinamyc_temp_data = dinamyc_temp_coin.get_all_history_info()
            df_temp = Data_transformation(coin, dict_coins[coin], dinamyc_temp_data)
            df_final = pd.concat([df_final, df_temp.transform_data()])
            print(coin, " Extração Finalizada")
        return df_final


if __name__ == "__main__":
    save_data = Get_all_data_coins.get_all_data()
