#!/bin/python3

from numpy.linalg import det


def cofactors(matrix, row, column):
    cof = matrix
    cof.pop(row)
    for x in range(len(matrix)):
        cof[x].pop(column)
    return cof
        

def determinant(matrix):
    print("len matrix: " + str(len(matrix)))
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


a = [[1,0,2],[3,0,0],[2,1,4]]
#a = [[3,0],[2,1]]

print(determinant(a))
print("-----")
print(det(a))
