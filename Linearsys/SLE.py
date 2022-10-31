from Matrixes.MatrixOperations import MatrixMath
from Matrixes.MatrixOperations import InverseMatrix
from Matrixes.MatrixOperations import Determinant

# class of Gauss method for system of linear equations 
class Gauss:
    @staticmethod
    def solve_string(input: str) -> list[float]:
        ls = []
        rows = input.split('\n')
        rows = [i.split(' ') for i in rows]

        for i in range(0, len(rows)):
            ls.append([])
            for j in range(0, len(rows[i])):
                ls[i].append(int(rows[i][j]))

        Gauss.fix_main_diagonal(ls)

        ls = Gauss.directDivision(ls)
        ls = Gauss.reverseDivision(ls)
        Gauss.diagonals_to_ones(ls)

        return Gauss.get_string_solution(ls)

    @staticmethod
    def solve(extend_matrix: list[list[float]]) -> list[float]:
        Gauss.fix_main_diagonal(extend_matrix)

        extend_matrix = Gauss.directDivision(extend_matrix)
        extend_matrix = Gauss.reverseDivision(extend_matrix)
        Gauss.diagonals_to_ones(extend_matrix)

        return Gauss.get_string_solution(extend_matrix)

    @staticmethod
    def get_string_solution(matrix: list[list[float]]) -> str:
        res = 'SOLUTION=( '
        for i in range(0, len(matrix)):
            res += f'{matrix[i][len(matrix)]}; '
        
        return res + ')'

    @staticmethod
    def fix_main_diagonal(matrix: list[list[float]]):
        for i in range(0, len(matrix)):
            if matrix[i][i] == 0:
                d = next ((i for i in range(0, len(matrix)) if matrix[i][i] != 0), -1)
                matrix[i], matrix[d] = matrix[d], matrix[i]

    @staticmethod
    def check_for_proportional(matrix: list[list[float]]) -> tuple[int, int]:
        for i in range(len(matrix)):
            okay = True
            for j in range(i + 1, len(matrix)):
                coefficient = matrix[i][1] / matrix[j][1]
                for k in range(1, len(matrix[i])):
                    if matrix[i][k] / matrix[j][k] == coefficient:
                        okay = False
                    else:
                        okay = True
                        break

                if not okay:
                    return (i, j)
        return None

    @staticmethod
    def diagonals_to_ones(matrix: list[list[float]]):
        for i in range(0, len(matrix)):
            element = matrix[i][i]
            for j in range(0, len(matrix[i])):
                matrix[i][j] /= element

    @staticmethod
    def directDivision(matrix: list[list[float]]) -> list[list[float]]:
        for i in range(0, len(matrix)):
            for j in range(i + 1, len(matrix)):
                koeff = matrix[j][i] / matrix[i][i]
                for k in range(0, len(matrix[i])):
                    matrix[j][k] -= matrix[i][k] * koeff      
        return matrix

    @staticmethod
    def reverseDivision(matrix: list[list[float]]) -> list[list[float]]:
        for i in range(len(matrix) - 1, -1, -1):
            for j in range(i - 1, -1, -1):
                koeff = matrix[j][i] / matrix[i][i]
                for k in range(len(matrix), -1, -1):
                    matrix[j][k] -= matrix[i][k] * koeff
        return matrix


# class of Kramer's method for system linear equations
class Kramer:
    def getsolutions(self, expandedmatrix: list[list[float]]) -> list[float]:
        systematrix = self.getinitialmatrix(expandedmatrix)
        rightside = self.getrightside(expandedmatrix)

        sourceDeterminant = Determinant().getforMatrix(systematrix)

        if sourceDeterminant == 0:
            return None

        res = []
        for i in range(len(expandedmatrix)):
            NrowDeterminant = Determinant().getforMatrix(self.columnreplacer(systematrix, rightside, i))
            res.append(NrowDeterminant / sourceDeterminant)

        return res

    def columnreplacer(self, matrix: list[list[float]], rightside: list[float], row: int) -> list[list[float]]:
        dummy = [matrix[i].copy() for i in range(len(matrix))]

        for i in range(len(matrix)):
            dummy[i][row] = rightside[i]
        return dummy

    def getinitialmatrix(self, expandedmatrix: list[list[float]]) -> list[list[float]]:
        dummy = [expandedmatrix[i].copy() for i in range(len(expandedmatrix))]

        for i in range(len(dummy)):
            dummy[i].pop(len(dummy))
        return dummy

    def getrightside(self, expandedmatrix: list[list[float]]) -> list[float]:
        vector = []

        for i in range(len(expandedmatrix)):
            vector.append(expandedmatrix[i][len(expandedmatrix)])
        return vector


# class for solve system of linear equations with inverse method
class InverseMethod:
    def solve(expandedmatrix: list[list[float]]):
        rightside = [[expandedmatrix[i][-1]] for i in range(len(expandedmatrix))]
        systematrix = [expandedmatrix[i].copy() for i in range(len(expandedmatrix))]

        for i in range(len(systematrix)):
            systematrix[i].pop(len(systematrix))

        systematrix = InverseMatrix.getfor(systematrix)

        return MatrixMath.multiply(systematrix, rightside)
