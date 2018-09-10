#!/bin/python3

import math
from decimal import Decimal
from prettytable import PrettyTable

def f(number):
    #fx = math.exp((3*number)-12) + (number * math.cos(3*number)) - (number**2) + 4
    #fx = (2 * (number**2)) + (3 * number) - 3
    #fx = math.exp(number) - number - 2
    #fx = (number*(math.exp(number))) - (number**2) - (5*number) -3
    #fx = (math.exp(-number)) - math.cos(4*number)
    #fx = math.exp((-(number)**2)+1) - (4*(number**3)) + 25
    #fx = (number**3)+(4*(number**2))-10
    fx = math.exp(-number) + (math.sqrt(number)*math.log((number**2) + 1)) - (number**2)
    #fx = math.exp(number) - (5 * number) + 2
    return fx


def secant(x0, x1, tolerance, iterations):
    table = PrettyTable(['Iteration','Xn', 'f(Xn)', 'Relative Error'])
    fx0 = f(x0)
    root = 0
    if fx0 == 0:
        root = x0
    else:
        fx1 = f(x1)
        cont = -1
        error = tolerance + 1
        den = fx1 - fx0
        table.add_row([cont, x0, '%.2E' % Decimal(str(fx0)), 'Doesnt exist'])
        cont += 1
        table.add_row([cont , x1, '%.2E' % Decimal(str(fx1)), 'Doesnt exist'])
        while error > tolerance and fx1 != 0 and den != 0 and cont < iterations:
            cont += 1
            x2 = x1 - ((fx1 * (x1 - x0)) / den)
            error = abs((x2-x1)/x2)
            x0 = x1 
            fx0 = fx1
            x1 = x2 
            fx1 = f(x1)
            den = fx1 - fx0
            table.add_row([cont, x1, '%.2E' % Decimal(str(fx1)), '%.2E' % Decimal(str(error))])
        if fx1 == 0:
            root = x1
        elif error < tolerance:
            root = (x1, '%.2E' % Decimal(str(error)))
        elif den == 0:
            root = (x1, "Multiple root")
        else:
            root = None
    print(table)
    return root


print(secant(1, 1.2, 1E-03, 10))
