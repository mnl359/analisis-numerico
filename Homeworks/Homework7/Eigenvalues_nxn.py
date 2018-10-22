#!/bin/python3

import numpy as np
import numpy.polynomial.polynomial as poly
from pandas import DataFrame
from copy import deepcopy, copy

def trace(A):
    trace = 0
    for i in range(len(A)):
        trace += A[i][i]
    return trace

def eigenvalues(A):
    n = len(A)
    I = np.identity(n)
    coef = []
    res = faddeevLeVerrier(n, A, n, I, coef)
    coef = list(reversed(coef))
    return poly.polyroots(coef)

def faddeevLeVerrier(k, A, n, I, coef):
    if k == 0:
        coef.append(1)
        return(np.zeros((n,n)), 0, A, 1, n, I, coef)
    else:
        nexIt = faddeevLeVerrier(k-1, A, n, I, coef)
        Mk = np.add(np.matmul(A,nexIt[0]), np.multiply(nexIt[3],I))
        cnk = (trace(np.matmul(A,Mk)))/(-k)
        coef.append(cnk)
        return (Mk, k, A, cnk, n, I, coef)

#Sample matrixes
# A = [[3, 1, 5], [3, 3, 1], [4, 6, 4]]
# A = [[1, 3], [-2, 4]]
# A = [[1, 0, 3], [1, -1, 2], [-1, 1, -2]]
# A = [[0, 1, -1], [1, 1, 0], [-1, 0, 1]]
# print("Eigenvalues:")
# print(eigenvalues(A))
# print("NOTE: If the resulting list contains repeated values, theses should be considered as one.")

name = input("Enter the name of the file you in which you want the answer to be saved. It's going to have a '.txt' extension: ")
matrix_rows = int(input("As this has to be a square matrix, the number of rows is going to be the same as the number of columns. \
               \nEnter the number of rows in the matrix: "))

matrix = []

print("Enter the %s x %s matrix: "% (matrix_rows, matrix_rows))
print("Separate each number with a space and to change the row press ENTER")
for j in range(matrix_rows):
        matrix.append(list(map(float, input().rstrip().split())))

print("You will find the result in " + name + ".txt")
with open(name + ".txt", "w") as result:
    eigVals = eigenvalues(matrix)

    print("The eigenvalues are:" , file=result)
    print(eigVals, file=result)
    print("NOTE: If the resulting list contains repeated values, theses should be considered as one.", file=result)