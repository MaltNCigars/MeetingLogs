import sympy as sy
symbols = sy.symbols('a[0:50]')
sy.ccode(sy.Min(*symbols))
