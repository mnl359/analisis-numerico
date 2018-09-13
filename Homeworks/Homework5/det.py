#!/bin/python3

from numpy.linalg import det
from copy import deepcopy
from random import randint


def aleatory(m ,n):
    matrix = []
    x = 0
    y = 0
    while x != m:
        aux = []
        while y != n:
            aux1 = randint(0,100)
            aux.append(aux1)
            y += 1
        x += 1
        y = 0
        matrix.append(aux)
    return matrix


def cofactors(matrix, row, column):
    cof = deepcopy(matrix)
    cof.pop(row)
    for x in range(len(cof)):
        cof[x].pop(column)
    return cof
        

def determinant(matrix):
    if len(matrix) != len(matrix[0]):
        print("The matrix must be an square")
        exit(1)
    elif len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        sign = 1
        for x in range(len(matrix[0])):
            det += sign * matrix[0][x]*determinant(cofactors(matrix, 0, x)) # El error está al pasar el determinante sigue sacando cofactores
            sign = -sign
        return det


a = aleatory(10, 10)

print(determinant(a))
print("-----")
print(det(a))
