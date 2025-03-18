import json
from datetime import datetime
from extract.extract_api import ExtractAPI


class TransformData:
    @staticmethod
    def unix_to_datetime(timestamp):
        if timestamp:
            return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
        return None

    @staticmethod
    def filter_columns(data, columns_selected):
        return {key: str(data[key]) for key in columns_selected if key in data and data[key] is not None}

    @staticmethod
    def rename_columns(data, rename_map):
        return {rename_map.get(key, key): value for key, value in data.items()}

    @staticmethod
    def transform_city_weather(city_weather_data):
        if not city_weather_data:
            return None

        # Convertendo timestamps
        city_weather_data["dt"] = TransformData.unix_to_datetime(city_weather_data.get("dt")).split(" ")[0]
        city_weather_data["sunrise"] = TransformData.unix_to_datetime(city_weather_data.get("sunrise")).split(" ")[1]
        city_weather_data["sunset"] = TransformData.unix_to_datetime(city_weather_data.get("sunset")).split(" ")[1]

        # Definindo as colunas necessárias
        columns_selected = [
            "name", "temp", "feels_like", "humidity", "weather_main",
            "weather_description", "sunrise", "sunset", "dt",
            "lon", "lat", "pressure", "wind_speed", "wind_deg", "clouds_all"
        ]

        filtered_data = TransformData.filter_columns(city_weather_data, columns_selected)

        # Renomeando as colunas para português
        rename_map = {
            "name": "cidade",
            "temp": "temperatura",
            "feels_like": "sensacao_termica",
            "humidity": "umidade",
            "weather_main": "condicao_clima",
            "weather_description": "descricao_clima",
            "sunrise": "nascer_do_sol",
            "sunset": "por_do_sol",
            "dt": "data_atualizacao",
            "lon": "longitude",
            "lat": "latitude",
            "pressure": "pressao_atmosferica",
            "wind_speed": "velocidade_vento",
            "wind_deg": "direcao_vento",
            "clouds_all": "cobertura_nuvens"
        }

        # Renomeando as colunas para português
        renamed_data = TransformData.rename_columns(filtered_data, rename_map)

        return renamed_data
