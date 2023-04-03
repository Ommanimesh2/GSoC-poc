# api.py

import requests

class ApiBase:
    def __init__(self, base_url):
        self.base_url = base_url
        print("this is called")

    def get(self, endpoint, params=None):
        url = self.base_url + endpoint
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def post(self, endpoint, data):
        url = self.base_url + endpoint
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()
