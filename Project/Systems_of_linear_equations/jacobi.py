#!/bin/python3

from prettytable import PrettyTable
from sympy import symbols, init_printing
from math import sqrt
from copy import copy
from numpy import linalg

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
    n = len(x0)
    for x in range(len(x0)): #El problema está aquí... x0 y x1 tienen tamaños diferente (4 y 3 respectivamente)
        sum += round((round(x1[x])-round(x0[x]))**2)
    try:
        if round(sqrt(round(sum))):
            error = round(sqrt(round(sum)))
            return error, 0
    except OverflowError as err:
        return 0, 1

def jacobi(tolerance, x0, iterations, matrix, b):
    det = linalg.det(matrix)
    if det == 0:
        return(1, "The system does not have an unique solution. Determinant is ZERO")
    try:
        linalg.inv(matrix)
    except linalg.LinAlgError:
        return 1, "Matrix is not invertible"
    
    title = ['n']
    aux = 0
    cont = 0
    while aux < len(x0):
        title.append("x"+str(aux))
        aux += 1
    title.append("Error")
    table = PrettyTable(title)
    result = [title]
    table.add_row([cont] + x0 + ["Doesn't exist"])
    result.append([cont] + x0 + ["Doesn't exist"])
    error = tolerance + 1
    while error > tolerance and cont < iterations:
        x1 = newJacobi(x0, matrix, b)
        aux = norma(x0, x1)
        error = aux[0]
        err = aux[1]
        if err==1:
            return 1, "Working with integers too big"
        cont += 1
        table.add_row([cont] + x1 + [error])
        result.append([cont] + x1 + [error])
        x0 = copy(x1)
    return 0, x0, result, cont
