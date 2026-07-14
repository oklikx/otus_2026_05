"""Тесты для сайта https://www.openbrewerydb.org/"""

import pytest

from http_client import HttpClient

http_client = HttpClient('https://api.openbrewerydb.org/v1/breweries')


@pytest.mark.brewery_api
def test_get_breweries_list():
    """Проверяет получение дефолтного списка пивоварен,
    его размер и наличие всех обязательных полей в объекте"""
    res = http_client.get('')

    assert isinstance(res, list)
    assert len(res) == 50

    first_brewery = res[0]

    assert 'id' in first_brewery
    assert 'name' in first_brewery
    assert 'brewery_type' in first_brewery
    assert 'address_1' in first_brewery
    assert 'address_2' in first_brewery
    assert 'address_3' in first_brewery
    assert 'city' in first_brewery
    assert 'state_province' in first_brewery
    assert 'postal_code' in first_brewery
    assert 'country' in first_brewery
    assert 'longitude' in first_brewery
    assert 'latitude' in first_brewery
    assert 'phone' in first_brewery
    assert 'website_url' in first_brewery
    assert 'state' in first_brewery
    assert 'street' in first_brewery


@pytest.mark.brewery_api
def test_get_single_brewery():
    """Проверяет получение информации об одной конкретной пивоварне
    по её динамически полученному ID"""
    breweries_list = http_client.get('')

    # находим реальный id одного напитка в списке, чтобы не хардкодить
    obdb_id = breweries_list[0]['id']

    # запрашиваем по этому параметру один напиток
    single_brewery = http_client.get(obdb_id)

    # проверяем, что его id совпал с найденым в списке
    assert single_brewery['id'] == obdb_id


@pytest.mark.brewery_api
def test_sort_brewery_list_by_name():
    """Проверяет сортировку списка пивоварен по типу и почтовому индексу
    по убыванию с ограничением вывода"""
    query = '?sort=type,postal_code:desc&per_page=3'
    res = http_client.get(query)

    [first, second, third] = res

    assert first['postal_code'] == 'Y35 HW27'
    assert second['postal_code'] == 'Y35 HN50'
    assert third['postal_code'] == 'X91 HP89'


@pytest.mark.brewery_api
def test_search_brewery_by_query():
    """Проверяет полнотекстовый поиск пивоварен по поисковому запросу
    города и валидирует результаты"""
    search = "san%20diego"
    path = f"search?query={search}&per_page=3"
    res = http_client.get(path)

    [first, second, third] = res

    assert first['city'] == 'San Diego'
    assert second['city'] == 'San Diego'
    assert third['city'] == 'San Diego'


@pytest.mark.brewery_api
def test_get_all_breweries_meta_data():
    """Проверяет получение метаданных обо всех пивоварнях и
    сверяет общее количество в базе"""
    path = "meta"
    res = http_client.get(path)

    assert isinstance(res["total"], int) and res["total"] == 11745
