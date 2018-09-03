#!/bin/python3

import math
from decimal import Decimal


def f(number):
    fx = math.exp((3*number)-12) + (number * math.cos(3*number)) - (number**2) + 4
    return fx


def bisection(xi, xs, tolerance, iterations):
    fxi = f(xi)
    fxs = f(xs)
    root = 0
    if fxi == 0:
        root = xi
    elif fxs == 0:
        root = xs
    elif fxi * fxs < 0:
        xm = (xi + xs)/2
        fxm = f(xm)
        cont = 1
        error = tolerance + 1
        while error > tolerance and fxm != 0 and cont < iterations:
            if fxi * fxm < 0:
                xs = xm
                fxs = fxm
            else:
                xi = xm
                fxi = fxm
            aux = xm
            xm = (xi + xs)/2
            fxm = f(xm)
            error = abs(xm-aux)
            cont += 1
        if fxm == 0:
            root = xm
        elif error < tolerance:
            root = (xm, '%.2E' % Decimal(str(error)))
        else:
            root = (None, iterations)
    else:
        root = None
    return root


print(bisection(2, 3, 5e-4, 15))
