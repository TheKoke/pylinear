from __future__ import annotations

import setup
setup.set()

import math
from Matrixes.matrixes import Matrix

class Vector:
    def __init__(self, xyz: list[float | complex]) -> None:
        self.components = xyz

    def __str__(self) -> str:
        return str(self.components)

    def __add__(self, __o) -> Vector:
        return self.sum(__o)
    
    def __sub__(self, __o) -> Vector:
        return self.sum(__o, subtract=True)

    def __mul__(self, __o) -> float | complex:
        return self.__dotproduct(__o)

    def sum(self, other: Vector, subtract: bool = False) -> Vector:
        if subtract:
            second = other.multiply_to_constant(-1)
        else:
            second = other
        return Vector([self.components[i] + second.components[i] for i in range(len(self.components))])

    def norm(self) -> float | complex:
        return math.sqrt(sum([self.components[i] ** 2 for i in range(len(self.components))]))

    def __dotproduct(self, other: Vector) -> float | complex:
        return sum([self.components[i] * other.components[i] for i in range(len(self.components))])

    def crossproduct(self, other: Vector) -> Vector:
        product_matrix = Matrix([[1, 1, 1], self.components, other.components])
        return Vector([product_matrix.cofactor(0, i) for i in range(len(self.components))])

    def multiply_to_constant(self, const: float) -> Vector:
        return Vector(list(map(lambda x: x * const, self.components)))