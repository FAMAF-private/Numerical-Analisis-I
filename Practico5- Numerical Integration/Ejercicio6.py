import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def pendulo(l, alfa):
    ang = alfa * np.pi / 180
    g = 9.8
    T = 4 * (l / g) ** (1/2) * integrate.quad(lambda x: 1/((1 - (np.sin(ang/2) ** 2) * (np.sin(x) ** 2)) ** (1/2)), 0, np.pi / 2)[0]
    return T

print(pendulo(10, 45))

#Here I made a graphic of the period of 90 angles between 0 and 90
''' 
fig, ax = plt.subplots(1, 1)
x = np.linspace(0, 90, 90)
imagenes = []
for i in range(1, 91):
    imagenes.append(pendulo(10, i))
ax.plot(x, imagenes, 'o', label='Periodos')
ax.grid()
ax.legend()
plt.show()
'''

