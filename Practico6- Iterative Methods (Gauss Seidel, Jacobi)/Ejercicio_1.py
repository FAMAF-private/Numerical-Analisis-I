import numpy as np
def soltrinf(A, b):
    assert np.prod(np.diag(A)) != 0,"Error: la matriz es singular"

    X = []   
    for n in range(len(b)):
        sumatoria = 0
        for j in range(n):
            sumatoria += A[n][j] * X[j]
        X.append((1 / A[n][n]) * (b[n] - sumatoria))

    return X

def soltrsup(A, b):
    assert np.prod(np.diag(A)) != 0,"Error: la matriz es singular"

    n = len(b) - 1
    X = [b[n] / A[n][n]]   

    for i in range(n - 1, -1, -1):
        con = 0
        sumatoria = 0
        for j in range(n , i, -1):
            sumatoria += A[i][j] * X[con]
            con += 1
        X.append((1 / A[i][i]) * (b[i] - sumatoria))
    X.reverse()

    return X
 
c = np.array([[1,3,2], [0,1,-15], [0,0,1]])
'''
print(c)
print(soltrsup(c, [11, -13, 1]))
'''