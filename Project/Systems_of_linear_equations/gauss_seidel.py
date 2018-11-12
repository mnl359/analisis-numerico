#!/bin/python3

from prettytable import PrettyTable
from sympy import symbols, init_printing
from math import sqrt
from copy import copy
from numpy import linalg

def newGaussSeidel(x0, matrix, b):
    if len(x0) != len(matrix[0]) or len(matrix[0]) != len(b) or len(x0) != len(b):
        return(1, "Length of matrix, initial vector or vector b are different\n \
        Please check and try again")
    aux = []
    newX0 = copy(x0)
    for i in range(len(matrix)):
        suma = 0
        for j in range(len(matrix)):
            if j != i:
                suma += matrix[i][j]*newX0[j]
        suma = (b[i] - suma)/matrix[i][i]
        newX0[i] = suma
        aux.append(suma)
    return aux

def norma(x0, x1):
    sum = 0
    for x in range(len(x0)):
        sum += (x1[x]-x0[x])**2
    error = sqrt(sum)
    return error

def gaussSeidel(tolerance, x0, iterations, matrix, b):
    det = linalg.det(matrix)
    if det == 0:
        return(1, "The system does not have an unique solution. Determinant is ZERO")
    
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
        x1 = newGaussSeidel(x0, matrix, b)
        error = norma(x0, x1)
        cont += 1
        table.add_row([cont] + x1 + [error])
        result.append([cont] + x0 + ["Doesn't exist"])
        x0 = copy(x1)
    #print(table)
    return 0, result, table, cont

m = [[13, -4, -5],[3, -7, 2],[-4, 5, -16]]
b = [-23, 5 ,34]
gaussSeidel(5e-06, [0, 0, 0], 20, m, b)