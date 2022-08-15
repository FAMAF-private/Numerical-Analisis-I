#Luego de el codigo de cada ejercicio esta la ejecucion comentada debajo del comentario #EJECUCION.
#Descomentar para ejecutar.

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

#Importo la funcion del polinomio de Lagrange del practico 3
def ilagrange(x, y, z):
    assert len(x) == len(y), 'x e y deben tener la misma cantidad de elementos'
    n = len(x)
    #En esta lista se agregaran los polinomios de lagrange evaluados en los valores de z.
    valores = []
    #Este for agrega un elemento a la lista anterior por cada vez que se repita.
    for p in range (len(z)):
        valor = 0
        #Este for construye el polinomio de lagrange y lo evalua.
        for i in range(n):
            li = 1
            for j in range(n):
                if j != i:
                    li = li * (z[p] - x[j]) / (x[i] - x[j])
            valor += y[i] * li
        valores.append(valor)
    return valores

#1

#Cargo los datos del archivo excel
tabla = np.loadtxt('C:\\Users\\Pedro\\Desktop\\LMA\\Analisis_Numerico_1\\ParcialLab2\\irma.csv',delimiter = ',')

#Guardo en distintas listas los datos que me dan en cada columna del excel
hora = tabla[:, 0]
longitud = tabla[:, 1]
latitud = tabla[:, 2]

#a
#EJECUCION Ejercico 1a.
'''
fig, ax = plt.subplots(1, 1)
ax.plot(longitud, latitud, 'o', label='Datos',color='purple')
ax.set_xlabel('Longitud')
ax.set_ylabel('Latitud')
ax.legend()
plt.show()
'''
#b

#Creo una lista con linspace con cada hora del dia, para luego evaluar el polinomio interpolante y el spline en estos puntos
HorasDia = np.linspace(0, 24, 25)

#Creo listas con los valores que toma la aproximacion por Lagrange en cada hora del dia
PolLong = ilagrange(hora, longitud, HorasDia)
PolLat = ilagrange(hora, latitud, HorasDia)

#Creo listas con los valores que toma la aproximacion por Spline en cada hora del dia
splineLong = interp1d(hora, longitud, kind='cubic')
CubicLong = splineLong(HorasDia)
splineLat = interp1d(hora, latitud, kind='cubic')
CubicLat = splineLat(HorasDia)

#EJECUCION Ejercicio 1b.
'''
#Hare dos graficos, uno para Longitud(t) y otro para Latitud(t)
fig, ax= plt.subplots(2,1)

#Ploteo las aproximaciones por Lagrange en cada grafico
ax[0].plot(HorasDia, PolLong,'o', label='Aproximacion lagrange', color='purple')
ax[1].plot(HorasDia, PolLat,'o', label='Aproximacion lagrange', color='purple')

#Ploteo las aproximaciones por Spline en cada grafico
ax[0].plot(HorasDia, CubicLong,'*', label='Aproximacion spline', color='yellow')
ax[1].plot(HorasDia, CubicLat,'*', label='Aproximacion spline', color='yellow')

#Ploteo los datos medidos cada 3 horas dados en el excel
ax[0].plot(hora, longitud,'o', label='Datos c/ 3 horas', color='green')
ax[1].plot(hora, latitud,'o', label='Datos c/ 3 horas', color='green')

#Agrego estetica a los graficos
fig.patch.set_facecolor('xkcd:grey')
ax[0].set_facecolor('xkcd:grey')
ax[1].set_facecolor('xkcd:grey')
ax[0].set_xlabel('Hora del dia')
ax[1].set_xlabel('Hora del dia')
ax[0].set_ylabel('Longitud')
ax[1].set_ylabel('Latitud')
ax[0].legend()
ax[1].legend()

plt.show()
'''
#2

#Escribo la tabla dada de datos
xis = [0, 1.5, 2, 2.9, 4, 5.6, 6, 7.1, 8.05, 9.2, 10, 11.3, 12]
yis = [0.1, 0.2, 1, 0.56, 1.5, 2.0, 2.3, 1.3, 0.8, 0.6, 0.4, 0.3, 0.2]

#a
#EJECUCION Ejercicio 2a.
'''
#Grafico los puntos dados
fig, ax = plt.subplots(1,1)
ax.plot(xis, yis, 'o', label='Mediciones dadas',color='brown')
ax.set_xlabel('Largo del terreno')
ax.set_ylabel('Altura de tierra')
ax.legend()
plt.show()
'''
#b

#Defino la funcion para que reciba como argumentos dos listas, X con las mediciones del eje de x, Y con las imagenes de 
# cada punto dado en la lista X 
def trapecio_adaptativo(X, Y):
    #En S ire guardando el valor de la integral en cada tramo.
    S = 0
    N = len(X)
    #Este for realiza la regla del trapecio simple en cada intervalo dado por los datos de la lista X y suma esos valores
    # a la variable S
    for i in range(1, N):
        S += ((X[i] - X[i - 1]) / 2) * (Y[i - 1] + Y[i])
    return S

#c
#EJECUCION Ejercicio 2c.
#Multiplico el valor de la integral por la profundidad del terreno para obtener el volumen de tierra.
#print(trapecio_adaptativo(xis, yis) * 10)

