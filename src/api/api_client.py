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
        self.headers = {
            "Content-Type": "application/json",  
            "Authorization": f"Bearer {self.api_key}"  
        }
        self.weather_data = self.get_response()

    def get_response(self):
        try:
            response = requests.get(self.base_url, params=self.params, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição GET: {e}")
            return None

    def post(self, data):
        try:
            response = requests.post(self.base_url, params=self.params, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição POST: {e}")
            return None