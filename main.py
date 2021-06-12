import math
from sympy.utilities.lambdify import lambdify
import sympy as sp

def trapezoidMethod(f, a, b, n):
    h = (b-a) / n
    sum = 0
    while a < b:
        sum += 0.5 * ((a + h) - a) * (f(a) + f(a+h))
        a += h
    return sum

def calculatMistake():
    pass


# x = sp.symbols('x')
f = math.sin

print(trapezoidMethod(f, 0, math.pi, 4))


