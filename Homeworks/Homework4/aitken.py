#!/bin/python3

import math, sympy
from decimal import Decimal
from prettytable import PrettyTable

def f(x):
    #
    #fx = math.exp(-x) - math.log10(x)
    #fx = math.cos(x) + 2*x + 3
    fx = (x*(math.exp(x))) - (x**2) - (5*x) -3
    #fx = -(sympy.exp(x))
    return fx


def aitken(x0, tolerance, iterations):
    table = PrettyTable(['Iteration','Xn', 'Relative Error'])
    fx0 = f(x0)
    root = 0
    if fx0 == 0:
        root = x0 
    else:
        cont = 0
        error = tolerance + 1
        table.add_row([cont, x0, 'Doesnt exist'])
        #prev = x0
        while cont < iterations and error > tolerance:
            x1 = f(x0)
            x2 = f(x1)
            numerator = (x1 - x0)**2
            denominator = x2 - (2*x1) + x0
            if denominator == 0:
                break
            aux = x0 - (numerator/denominator)
            error = abs((aux - x0)/aux) # Error relativo
            cont += 1
            table.add_row([cont, aux, '%.2E' % Decimal(str(error))])
            x0 = aux
            #prev = aux
        if error < tolerance:
            root = (aux, '%.2E' % Decimal(str(error)))
        else:
            root = (None, iterations)

        print(table)
    return root

print(aitken(0.5, 5e-05, 100))

