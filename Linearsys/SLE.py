from Matrixes.matrixes import Matrix, Unity
from Vectors.vectors import Vector

# class of Gauss method for system of linear equations 
class Gauss:
    @staticmethod
    def solve_string(input: str) -> str:
        ls = []
        rows = input.split('\n')
        rows = [i.split(' ') for i in rows]

        for i in range(0, len(rows)):
            ls.append([])
            for j in range(0, len(rows[i])):
                ls[i].append(int(rows[i][j]))

        ls = Matrix(ls)
        Gauss.fix_main_diagonal(ls)

        ls = Gauss.directDivision(ls)
        ls = Gauss.reverseDivision(ls)
        Gauss.diagonals_to_ones(ls)

        return Gauss.get_string_solution(ls)

    @staticmethod
    def solve(extend_matrix: Matrix) -> Vector:
        Gauss.fix_main_diagonal(extend_matrix)

        extend_matrix = Gauss.directDivision(extend_matrix)
        extend_matrix = Gauss.reverseDivision(extend_matrix)
        Gauss.diagonals_to_ones(extend_matrix)

        return Vector([extend_matrix[i][extend_matrix.dim] for i in range(extend_matrix.dim)])

    @staticmethod
    def get_string_solution(matrix: Matrix) -> str:
        res = 'SOLUTION=( '
        for i in range(0, matrix.dim):
            res += f'{matrix.components[i][-1]}; '
        
        return res + ')'

    @staticmethod
    def fix_main_diagonal(matrix: Matrix) -> None:
        for i in range(matrix.dim):
            if matrix.components[i][i] == 0:
                d = next((i for i in range(0, matrix.dim) if matrix.components[i][i] != 0), -1)
                matrix.components[i], matrix.components[d] = matrix.components[d], matrix.components[i]

    @staticmethod
    def check_for_proportional(matrix: Matrix) -> tuple[int, int]:
        for i in range(matrix.dim):
            okay = True
            for j in range(i + 1, matrix.dim):
                coefficient = matrix[i][1] / matrix[j][1]
                for k in range(1, matrix.dim + 1):
                    if matrix.components[i][k] / matrix.components[j][k] == coefficient:
                        okay = False
                    else:
                        okay = True
                        break

                if not okay:
                    return (i, j)
        return None

    @staticmethod
    def diagonals_to_ones(matrix: Matrix) -> None:
        for i in range(matrix.dim):
            element = matrix.components[i][i]
            for j in range(matrix.dim):
                matrix.components[i][j] /= element

    @staticmethod
    def directDivision(matrix: Matrix) -> Matrix:
        for i in range(matrix.dim):
            for j in range(i + 1, matrix.dim):
                koeff = matrix.components[j][i] / matrix.components[i][i]
                for k in range(matrix.dim + 1):
                    matrix[j][k] -= matrix[i][k] * koeff      
        return matrix

    @staticmethod
    def reverseDivision(matrix: Matrix) -> Matrix:
        for i in range(matrix.dim - 1, -1, -1):
            for j in range(i - 1, -1, -1):
                koeff = matrix.components[j][i] / matrix.components[i][i]
                for k in range(matrix.dim, -1, -1):
                    matrix[j][k] -= matrix[i][k] * koeff
        return matrix


# class of Kramer's method for system linear equations
class Kramer:
    def __init__(self, expanded_matrix: Matrix) -> None:
        self.expanded_matrix = expanded_matrix

        self.systematrix = self.get_initialmatrix()
        self.rightside = self.get_rightside()

    def getsolutions(self) -> Vector:
        source_determinant = self.systematrix.determinant()

        if source_determinant == 0:
            return None

        res = []
        for i in range(self.expanded_matrix.dim):
            row_determinant = self.columnreplacer(i).determinant()
            res.append(row_determinant / source_determinant)

        return Vector(res)

    def columnreplacer(self, row: int) -> Matrix:
        dummy = [self.expanded_matrix.components[i].copy() for i in range(self.expanded_matrix.dim)]

        for i in range(self.expanded_matrix.dim):
            dummy[i][row] = self.rightside.components[i]
        return Matrix(dummy)

    def get_initialmatrix(self) -> Matrix:
        dummy = [self.expanded_matrix.components[i].copy() for i in range(self.expanded_matrix.dim)]

        for i in range(len(dummy)):
            dummy[i].pop(len(dummy))
        return Matrix(dummy)

    def get_rightside(self) -> Vector:
        vector = []

        for i in range(self.expanded_matrix.dim):
            vector.append(self.expanded_matrix.components[i][-1])
        return Vector(vector)


# class for solve system of linear equations with inverse method
class InverseMethod:
    def solve(expandedmatrix: Matrix):
        rightside = Vector([expandedmatrix[i][-1] for i in range(len(expandedmatrix))])
        systematrix = Unity(expandedmatrix.dim) + expandedmatrix - Unity(expandedmatrix.dim)

        for i in range(len(systematrix)):
            systematrix.components[i].pop(systematrix.dim)

        systematrix = systematrix.inverse()

        return systematrix * rightside
