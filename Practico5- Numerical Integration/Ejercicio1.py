import numpy as np
def f(c):
    return c ** 2

def intenumcomp(fun, a, b, N, regla):
    assert regla == 'pm' or regla == 'trapecio' or regla == 'simpson', 'Por favor intruduzca un metodo de integracion valido'
    #Este if es para que en el ejercicio 3 pueda graficar en xi = 0
    if a == b:
        return 0 
    S = 0
    sumatoria = 0

    if regla == 'pm':
        h = (b - a) / (N + 2)
        nodos = []
        for j in range(-1, N + 2):
            nodos.append(a + (j + 1) * h)
        for i in range (int(N/2) + 1):
            sumatoria += fun(nodos[2 * i])
        S = 2 * h * sumatoria

    elif regla == 'trapecio':
        h = (b - a) / N
        nodos = np.linspace(a, b, N + 1)
        for i in range(1, N):
            sumatoria += fun(nodos[i])
        S = (h / 2) * (fun(a) + 2 * sumatoria + fun(b))
    
    else:
        h = (b - a) / N
        nodos = np.linspace(a, b, N + 1)
        sumatoria_2 = 0
        for j in range(1, int(N/2)):
            sumatoria_2 += fun(nodos[2*j])
        for j in range(1, int(N/2) + 1):
            sumatoria += fun(nodos[2*j - 1])
        S = (h / 3) * (fun(a) + 2 * sumatoria_2 + 4 * sumatoria + fun(b))

    return S
'''
print(intenumcomp(f, -1, 1, 10, 'pm'))
print(intenumcomp(f, -1, 1, 10, 'trapecio'))
print(intenumcomp(f, -1, 1, 10, 'simpson'))
'''