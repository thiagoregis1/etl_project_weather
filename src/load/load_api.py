import os
import json
import csv
import pandas as pd
from pathlib import Path


class LoadData:
    def __init__(self, data):
        self.data = data
        self.output_dir = Path(__file__).resolve().parent.parent.parent / 'data'


    def save_to_json(self, filename="weather_data.json"):
        json_path = self.output_dir / 'json' / filename
        try:
            with open(json_path, 'w', encoding='utf-8') as json_file:
                json.dump(self.data, json_file, ensure_ascii=False, indent=4)
            print(f"Dados salvos em JSON: {json_path}")
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
        except Exception as e:
            print(f"Erro ao salvar em CSV: {e}")

    def save_to_parquet(self, filename="weather_data.parquet"):
        parquet_path = self.output_dir / 'parquet' / filename
        try:
            if isinstance(self.data, list) and isinstance(self.data[0], dict):
                df = pd.DataFrame(self.data)
                df.to_parquet(parquet_path, engine='pyarrow', index=False)
                print(f"Dados salvos em Parquet: {parquet_path}")
        except Exception as e:
            print(f"Erro ao salvar em Parquet: {e}")
