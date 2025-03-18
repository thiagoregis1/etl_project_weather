import json
from api.api_client import ApiClient
from extract.extract_api import ExtractAPI
from transform.transform_api import TransformData
from load.load_api import LoadData


class ETLPipeline:
    def __init__(self, list_of_cities):
        self.list_of_cities = list_of_cities

    def process_city(self, city):
        api_client = ApiClient(city=city)
        if not api_client.weather_data:
            print(f"Falha ao obter dados para {city}")
            return None

        extracted_data = ExtractAPI(api_client.weather_data).columns
        transformed_data = TransformData.transform_city_weather(extracted_data)
        print(f"Dados processados para {city}!")
        return transformed_data

    def run(self):
        date_to_save = []
        for city in self.list_of_cities:
            transformed_data = self.process_city(city)
            if transformed_data:
                date_to_save.append(transformed_data)

        LoadData(date_to_save).save_to_json()
        LoadData(date_to_save).save_to_csv()
        LoadData(date_to_save).save_to_parquet()

        return json.dumps(date_to_save, ensure_ascii=False, indent=4)
