import pandas as pd
import boto3
from io import StringIO,BytesIO


class Save_data_coin:
    def __init__(self, data: pd.DataFrame) -> None:
        self.data = data

    def save_data_csv(self, path: str) -> None:
        df = self.data
        path = path + f""
        df.to_csv(path, index=False)

    def save_data_excel(self, path: str) -> None:
        df = self.data
        df.to_excel(path, index=False)

    def save_data_parquet(self, path: str) -> None:
        df = self.data
        df.to_parquet(path, index=False)

    def save_data_csv_to_s3(self, bucket_name: str, name_file: str):
        df = self.data
        bucket = bucket_name
        csv_buffer = StringIO()
        df.to_csv(csv_buffer,index = False)
        s3_resource = boto3.resource("s3")
        s3_resource.Object(bucket, name_file).put(Body=csv_buffer.getvalue())

    def save_data_parquet_to_s3(self, bucket_name: str, name_file: str):
        df = self.data
        bucket = bucket_name
        parquet_buffer = BytesIO()
        df.to_csv(parquet_buffer)
        s3_resource = boto3.resource("s3")
        s3_resource.Object(bucket, name_file).put(Body=parquet_buffer.getvalue())

