#!/bin/python3

from prettytable import PrettyTable
from sympy import symbols, init_printing
from math import sqrt
from copy import copy

def newJacobi(x0, matrix, b):
    aux = []
    for i in range(len(matrix)):
        suma = 0
        for j in range(len(matrix)):
            if j != i:
                suma += matrix[i][j]*x0[j]
        suma = (b[i] - suma)/matrix[i][i]
        aux.append(suma)
    return aux

def norma(x0, x1):
    sum = 0
    den = 0
    for x in range(len(x0)):
        sum += (x1[x]-x0[x])**2
        den += (x1[x])**2
    error = (sqrt(sum))/(sqrt(den))
    return error

def jacobi(tolerance, x0, iterations, matrix, b):
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
        x1 = newJacobi(x0, matrix, b)
        error = norma(x0, x1)
        cont += 1
        table.add_row([cont] + x1 + [error])
        x0 = copy(x1)
    print(table)

m = [[13, -4, -5],[3, -7, 2],[-4, 5, -16]]
b = [-23, 5 ,34]
jacobi(5e-06, [0,0,0], 20, m, b)
    