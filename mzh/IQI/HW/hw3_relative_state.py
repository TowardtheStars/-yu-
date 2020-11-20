from sympy import *

p=Symbol('p')

rho2=Matrix([
[1-p/2,0,0,1-p],
[0,p/2,0,0],
[0,0,p/2,0],
[1-p,0,0,1-p/2]
])

print(rho2.eigenvals())
pretty_print(rho2.eigenvects())
