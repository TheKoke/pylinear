import math
import setup

setup.set()

from Matrixes.matrixes import Matrix
from Matrixes.matrix_decompositions import QRDecomposition
from Vectors.vectors import Vector

class QRAlgorithm:

    def __init__(self, matrix: Matrix, epsilon: float = 1e-3) -> None:
        self.matrix = matrix
        self.epsilon = epsilon 

    def eigens(self) -> dict[float, Vector]:
        zero = QRDecomposition.get(self.matrix)

        An = [self.matrix, zero[1].multiply(zero[0])]
        Qn = [zero[0]]

        while difference(An[0], An[1]) > self.epsilon:
            next = QRDecomposition.get(An[1])

            An[0] = An[1]
            An[1] = next[1].multiply(next[0])

            Qn.append(next[0])

        p = QRAlgorithm.__build_vectors(Qn)
        return {An[1].components[i][i] : p[i] for i in range(An[1].dim)}
    
    def eigenvalues(self) -> list[float]:
        return list(self.eigens().keys())

    def eigenvectors(self) -> list[Vector]:
        return list(self.eigens().values())

    @staticmethod
    def __build_vectors(qn: list[Matrix]) -> list[Vector]:
        p = qn[0]
        for i in range(1, len(qn)):
            p = p.multiply(qn[i])

        return [Vector(p.transparence().components[i]) for i in range(len(p))]


# TODO: Settle the Jacobi class
class Jacobi:

    def __init__(self, matrix: Matrix, epsilon: float = 1e-3) -> None:
        self.matrix = Matrix([matrix.components[i].copy() for i in range(matrix.dim)])
        self.epsilon = epsilon

    def eigens(self) -> dict[float, Vector]:
        pass

    def eigenvalues(self) -> list[float]:
        return list(self.eigens().keys())

    def eigenvectors(self) -> list[Vector]:
        return list(self.eigens().values())

    def __find_anlge(self, i: int, j: int) -> float:
        pass

    def __build_transform(self, i: int, j: int, angle: float) -> Matrix:
        t = [[1 if i == j else 0 for i in range(self.matrix.dim)] for j in range(self.matrix.dim)]

        t[i][i] = math.cos(angle)
        t[i][j] = -math.sin(angle)
        t[j][i] = math.sin(angle)
        t[j][j] = math.cos(angle)

        return Matrix(t)

    def __find_max(self) -> tuple[int]:
        max = -99999
        result = (0, 0)
        for i in range(self.matrix.dim):
            for j in range(self.matrix.dim):
                if i == j:
                    continue

                if max < self.matrix.components[i][j]:
                    max = self.matrix.components[i][j]
                    result = (i, j)
        return result

def difference(first: Matrix, second: Matrix) -> float:
    return sum([abs(first.components[j][j] - second.components[j][j]) for j in range(first.dim)]) / first.dim