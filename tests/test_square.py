"""Тесты для проверки Квадрата"""
import pytest
from src.square import Square


def test_square_creation_success():
    """Проверка создания квадрата"""
    square = Square(4)
    assert square.name == "Square"
    assert square.side_a == 4


@pytest.mark.parametrize("side", [0, -4])
def test_square_not_created(side):
    """Проверка на невозможность создания квадрата"""
    with pytest.raises(ValueError):
        Square(side)


def test_square_perimeter():
    """Проверка правильного расчета периметра квадрата"""
    square = Square(4)
    assert square.get_perimeter() == 16


def test_square_area():
    """Проверка правильного расчета площади квадрата"""
    square = Square(5)
    assert square.get_area() == 25
