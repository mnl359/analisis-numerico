#!/bin/python3

from pandas import DataFrame
from copy import deepcopy
import numpy as np

def crout(matrix, vector):
    try:
        np.linalg.inv(matrix)
    except np.linalg.LinAlgError:
        return 1, "Matrix is not invertible"
    l = []
    u = []
    ucont = 0
    for i in range(len(matrix)):
        laux = []
        uaux = []
        for j in range(len(matrix)):
            if j == ucont:
                uaux.append(1)
            else:
                uaux.append(0)
            laux.append(0)
        ucont += 1
        l.append(laux)
        u.append(uaux)
    n = len(matrix)
    for j in range(n):
        for i in range(j,n):
            sum = 0
            for k in range(j):
                sum = sum + l[i][k]*u[k][j]
            l[i][j] = matrix[i][j] - sum
        
        for i in range(j,n):
            sum = 0
            for k in range(j):
                sum = sum + l[j][k] * u[k][i]
            if l[j][j] == 0:
                return(1, "Division by 0")
            u[j][i] = (matrix[j][i] - sum)/ l[j][j]
    Lz = aumMatrix(l, vector)
    vector_z = progressive_substitution(Lz)
    Ux = aumMatrix(u, vector_z)
    result = regressive_substitution(Ux)
    result = list(np.linalg.solve(matrix,vector))    
    return 0, l, u, result

def progressive_substitution(stepMat):
    vector = []
    n = len(stepMat)
    for x in range(n):
        vector.append(0)
    vector[0] = stepMat[0][n] / stepMat[0][0]
    i = 1
    while i <= n - 1:
        result = 0
        p = 0
        while p <= len(vector) - 1:
            result += (stepMat[i][p] * vector[p])
            p += 1
        vector[i] = stepMat[i][n] - result / stepMat[i][i]
        i += 1
    return vector
  
def regressive_substitution(stepMat):
    n = len(stepMat)
    vector = []
    for x in range(n):
        vector.append(0)
    vector[n - 1] = stepMat[n - 1][n] / stepMat[n - 1][n - 1]
    i = n - 2
    while i >= 0:
        result = 0
        p = len(vector) - 1
        while p >= 0:
            result += (stepMat[i][p] * vector[p])
            p -= 1
        vector[i] = (stepMat[i][n] - result) / stepMat[i][i]
        i -= 1
    return vector

def aumMatrix(A, b):
    cont = 0
    aux = []
    for i in range(len(A)):
        row = list(A[i])
        row.append(b[cont])
        aux.append(row)
        cont += 1
    return aux

#m = [[60.0, 30.0, 20.0],
#      [30.0, 20.0, 15.0],
#      [20.0, 15.0, 12.0]]
#print(crout(m, [1.0,1.0,1.0]))
# name = input("Enter the name of the file you want the answer to be saved. It's going to have '.txt' extension: ")
# matrix_rows = int(input("As this has to be a square matrix, the number of rows is going to be the same number of columns. \
#                 \nEnter number of rows in the matrix: "))
# matrix = []
# print("Enter the %s x %s matrix: "% (matrix_rows, matrix_rows))
# print("Separe each number with a space and to change the row press ENTER")
# for j in range(matrix_rows):
#         matrix.append(list(map(float, input().rstrip().split())))
# matrix_aux = deepcopy(matrix)
# with open(name + ".txt", "w") as result:
#     mat = crout(matrix)
#     print("The L matrix is:" , file=result)
#     print(DataFrame(mat[0]), file=result)
#     print("\n", file=result)
#     print("The U matrix is:" , file=result)
#     print(DataFrame(mat[1]), file=result)
#     print("\n", file=result)