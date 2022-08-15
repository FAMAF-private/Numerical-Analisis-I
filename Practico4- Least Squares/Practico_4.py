from datetime import date
from re import I
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

#EJ1
def f(x):
    return a1*x + a0

datos = np.loadtxt('C:/Users/Pedro/Desktop/LMA/Analisis_Numerico_1/Practico4/datos1a.dat.txt')

xs = datos[: , 0]
ys = datos[: , 1]
m = len(xs)
#a
'''
xssq = [x ** 2 for x in xs]
yssq = [y ** 2 for y in ys]
xsys = []

for i in range(len(xs)):
    xsys.append(xs[i] * ys[i])

sumax = sum(xs)
sumay = sum(ys)
sumaxsq = sum(xssq)
sumaxsys = sum(xsys)

a0 = (sumaxsq * sumay - sumaxsys * sumax) / (m * sumaxsq - sumax ** 2)
a1 = (m * sumaxsys - sumax * sumay) / (m * sumaxsq - (sumax) ** 2)

x = np.linspace(0, 5, 500)
fig, ax = plt.subplots(1,1)
ax.plot(xs, ys, 'o', label = 'Datos')
ax.plot(x, f(x), label = 'Aproximacion')
ax.legend()
ax.grid()
plt.show()
'''
#b
'''
xs_sq = np.dot(xs, xs, out = None)
xs_ys = np.dot(xs, ys, out = None)
ones = np.ones(len(xs))
xs_np = np.dot(xs, ones)
ys_np = np.dot(ys, ones)

a0 = (xs_sq * ys_np - xs_ys * xs_np) / (m * xs_sq - xs_np ** 2)
a1 = (m * xs_ys - xs_np * ys_np) / (m * xs_sq - xs_np ** 2)

x = np.linspace(0, 5, 500)
fig, ax = plt.subplots(1, 1)
ax.plot(xs, ys, 'o')
ax.plot(xs, f(xs), label = 'Aproximacion por Cuadrados Minimios')
ax.legend()
ax.grid()
plt.show()
'''
#c
'''
def fun(x):
    return (3/4)*x-1/2

puntos_ord = np.arange(0, 10, 1/2)
x = [fun(x) for x in puntos_ord]
puntos_dis = x + np.random.randn(20)
#polyfit minimiza el error de la aproximacion usando cuadrados minimos(da una lista con la pendiente y la ordenada al origen)
pendiente_origen_polyfit = np.polyfit(puntos_ord, puntos_dis, 1)
#polyval me genera un polinomio de grado 1(por la x que pongo) con los coeficientes que le doy como argumento
pendiente_origen_polyfit = np.polyval(pendiente_origen_polyfit, puntos_ord)

fig, ax = plt.subplots(1, 1)
ax.plot(puntos_ord, x, label='Recta original', color='yellow')
ax.plot(puntos_ord, puntos_dis, 'o', label='Distribucion normal', color='red')
ax.plot(puntos_ord, pendiente_origen_polyfit, label='Aproximacion', color='red')
ax.grid()
plt.legend()
plt.show()
'''
#EJ2

#a
'''
x = np.linspace(0, 1, 50)

yots = [np.arcsin(x) for x in x]

fig, ax = plt.subplots(6 , 1)

for i in range(6):

    pendiente_origen = np.polyfit(x, yots, i)    
    imagen_final = np.polyval(pendiente_origen, x)
    ax[i].plot(x, np.arcsin(x), 'o', label = 'Arcoseno')
    ax[i].plot(x, imagen_final, label = f'Aproximacion de grado {i}')
    ax[i].grid()
    ax[i].legend()
plt.show()
'''
'''
#b

x = np.linspace(0, 4*np.pi, 50)

yots = [np.cos(x) for x in x]

fig, ax = plt.subplots(6, 1)

for i in range(6):

    pendiente_origen = np.polyfit(x, yots, i)    
    imagen_final = np.polyval(pendiente_origen, x)
    ax[i].plot(x, np.cos(x), 'o', label = 'Coseno')
    ax[i].plot(x, imagen_final, label = f'Aproximacion de grado {i}')
    ax[i].grid()
    ax[i].legend()
plt.show()
'''

#Ej3
'''
#Load the data
dats = np.loadtxt('C:/Users/Pedro/Desktop/LMA/Analisis_Numerico_1/Practico4/datos3a.dat.txt')

#Create two variables with each list on the data loaded
odats = dats[0]
oydats = dats[1]

#The best aproximation of the data is an exponential function, so I will take my model from one exponential toa one linear
logxdats = np.log(odats)
logdats = np.log(oydats)

f = np.polyfit(logxdats, logdats, 1)
fig, ax = plt.subplots(1,1)
A = f[0]
C = np.exp(f[1])
ax.plot(odats, oydats, 'o', label='Datos a aproximar')
ax.plot(odats, C * odats ** A)
plt.show()
'''
#b
'''
#Load the data
dats = np.loadtxt('C:/Users/Pedro/Desktop/LMA/Analisis_Numerico_1/Practico4/datos3b.dat.txt')

#Create two variables with each list on the data loaded
xori = dats[0]
yori = dats[1]

#The bes aproximation is of the form y=x/(Ax+B), but I'll take it to a linear
ymod = xori/yori
g = np.polyfit(xori, ymod, 1)

fig, ax = plt.subplots(1, 1)
ax.plot(xori, yori, 'o', label='Datos iniciales', color='green')
ax.plot(xori, xori/(g[0] * xori + g[1]), label='Aproximacion', color='black')
ax.grid()
ax.legend()
plt.show()
'''
#Ej4
#Load and clear the data from the excel
dats = np.loadtxt('C:/Users/Pedro/Desktop/LMA/Analisis_Numerico_1/Practico4/covid_italia.csv',delimiter = ',', dtype = str)

#Get two list, one with the dates an other with de cases each date
dates = dats[:,0].astype(date)
cases = dats[:,1].astype(int)

# I can't make operations with dates, so I plug them a number to make de adjust
x = np.array(range(1, len(dates) + 1))

#One suggested aproximation is exponential, so I'll take de problem to a linear one so I can calculate the coeficients
casestr = np.log(cases)
t = np.polyfit(x, casestr, 1)
a = np.exp(t[1])
b = t[0]
fig, ax = plt.subplots(1,1)
ax.plot(x, cases, 'o')
ax.plot(x, a*(np.exp(b*x)))
plt.show()
#As it's seen, the exponential aproximation is a good one in the first days, but as time pass, wont adjust well to the data
