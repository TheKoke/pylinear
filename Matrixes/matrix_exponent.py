import math
from Matrixes.matrixes import Matrix

class Taylor:
    def __init__(self, matrix: Matrix, epsilon: float = 0.001) -> None:
        self.matrix = matrix
        self.epsilon = epsilon

    def approximate(self) -> Matrix:
        pass

    def series(self) -> Matrix:
        pass

    def check(self) -> bool:
        pass

class Pade:
    def __init__(self, matrix: Matrix, epsilon: float = 0.001) -> None:
        self.matrix = matrix
        self.epsilon = epsilon

    def approximate(self) -> Matrix:
        pass

    def check(self) -> bool:
        pass

class MMPA:
    def __init__(self, matrix: Matrix, epsilon: float = 0.001) -> None:
        self.matrix = matrix
        self.epsilon = epsilon

    def approximate(self) -> Matrix:
        pass

    def check(self) -> bool:
        pass

def powers(matrix: Matrix) -> list[Matrix]:
    pows = [matrix]
    for i in range(1, 5):
        pows.append(pows[i - 1].multiply(matrix))
    return pows