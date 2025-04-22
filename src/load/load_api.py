import os
import json
import csv
import boto3
import pandas as pd
from pathlib import Path


class LoadData:
    def __init__(self, data, bucket_name=None):
        self.data = data
        self.output_dir = Path(__file__).resolve().parent.parent.parent / 'data'
        self.bucket_name = bucket_name

    def upload_to_s3(self, file_path, bucket_name, s3_key):
        #SALVAR APENAS PARQUET
        s3_client = boto3.client('s3')
        try:
            # s3_client.upload_file(file_path, bucket_name, s3_key)
            print(f"Arquivo {file_path} enviado para o S3 em {bucket_name}/{s3_key}")
        except Exception as e:
            print(f"Erro ao enviar arquivo para o S3: {e}")

    def save_to_json(self, filename="weather_data.json"):
        json_path = self.output_dir / 'json' / filename
        try:
            with open(json_path, 'w', encoding='utf-8') as json_file:
                json.dump(self.data, json_file, ensure_ascii=False, indent=4)
            print(f"Dados salvos em JSON: {json_path}")
            self.upload_to_s3(json_path, self.bucket_name, filename)
        except Exception as e:
            print(f"Erro ao salvar em JSON: {e}")

    def save_to_csv(self, filename="weather_data.csv"):
        """Salva os dados em formato CSV."""
        csv_path = self.output_dir / 'csv' / filename
        try:
            if isinstance(self.data, list) and isinstance(self.data[0], dict):
                df = pd.DataFrame(self.data)
                df.to_csv(csv_path, index=False, encoding='utf-8')
                print(f"Dados salvos em CSV: {csv_path}")
                self.upload_to_s3(csv_path, self.bucket_name, filename)
        except Exception as e:
            print(f"Erro ao salvar em CSV: {e}")

    def save_to_parquet(self, filename="weather_data.parquet"):
        parquet_path = self.output_dir / 'parquet' / filename
        try:
            if isinstance(self.data, list) and isinstance(self.data[0], dict):
                df = pd.DataFrame(self.data)
                df.to_parquet(parquet_path, engine='pyarrow', index=False)
                print(f"Dados salvos em Parquet: {parquet_path}")
                self.upload_to_s3(parquet_path, self.bucket_name, filename)
        except Exception as e:
            print(f"Erro ao salvar em Parquet: {e}")

