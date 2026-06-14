"""Вычисляем площадь и периметр прямоугольника"""

# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
from figure import Figure


class Rectangle(Figure):
    """Вычисляем площадь и периметр прямоугольника"""

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_perimeter(self):
        return 2 * (self.a + self.b)

    def get_area(self):
        return self.a * self.b
