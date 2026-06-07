"""Вычисляем площадь и периметр круга"""

# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
import math
from figure import Figure


class Circle(Figure):
    """Вычисляем площадь и периметр круга"""

    def __init__(self, r):
        self.r = r

    def get_perimeter(self):
        return 2 * math.pi * self.r

    def get_area(self):
        return math.pi * (self.r**2)
