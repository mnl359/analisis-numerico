#!/bin/python3

from copy import deepcopy, copy
from pandas import DataFrame

def stepped(A, b):
    aux = deepcopy(A)
    Ab = aumMatrix(A, b)
    n = len(Ab)
    marks = []
    for x in range(len(aux[0])):
        marks.append(x)
    for i in range(n):
        biggest = biggestNumber(aux)
        mult = Ab[biggest[0]][biggest[1]]
        if biggest[0] != 0:
            Ab = changeRows(Ab, biggest[0], 0)
        if biggest[1] != 0:
            Ab = changeColumns(Ab, biggest[1], 0)
            marks = changeMarks(marks, biggest[1], 0)
        Ab = multiply(Ab, mult, i)
        aux = deepcopy(Ab)
        k = len(aux)
        for m in aux:
            m.pop(k)
        if len(aux) > 1:
            for x in range(i):
                aux.pop(x)
            for y in aux:
                for w in range(i):
                    y.pop(w)
        print(DataFrame(aux))
        print(DataFrame(Ab))


def biggestNumber(A):
    biggest = 0
    biggest_row = 0
    biggest_col = 0
    for i in range(len(A)):
        for j in range(len(A)):
            if A[i][j] > biggest:
                biggest = A[i][j]
                biggest_col = j
                biggest_row = i
    print("i ", i, " j ", j)
    return (biggest_row, biggest_col)

def multiply(Ab, mult, i):
    for j in range(i + 1, len(Ab)):
        helper = Ab[j][i]
        print("helper ", helper, " Ab[i][i] ", Ab[i][i])
        mult = helper / Ab[i][i]
        row1 = Ab[i]
        row2 = Ab[j]
        for k in range(0, len(row2)):
            row2[k] -= (mult*row1[k])
        Ab[j] = row2
    return Ab

def changeRows(Ab, biggest_row, i):
    aux = Ab[biggest_row]
    Ab[biggest_row] = Ab[i]
    Ab[i] = aux
    return Ab

def changeColumns(Ab, biggest_col, i):
    for x in Ab:
        aux = x[i]
        x[i] = x[biggest_col]
        x[biggest_col] = aux
    return Ab

def changeMarks(marks, biggest_col, i):
    aux = marks[i]
    marks[i] = marks[biggest_col]
    marks[biggest_col] = aux
    return marks

def aumMatrix(A, b):
    cont = 0
    for i in A:
        i.append(b[cont])
        cont += 1
    return A

def clear(stepMat):
    vector = []
    n = len(stepMat)
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

m = [[-7, 2, -3, 4],[5, -1, 14, -1], [1, 9, -7, 13], [-12, 13, -8, -4]]
b = [-12, 13, 31, -32]
print(stepped(m, b))