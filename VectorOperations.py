from MatrixOperations import Determinant, MatrixAlgebra

class VectorAlgebra:
    @staticmethod
    def dot_product(first: list[float], second: list[float]) -> float:
        if len(first) != len(second):
            raise ValueError('Vector must be same dimensional')

        result = 0
        for i in range(len(first)):
            result += first[i] * second[i]

        return result

    @staticmethod
    def cross_product(first: list[float], second: list[float]) -> list[float]:
        if len(first) != len(second):
            raise ValueError('Vector must be same dimensional')

        picture_matrix = [[1] * 3, *first, *second]
        result_vector = []

        for i in range(len(picture_matrix)):
            result_vector.append
            (Determinant.getforMatrix(MatrixAlgebra.minor(picture_matrix, 0, i)))

        return result_vector