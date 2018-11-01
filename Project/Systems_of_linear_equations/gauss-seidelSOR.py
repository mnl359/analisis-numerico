#!/bin/python3

from prettytable import PrettyTable
from sympy import symbols, init_printing
from math import sqrt
from copy import copy
from decimal import Decimal

def newGaussSeidel(x0, matrix, b, rel):
    aux = []
    newX0 = copy(x0)
    for i in range(len(matrix)):
        suma = 0
        for j in range(len(matrix)):
            if j != i:
                suma += matrix[i][j]*newX0[j]
        suma = (b[i] - suma)/matrix[i][i]
        relaxing = rel*suma + (1-rel)*x0[i]
        newX0[i] = relaxing
        aux.append(relaxing)
    return aux

def norma(x0, x1):
    sum = 0
    den = 0
    for x in range(len(x0)):
        sum += (x1[x]-x0[x])**2
    error = sqrt(sum)
    return error

def gaussSeidel(tolerance, x0, iterations, matrix, b, rel):
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
        x1 = newGaussSeidel(x0, matrix, b, rel)
        error = norma(x0, x1)
        cont += 1
        table.add_row([cont] + x1 + ['%.2E' % Decimal(str(error))])
        x0 = copy(x1)
    print(table)

m = [[5,3,1],[3,4,-1],[1,-1,4]]
b = [24,30,-24]
gaussSeidel(6e-06, [0,0,0], 40, m, b, 1)