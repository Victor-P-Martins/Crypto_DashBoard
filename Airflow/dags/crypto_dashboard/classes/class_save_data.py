from Airflow.dags.crypto_dashboard.classes.class_get_all_data_coin import (
    Get_all_data_coins,
)

import pandas as pd


class Save_data_coin:
    def __init__(self) -> None:
        self.data = Get_all_data_coins.get_all_data()

    def save_data_csv(self, path: str) -> None:
        df = self.data
        df.to_csv(path, index=False)

    def save_data_excel(self, path: str) -> None:
        df = self.data
        df.to_excel(path, index=False)

    def save_data_parquet(self, path: str) -> None:
        df = self.data
        df.to_parquet(path, index=False)


if __name__ == "__main__":
    save_data = Save_data_coin()
    save_data.save_data_csv(r"C:\Users\victo\Desktop\arquivo.csv")