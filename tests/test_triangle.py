"""Тесты для проверки Треугольника"""
import pytest

from src.triangle import Triangle
from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square


def test_triangle_creation_success():
    """Проверка успешного создания валидного треугольника"""
    triangle = Triangle(3, 4, 5)
    assert triangle.name == "Triangle"
    assert triangle.side_a == 3
    assert triangle.side_b == 4
    assert triangle.side_c == 5


@pytest.mark.parametrize(
    ("a", "b", "c"),
    [
        pytest.param(2, 2, 8, id='сторона больше суммы двух других'),
        pytest.param(3, 5, 8, id='сторона равна суммы двух других'),
        pytest.param(0, 1, 2, id='одна сторона = 0'),
        pytest.param(-1, 2, 8, id='одна сторона меньше 0'),
        pytest.param(-1, -2, -8, id='все стороны меньше 0')
    ]
)
def test_triangle_not_created(a, b, c):
    """Проверка на невозможность создания треугольника"""
    with pytest.raises(ValueError):
        Triangle(a, b, c)


def test_triangle_perimeter():
    """Проверка правильного расчета периметра треугольника"""
    triangle = Triangle(3, 4, 5)
    assert triangle.get_perimeter() == 12


def test_triangle_area():
    """Проверка правильного расчета площади треугольника"""
    triangle = Triangle(3, 4, 5)
    assert triangle.get_area() == 6


def test_triangle_area_circle():
    """Проверка сложения площадей круга и треугольника"""
    triangle = Triangle(3, 4, 5)  # Площадь = 6
    circle = Circle(5)            # Площадь = 78.539816
    assert triangle.add_area(circle) == pytest.approx(84.539816)


def test_triangle_area_rectangle():
    """Проверка сложения площадей квадрата и треугольника"""
    triangle = Triangle(3, 4, 5)  # Площадь = 6
    square = Square(4)            # Площадь = 16
    assert triangle.add_area(square) == 22.0


def test_triangle_area_square():
    """Проверка сложения площадей прямоугольника и треугольника"""
    triangle = Triangle(3, 4, 5)  # Площадь = 6
    rectangle = Rectangle(6, 7)   # Площадь = 42
    assert triangle.add_area(rectangle) == 48.0


def test_triangle_figure_check():
    """Проверка создания фигуры"""
    triangle = Triangle(3, 4, 5)
    with pytest.raises(ValueError):
        triangle.add_area("Передана не геометрическая фигура")
