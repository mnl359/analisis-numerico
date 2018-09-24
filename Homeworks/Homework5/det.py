#!/bin/python3

from copy import deepcopy
from random import randint
from sys import stdout
from pandas import DataFrame


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
            det += sign * matrix[0][x]*determinant(cofactors(matrix, 0, x))
            sign = -sign
        return det

matrix_rows = int(input("Enter number of rows in the matrix: "))
matrix_columns = int(input("Enter number of columns in the matrix: "))
matrix = []
print("Enter the %s x %s matrix: "% (matrix_rows, matrix_columns))
print("Separe each number with a space and to change the row press ENTER")
for j in range(matrix_rows):
        matrix.append(list(map(float, input().rstrip().split())))
print("You will find the result in result_determinant.txt")
with open("result_determinant.txt", "w") as result:
    print("The matrix is:", file=result)
    print(DataFrame(matrix), file=result)
    print("\n", file=result)
    print("The determinant is: %s" % str(determinant(matrix)), file=result)
