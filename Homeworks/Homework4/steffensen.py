#!/bin/python3

import math, sympy
from decimal import Decimal
from prettytable import PrettyTable

def f(number):
    sympy.init_printing(use_unicode=True)
    x = sympy.symbols('x')
    #function = sympy.exp(-x) - sympy.log(x)
    #function = 3*(x**3) + 10*(x**2) - x + 20
    #function = (x**3) - (x**2) - x + 1 + (sympy.sin(x-1) * sympy.sin(x-1))
    function = sympy.sqrt((2*x) + 3)
    #function = -(sympy.exp(x))
    #fx = (x**3)+(4*(x**2))-10
    #sympy.exp((-(x)**2)+1) - (4*(x**3)) + 25
    fx = function.evalf(subs={x:number})
    return fx


def steffensen(x0, tolerance, iterations):
    table = PrettyTable(['Iteration','X', 'Relative Error'])
    fx = f(x0)
    fx0 = x0 + f(x0)
    fx1 = fx0 + f(fx0)
    #fx1 = fx0 + f(fx0)
    root = 0
    if fx == 0:
        root = x0 
    else:
        cont = 0
        error = tolerance + 1
        table.add_row([cont, x0, 'Doesnt exist'])
        while cont < iterations and error > tolerance:
            numerator = (fx0 - x0)**2
            #fHelper = f(x0 + fx0)
            denominator = fx1 - (2*fx0) + x0
            if denominator == 0:
                break
            x = x0 - numerator / denominator
            error = abs((x - x0)/x)
            cont += 1
            table.add_row([cont, x, '%.2E' % Decimal(str(error))])
            x0 = x
            fx0 = x0 + f(x0)
            fx1 = fx0 + f(fx0)
        if error < tolerance:
            root = (x, '%.2E' % Decimal(str(error)))
        else:
            root = (None, iterations)

        print(table)
    return root


print(steffensen(4, 1e-03, 100))
