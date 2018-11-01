#!/bin/python3

from prettytable import PrettyTable
from sympy import symbols, init_printing
from math import sqrt
from copy import copy

def newGaussSeidel(x0, matrix, b):
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
        x1 = newGaussSeidel(x0, matrix, b)
        error = norma(x0, x1)
        cont += 1
        table.add_row([cont] + x1 + [error])
        x0 = copy(x1)
    print(table)

A = [
    [9.1622,    0.4505,    0.1067,    0.4314,    0.8530,    0.4173,    0.7803,    0.2348,    0.5470,    0.5470],
    [0.7943,    9.0838,    0.9619,    0.9106,    0.6221,    0.0497,    0.3897,    0.3532,    0.2963,    0.7757],
    [0.3112,    0.2290,    9.0046,    0.1818,    0.3510,    0.9027,    0.2417,    0.8212,    0.7447,    0.4868],
    [0.5285,    0.9133,    0.7749,    9.2638,    0.5132,    0.9448,    0.4039,    0.0154,    0.1890,    0.4359],
    [0.1656,    0.1524,    0.8173,    0.1455,    9.4018,    0.4909,    0.0965,    0.0430,    0.6868,    0.4468],
    [0.6020,    0.8258,    0.8687,    0.1361,    0.0760,    9.4893,    0.1320,    0.1690,    0.1835,    0.3063],
    [0.2630,    0.5383,    0.0844,    0.8693,    0.2399,    0.3377,    9.9421,    0.6491,    0.3685,    0.5085],
    [0.6541,    0.9961,    0.3998,    0.5797,    0.1233,    0.9001,    0.9561,    9.7317,    0.6256,    0.5108],
    [0.6892,    0.0782,    0.2599,    0.5499,    0.1839,    0.3692,    0.5752,    0.6477,    9.7802,    0.8176],
    [10.0000,    0.4427,    0.8001,    0.1450,    0.2400,    0.1112,    0.0598,    0.4509,    0.0811,   20.0000]  
    ]

b = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

X0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

tol=1e-07 

fileToPrint = "gauss-seidel.txt"
with open(fileToPrint, "w") as result:
    print(gaussSeidel(tol, X0, 100, A, b), file=result)
    