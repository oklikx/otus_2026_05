"""Тесты для проверки Круга"""
import math
import pytest
from src.circle import Circle


def test_circle_creation_success():
    """Проверка успешного создания круга."""
    circle = Circle(3)
    assert circle.name == "Circle"
    assert circle.radius == 3


@pytest.mark.parametrize("radius", [0, -3])
def test_circle_not_created(radius):
    """Проверка на невозможность создания круга"""
    with pytest.raises(ValueError):
        Circle(radius)


def test_circle_perimeter():
    """Проверка правильного расчета периметра круга"""
    circle = Circle(3)
    assert circle.get_perimeter() == pytest.approx(2 * math.pi * 3)


def test_circle_area():
    """Проверка правильного расчета площади круга"""
    circle = Circle(3)
    assert circle.get_area() == pytest.approx(math.pi * (3 ** 2))
