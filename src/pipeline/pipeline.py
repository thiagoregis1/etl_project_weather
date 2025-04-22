import os
import json
from api.api_client import ApiClient
from extract.extract_api import ExtractAPI
from transform.transform_api import TransformData
from load.load_api import LoadData
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("api_key")
base_url = os.getenv("base_url")
bucket_name = os.getenv("bucket_name")


class ETLPipeline:
    def __init__(self, list_of_cities):
        self.list_of_cities = list_of_cities
        self.api_key = api_key
        self.base_url = base_url

    def process_city(self, city, params):
        headers = {
            "Content-Type": "application/json",  
            "Authorization": f"Bearer {self.api_key}"  
        }
        api_client = ApiClient(base_url=base_url, params=params, headers=headers)
        if not api_client.result:
            print(f"Falha ao obter dados para {city}")
            return None

        extracted_data = ExtractAPI(api_client.result).columns
        transformed_data = TransformData.transform_city_weather(extracted_data)
        print(f"Dados processados para {city}!")
        return transformed_data

    def run(self):
        date_to_save = []
        for city in self.list_of_cities:
            self.params = {
                "q": city,
                "appid": self.api_key,
                "lang": "pt",
                "units": "metric"
            }
            transformed_data = self.process_city(city, self.params)
            if transformed_data:
                date_to_save.append(transformed_data)

        LoadData(date_to_save).save_to_json()
        LoadData(date_to_save).save_to_csv()
        LoadData(date_to_save).save_to_parquet()     

        return json.dumps(date_to_save, ensure_ascii=False, indent=4)
