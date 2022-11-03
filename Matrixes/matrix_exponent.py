import math
from Matrixes.matrixes import Matrix

class Taylor:
    def __init__(self, matrix: Matrix, epsilon: float = 0.001) -> None:
        self.matrix = matrix
        self.epsilon = epsilon

    def approximate(self) -> Matrix:
        single = Matrix([[1 if i == j else 0 for j in range(len(self.matrix))] for i in range(len(self.matrix))])

        return single.sum(self.series())

    def series(self) -> Matrix:
        powers = self.powers()

        localsum = powers[0]
        for i in range(1, len(powers)):
            localsum = localsum.sum(powers[i - 1].multiply_const(1 / math.factorial(i + 1)))

        return localsum

    def powers(self) -> list[Matrix]:
        pows = [self.matrix]
        for i in range(1, 8):
            pows.append(pows[i - 1].multiply(self.matrix))
        return pows

    def check(self) -> bool:
        pass

class Pade:
    pass

class MMPA:
    pass