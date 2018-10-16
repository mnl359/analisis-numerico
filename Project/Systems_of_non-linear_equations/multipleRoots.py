#!/bin/python3
import math, sympy
from decimal import Decimal
from prettytable import PrettyTable

def f(number):
    sympy.init_printing(use_unicode=True)
    x = sympy.symbols('x')
    #fx = sympy.exp(-x) - sympy.log(x)
    #fx = 3*(x**3) + 10*(x**2) - x + 20
    #fx = sympy.cos(x) 
    #fx = (x**4) - (18*(x**2)) + 81
    #fx = (x**3) - (x**2) - x + 1 + (sympy.sin(x-1) * sympy.sin(x-1))
    fx = sympy.exp(x-2) - sympy.ln(x-1) - (x**2) + (4*x) - 5
    #fx = (x**3)+(4*(x**2))-10
    #sympy.exp((-(x)**2)+1) - (4*(x**3)) + 25
    function = fx.evalf(subs={x:number})
    #math.exp((-(number)**2)+1) - (4*(number**3)) + 25
    dfx = sympy.Derivative(fx, x).doit()
    derivative = dfx.evalf(subs={x:number})
    dfx2 = sympy.Derivative(dfx, x).doit()
    derivative2 = dfx2.evalf(subs={x:number})
    # dfx = (3*(number**2)) + (8*number)
    return (function, derivative, derivative2)

def multipleRoots(x0, tolerance, iterations):
    table = PrettyTable(['Iteration','Xn','f(Xn)', 'df(Xn)', 'd(2)f(Xn)', 'Error'])
    fx = f(x0)[0]
    dfx = f(x0)[1]
    dfx2 = f(x0)[2]
    cont = 0
    error = tolerance + 1
    table.add_row([cont, x0, '%.2E' % Decimal(str(fx)), '%.2E' % Decimal(str(dfx)), '%.2E' % Decimal(str(dfx2)), 'Doesnt exist'])
    while error > tolerance and fx != 0 and dfx != 0 and cont < iterations:
        numerator = fx * dfx
        denominator = (dfx**2) - (fx * dfx2)
        x1 = x0 - (numerator / denominator)
        fx = f(x1)[0]
        dfx = f(x1)[1]
        dfx2 = f(x1)[2]
        error = abs((x1-x0))
        x0 = x1
        cont += 1
        table.add_row([cont, x1, '%.2E' % Decimal(str(fx)), '%.2E' % Decimal(str(dfx)), '%.2E' % Decimal(str(dfx2)), '%.2E' % Decimal(str(error))])
        
    if fx == 0:
        root = x0
    elif error < tolerance:
        root = (x1, '%.2E' % Decimal(str(error)))
    elif dfx == 0 and fx == 0 and dfx2 != 0:
        root = x1
    else:
        root = None
    print(table)
    return root

print(multipleRoots(1.6, 1e-04, 100))


