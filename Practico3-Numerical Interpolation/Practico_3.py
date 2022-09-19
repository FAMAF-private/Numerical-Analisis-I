import numpy as np
import matplotlib.pyplot as plt
from math import cos, pi
from scipy.interpolate import interp1d

#Ej 1
def ilagrange(x, y, z):
    assert len(x) == len(y), 'x e y deben tener la misma cantidad de elementos'
    n = len(x)
    #En esta lista se agregaran los polinomios de newton evaluados en los valores de z.
    valores = []
    #Este for agrega un elemento a la lista anterior por cada vez que se repita.
    for p in range (len(z)):
        valor = 0
        #Este for construye el polinomio de newton y lo evalua.
        for i in range(n):
            li = 1
            for j in range(n):
                if j != i:
                    li = li * (z[p] - x[j]) / (x[i] - x[j])
            valor += y[i] * li
        valores.append(valor)
    return valores

#print(ilagrange([2, 5/2, 4], [1/2, 2/5, 1/4], [1, 2, 3]))
#w = (ilagrange([0, 1, 2], [0, 1, 4], [5, 6, 7]))
#print(ilagrange([0, 1, 2, 3], [0, 1, 8, 27], [5, 6, 7]))

#Ej 2
def inewton(x, y, z):
    assert len(x) == len(y), 'x e y deben tener la misma cantidad de elementos'
    #Esta lista de listas tendra una lista por columna de la tabla de diferencias divididas.
    Coeficientes = [x, y]
    n = len(x)
    #Este for agregara una columna a la tabla de diferencias por cada vez que se ejecute.
    for j in range(n - 1):
        Coeficientes.append([])
        p = len(Coeficientes[j + 1]) - 1
        #Este for completara la columna de la tabla de diferencias divididas.
        for i in range(p):
            fx = (Coeficientes[j + 1][i + 1] - Coeficientes[j + 1][i]) / (Coeficientes[0][i + j + 1] - Coeficientes[0][i])
            Coeficientes[j + 2].append(fx)

    #En esta lista se agregaran los polinomios de newton evaluados en los valores de z.
    Valores = []
    #Este for agrega un elemento a la lista anterior por cada vez que se repita.
    for u in range(len(z)):
        polinomio = 0
        #Este for construye el polinomio de newton.
        for i in range(1, len(x) + 1):
            if i == 1:
                polinomio += Coeficientes[i][0]
            else:
                productoria = 1
                for r in range(i - 1):
                    productoria = productoria * (z[u] - Coeficientes[0][r])
                polinomio += Coeficientes[i][0] * productoria
        Valores.append(polinomio) 
    #Devuelvo los polinomios de Newton evaluados en los valores de z.
    return Valores

#print(inewton([2, 5/2, 4], [1/2, 2/5, 1/4], [1, 2, 3]))
#u = (inewton([0, 1, 2, 3, 4], [0, 1/11, 8/12, 27/13, 64/14], x))
#print(inewton([0, 1, 2, 3], [0, 1, 8, 27], [5, 6, 7]))

