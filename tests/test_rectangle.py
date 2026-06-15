"""Тесты для проверки Прямоугольника"""

# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
import pytest
from src.rectangle import Rectangle


def test_rectangle_creation_success():
    """Проверка успешного создания прямоугольника."""
    rectangle = Rectangle(4, 5)
    assert rectangle.name == "Rectangle"
    assert rectangle.side_a == 4
    assert rectangle.side_b == 5


@pytest.mark.parametrize(
    "a, b",
    [
        pytest.param(0, 5, id='одна сторона = 0'),
        pytest.param(5, -6, id='одна сторона меньше 0'),
        pytest.param(-5, -6, id='обе стороны меньше 0')
    ]
)
def test_rectangle_not_created(a, b):
    """Проверка на невозможность создания прямоугольника"""
    with pytest.raises(ValueError):
        Rectangle(a, b)


def test_rectangle_perimeter():
    """Проверка правильного расчета периметра прямоугольника"""
    rectangle = Rectangle(4, 5)
    assert rectangle.get_perimeter() == 18


def test_rectangle_area():
    """Проверка правильного расчета площади прямоугольника"""
    rectangle = Rectangle(4, 5)
    assert rectangle.get_area() == 20


def test_rectangle_add_area_failure():
    """Проверка валидации типа при сложении площадей."""
    rectangle = Rectangle(4, 5)
    with pytest.raises(ValueError):
        rectangle.add_area(123)
