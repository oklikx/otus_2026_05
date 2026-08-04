"""Тесты для сайта https://dog.ceo/dog-api/"""
import pytest

from http_client import HttpClient

http_client = HttpClient('https://dog.ceo/api')


def get_path_by_breed(breed: str = 'affenpinscher'):
    """Формирует относительный URL-путь для получения
    случайного изображения породы"""
    return f'breed/{breed}/images/random'


def get_sub_breeds_path(breed: str = 'hound'):
    """Формирует относительный URL-путь для получения списка субпород"""
    return f'breed/{breed}/list'


@pytest.mark.dog_api
def test_random_dog_image_by_breed():
    """Проверяет успешное получение ссылки на
    фото собаки по породе и ошибку 404
    для неверной породы"""
    success_path = get_path_by_breed()
    success_res = http_client.get(success_path)

    assert 'message' in success_res and isinstance(
        success_res["message"], str)
    assert 'status' in success_res and success_res["status"] == 'success'

    # ошибка
    error_path = get_path_by_breed('несуществующаяпорода')
    err_res = http_client.get(error_path, code=404)

    assert err_res["message"] == 'Breed not found (main breed does not exist)'
    assert err_res["status"] == 'error'


@pytest.mark.dog_api
def test_get_all_breeds():
    """Проверка всех доступных пород и их субпород."""
    path = 'breeds/list/all'
    res = http_client.get(path)

    assert 'status' in res and res["status"] == 'success'
    assert isinstance(res["message"]["affenpinscher"], list)
    assert res["message"]["african"][0] == 'wild'


@pytest.mark.dog_api
def test_get_single_random_dog_image():
    """Проверяет получение ссылки на ровно одно случайное
    изображение собаки любой породы"""
    path = 'breeds/image/random'
    res = http_client.get(path)

    assert 'message' in res and isinstance(
        res["message"], str)
    assert 'status' in res and res["status"] == 'success'


@pytest.mark.dog_api
def test_get_multuple_random_dog_images():
    """Проверяет запрос списка из 10 случайных изображений собак любых пород"""
    path = 'breeds/image/random/10'
    res = http_client.get(path)

    assert len(res["message"]) == 10
    assert 'status' in res and res["status"] == 'success'


@pytest.mark.dog_api
def test_get_list_of_sub_breeds():
    """Проверяет точный список и количество
    субпород для пород hound и mastiff"""
    hound_path = get_sub_breeds_path()
    hound_res = http_client.get(hound_path)

    hound_sub_breeds = hound_res['message']

    assert 'status' in hound_res and hound_res["status"] == 'success'
    assert len(hound_sub_breeds) == 7
    assert hound_sub_breeds[0] == 'afghan'
    assert hound_sub_breeds[1] == 'basset'
    assert hound_sub_breeds[2] == 'blood'
    assert hound_sub_breeds[3] == 'english'
    assert hound_sub_breeds[4] == 'ibizan'
    assert hound_sub_breeds[5] == 'plott'
    assert hound_sub_breeds[6] == 'walker'

    # mastiff
    mastiff_path = get_sub_breeds_path('mastiff')
    mastiff_res = http_client.get(mastiff_path)

    mastiff_sub_breeds = mastiff_res["message"]

    assert 'status' in hound_res and hound_res["status"] == 'success'

    assert len(mastiff_sub_breeds) == 4
    assert mastiff_sub_breeds[0] == 'bull'
    assert mastiff_sub_breeds[1] == 'english'
    assert mastiff_sub_breeds[2] == 'indian'
    assert mastiff_sub_breeds[3] == 'tibetan'
