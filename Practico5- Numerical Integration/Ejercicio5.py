from scipy import integrate
from numpy import inf, e, log

Integral1 = integrate.quad(lambda x: e**(-x**(2)), -inf, inf)
Integral2 = integrate.quad(lambda x: x ** 2 * log(x + (x**2 + 1)**(1/2)), 0, 2)

print(Integral1)
print(Integral2)