import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("api_key")
base_url = os.getenv("base_url")

class ApiClient:
    def __init__(self, city, api_key=api_key, base_url=base_url):
        self.api_key = api_key
        self.base_url = base_url
        self.city = city
        self.params = {
            "q": self.city,
            "appid": self.api_key,
            "lang": "pt",
            "units": "metric"
        }
        self.weather_data = self.get_weather()

    def get_weather(self):
        try:
            response = requests.get(self.base_url, params=self.params)
            # print(f"Requisição para {self.city} concluída com sucesso!")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição para {self.city}: {e}")
            return None