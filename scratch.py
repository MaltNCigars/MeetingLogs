from sympy import *

A = MatrixSymbol('A', 2, 2)
B = MatrixSymbol('B', 2, 2)
C = exp(A)*exp(B) - exp(B)*exp(A)
print(C)
try:
  print(C.simplify())
except:
  print("simplification error")
print()

m = Matrix([[0,1],[1,0]])
n = Matrix([[0,1],[-1,0]])
print(repr(exp(m)*exp(n)))
print(repr((exp(A)*exp(B)).subs({A:m, B:n})))
print()
print(repr(exp(n)*exp(m)))
print(repr((exp(B)*exp(A)).subs({A:m, B:n})))
print()


a,b = symbols('a b', commutative=False)
c = exp(a)*exp(b) - exp(b)*exp(a)
print(c)
print(c.simplify())
print(exptrigsimp(c))
print(exptrigsimp(exp(a)*exp(b))) #See line 547 of sympy/simplify/trigsimp.py


x = Symbol('x')
expr = sin(x**-0.5) ** -2 - x
pow = -1 / sympify(2)
expr2 = sin(x**pow) ** -2 - x
print()
print()
print(expr)
print(limit(expr, x, oo))
print(limit(expr2, x, oo))
print(expr.subs(x,10000))

