#!/bin/python3

import math, sympy
from decimal import Decimal
from prettytable import PrettyTable

def f(x):
    #fx = math.exp(-x) - math.log10(x)
    fx = math.cos(x) + 2*x + 3
    return fx

def aitken(x0, tolerance, iterations):
    table = PrettyTable(['Iteration','Xn', 'Error Relativo'])
    fx0 = f(x0)
    root = 0
    if fx0 == 0:
        root = x0 
    else:
        cont = 0
        error = tolerance + 1
        table.add_row([cont, x0, 'Doesnt exist'])
        while cont < iterations and error > tolerance:
            x1 = f(x0)
            x2 = f(x1)
            if (x2-x1) - (x1-x0) == 0:
                  break
            aux = x2-(((x2-x1)**2)/((x2-x1)-(x1-x0)))
            error = abs((aux - x0)/aux) # Error relativo
            cont += 1
            table.add_row([cont, aux, '%.2E' % Decimal(str(error))])
            x0 = aux
            fx0 = f(x0)
        if error < tolerance:
            root = (aux, '%.2E' % Decimal(str(error)))
        else:
            root = (None, iterations)

        print(table)
    return root

print(aitken(-1.6, 0.5e-05, 100))

