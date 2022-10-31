import math
from Matrixes.MatrixOperations import MatrixMath

class Taylor:
    def __init__(self, matrix: list[list[float]], epsilon: float = 0.001) -> None:
        self.matrix = matrix
        self.epsilon = epsilon

    def approximate(self) -> list[list[float]]:
        single = [[1 if i == j else 0 for j in range(len(self.matrix))] for i in range(len(self.matrix))]

        return MatrixMath.sum(single, self.series())

    def series(self) -> list[list[float]]:
        powers = self.powers()

        localsum = powers[0]
        for i in range(1, len(powers)):
            localsum = MatrixMath.sum(localsum, MatrixMath.multiplyToConstant(powers[i - 1], 1 / math.factorial(i + 1)))

        return localsum

    def powers(self) -> list[list[list[float]]]:
        pows = [self.matrix]

        for i in range(1, 8):
            pows.append(MatrixMath.multiply(pows[i - 1], self.matrix))

        return pows

    def check(self) -> bool:
        pass

class Pade:
    pass

class MMPA:
    pass