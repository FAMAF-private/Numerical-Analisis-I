import matplotlib.pyplot as plt
import numpy as np
from Ejercicio1 import intenumcomp

#a, b, c  #Just change the name of the rule and the function as a parameter
n_1 = 10
n_2 = 0
i = 2

#This while will gime me the number of sub intervals needed to reach the mistake tolerance asked
while np.abs(n_1 - n_2) > 10e-5:
    n_1 = intenumcomp(lambda x: x * (np.e ** -x), 0, 1, i, 'trapecio')
    i += 2
    n_2 = intenumcomp(lambda x: x * (np.e ** -x), 0, 1, i, 'trapecio')
    print(i)

print(intenumcomp(lambda x: x * (np.e ** -x), 0, 1, i, 'trapecio'))