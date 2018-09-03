#!/bin/python3
import math, sympy
from decimal import Decimal

def f(number):
    fx = (number**3) + (4*(number**2)) - 10
    dfx = (3*(number**2)) + (8*number)
    #dfx = sympy.Derivative(fx, number).doit()
    return (fx, dfx)

def newton(x0, tolerance, iterations):
    fx = f(x0)[0]
    dfx = f(x0)[1]
    cont = 1
    error = tolerance + 1
    while error > tolerance and fx != 0 and dfx != 0 and cont < iterations:
        x1 = x0 - (fx/dfx)
        fx = f(x1)[0]
        dfx = f(x1)[1]
        error = abs((x1-x0)/x1)
        x0 = x1
        cont += 1
    if fx == 0:
        root = (x0, '%.2E' % Decimal(str(error)))
    elif error < tolerance:
        root = (x1, '%.2E' % Decimal(str(error)))
    elif dfx == 0:
        root = (x1, "Multiple root")
    else:
        root = None
    return root

print(newton(1.5, 0.5e-08, 100))


