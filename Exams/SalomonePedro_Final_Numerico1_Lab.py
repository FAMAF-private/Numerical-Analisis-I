import numpy as np
import matplotlib.pyplot as plt
from math import e

def funEja(x):
    return 1/x

def integral_simpson(b):

    #El extremo menor de mi intervalo sera 1
    a = 1

    #Defino el numero de subintervalos
    N = 100

    #Defino la longitud de cada subintervalo
    h = (b - a) / N

    #Creo los nodos x_j
    nodos = np.linspace(a, b, N + 1)

    sumatoria = 0
    sumatoria_2 = 0

    for j in range(1, int(N/2)):
        sumatoria_2 += funEja(nodos[2*j])
    for j in range(1, int(N/2) + 1):
        sumatoria += funEja(nodos[2*j - 1])

    S = (h / 3) * (funEja(a) + 2 * sumatoria_2 + 4 * sumatoria + funEja(b))

    return S

#b
#La integral dada es igual a ln(x), por lo que tengo que encontrar un x tal que ln(x) = 1, por lo que debo resolver
#la ecucacion ln(x) - 1 = 0. No usare el metodo de newton ni el de punto fijo para no tener problemas con la convergencia
#del punto inicial. En cambio, no tendre problema con el metodo de biseccion ya que usare el intervalo [1,8], por lo que
#ln(1) - 1 < 0 y ln(8) - 1 > 0. Como la funcion es continua entonces el metodo convergera a la raiz en [1,8].

def funEjb(x):
    return np.log(x) - 1

def rbisec(fun, I, err, mit):
    a = I[0]
    b = I[1]
    valoresC = []
    evaluacionesC = []

    if fun(a)*fun(b) < 0:
        for _ in range(mit):
            c = (a+b)/2
            if abs(fun(c)) < err:
                break
            #Aca sumo 1 a cada valor que se agrega en evaluacionesC para que cuando plotee los puntos estos esten sobre ln(x) y no ln(x) - 1
            evaluacionesC.append(fun(c) + 1)
            valoresC.append(c)
            if fun(c) * fun(a) < 0:
                b = c
            elif fun(c) * fun(b) < 0:
                a = c
            else:
                 return'None1'
    return valoresC, evaluacionesC

I = [1, 8]
busqueda = rbisec(funEjb, I, 1e-6, 100)

print(f'El valor aproximado de e es: {busqueda[0][-1]}')

#c

print(f'El error absoluto de la aproximacion dada por integral_simpson es: {e - busqueda[0][-1]}')

fig, ax = plt.subplots(1,1)
r = np.linspace(1, 8, 1000)
ax.plot(r, integral_simpson(r), color = 'blue', label = 'ln(x)')
ax.plot(busqueda[0], busqueda[1], 'o', color = 'green', label = 'Aproximaciones de ln(e)')
ax.plot(busqueda[0][-1], integral_simpson(busqueda[0][-1]), 'o', color = 'purple', label = 'Aproximacion ln(e)')
ax.grid()
ax.legend()
plt.xlim([1,8])
plt.ylim([0,2.2])
plt.show()