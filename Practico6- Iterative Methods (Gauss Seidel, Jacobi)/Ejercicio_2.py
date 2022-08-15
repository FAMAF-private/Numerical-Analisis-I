import numpy as np
import math
from Ejercicio_1 import soltrsup

#a
def egauss(A, b):
    n = len(A) - 1

    for i in range(n):
        B = A.copy()
        for j in range(i , n):

            A[j + 1] = A[j + 1] - A[i] * (A[j + 1][i] / A[i][i])
            b[j + 1] = b[j + 1] - b[i] * (B[j + 1][i] / B[i][i])
        
    return A, b
                
A = np.array([
    [1, 2, 0], 
    [0, 3, 1], 
    [1, 2, 5]
])
#print(egauss(A, [0,0,0]))

#b 
def soleg(A, b):
    R, k = egauss(A, b)
    return soltrsup(R, k)

print(soleg(A, [11,17,21]))

