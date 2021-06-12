import math
from sympy.utilities.lambdify import lambdify
import sympy as sp


def calcDerivative(func):
    """
    :param func: original function
    :return: None
    """
    x = sp.symbols('x')
    f_prime = func.diff(x)
    return f_prime


def trapezoidMethod(f, a, b, n):
    """
    :param f: Original function
    :param a: start of the range
    :param b: end of the range
    :param n: the number of the segments
    :return: The area in the range
    """
    f = lambdify(x, f)
    h = (b-a) / n
    sum = 0
    while a < b:
        sum += 0.5 * ((a + h) - a) * (f(a) + f(a+h))
        a += h
    return sum


def calcMistake(f, a, b, n):
    """
    :param f: Original function
    :param a: start of the range
    :param b: end of the range
    :param n: the number of the segments
    :return: the mistake
    """
    h = (b-a)/n
    fTag = calcDerivative(f)
    fTag = calcDerivative(fTag)
    tTag = calcDerivative(fTag)
    s = sp.solve(tTag)
    fTag = lambdify(x, fTag)
    if len(s) > 0:
        maximum = fTag(s[0])
        for _ in range(1, len(s)):
            if fTag(s[_]) > maximum:
                maximum = fTag(s[_])
        return (1/12)*(h**2)*(b - a)*maximum


def rombergMethod(f, a, b, end, epsilon):
    """
    :param f: Original function
    :param a: start of the range
    :param b: end of the range
    :param end: limit of iteration
    :param epsilon: allowed error
    :return: The area in the range
    """
    results = [[0 for i in range(end + 1)] for j in range(end+1)]
    for k in range(0, end):
        res = trapezoidMethod(f, a, b, 2**k)
        results[k][1] = res
    print(results)
    for j in range(2, end+1):
        for k in range(2, end+1):
            results[k][j] = results[k][j-1] + ((1 / ((4 ** (j - 1)) - 1)) * (results[k][j-1] - results[k - 1][j - 1]))
            if abs(results[k][j] - results[k-1][j]) < epsilon:
                return results[k][j]


x = sp.symbols('x')
f = sp.sin(x)
#f = 3*x
# epsilon = 10**-7
#print(trapezoidMethod(f, 0, math.pi, 4))
print(calcMistake(f, 0,  math.pi, 4))
#print(rombergMethod(f, 0, math.pi, 5, 0.0001))
