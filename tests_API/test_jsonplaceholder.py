"""Тесты для сайта https://jsonplaceholder.typicode.com/"""
import json
import pytest

from http_client import HttpClient

http_client = HttpClient('https://jsonplaceholder.typicode.com')


@pytest.mark.jsonplaceholder_api
def test_get_users_list():
    """Проверяет получение полного списка пользователей,
    его длину и структуру первого элемента"""
    path = "users"
    users = http_client.get(path)

    assert len(users) == 10
    assert users[0]["name"] == "Leanne Graham"
    assert users[0]["id"] == 1
    assert users[0]["address"]["street"] == "Kulas Light"


@pytest.mark.jsonplaceholder_api
def test_get_one_user_by_id():
    """Проверяет точечное получение данных конкретных
    пользователей по их уникальному идентификатору (ID)"""
    first_user_path = "users/1"
    first_user = http_client.get(first_user_path)

    assert first_user["id"] == 1
    assert first_user["name"] == "Leanne Graham"
    assert first_user["address"]["street"] == "Kulas Light"

    seventh_user_path = "users/7"
    seventh_user = http_client.get(seventh_user_path)

    assert seventh_user["id"] == 7
    assert seventh_user["name"] == "Kurtis Weissnat"
    assert seventh_user["address"]["street"] == "Rex Trail"


@pytest.mark.jsonplaceholder_api
def test_create_todo():
    """Проверяет успешное создание новой задачи (POST) и
    валидность возвращаемых сервером полей"""
    path = "todos"
    body = {
        "userId": 1,
        "title": "Test Todo"
    }

    res = http_client.post(path, body=json.dumps(body), code=201)

    assert res["id"] == 201
    assert res["userId"] == 1
    assert res["title"] == "Test Todo"


@pytest.mark.jsonplaceholder_api
def test_update_todo():
    """Проверяет обновление существующей задачи (PUT) и
    сохранение измененных атрибутов"""
    path = "todos/5"
    body = {
        "title": "updated todo title",
        "completed": True
    }

    res = http_client.put(path, body=json.dumps(body))

    assert res["title"] == "updated todo title"
    assert res["completed"] is True


@pytest.mark.jsonplaceholder_api
def test_delete_todo():
    """Проверяет удаление задачи (DELETE) и
    получение пустого объекта в качестве ответа"""
    path = "todos/5"

    res = http_client.delete(path)

    assert res == {}
