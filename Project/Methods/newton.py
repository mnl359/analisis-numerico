#!/bin/python3
import math, sympy
from decimal import Decimal
from prettytable import PrettyTable

def f(number):
    #fx = math.exp(number) - number - 2
    #dfx = math.exp(number) - 1
    #fx = (number*(math.exp(number))) - (number**2) - (5*number) -3
    #dfx = number*(math.exp(number)) + math.exp(number) -2*number - 5 
    sympy.init_printing(use_unicode=True)
    x = sympy.symbols('x')
    #fx = sympy.exp(-x) - sympy.log(x)
    #fx = 3*(x**3) + 10*(x**2) - x + 20
    fx = fx = (x**3) - (x**2) - x + 1 + (sympy.sin(x-1) * sympy.sin(x-1)) 
    #fx = (x**3)+(4*(x**2))-10
    #sympy.exp((-(x)**2)+1) - (4*(x**3)) + 25
    function = fx.evalf(subs={x:number})
    #math.exp((-(number)**2)+1) - (4*(number**3)) + 25
    dfx = sympy.Derivative(fx, x).doit()
    derivative = dfx.evalf(subs={x:number})
    # dfx = (3*(number**2)) + (8*number)
    return (function, derivative)

def newton(x0, tolerance, iterations):
    table = PrettyTable(['Iteration','Xn','f(Xn)', 'df(Xn)','Error'])
    fx = f(x0)[0]
    dfx = f(x0)[1]
    cont = 0
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

print(newton(-0.5, 1e-07, 100))


