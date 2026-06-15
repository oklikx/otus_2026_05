"""Вычисляем площадь и периметр прямоугольника"""

# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
from src.figure import Figure


class Rectangle(Figure):
    """Вычисляем площадь и периметр прямоугольника"""

    def __init__(self, side_a, side_b):
        super().__init__("Rectangle")
        if side_a <= 0 or side_b <= 0:
            raise ValueError("Сторона прямоугольника должна быть больше 0")
        self.side_a = side_a
        self.side_b = side_b

    def get_perimeter(self):
        return 2 * (self.side_a + self.side_b)

    def get_area(self):
        return self.side_a * self.side_b
