"""Вычисляем площадь и периметр треугольника"""

# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
import math
from src.figure import Figure


class Triangle(Figure):
    """Вычисляем площадь и периметр треугольника"""

    def __init__(self, side_a, side_b, side_c):
        super().__init__("Triangle")
        if ((side_a + side_b <= side_c) or (side_a + side_c <= side_b)
                or (side_b + side_c <= side_a)):
            raise ValueError("Треугольник создать нельзя")
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Стороны треугольника должны быть больше 0")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def get_area(self) -> float:
        p = self.get_perimeter() / 2
        square = math.sqrt(p * (p - self.side_a) * (p - self.side_b)
                           * (p - self.side_c))
        return square
