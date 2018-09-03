#!/bin/python3
import math, sympy
from decimal import Decimal

def f(number):
    #fx = math.exp(number) - number - 2
    #dfx = math.exp(number) - 1
    fx = (number*(math.exp(number))) - (number**2) - (5*number) -3
    dfx = number*(math.exp(number)) + math.exp(number) -2*number - 5 
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

print(newton(-0.5, 5e-05, 15))


