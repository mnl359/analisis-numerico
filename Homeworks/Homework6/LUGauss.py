#!/bin/python3

def upper_triangular(A):
    n = len(A) 
    if n != len(A[0]):
        print("The matrix has to be squared")
        exit(-1)
    for i in range (0, n):
        for j in range (i, n):
            if i == j:
                column = [row[i] for row in A]
                lenColumn = len(column)
                if all(v == 0 for v in column):
                    continue
                if A[i][i] == 0 and i < n - 1:
                    for k in range(i + 1, lenColumn):
                        if 1 in column:
                            swapping(A, column, i)
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

def swapping(A, column, i):
    for k in range(i + 1, len(column)):
        if column[k] == 1:
            aux = A[k]
            A[k] = A[i]
            A[i] = aux
            break

def lower_triangular():
    pass

def progresive_substitution(stepMat, n):
    vector = []
    for x in range(n):
        vector.append(0)
    vector[0] = stepMat

def regressive_substitution(stepMat, n):
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