"""Вычисляем площадь и периметр квадрата"""

# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
from figure import Figure


class Square(Figure):
    """Вычисляем площадь и периметр квадрата"""

    def __init__(self, a):
        self.a = a

    def get_perimeter(self):
        return 4 * self.a

    def get_area(self):
        return self.a**2
