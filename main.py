from SLEParser import ShuntingYard
from SLE  import Gauss

s = ["0.6x+y-5z=1", "2x-3y-3z=2", "-x+2y+4z=x-y-z+6"]

r = ShuntingYard.get_extend_matrix(s)

print(r)

r = Gauss.solve(r)

print(r)