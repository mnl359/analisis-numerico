#!/bin/python3

import math, sympy
from sympy import *
from decimal import Decimal
from prettytable import PrettyTable

def f(x, expr):
    fx = eval(expr)
    return fx
	
def stephensen(xn, exp, tolerance, iterations):
    table = PrettyTable(['Iteration','Xn', 'Error Absoluto'])
    fxn = f(xn, exp)
    root = 0
    if fxn == 0:
        root = xn 
    else:
        cont = 0
        error = tolerance + 1
        table.add_row([cont, xn, 'Doesnt exist'])

        while cont < iterations and error > tolerance:
            
            fxn = f(xn, exp)
            den = f(xn + fxn, exp) - fxn #Denominator
            if den == 0:
                print ("The denominator became 0.")
                break
            xn1 = xn - (fxn**2)/den
			
            
            error = abs((xn1 - xn)) # Abs error
            cont += 1
            table.add_row([cont, xn1, '%.2E' % Decimal(str(error))])
            xn = xn1
            #prev = aux
            
        if error < tolerance:
            root = (xn1, '%.2E' % Decimal(str(error)))
        else:
            if (cont == iterations):
                print ("The method failed.")
                root = (None, cont)
            else:
                root = (xn1, '%.2E' % Decimal(str(error)))

        print(table)
    return root

print(stephensen(-0.5, "log((sin(x)*sin(x)) + 1) - 1/2 - x",1e-7, 100))

#print(stephensen(6.5, "(2*x)**(1/2)+3-x",0.5e-11, 20))
#print(stephensen(0.5, "exp(-1*x)-x",0.5e-11, 20))
