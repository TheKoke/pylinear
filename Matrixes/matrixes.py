from __future__ import annotations

import math

class Matrix:
    def __init__(self, ij: list[list[float]] = [[1]]) -> None:
        self.components = ij
        self.dim = len(self.components)

    def __str__(self) -> str:
        return '\n'.join(self.components[i] for i in range(self.dim))
    
    @staticmethod
    def __second_order(components: list[list[float]]) -> float:
        return components[0][0] * components[1][1] - components[0][1] * components[1][0]

    def determinant(self) -> float:
        if self.dim == 1:
            return self.components[0][0]

        if self.dim == 2:
            return Matrix.__second_order(self.components)

        result = 0
        for i in range(self.dim):
            result += self.cofactor(0, i)
        return result

    def transparence(self) -> Matrix:
        clone = [self.components[i].copy() for i in range(self.dim)]

        for i in range(len(clone)):
            for j in range(len(clone[i])):
                clone[i][j] = self.components[j][i]
                clone[j][i] = self.components[i][j]
        return Matrix(clone)

    def minor(self, row: str, col: int) -> Matrix:
        if row >= self.dim or col >= self.dim:
            raise ValueError("Invalid minor indexes")

        clone = [self.components[i].copy() for i in range(self.dim)]

        for i in range(len(clone)):
            if i == row:
                 clone.pop(i)
                 break

        for i in range(len(clone)):
            for j in range(len(clone[i])):
                if j == col:
                    clone[i].pop(j)
                    break
        return Matrix(clone)

    def inverse(self) -> Matrix:
        if self.determinant() == 0:
            return None

        coeff = 1 / self.determinant()
        return self.adjunt_matrix().multiply_const(coeff)

    def adjunt_matrix(self) -> Matrix:
        cofactormatrix = []

        for i in range(self.dim):
            cofactormatrix.append([])
            for j in range(self.dim):
                cofactormatrix[i].append(self.cofactor(i, j))
        return Matrix(cofactormatrix).transparence()

    def sum(self, other: Matrix) -> Matrix:
        if self.dim != other.dim:
            return None

        mask = [self.components[i].copy() for i in range(self.dim)]

        for i in range(len(mask)):
            for j in range(len(mask)):
                mask[i][j] += other.components[i][j]
        return Matrix(mask)

    def subtract(self, other: Matrix) -> Matrix:
        return self.sum(other.multiply_const(-1))

    def multiply(self, other: Matrix) -> Matrix:
        if self.dim != other.dim:
            return None
        
        result = []
        for i in range(other.dim):
            result.append([])
            for j in range(other.dim):
                nextelement = 0
                for k in range(other.dim):
                    nextelement += self.components[i][k] * other.components[k][j]
                result[i].append(nextelement)
        return Matrix(result)

    def multiply_const(self, const: float) -> Matrix:
        mask = [self.components[i].copy() for i in range(self.dim)]

        for i in range(len(mask)):
            for j in range(len(mask[i])):
                mask[i][j] *= const
        return Matrix(mask)

    def cofactor(self, row: int, col: int) -> float:
        minor = self.minor(row, col)
        return (-1) ** (row + col) * minor.determinant()

    def trace(self) -> float:
        return sum(self.components[i][i] for i in range(self.dim))

    def norm(self) -> float:
        '''
        Method for L2 norm of matrix
        '''
        rowsums = []
        for i in range(self.dim):
            rowsums.append(sum(self.components[i][j] ** 2 for j in range(self.dim)))
        return math.sqrt(sum(rowsums))