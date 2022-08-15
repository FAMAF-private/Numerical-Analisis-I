import numpy as np

A = np.array([
    [1, 2, -2],
    [1, 1, 1],
    [2, 2, 1]
])
b = np.array([7, 2, 5])

def jacobi(A,b,err,mit):
    M = np.diag(np.diag(A))
    N = M - A
    Minv = np.diag(1/np.diag(M))
    x0 = np.zeros(b.shape)

    for k in range(mit):
        x1 = Minv @ ( N @ x0 + b)

        if np.linalg.norm(x1-x0, ord=np.inf) < err:
            break
        else:
            x0 = x1.copy()

    return [x1,k]

def gauss_seidel(A,b,err,mit):
    M = np.tril(A)
    N = M - A
    Minv = np.linalg.inv(M)
    x0 = np.zeros(b.shape)

    for k in range(mit):
        x1 = Minv @ ( N @ x0 + b)

        if np.linalg.norm(x1-x0, ord=np.inf) < err:
            break
        else:
            x0 = x1.copy()

    return [x1,k]

print(gauss_seidel(A, b, 1e-6, 100))