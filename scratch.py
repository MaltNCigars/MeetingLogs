from sympy import *


# This was the initial test for the noncommutative simplification issue.
#a,b = symbols('a b', commutative=False)
#c = exp(a)*exp(b) - exp(b)*exp(a)
#print(c)
#print(c.simplify())
#print(exptrigsimp(c))
#print(exptrigsimp(exp(a)*exp(b)))
##For comarison, here is the test code for the issue that's headed for sympy:
##a,b = symbols('a b', commutative=False)
##x = Symbol('x', commutative=True)
##assert exp(a + x) == exptrigsimp(exp(a)*exp(x))
##p = exp(a)*exp(b) - exp(b)*exp(a)
##assert p == exptrigsimp(p) != 0


#MatrixSymbol simplification problem. It seems unsuitable for working on now.
#A = MatrixSymbol('A', 2, 2)
#B = MatrixSymbol('B', 2, 2)
#C = exp(A)*exp(B) - exp(B)*exp(A)
#print(C)
#print(C.simplify())
#print()


#Some weird issue with substitution of matrices into exponentials.
#m = Matrix([[0,1],[1,0]])
#n = Matrix([[0,1],[-1,0]])
#print(repr(exp(m)*exp(n)))
#print(repr((exp(A)*exp(B)).subs({A:m, B:n})))
#print()
#print(repr(exp(n)*exp(m)))
#print(repr((exp(B)*exp(A)).subs({A:m, B:n})))
#print()


#Some limit issue.
#x = Symbol('x')
#expr = sin(x**-0.5) ** -2 - x
#pow = -1 / sympify(2)
#expr2 = sin(x**pow) ** -2 - x
#print()
#print()
#print(expr)
#print(limit(expr, x, oo))
#print(limit(expr2, x, oo))
#print(expr.subs(x,10000))

