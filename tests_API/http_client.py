"""http_client.py"""
import os
import requests


GORES_TOKEN = os.getenv('GORES_TOKEN')


class HttpClient:
    """Класс для API запросов"""
    def __init__(self, base_url):
        self.base_url = base_url

    def request(self, method, path: str, body: dict = None,
                code: int = 200):
        """Отправляет общий запрос"""

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        response = requests.request(
            method,
            f'{self.base_url}/{path}',
            data=body,
            headers=headers,
            timeout=5
        )

        response_json = response.json()

        assert response.status_code == code
        return response_json

    def get(self, path: str, code: int = 200):
        """Выполняет GET запрос"""
        return self.request('GET', path=path, code=code)

    def post(self, path: str, body: dict = None, code: int = 200):
        """Выполняет POST запрос"""
        return self.request(
            'POST', path=path, body=body, code=code
        )

    def put(self, path: str, body: dict = None, code: int = 200):
        """Выполняет PUT запрос"""
        return self.request(
            'PUT', path=path, body=body, code=code
        )

    def delete(self, path: str, body: dict = None, code: int = 200):
        """Выполняет DELETE запрос"""
        return self.request(
            'DELETE', path=path, body=body, code=code
        )
