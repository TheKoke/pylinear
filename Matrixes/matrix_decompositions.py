import math
import setup

setup.set()

from Matrixes.matrixes import Matrix
from Vectors.vectors import Vector

# class for composition matrix to Q*R 
class QRDecomposition:
    @staticmethod
    def get(matrix: Matrix) -> list[Matrix]:
        '''
        Returns a two matrices in row-list, where first is Q matrix,
        second is R matrix.
        '''
        an = QRDecomposition.__breakup(matrix)
        en = QRDecomposition.__recurrence(an)

        q = QRDecomposition.unitary(en)
        r = QRDecomposition.uppertriangular(an, en)

        return [q, r]

    @staticmethod
    def unitary(en: list[Vector]) -> Matrix:
        q: list[list] = []
        for i in range(len(en)):
            q.append([])
            for j in range(len(en[i].components)):
                q[i].append(en[j].components[i])
        return Matrix(q)

    @staticmethod
    def uppertriangular(an: list[Vector], en: list[Vector]) -> Matrix:
        r: list[list] = []
        for i in range(len(en)):
            r.append([])
            for j in range(len(an)):
                if j >= i:
                    r[i].append(an[j] * en[i])
                else:
                    r[i].append(0)
        return Matrix(r)

    @staticmethod
    def __breakup(matrix: Matrix) -> list[Vector]:
        trans = matrix.transparence()
        return [Vector(trans.components[i]) for i in range(len(trans))]

    @staticmethod
    def __recurrence(vectors: list[Vector]) -> list[Vector]:
        en: list[Vector] = []
        for i in range(len(vectors)):
            un = vectors[i]
            for j in range(i):
                un = un - en[j].multiply_to_constant(vectors[i] * en[j])
            en.append(un.multiply_to_constant(1 / un.norm()))
        return en

# TODO: Develop this 2 classes
class LUDecomposition:
    pass

class LUPDecmposition:
    pass