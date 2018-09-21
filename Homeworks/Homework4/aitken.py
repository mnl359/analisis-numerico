#!/bin/python3

import math, simpy
from sympy import *
from decimal import Decimal
from prettytable import PrettyTable

def f(x, exp):
    fx = eval(exp)
    return fx

def aitken(x0, exp, tolerance, iterations):
    table = PrettyTable(['Iteration','Xn', 'Error Absoluto'])
    fx0 = f(x0, exp)
    root = 0
    if fx0 == 0:
        root = x0 
    else:
        cont = 0
        error = tolerance + 1
        table.add_row([cont, x0, 'Doesnt exist'])
        prev = x0

        while cont < iterations and error > tolerance:
            x1 = f(x0, exp)
            x2 = f(x1, exp)
            
            if (x2-x1) - (x1-x0) == 0:
                break
            aux = x2-(((x2-x1)**2)/((x2-x1)-(x1-x0)))
            if aux == 0:
                break
            error = abs((aux - prev)) # Error absoluto
            cont += 1
            table.add_row([cont, aux, '%.2E' % Decimal(str(error))])
            x0 = x1
            prev = aux
            
        if error < tolerance:
            root = (aux, '%.2E' % Decimal(str(error)))
        else:
            root = (None, cont)

        print(table)
    return root

#print(aitken(1.0, "log(x+2)",0.5e-11, 100))

#print(aitken(1.0, "(2*x+2)**(1/2)",0.5e-11, 100))
#print(aitken(1.0, "(2*x+3)**(1/2)",0.5e-11, 100))

print(aitken(6.0, "(2*x)**(1/2)+3",0.5e-11, 100))
