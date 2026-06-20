"""Вычисляем площадь и периметр круга"""

# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
import math
from src.figure import Figure


class Circle(Figure):
    """Вычисляем площадь и периметр круга"""

    def __init__(self, radius):
        super().__init__("Circle")
        if radius <= 0:
            raise ValueError("Радиус круга должен быть больше 0")
        self.radius = radius

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def get_area(self):
        return math.pi * (self.radius**2)
