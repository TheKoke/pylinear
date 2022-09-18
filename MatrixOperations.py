# class of matrixes specific algebra
class MatrixAlgebra:
    @staticmethod
    def get_transparence(matrix: list[list]) -> list[list]:
        clone = [matrix[i].copy() for i in range(len(matrix))]

        for i in range(len(clone)):
            for j in range(len(clone[i])):
                clone[i][j] = matrix[j][i]
                clone[j][i] = matrix[i][j]
        return clone

    @staticmethod
    def minor(matrix: list[list], delrow: int, delcol: int) -> list[list]:
        if delrow >= len(matrix) or delcol >= len(matrix[0]):
            raise ValueError("Invalid minor indexes")

        clone = [matrix[i].copy() for i in range(len(matrix))]

        for i in range(len(clone)):
            if i == delrow:
                 clone.pop(i)
                 break

        for i in range(len(clone)):
            for j in range(len(clone[i])):
                if j == delcol:
                    clone[i].pop(j)
                    break
        return clone

    @staticmethod
    def cofactor(matrix: list[list], row: int, col: int) -> float:
        minor = MatrixAlgebra.minor(matrix, row, col)

        return (-1)**(row + col) * Determinant.getforMatrix(minor)

# class for find inverse matrix to any square matrix
class InverseMatrix:
    @staticmethod
    def getfor(matrix: list[list[float]]) -> list[list]:
        if Determinant.getforMatrix(matrix) == 0:
            return None

        koefficient =  1 / Determinant.getforMatrix(matrix)

        return MatrixMath.multiplyToConstant(InverseMatrix.getAdjuntMatrix(matrix), koefficient)

    def getCofactorMatrix(matrix: list[list[float]]) -> list[list[float]]:
        cofactormatrix = []

        for i in range(len(matrix)):
            cofactormatrix.append([])
            for j in range(len(matrix[i])):
                cofactormatrix[i].append(MatrixAlgebra.cofactor(matrix, i, j))
        return cofactormatrix

    def getAdjuntMatrix(matrix: list[list[float]]) -> list[list[float]]:
        return MatrixAlgebra.get_transparence(InverseMatrix.getCofactorMatrix(matrix))


# class contanining all basic math operations for matrixes
class MatrixMath:
    @staticmethod
    def sum(first: list[list[float]], second: list[list[float]]) -> list[list[float]]:
        if len(first) != len(second):
            return None

        mask = [first[i].copy() for i in range(len(first))]

        for i in range(len(mask)):
            for j in range(len(mask)):
                mask[i][j] += second[i][j]
        return mask

    @staticmethod
    def subtract(first: list[list[float]], second: list[list[float]]) -> list[list[float]]:
        return MatrixMath.sum(first, MatrixMath.multiplyToConstant(second, -1))

    @staticmethod
    def multiply(first: list[list[float]], second: list[list[float]]) -> list[list[float]]:
        if len(first[0]) != len(second):
            return None
        
        result = []
        for i in range(len(second)):
            result.append([])
            for j in range(len(second[0])):
                nextelement = 0
                for k in range(len(second)):
                    nextelement += first[i][k] * second[k][j]
                result[i].append(nextelement)
        return result


    @staticmethod
    def multiplyToConstant(matrix: list[list[float]], const: float) -> list[list[float]]:
        mask = [matrix[i].copy() for i in range(len(matrix))]

        for i in range(len(mask)):
            for j in range(len(mask[i])):
                mask[i][j] *= const
        return mask


# class for find determinant of any square matrix
class Determinant:
    @staticmethod
    def getforMatrix(matrix: list[list[float]]) -> float:
        if len(matrix) == 1:
            return matrix[0][0]

        if (len(matrix) == 2):
            return Determinant.secondorder(matrix)

        result = 0
        for i in range(len(matrix)):
            if i % 2 == 0:
                result += matrix[0][i] * Determinant.getforMatrix(MatrixAlgebra.minor(matrix, 0, i))
            else:
                result -= matrix[0][i] * Determinant.getforMatrix(MatrixAlgebra.minor(matrix, 0, i))
        return result

    @staticmethod
    def secondorder(matrix: list[list[float]]) -> float:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]