#!/bin/python3

import math
from decimal import Decimal


def f(number):
    # fx = math.exp((3*number)-12) + (number * math.cos(3*number)) - (number**2) + 4
    # fx = math.exp((-(number)**2)+1)-(4*(number**3)) + 25
    # fx = (2 * (number**2)) + (3 * number) - 3
    fx = (number**3) + (4*(number**2)) - 10
    return fx


def falseRule(xi, xs, tolerance, iterations):
    fxi = f(xi)
    fxs = f(xs)
    si = xi - xs
    helper = fxi - fxs
    root = 0
    if fxi == 0:
        root = xi
    elif fxs == 0:
        root = xs
    elif fxi * fxs < 0:
        if helper != 0:
            xm = xi - ((fxi*si)/helper)
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
                si = xi - xs
                helper = fxi - fxs
                if helper == 0:
                    break
                xm = xi - ((fxi*si)/helper)
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
            root = False
    else:
        root = None
    return root


print(falseRule(1, 2, 0.0001, 20))
