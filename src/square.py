"""Вычисляем площадь и периметр квадрата"""

# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
from src.rectangle import Rectangle


class Square(Rectangle):
    """Вычисляем площадь и периметр квадрата"""

    def __init__(self, side):
        if side <= 0:
            raise ValueError("Сторона квадрата должна быть больше 0")
        super().__init__(side, side)
        self.name = "Square"
        self.side = side
