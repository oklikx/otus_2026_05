"""test_module.py"""
import requests


def test_check_url_status(url: str, status_code: int):
    """Проверяет соответствие реального HTTP-статуса ответа заданного URL
    ожидаемому коду без выполнения редиректов"""
    response = requests.get(url, allow_redirects=False, timeout=10)

    # Проверяем, совпадает ли реальный статус-код с ожидаемым
    assert response.status_code == status_code, \
        f"Ожидали статус {status_code}, но получили {response.status_code} для {url}"
