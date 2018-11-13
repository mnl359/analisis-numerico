#!/bin/python3

import numpy as np
from prettytable import PrettyTable

def spline1(X):
    print(X)
    check = checkData(X)
    if(check[0] == 1):
        return(check)
    n = 2 * (len(X) - 1) + 1
    A = []
    A = introByEval(A, X, n)
    A = introBySmoothness(A, X, n)
    A = gaussJordan(A)
    coef = clear(A, len(A))
    print(orderCoef(coef))
    return (0, orderCoef(coef))
    
    return (np.array(A),coef)

def introByEval(A, X, n):
    row = list(np.zeros(n))
    row[0] = X[0][0]
    row[1] = 1
    row[n-1] = X[0][1]
    A.append(row)
    col = 0
    for i in range(1, len(X)):
        row = list(np.zeros(n))
        row[i-1 + col] = X[i][0]
        row[i + col] = 1
        row[n-1] = X[i][1]
        col += 1
        A.append(row)
    return A

def introBySmoothness(A, X, n):
    col = 0
    for i in range(1, len(X)-1):
        row = list(np.zeros(n))
        row[col] = X[i][0]
        row[col + 1] = 1
        row[col + 2] = -X[i][0]
        row[col + 3] = -1
        col += 2
        A.append(row)
    return A

def gaussJordan(Ab):
    n = len(Ab) 
    for i in range (0, n):
        for j in range (i, n):
            if i == j:
                column = [row[i] for row in Ab]
                lenColumn = len(column)
                if Ab[i][i] == 0:
                    for k in range(i, lenColumn):
                        if column[k] != 0:
                            aux = Ab[k]
                            Ab[k] = Ab[i]
                            Ab[i] = aux
                            break
                
                helper = Ab[i][i]
                if helper == 0:
                    print("WARNING! It's not possible to step the matrix. Error in row", i)
                    exit(1) 
                   
            else:
                helper = Ab[j][i]
                mult = helper / Ab[i][i]
                row1 = Ab[i]
                row2 = Ab[j]
                for k in range(0, len(row2)):
                    row2[k] -= (mult*row1[k])
                Ab[j] = row2
    return Ab

def clear(stepMat, n):
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

def orderCoef(coef):
    table = PrettyTable(['i','Ai', 'Bi'])
    res = []
    cont = 0
    for i in range(int(len(coef)/2)):
        table.add_row([i, coef[cont], coef[cont+1]])
        res.append([i, coef[cont], coef[cont+1]])
        cont += 2
    return res

def checkData(X):
    n = len(X)
    if(n < 2):
        return(1, "The set of dots must have at least 2 elements.")
    for i in range(n - 1):
        if(len(X[i]) < 2):
            return(1, "Every dot must have both X and Y components. Problem found at: " + str(i))
        elif(X[i+1][0] < X[i][0]):
            return(1, "The set of dots must be arranged in ascending order with respect to their X component. Problem found at: " + str(i))
        elif(X[i+1][0] == X[i][0]):
            return(1, "All dots must be different. Problem found at: " + str(i))
    return(0, "Ok.")

#X = [1, 3, 4, 5]
#Y = [3, 1, 3.5, 2]
#X = [1, 3, 4, 5, 7]
#Y = [4.31, 1.5, 3.2, 2.6, 1.8]
#X = [1.0000, 2.0000, 3.0000, 4.0000, 5.0000, 6.0000, 7.0000, 8.0000, 9.0000, 10.0000]
#Y = [0.5949, 0.2622, 0.6028, 0.7112, 0.2217, 0.1174, 0.2967, 0.3188, 0.4242, 0.5079]
X = [[1.0000,0.5949], [2.0,0.2622], [3.0, 0.6028], [4.0, 0.7112], [5.0, 0.2217], [6.0, 0.1174], [7.0, 0.2967], [8.0, 0.3188], [9.0, 0.4242], [10.0, 0.5079]]

print(spline1(X))