import math
import setup

setup.set()

from Matrixes.matrixes import Matrix
from Matrixes.matrix_decompositions import QRDecomposition
from Vectors.vectors import Vector

def difference(first: Matrix, second: Matrix) -> float:
    return sum([abs(first.components[j][j] - second.components[j][j]) for j in range(first.dim)]) / first.dim

class QRAlgorithm:

    def __init__(self, matrix: Matrix, epsilon: float = 1e-3) -> None:
        self.matrix = matrix
        self.epsilon = epsilon 

    def eigens(self) -> dict[float, Vector]:
        zero = QRDecomposition.get(self.matrix)

        An: list[Matrix] = [self.matrix, zero[1] * zero[0]]
        Qn = [zero[0]]

        while difference(An[0], An[1]) > self.epsilon:
            next = QRDecomposition.get(An[1])

            An[0] = An[1]
            An[1] = next[1] * next[0]

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
            p = p * qn[i]

        return [Vector(p.transparence().components[i]) for i in range(p.dim)]


# TODO: Settle the Jacobi class
class Jacobi:

    def __init__(self, matrix: Matrix, epsilon: float = 1e-3) -> None:
        self.matrix = Matrix([matrix.components[i].copy() for i in range(matrix.dim)])
        self.epsilon = epsilon

    def eigens(self) -> dict[float, Vector]:
        maximum = Jacobi.__find_max(self.matrix)
        transform = Jacobi.__build_transform(self.matrix, maximum[0], maximum[1])

        An = [self.matrix, transform * self.matrix * transform.transparence()]
        Tn = [transform]

        while not An[1].is_diagonal():
            maximum = Jacobi.__find_max(An[1])
            transform = Jacobi.__build_transform(An[1], maximum[0], maximum[1])

            An[0] = An[1]
            An[1] = transform * An[1] * transform.transparence()

            Tn.append(transform)

        vectors = Jacobi.__build_vectors(Tn)

        return {An[1].components[i][i] : vectors[i] for i in range(An[1].dim)}

    def eigenvalues(self) -> list[float]:
        return list(self.eigens().keys())

    def eigenvectors(self) -> list[Vector]:
        return list(self.eigens().values())

    @staticmethod
    def __build_transform(selfish: Matrix, i: int, j: int) -> Matrix:
        t = [[1 if i == j else 0 for i in range(selfish.dim)] for j in range(selfish.dim)]
        angle = Jacobi.__find_angle(selfish, i, j)

        t[i][i] = math.cos(angle)
        t[i][j] = -1 * math.sin(angle)
        t[j][i] = math.sin(angle)
        t[j][j] = math.cos(angle)

        return Matrix(t)

    @staticmethod
    def __find_angle(selfish: Matrix, i: int, j: int) -> float:
        if selfish.components[i][i] - selfish.components[j][j] == 0:
            return math.pi / 4

        return math.atan(2 * selfish.components[i][j] / (selfish.components[i][i] - selfish.components[j][j])) / 2

    @staticmethod
    def __build_vectors(v: list[Matrix]) -> list[Vector]:
        p = v[0]
        for i in range(1, len(v)):
            p = p * v[i]

        return [Vector(p.transparence().components[i]) for i in range(p.dim)]

    @staticmethod
    def __find_max(matrix: Matrix) -> tuple[int]:
        max = matrix.components[0][0]
        result = (0, 0)
        for i in range(matrix.dim):
            for j in range(matrix.dim):
                if i == j:
                    continue

                if max < abs(matrix.components[i][j]):
                    max = abs(matrix.components[i][j])
                    result = (i, j)
        return result