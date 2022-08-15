import numpy as np
from Ejercicio5 import jacobi, gauss_seidel

#(1)

A1 = np.array([[3,1,1], [2,6,1], [1,1,4]])
b1 = np.array([5, 9, 6])

print(f'Jacobi: {jacobi(A1, b1, 1e-11, 100)}')
print(f'Gauss-Seidel: {gauss_seidel(A1, b1, 1e-11, 100)}')

#(2)

A2 = np.array([[2,7,6,5], [7,10,8,7], [6,8,10,9],[5,7,9,10]])
b2 = np.array([23,32,33,31])

print(f'Jacobi: {jacobi(A2, b2, 1e-4, 100)}')
print(f'Gauss-Seidel: {gauss_seidel(A2, b2, 1e-4, 100)}')