#Ej3
'''
puntos = []
#Agrego los puntos que evaluare el polinomio de newton a la lista 'puntos'.
for j in range(1, 102):
    z = (24/25) + (j/25)
    puntos.append(z)

#Creo una lista donde guardare todos los puntos interpolados.
w = inewton([1, 2, 3, 4, 5], [1, 1/2, 1/3, 1/4, 1/5], puntos)

x2 = np.array(puntos)
x = np.linspace(1, 5, 101)
x3 = np.array([1, 2, 3, 4, 5])

fig, ax = plt.subplots()
ax.plot(puntos, w, label = 'Polinomio interpolante')
#En este plot se puede usar tanto la lista x como la lista puntos(x2)
ax.plot(x, 1/x, label = 'Funcion f')
ax.plot(x3, 1/x3, '*', label = 'Puntos de interpolacion')

ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_title('Ejercicio 3')

plt.legend()
plt.show()
'''
#Ej4
'''
x = np.linspace(-1, 1, 200) 
n = 0
fig, ax = plt.subplots(3, 5)
for idx in range(3):
    for idy in range(5):
        n += 1
        N = []
        Y = []
        M = []
        A = []

        #Este for genera las listas que tendran los xi, yi para que interpole pn
        for i in range(1, n + 2):
            p = ((2*(i-1))/n) - 1
            N.append(p)
            Y.append(1/(1 + 25*(p)**2))

        #Hago una lista con todas las interpolaciones de los puntos de x, interpolando los puntos generados por el for anterior
        w = ilagrange(N, Y, x)

        #Este for genera las listas que tendran los xi, yi para que interpole pq
        for i in range(n + 1):
            p = cos(pi*(2*i + 1) / (2*n + 2))
            M.append(p)
            A.append(1/(1 + 25*(p)**2))

        #Hago una lista con todas las interpolaciones de los puntos de x, interpolando los puntos generados por el for anterior
        u = ilagrange(M, A, x)

        ax[idx][idy].plot(x, w, label = 'Ej4a')
        ax[idx][idy].plot(x, u, label = 'Ej4b')
        ax[idx][idy].plot(x, 1/(1 + 25*x**2), label = 'Fun 1/25*x**2')
        ax[idx][idy].set_title(f'n = {n}')

plt.legend()
plt.show()
'''
#EJ5
'''
#Load the data
datos = np.loadtxt("C:/Users/Pedro/Desktop/LMA/Analisis_Numerico_1/Prectico3/datos_aeroCBA.dat.txt")

#Set two variables with the first and second columns of the matrix loaded
anos = datos[: , 0]
temperaturas = datos[: , 1]

#Clean the lists of years and temperatures taking out the elements that are not a number
notAnumber = ~ np.isnan(temperaturas)
anos_interpol = anos[notAnumber]
temps_interpol = temperaturas[notAnumber]

#This code will generate three diferent graphics, each one of a different kind of spline
anos_plot = np.linspace(1957, 2018, 2000)
fig, ax = plt.subplots(3, 1)
u = ['slinear' , 'quadratic', 'cubic']
for idx in range(3):

    pol = interp1d(anos_interpol, temps_interpol, kind = u[idx], fill_value = 'extrapolate')
    temperaturas_plot = pol(anos_plot)
    ax[idx].plot(anos_plot, temperaturas_plot, label = u[idx])
    ax[idx].plot(anos_interpol, temps_interpol, 'o')
    ax[idx].legend()
    ax[idx].grid()


plt.show()
'''

#Ej6
'''
#Create the lists of values
xi = [-3, -2, -1, 0, 1, 2, 3]
yi = [1, 2, 5, 10, 5, 2, 1]

#This code will give two interpolations(Lagrange and Newton) an a cubic spline of the values
puntos = np.linspace(-3, 3, 200)
w = ilagrange(xi, yi, puntos)
u = inewton(xi, yi, puntos)
ynew = interp1d(xi, yi, kind = 'cubic')(puntos)

#Plot them into a graphic
fig, ax = plt.subplots()
ax.plot(puntos, w, label = 'Lagrange')
ax.plot(puntos, u, label = 'Newton')
ax.plot(puntos, ynew, label = 'interp1d')
ax.plot(xi, yi, 'o')

plt.legend()
plt.show()
'''

#EJ7
def rinterp(fun, x0, x1, x2, err, mit):
    xn = [x0, x1, x2]
    fxn = [fun(x0), fun(x1), fun(x2)]
    x = np.linspace(-50, 50, 20000)
    poli = inewton(xn, fxn, x)
    lista = [xn[0], fun(xn[0])]
    for i in range(3):
        if abs(lista[1]) > abs(fxn[i]):
            lista = [xn[i], fxn[i]]
