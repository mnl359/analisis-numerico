#!/bin/python3

import math, sympy
from sympy import *
from decimal import Decimal
from prettytable import PrettyTable

def f(x, expr):
    fx = eval(expr)
    return fx
	
def muller(x0, x1, exp, tolerance, iterations):
    table = PrettyTable(['Iteration','X1', 'X2', 'X3', 'Error Absoluto'])
    x2 = (x1 - x0)/2.0 # We get the third value using bisection
    fx0 = f(x0, exp)
    fx1 = f(x1, exp)
    fx2 = f(x2, exp)
    root = 0
    if fx0 == 0:
        root = x0
    elif fx1 == 0:
        root = x1
    if fx2 == 0:
        root = x2
    else:
        cont = 0
        error = tolerance + 1
        table.add_row([cont, x0, x1, x2, 'Doesnt exist'])

        while cont < iterations and error > tolerance:
            h0 = x1 - x0
            h1 = x2 - x1
            if (h0 == 0) | (h1 == 0):
                print ("h0 or h1 became 0.")
                break
            delta0 = (fx1 - fx0)/h0
            delta1 = (fx2 - fx1)/h1
            if h1 - h0 == 0:
                print ("h1 - h0 became 0.")
                break
            a = (delta1 - delta0)/(h1 - h0)
            b = a*h1 + delta1
            c = fx2
            #Solving the quadratic equation
            den = 1
            if b < 0:
                den = b - math.sqrt(b**2 - 4*a*c)
            else:
                den = b + math.sqrt(b**2 - 4*a*c)
            x3 = x2 + (-2*c)/den
            
            error = abs(x3 - x2) # Abs error
            cont += 1
            table.add_row([cont, x1, x2, x3, '%.2E' % Decimal(str(error))])
            x0 = x1
            x1 = x2
            x2 = x3
            fx0 = fx1
            fx1 = fx2
            fx2 = f(x3, exp)
            
        if error < tolerance:
            root = (x3, '%.2E' % Decimal(str(error)))
        else:
            if (cont == iterations):
                print ("The method failed.")
                root = (None, cont)
            else:
                root = (x3, '%.2E' % Decimal(str(error)))

        print(table)
    return root

#print(muller(0.0, 1.0, "log(x+2)",0.5e-7, 100))

#print(stephensen(6.5, "(2*x)**(1/2)+3-x",0.5e-11, 20))
#print(muller(0.0, 1.0, "exp(-x)-x",0.5e-11, 100))
print(muller(0.5, 1.0, "log(sin(x)**2 + 1) - 1/2",0.5e-11, 100))
