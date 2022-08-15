
from cmath import pi
import matplotlib.pyplot as plt
from math import exp, fabs, cos, tan, atan
import numpy as np

I = [0, 2]

def rbisec(fun, I, err, mit):
    a = I[0]
    b = I[1]
    valoresC = []
    evaluacionesC = []


    if fun(a)*fun(b) < 0:
        for _ in range(mit):
            c = (a+b)/2
            if abs(fun(c)) < err:
                print(f'El valor {c} es raiz')
                break
            evaluacionesC.append(fun(c))
            valoresC.append(c)
            if fun(c) * fun(a) < 0:
                b = c
            elif fun(c) * fun(b) < 0:
                a = c
            else:
                 return'None1'
    return valoresC, evaluacionesC

 

def fun2a(x):
    return atan(2*x)
#print(rbisec(fun2a, [0.8, 1.4], 1e-6, 100))

def funEj2b(x):
    return x**2 - 3 

#print(rbisec(funEj2b, [0, 2], 1e-6, 100))

def fun_ej3(x):
    t = []
    t.append((x**6)-5*x)
    t.append(6*(x**5) - 5)
    return t

'''
x = np.linspace(0, 2, 120)
fig, ax = plt.subplots()
ax.plot(valoresC, evaluacionesC, '*', label = 'Aproximaciones')
ax.plot(x, (x**2- 3), label = 'Funcion f')
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_title('Ejercicio 2C')
plt.legend
plt.show()
return valoresC, evaluacionesC
'''

#3
def rnewton(fun, x0, err, mit):
    hx = []
    hf = []
    x_1 = x0

    for k in range(0, mit):
        x, xprim = fun(x_1)
        xk = x_1 - x/xprim
        hx += [xk]
        hf += [fun(x_1)[0]]
        if fabs(xk-x_1)/fabs(xk) < err or fabs(fun(xk)[0]) < err:
            break
        x_1 = xk

    #print(hx)
    return (hx, hf)

#print(rnewton(fun_ej3, 20, 10**-5, 100))
#4
def fun_ej4(x, a):
    t = []
    t.append((x**3) - a)
    t.append(3*(x**2))
    return t

def rNewton4(fun, x0, err, mit, a):
    hx = [x0]
    hf = [fun(x0, a)[0]]
    Xn = x0
    for k in range(mit):
        Xn = Xn - (fun(Xn, a)[0]/fun(Xn, a)[1])
        hx.append(Xn)
        hf.append(fun(Xn, a)[0])
        if fun(Xn, a)[0] < err:
            break
        elif (abs(Xn - hx[k])/abs(Xn)) < err:
            break
    return hx, hf, f'La raiz es {hx[-1]}'

#print(rNewton4(fun_ej4, 200, 10**-5, 100, 10))

#5
def fun_Ej5(x):
    return (x**2) - 2 

def ripf(fun, x0, err, mit):
    i = 0
    p0 = x0
    hx = [p0]
    while i < mit:
        Pn = fun(p0)
        hx.append(Pn)
        if fabs(Pn - p0) < err:
            break
        i = i + 1
        p0 = Pn
    return hx, f'El punto fijo esta en {hx[-1]}'

#print(ripf(fun_Ej5, 0, 10**-5, 100))
#Para algunas funciones da error de overflow y para otras no se corta la ejecucion

#6
def fun_Ej6(x):
    return 2**(x-1)
#print(ripf(fun_Ej6, 0, 10**-5, 100))

#7
'''
def fun_Ej7Biseccion(x):
    def ec(y):
        return y - exp(-(1-x*y)**2)
    _ , hy = rbisec(ec, [0, 2], 10**-5, 100)
    return _[-1]

print(fun_Ej7Biseccion(1.5))


def fun_Ej7Newton(x):
    def ec(y):
        return y - exp(-(1-x*y)**2)
    def ecd(y):
        return 1 - exp(-(1-x*y)**2)*((-2)*(x**2)*y+2*x)
    def f(y):
        return(ec(x), ecd(x))
    hy, _ = rnewton(f, 0.5, 10**-5, 100)
    return _[-1]

print(fun_Ej7Newton(1.5))

def fun_Ej7pf(x):
   # funcion de la que buscar una raiz
    def ec(y): 
        return exp(-((1-x*y)**2))

    # Al despejar la ecuacion y = e**(-(1-xy)**2),
    # Obtenemos ln y = -((1-xy)**2), osea que ln y<0
    # Por lo tanto y esta entre 0 y 1.
    # Uso entonces y0 = 0.5

    hy = ripf(ec, 0.5, 1e-5, 100)
    return hy[-1]

print(fun_Ej7pf(1.5))

'''
def Ej_8():
    def derivada(x):
        return (x+x*tan(x)**2-2*tan(x))/x**3
    def derivadafea(x):
        return 2*(x**2*(1/cos(x))**2 * tan(x)-2*x*(1/cos(x))**2+3*tan(x))/x**4
        
    def fun_Ej8(x):
        return (derivada(x), derivadafea(x))
    return(rnewton(fun_Ej8, pi/10, 1e-12, 100))

#print(Ej_8())

def fun_Ej9(x):
    return (x**2)*(39.35)-500

def deri_Ej9(x):
    return 2*x*(39.35)

def Funn(x):
    return (fun_Ej9(x), deri_Ej9(x))
hx , _ = rnewton(Funn, 50, 1e-5, 100)
#print(hx[-1])

'''def rsecante(fun, x0, x1, err, mit):
    assert(x0 < x1), 'x1 debe ser mayor que x0'
    hx = [x0, x1]
    hf = [fun(x0), fun(x1)]
    for k in range(1, mit):
        x_n_minus1 = hx[-2]
        x_n = hx[-1]
        fx_n = hf[-1]
        fx_nminus1 = hf[-2]

        x_n_plus1 = x_n - hf[-1]*((x_n / x_n_minus1)/(fx_n - fx_nminus1))

        hx.append(x_n_plus1)
        hf.append(fun(x_n_plus1))
        
        if fabs(x_n_plus1 - x_n) < err or fabs(fun(x_n_plus1)) < err:
            break
    
    return hx[-1]'''
        
def fun_paraSecante(x):
    return x**2 - 3

def rsecante(fun, xn, xn_minus1, err):
    assert(xn < xn_minus1), 'x1 debe ser mayor que x0'

    error = 1e4
    xn_plus1 = 0
    while error > err:
        x_nplus1 = xn - fun(xn) * (xn - xn_minus1) / (fun(xn) - fun(xn_minus1))
        xn = xn_minus1
        xn_minus1 = xn_plus1
        error = fun(xn_plus1)
    return xn_plus1
#print(rsecante(fun_paraSecante, 3, 4, 1e-5))
