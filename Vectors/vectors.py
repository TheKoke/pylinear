from __future__ import annotations

import setup
setup.set()

import math
from Matrixes.matrixes import Matrix

class Vector:
    def __init__(self, xyz: list[float]) -> None:
        self.components = xyz

    def sum(self, other: Vector, subtract: bool = False) -> Vector:
        if subtract:
            second = other.multiply_to_constant(-1)
        else:
            second = other
        return Vector([self.components[i] + second.components[i] for i in range(len(self.components))])

    def norm(self) -> float:
        return math.sqrt(sum([self.components[i] ** 2 for i in range(len(self.components))]))

    def dotproduct(self, other: Vector) -> float:
        return sum([self.components[i] * other.components[i] for i in range(len(self.components))])

    def crossproduct(self, other: Vector) -> Vector:
        product_matrix = Matrix([[1, 1, 1], self.components, other.components])
        return Vector([product_matrix.cofactor(0, i) for i in range(len(self.components))])

    def multiply_to_constant(self, const: float) -> Vector:
        return Vector(list(map(lambda x: x * const, self.components)))