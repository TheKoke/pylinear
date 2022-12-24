# from Linearsys.SLEParser import ShuntingYard
# from Linearsys.SLE  import Gauss

# s = ["0.6x+y-5z=1", "2x-3y-3z=2", "-x+2y+4z=x-y-z+6"]

# r = ShuntingYard.get_extend_matrix(s)

# print(r)

# r = Gauss.solve(r)

# print(r)
import math
from Vectors.vectors import Vector
from Matrixes.matrixes import Matrix
from Matrixes.eigens import Jacobi

example = Matrix(
    [
        [-17, -2, -2],
        [-2, 14, -4], 
        [-2, -4, 14]
    ]
)

jac = Jacobi(example)

numeric = jac.eigens()

for item in numeric:
    print(round(item), list(map(lambda x: round(x, 3), numeric[item].components)))