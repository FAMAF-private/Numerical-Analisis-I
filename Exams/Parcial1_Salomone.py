import math
import matplotlib.pyplot as plt
import numpy as np

#Las ejecuciones de los ejercicios estan al final del codigo.

#EJ1
def serie_seno(x):
    #Variable donde se guardara el valor que estoy aproximando
    valor = 0

    #For que se repetira 5 veces y le dara valores a n 0, 1, 2, 3, 4
    for n in range(5):

        #Calculo el polinomio n-esimo de taylor de la funcion seno
        polinomio_grado_n = (((-1) ** (n))/math.factorial(2 * n + 1)) * (x ** (2 * n + 1))

        #Actualizo el valor de la aproximacion
        valor += polinomio_grado_n

    #Devuelvo el valor aproximado de sin(x)
    return valor


#EJ2
#Defino que mi eje x ira de 0 a 6.4
#Como quiero graficar con puntos a una distancia de 0.01, debo graficar 640 puntos en total
def puntos_x_y():
    hx = []
    hy = []
    x = 0
    for i in range(640):
        hx.append(x)
        x = x + 0.01
        hy.append(serie_seno(x))
    return hx, hy

x = puntos_x_y()[0]
y = puntos_x_y()[1]

fig, ax = plt.subplots()
ax.plot(x, y, label = 'Seno')
ax.plot(x, np.sin(x), label = 'SenoReal')
ax.set(xlabel = 'Eje X')
ax.set_ylabel('Eje Y')
ax.set_title('Grafico de aproximacion por Taylor de Seno')
ax.legend()

#EJ3
def rbisec(fun, I, err, mit):
    a = I[0]
    b = I[1]
    valoresC = []
    evaluacionesC = []

    if fun(a)*fun(b) < 0:
        for _ in range(mit):
            c = (a+b)/2
            if abs(fun(b) - fun(a)) < err:
                break
            evaluacionesC.append(fun(c))
            valoresC.append(c)
            if fun(c) * fun(a) < 0:
                b = c
            elif fun(c) * fun(b) < 0:
                a = c
            else:
                 return'None1'
           
    else:
        return None
    return valoresC, evaluacionesC

#EJ4
def rsteffensen(fun, x0, err, mit):
    hx = [x0]
    hf = [fun(x0)]
    x_1 = x0

    for k in range(mit):
        x = fun(x_1)
        xk = x_1 - (x ** 2) / (fun(x_1 + x) - x)
        hx.append(xk)
        hf.append(fun(x_1))
        if abs(fun(xk)) < err:
            break
        x_1 = xk

    return hx, hf

'''                         --EJECUCIONES--                         '''
#Para ejecutar ejercicios 1, 3, 4, 5 descomentar sus respectivos prints.
#En ejercicio 2 descomentar linea que dice plt.show.

#Ejercicio 1
#print((serie_seno(math.pi/4)))
#Se obtendra una aproximacion de seno de pi/4. (2 ** (1/2))/2

#Ejercicio 2
plt.show()
#El grafico muestra que la suma de taylor aproxima a la funcion seno cerca de 0. 

#Ejercicio 3
#Viendo el grafico, identifico que una raiz esta en el intervalo (0, 4] y la otra en [4, 6.4]
I_1 = [0.01, 4]
I_2 = [4, 6]
#print(rbisec(serie_seno, I_1, 1e-5, 100)[0][-1]) # Pi
#print(rbisec(serie_seno, I_2, 1e-5, 100)[0][-1]) # 2*Pi (No es preciso porque estamos lejos del 0)
#La raiz es el ultimo elemento de la primer lista del output.

#Ejercicio 4
#print(rsteffensen(serie_seno, 2, 1e-5, 100))
#Devuelve la raiz cerca de la aproximacion inicial 2.

#Ejercicio 5
#print(f'La raiz cercana a 3 es {rsteffensen(serie_seno, 3, 1e-5, 100)[0][-1]}. Fueron necesarias {len(rsteffensen(serie_seno, 3, 1e-5, 100)) - 1} iteraciones para encontrarla.')
#print(f'La raiz cercana a 6 es {rsteffensen(serie_seno, 6, 1e-5, 100)[0][-1]}. Fueron necesarias {len(rsteffensen(serie_seno, 6, 1e-5, 100)) - 1} iteraciones para encontrarla.')
#print(f'La raiz cercana a 4.5 es {rsteffensen(serie_seno, 4.5, 1e-5, 100)[0][-1]}. Fueron necesarias {len(rsteffensen(serie_seno, 4.5, 1e-5, 100)) - 1} iteraciones para encontrarla.')
#Cuando utilizo como aproximacion inicial el 4.5, el metodo no funciona
