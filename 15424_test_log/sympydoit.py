from sympy import pprint, symbols, Integral, sin, pi

x = symbols('x')
Integral(abs(sin(x)), (x, 0, 7 * pi)).doit()
