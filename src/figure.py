"""Базовый класс геометрической фигуры"""

# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
from abc import ABC, abstractmethod


class Figure(ABC):
    """Вычисляем площадь и периметр фигуры"""

    @abstractmethod
    def get_perimeter(self) -> float:
        pass

    @abstractmethod
    def get_area(self) -> float:
        pass

    def add_area(self, figure) -> float:
        if not isinstance(figure, Figure):
            raise ValueError("Передана не геометрическая фигура")
        return self.get_area() + figure.get_area()
