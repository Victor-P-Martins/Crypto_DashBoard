import pandas as pd
from pandas import DataFrame
from datetime import datetime
from classes.class_coin import Coin


class Data_transformation:
    def __init__(self, coin_name: str, coin_code: str, data: list) -> None:
        self.coin_name = coin_name
        self.coin_code = coin_code
        self.data = data
        self.__dict_rename = dict_rename = {
            "date": "dt_date",
            "opening": "value_opening",
            "closing": "value_closing",
            "lowest": "value_lowest",
            "highest": "value_highest",
            "volume": "value_volume",
            "quantity": "value_quantity",
            "amount": "value_amount",
            "avg_price": "value_avg_price",
        }

    def transform_data(self) -> DataFrame:

        df = pd.DataFrame.from_records(self.data)
        df = df.rename(columns=self.__dict_rename)

        df["coin_name"] = self.coin_name
        df["coin_code"] = self.coin_code
        df["time_stamp"] = datetime.now()

        df = df[
            [
                "dt_date",
                "value_opening",
                "value_closing",
                "value_lowest",
                "value_highest",
                "value_volume",
                "value_quantity",
                "value_amount",
                "value_avg_price",
                "coin_name",
                "coin_code",
                "time_stamp",
            ]
        ]

        return df
