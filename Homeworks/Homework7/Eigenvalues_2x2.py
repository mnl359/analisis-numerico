#!/bin/python3

from copy import deepcopy, copy
from pandas import DataFrame
import numpy as np
from random import randint
from sys import stdout

def trace(A):
    trace = 0
    for i in range(len(A)):
        trace += A[i][i]
    return trace

def cofactors(matrix, row, column):
    cof = deepcopy(matrix)
    cof.pop(row)
    for x in range(len(cof)):
        cof[x].pop(column)
    return cof

def determinant(matrix):
    if len(matrix) != len(matrix[0]):
        print("The matrix must be square")
        exit(1)
    elif len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        sign = 1
        for x in range(len(matrix[0])):
            det += sign * matrix[0][x]*determinant(cofactors(matrix, 0, x))
            sign = -sign
        return det

def eigenvalues2(matrix):
    if len(matrix) >2:
        print("The matrix is too big.")
    else:
        tr = -1*trace(matrix)
        det = determinant(matrix)
        eigenvalue1 = (-tr + np.sqrt(tr**2 - 4.0 *det)) / 2.0
        eigenvalue2 = (-tr - np.sqrt(tr**2 - 4.0 *det)) / 2.0
        return eigenvalue1, eigenvalue2

A=[[2,1], [-1,0]]
A=[[1, 1], [-2, 4]]
print(eigenvalues2(A))