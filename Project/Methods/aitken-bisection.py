#!/bin/python3

import math, simpy
from sympy import *
from decimal import Decimal
from prettytable import PrettyTable

def f(x, expr):
    fx = eval(expr)
    return fx

def bisection(a, b, exp):
    fa = f(a, exp)
    x = (a + b)/2.0
    fx = f(x, exp)
    if (fa*fx) < 0:
        b = x;
    else:
        a = x;
    x = (a + b)/2.0
    return a, b, x

def aitken(a, b, exp, tolerance, iterations):
    table = PrettyTable(['Iteration','Xn', 'Error Absoluto'])
    x0 = (a + b)/2.0
    fa = f(a, exp)
    fb = f(b, exp)
    fx0 = f(x0, exp)
    root = 0
    if fx0 == 0:
        root = x0
    elif fa == 0:
        root = a
    elif fb == 0:
        root = b
    else:
        cont = 0
        error = tolerance + 1
        table.add_row([cont, x0, 'Doesnt exist'])
        prev = x0

        while cont < iterations and (error > tolerance or error == 0):
            a1, b1, x1 = bisection(a, b, exp)
            a2, b2, x2 = bisection(a1, b1, exp)
            den = (x2-x1) - (x1-x0)
            if den == 0:
                print("The denominator became 0.")
                break
            xn = x2-(((x2-x1)**2)/den)
            if xn == prev:
                a, b, x0 = a1, b1, x1
                prev = xn
                continue
            error = abs(xn - prev) # Error absoluto
            cont += 1
            table.add_row([cont, xn, '%.2E' % Decimal(str(error))])
            a, b, x0 = a1, b1, x1
            prev = xn
            
        if error < tolerance:
            root = (xn, '%.2E' % Decimal(str(error)))
        else:
            print (error)
            root = (None, cont)

        print(table)
    return root

#print(aitken(1.0, "log(x+2)",0.5e-11, 100))

#print(aitken(1.0, "(2*x+2)**(1/2)",0.5e-11, 100))
#print(aitken(1.0, "(2*x+3)**(1/2)",0.5e-11, 100))

#print(aitken(6.0, 7.0, "(2*x)**(1/2)+3",0.5e-11, 100))
#print(bise(1.0, 2.0, "x**3+4*x**2-10",0.5e-11, 100))
#print(aitken(1.0, 2.0, "x**3+4*x**2-10",0.5e-11, 100))
print(aitken(0.0, 1.0, "log(sin(x)**2 + 1) - 1/2",0.5e-11, 100))