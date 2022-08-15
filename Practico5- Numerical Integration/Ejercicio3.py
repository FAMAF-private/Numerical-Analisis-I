import numpy as np
import matplotlib.pyplot as plt
from Ejercicio1 import intenumcomp
def coseno(v):
    return np.cos(v)

#Define the function asked in the excercise
def senint(x):
    y = []
    for j in range(len(x)):
        #I use the ceil comand, so the number of sub intervals used in the interval is such that they are smaller than 0.1
        subs = int(np.ceil((x[j]) / 0.1))
        y.append(intenumcomp(coseno, 0, x[j], subs, 'trapecio'))
    return y

x = np.arange(0, 2 * np.pi, 1/2)
fig, ax = plt.subplots(1,1)
ax.plot(x, np.sin(x), label = 'Seno', color = 'green')
ax.plot(x, senint(x), label = 'Senint', color = 'blue')
ax.grid()
plt.legend()
plt.show()
