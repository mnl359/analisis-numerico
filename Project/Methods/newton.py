#!/bin/python3
import math, sympy
from decimal import Decimal
from prettytable import PrettyTable

def f(number):
    #fx = math.exp(number) - number - 2
    #dfx = math.exp(number) - 1
    #fx = (number*(math.exp(number))) - (number**2) - (5*number) -3
    #dfx = number*(math.exp(number)) + math.exp(number) -2*number - 5 
    fx = (number**3) + (4*(number**2)) - 10
    dfx = (3*(number**2)) + (8*number)
    return (fx, dfx)

def newton(x0, tolerance, iterations):
    table = PrettyTable(['Iteration','Xn','f(Xn)', 'df(Xn)','Error'])
    fx = f(x0)[0]
    dfx = f(x0)[1]
    cont = 1
    error = tolerance + 1
    table.add_row([cont, x0, fx, dfx, 'Doesnt exist'])
    while error > tolerance and fx != 0 and dfx != 0 and cont < iterations:
        x1 = x0 - (fx/dfx)
        fx = f(x1)[0]
        dfx = f(x1)[1]
        error = abs((x1-x0)/x1)
        x0 = x1
        cont += 1
        table.add_row([cont, x1, fx, dfx, '%.2E' % Decimal(str(error))])
    if fx == 0:
        root = (x0, '%.2E' % Decimal(str(error)))
    elif error < tolerance:
        root = (x1, '%.2E' % Decimal(str(error)))
    elif dfx == 0:
        root = (x1, "Multiple root")
    else:
        root = None
    print(table)
    return root

print(newton(1.5, 0.5e-08, 20))


