#!/bin/python3

import math
from decimal import Decimal

def f(number):
    #fx = (number**3) + (4*(number**2)) - 10
    fx = (number*(math.exp(number))) - (number**2) - (5*number) -3
    #fx = math.exp(number) - number - 2
    return fx

def g(number):
    #gx = math.sqrt(10/(number+4))
    gx = ((number*(math.exp(number))) - (number**2) -3)/5
    #gx = math.log10(number+2)
    return gx

def fixedPoint(xa, tolerance, iterations):
    fx = f(xa)
    cont = 0
    error = tolerance + 1
    while fx != 0 and error > tolerance and cont < iterations:
        xn = g(xa)
        fx = f(xn)
        error = abs((xn-xa)/xn)
        xa = xn
        cont += 1
    if fx == 0:
        root = xa
    elif error < tolerance:
        root = (xa, '%.2E' % Decimal(str(error)))
    else:
        root = (None, iterations)
    return root


print(fixedPoint(-0.5, 5e-05, 15))
