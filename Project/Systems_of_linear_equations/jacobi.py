#!/bin/python3

from prettytable import PrettyTable
from sympy import symbols, init_printing
from math import sqrt
from copy import copy

def newJacobi(x):
    init_printing(use_unicode=True)
    x0, x1, x2 = symbols('x0, x1, x2')
    functions = [(-23+(4*x1)+(5*x2))/13, (5-(3*x0)-(2*x2))/(-7), (34+(4*x0)-(5*x1))/(-16)]
    result = []
    for i in functions:
        aux = i.evalf(subs={x0:x[0], x1:x[1], x2:x[2]})
        result.append(aux)
    return result

def norma(x0, x1):
    sum = 0
    den = 0
    for x in range(len(x0)):
        sum += (x1[x]-x0[x])**2
        den += (x1[x])**2
    error = (sqrt(sum))/(sqrt(den))
    return error

def jacobi(tolerance, x0, iterations):
    title = ['n']
    aux = 0
    cont = 0
    while aux < len(x0):
        title.append("x"+str(aux))
        aux += 1
    title.append("Error")
    table = PrettyTable(title)
    table.add_row([cont] + x0 + ["Doesn't exist"])
    error = tolerance + 1
    while error > tolerance and cont < iterations:
        x1 = newJacobi(x0)
        error = norma(x0, x1)
        cont += 1
        table.add_row([cont] + x1 + [error])
        x0 = copy(x1)
    print(table)

jacobi(5e-06, [0,0,0], 20)
    