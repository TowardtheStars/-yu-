from sympy import *

L1 = Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]])

L2 = Matrix([[0, -I, 0], [I, 0, 0], [0, 0, 0]])

L3 = Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]])

L4 = Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]])

L5 = Matrix([[0, 0, -I], [0, 0, 0], [I, 0, 0]])

L6 = Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]])

L7 = Matrix([[0, 0, 0], [0, 0, -I], [0, I, 0]])

L8 = 1/sqrt(3)*Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -2]])

L = [L1, L2, L3, L4, L5, L6, L7, L8]

g = [L1/2, L2/2, L3/2, L4/2, L5/2, L6/2, L7/2, L8/2]



for i in range(0, 8):
    rst = Matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    for j in range(0, 8):
        temp=L[j]*L[i]*L[j]
        print(temp)
        rst+=temp
    print('\n')
    print(L[i])
    print(rst)
    print('##################\n')

rst = Matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
for i in range(0, 8):
    temp=L[i]*L[i]
    print(temp)
    rst+=temp
print('\n')
print(rst)
print('##################\n')

for i in range(0, 8):
    print(latex(L[i]))


