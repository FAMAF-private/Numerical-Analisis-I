import numpy as np

#Function that calculate sempson's rule
def S(f, a, b):
    return (b-a)/6 * (f(a) + 4*f((a+b)/2) + f(b))

#Function of compound cuadrature
def simpson_cebado(fun, a, b, epsilon):
    c = (a + b) / 2
    q = S(fun, a, b)
    q1 = S(fun, a, c)
    q2 = S(fun, c, b)
    error = np.abs(S(fun, a, b) - S(fun, a, c) - S(fun, c, b))
    if error > 15 * epsilon:
        q1 = simpson_cebado(fun, a, c, epsilon)
        q2 = simpson_cebado(fun, c, b, epsilon)
    return q1 + q2

print(simpson_cebado(lambda x: x * np.e ** (-x ** 2), 0, 1, 1e-10)) #Equal to 1/2 * (1-e**-1)