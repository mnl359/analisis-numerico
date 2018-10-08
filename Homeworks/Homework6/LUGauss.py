#!/bin/python3

from pandas import DataFrame

mults = []

def create_matrix_L(lenMatrix):
    global mults
    mults = [[0 for x in range(lenMatrix)] for y in range(lenMatrix)]

def lower_triangular(A):
    n = len(A) 
    if n != len(A[0]):
        print("The matrix has to be squared")
        exit(-1)
    for i in range (n - 1, -1, -1):
        for j in range (i, -1, -1):
            if i == j:
                column = [row[i] for row in A]
                if A[i][i] == 0:
                    for k in range(i - 1, -1 , -1):
                        if 1 in column:
                            swapping_lower(A, column, i)
                            break
                        elif column[k] != 0:
                            aux = A[k]
                            A[k] = A[i]
                            A[i] = aux
                            break
                
                helper = A[i][i]
                if helper != 1: 
                    if helper == 0:
                        print("WARNING! It's not possible to step the matrix. Error in row", i)
                        exit(1)
                    row = A[i]             
                    for k in range(0, len(row)):
                        row[k] = row[k] / helper
                    A[i] = row
            else:
                helper = A[j][i]
                if helper != 0:
                    row1 = A[i]
                    row2 = A[j]
                    for k in range(0, len(row2)):
                        row2[k] += ((-1 * helper) * row1[k])
                    A[j] = row2
    return A

def swapping_lower(A, column, i):
    for k in range(0, i):
        if column[k] == 1:
            aux = A[k]
            A[k] = A[i]
            A[i] = aux
            break

def upper_triangular(A):
    global mults
    n = len(A) 
    create_matrix_L(n)
    for i in range (0, n):
        for j in range (i, n):
            if i == j:
                mults[i][i] = 1
                column = [row[i] for row in A]
                lenColumn = len(column)
                if A[i][i] == 0:
                    for k in range(i, lenColumn):
                        if column[k] != 0:
                            aux = A[k]
                            A[k] = A[i]
                            A[i] = aux
                            break
                
                helper = A[i][i]
                if helper == 0:
                    print("WARNING! It's not possible to step the matrix. Error in row", i)
                    exit(1)

            else:
                helper = A[j][i]
                mult = helper / A[i][i]
                mults[j][i] = mult
                row1 = A[i]
                row2 = A[j]
                for k in range(0, len(row2)):
                    row2[k] -= (mult*row1[k])
                A[j] = row2
    return A


def progressive_substitution(stepMat):
    vector = []
    n = len(stepMat)
    for x in range(n):
        vector.append(0)
    vector[0] = stepMat[0][n]/stepMat[0][0]
    i = 1
    while i <= n-1:
        result = 0
        p = 0
        while p <= len(vector)-1:
            result += (stepMat[i][p]*vector[p])
            p += 1
        vector[i] = stepMat[i][n]-result/stepMat[i][i]
        i += 1
    return vector

def regressive_substitution(stepMat):
    n = len(stepMat)
    vector = []
    for x in range(n):
        vector.append(0)
    vector[n-1]=stepMat[n-1][n]/stepMat[n-1][n-1]
    i = n-2
    while i >= 0:
        result = 0
        p = len(vector)-1
        while p >= 0:
            result += (stepMat[i][p]*vector[p])
            p -= 1
        vector[i] = (stepMat[i][n]-result)/stepMat[i][i]
        i -= 1
    return vector

def aumMatrix(A, b):
    cont = 0
    for i in A:
        i.append(b[cont])
        cont += 1
    return A

def lu_pivoting(A, vector):
    u_matrix = upper_triangular(A)
    print(DataFrame(u_matrix), "\n")
    l_matrix = mults
    print(DataFrame(l_matrix), "\n")
    Lz = aumMatrix(l_matrix, vector)
    vector_z = progressive_substitution(Lz)
    Ux = aumMatrix(u_matrix, vector_z)
    result = regressive_substitution(Ux)
    return result

A = [[2, -3, 4, 1], [-4, 2, 1, -2], [1, 3, -5, 3], [-3, -1, 1, -1]]
b = [10, -10, 32, -21]

print(lu_pivoting(A, b))