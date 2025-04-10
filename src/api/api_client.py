import requests

class ApiClient:
    def __init__(self, base_url, params, headers):
        self.base_url = base_url
        self.params = params
        self.headers = headers
        self.result = self.get_response()

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