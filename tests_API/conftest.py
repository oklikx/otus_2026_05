"""conftest.py"""

import pytest


def pytest_addoption(parser: pytest.Parser):
    """Регистрирует кастомные параметры командной строки для конфигурации тестов"""
    parser.addoption(
        "--url",
        default="https://ya.ru",
        help="урл запроса"
    )

    parser.addoption(
        "--status_code",
        default=200,
        type=int,
        help="код выполнения запроса"
    )


@pytest.fixture()
def url(pytestconfig):
    """Возвращает базовый URL-адрес, переданный через параметр командной строки --url"""
    return pytestconfig.getoption("--url")


@pytest.fixture()
def status_code(pytestconfig):
    """Возвращает ожидаемый HTTP статус-код, переданный
    через параметр командной строки --status_code"""
    return pytestconfig.getoption("--status_code")
