#!/bin/python3

from prettytable import PrettyTable
from sympy import symbols, init_printing
from math import sqrt
from copy import copy
from decimal import Decimal
from numpy import linalg, diag, tril, triu, asarray, matmul
from scipy import linalg as LA

# Retorna 0 (exito), vector resultado, tabla de iteraciones, número de iteraciones, pasos
# Pasos: matriz de transición, radio espectral

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
    for x in range(len(x0)):
        sum += (x1[x]-x0[x])**2
    error = sqrt(sum)
    return error

def gaussSeidel(tolerance, x0, iterations, matrix, b, rel):
    n = len(matrix)
    det = linalg.det(matrix)
    if det == 0:
        return(1, "The system does not have an unique solution. Determinant is ZERO")

    diagonal_matrix = diag(diag(matrix))
    l_matrix = diagonal_matrix - tril(matrix)
    u_matrix = diagonal_matrix - triu(matrix)
    helper = diagonal_matrix - (rel * l_matrix)
    helper2 = ((1- rel) * diagonal_matrix) + (rel * u_matrix)

    power = linalg.matrix_power(helper, -1)
    t_matrix = matmul(power, helper2)

    Z = [[abs(matrix[i][j]) for i in range(n)] for j in range(n)]
    helper3 = asarray(Z)
    suma = helper3.sum(axis=1)
    a = 0
    
    for i in range(n):      
        aux2 = (2*(Z[i][i]))
        if all(aux2 > suma):
            a = 1 
        else:
            a = 2
    
    RE = 0
    if a == 2:
        RE = max(abs(LA.eigvals(t_matrix)))
        if RE > 1:
            return (1, "The spectral radio is larger than 1 (" + str(RE) + "). Method won't converge\n \
                    The matrix is not dominant on its diagonal")

    
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
        x1 = newGaussSeidel(x0, matrix, b, rel)
        error = norma(x0, x1)
        cont += 1
        table.add_row([cont] + x1 + ['%.2E' % Decimal(str(error))])
        result.append([cont] + x1 + ['%.2E' % Decimal(str(error))])
        x0 = copy(x1)
    
    return 0, x0, result, cont, t_matrix, RE

#m = [[5,3,1],[3,4,-1],[1,-1,4]]
#b = [24,30,-24]
#print(gaussSeidel(6e-06, [0,0,0], 40, m, b, 1))