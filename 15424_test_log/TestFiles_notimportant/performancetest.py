import sympy as sy

symbols = sy.symbols('a[0:20]')
print sy.ccode(sy.Min(*symbols))