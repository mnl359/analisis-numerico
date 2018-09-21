#!/bin/python3

import math, sympy
from decimal import Decimal
from prettytable import PrettyTable

def f(x):
    #fx = -(math.exp(x))
    fx = math.sqrt((2*x)) + 3
    return fx

def aitken(x0, tolerance, iterations):
    table = PrettyTable(['Iteration','Xn', 'Error Relativo'])
    root = 0
    fx0 = f(x0)
    if fx0 == 0:
        root = x0 
    else:
        cont = 0
        error = tolerance + 1
        table.add_row([cont, x0, 'Doesnt exist'])
        while cont < iterations and error > tolerance:
            x1 = f(x0)
            x2 = f(x1)
            num = (x1-x0)**2
            den = (x2-(2*x1)+x0)
            if den == 0:
                  break
            aux = x0-(num/den)
            if aux == 0:
                break
            aux = x0 - (num/den)
            error = abs((aux - x0)/aux) # Error relativo
            cont += 1
            table.add_row([cont, aux, '%.2E' % Decimal(str(error))])
            x0 = aux
        if error < tolerance:
            root = (aux, '%.2E' % Decimal(str(error)))
        else:
            root = (None, iterations)

        print(table)
    return root

#print(aitken(0.5, 1e-07, 100))
print(aitken(4, 1e-03, 100))

