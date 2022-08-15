from Ejercicio1 import intenumcomp
import numpy as np
def f(c):
    return np.e ** c
def error_de(fun, a, b, N, regla):
    assert (regla == 'pm') or (regla == 'trapecio') or (regla == 'simpson'), 'Por favor intruduzca un metodo de integracion valido'
    error = 0
    sumatoria = 0
    #Cota de derivada segunda de la funcion = e ** 1
    #Cota de derivada cuarta de la funcion = e ** 1
    if regla == 'pm':
       
        h = (b - a) / (N + 2)
        error = ((b - a) / 2) * (h ** 2) * np.exp(0)

    elif regla == 'trapecio':
        h = (b - a) / N
        error = ((b - a) / 12) * h ** 2 * np.exp(0)
    
    elif regla == 'simpson':
        h = (b - a) / N
        error = ((h ** 5) / 90) * np.exp(0)

    return np.abs(error)
'''
print(error_de(f, 0, 1, 20, 'simpson'))
print(error_de(f, 0, 1, 20, 'trapecio'))
print(error_de(f, 0, 1, 20, 'pm'))
'''