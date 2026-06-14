"""Вычисляем площадь и периметр треугольника"""

# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
import math
from figure import Figure


class Triangle(Figure):
    """Вычисляем площадь и периметр треугольника"""

    def __init__(self, a, b, c):
        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            raise ValueError("Треугольник создать нельзя")
        self.a = a
        self.b = b
        self.c = c

    def get_perimeter(self):
        return (self.a + self.b + self.c) / 2

    def get_area(self) -> float:
        p = self.get_perimeter() / 2
        square = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return square
