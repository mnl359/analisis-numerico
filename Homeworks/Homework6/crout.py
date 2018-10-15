#!/bin/python3

from pandas import DataFrame

def crout(matrix):
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
                print("Divided by 0")
                exit(1)
            u[j][i] = (matrix[j][i] - sum)/ l[j][j]
    print(DataFrame(l))
    print(DataFrame(u))

crout([[1,2,3],[2,20,26],[3,26,70]])