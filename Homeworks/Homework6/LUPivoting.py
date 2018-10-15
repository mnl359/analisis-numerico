#!/bin/python3

from copy import deepcopy, copy
from pandas import DataFrame

mults = []
marks = []
aux_matrix =[]

def create_matrix(arr, lenMatrix):
    arr = [[0 for x in range(lenMatrix)] for y in range(lenMatrix)]
    return arr

def aumMatrix(A, b):
    cont = 0
    for i in A:
        i.append(b[cont])
        cont += 1
    return A

def exchange_rows(i, k, A):
    aux = A[i]
    A[i] = A[k]
    A[k] = aux
    return A

def multiply(m, n):
    if len(m[0]) != len(n):
        print("Dimensions are not compatible")
        exit(1)
    result = []
    for col in range(len(m)):
        aux = []
        column = 0
        while column != 1:
            pos = 0
            row = 0
            while row != len(n):
                pos += m[col][row] * n[row]
                row += 1
            aux.append(pos)
            column += 1
        result.append(aux)
    
    return result

def upper_triangular(A):
    global mults
    global marks
    global aux_matrix
    
    n = len(A) 
    mults = create_matrix(mults, n)
    marks = create_matrix(marks, n)
    aux_matrix = deepcopy(A)
    
    for i in range(n):
        marks[i][i] = 1
    
    for i in range (n):
        for j in range (i, n):            
            if i == j:
                mults[i][i] = 1
                column = [row[i] for row in A]
                lenColumn = len(column)
                helper = abs(A[i][i])
                cont = i
                for k in range(i, lenColumn):
                    if abs(column[k]) > helper:
                        helper = abs(column[k])
                        cont = k
                A = exchange_rows(i, cont, A)
                marks = exchange_rows(i, cont, marks)  
                aux_matrix = exchange_rows(i, cont, aux_matrix)

                if A[i][i] == 0:
                    print("WARNING! It's not possible to step the matrix. Error in row ", i)
                    exit(1)

            else:
                helper = A[j][i]
                mult = helper / A[i][i]
                mults[j][i] = round(mult, 15)
                row1 = A[i]
                row2 = A[j]
                for k in range(n):
                    row2[k] -= (mult*row1[k])
                    row2[k] = round(row2[k], 10)
                A[j] = row2
                aux_matrix[j] = row2
                aux_matrix[j][i] = round(mult, 15)
    print(DataFrame(aux_matrix), "\n")
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


def lu_pivoting(A, vector):
    u_matrix = upper_triangular(A)
    print(DataFrame(u_matrix), "\n")
    l_matrix = mults
    print(DataFrame(l_matrix), "\n")
    aux = multiply(marks, vector)
    helper = [aux[i][0] for i in range(len(aux))]
    print(helper, "\n")
    Lz = aumMatrix(l_matrix, helper)
    vector_z = progressive_substitution(Lz)
    print(vector_z, "\n")
    Ux = aumMatrix(u_matrix, vector_z)
    result = regressive_substitution(Ux)
    return result

A = [[-7, 2, -3, 4], [5, -1, 14, -1], [1, 9, -7, 5], [-12, 13, -8, -4]]
b = [-12, 13, 31, -32]

#A = [[2, -3, 4, 1], [-4, 2, 1, -2], [1, 3, -5, 3], [-3, -1, 1, -1]]
#b = [10, -10, 32, -21]

print(lu_pivoting(A, b))