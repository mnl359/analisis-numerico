#!/bin/python3

import math
from decimal import Decimal
from prettytable import PrettyTable

def f(x):
    #fx = (number**3) + (4*(number**2)) - 10
    #fx = (number*(math.exp(number))) - (number**2) - (5*number) -3
    #fx = math.sqrt((math.exp(x+1)-(4*x)+2)/7)
    #fx = math.log((7*(x**2))+(4*x)-2)-1
    #fx = (math.exp(x+1)-(7*(x**2))+2)/4
    #fx = math.exp(number) - number - 2
    fx = math.exp(x+1)-(7*(x**2))-(4*x)+2
    return fx

def g(x):
    #gx = math.sqrt(10/(number+4))
    #gx = ((number*(math.exp(number))) - (number**2) -3)/5
    #gx = math.log10(number+2)
    #fx = math.sqrt((math.exp(x+1)-(4*x)+2)/7)
    #fx = math.log((7*(x**2))+(4*x)-2)-1
    fx = (math.exp(x+1)-(7*(x**2))+2)/4
    return fx

def fixedPoint(xa, tolerance, iterations):
    table = PrettyTable(['Iteration','Xn','f(Xn)', 'Error'])
    fx = f(xa)
    cont = 0
    error = tolerance + 1
    table.add_row([cont, xa, fx, 'Doesnt exist'])
    while fx != 0 and error > tolerance and cont < iterations:
        xn = g(xa)
        fx = f(xn)
        error = abs((xn-xa))
        xa = xn
        cont += 1
        table.add_row([cont, xn, fx, '%.2E' % Decimal(str(error))])
    if fx == 0:
        root = xa
    elif error < tolerance:
        root = (xa, '%.2E' % Decimal(str(error)))
    else:
        root = (None, iterations)
    print(table)
    return root


print(fixedPoint(3.1, 1e-07, 100))
