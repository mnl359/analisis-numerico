#!/bin/python3

from sympy import Symbol, expand, simplify, factor, init_printing
import numpy as np

def neville(value, xy):
    x = Symbol("x")
    n = len(xy)
    check = checkData(xy)
    if(check[0] == 1):
        return(check)
    polys = []
    for i in range(n):
        row = [None]*n
        polys.append(row)
    for i in range(n):
        polys[i][i] = xy[i][1]

    for j in range(1,n):
        for i in range(n-j):
            xi = xy[i][0]
            xj = xy[j + i][0]
            polij = expand(((x - xi) * polys[i+1][j + i] - (x - xj) * polys[i][j-1+i]) / (xj - xi))
            polys[i][j+i] = polij
    poly = polys[0][n-1]
    value = evalPoly(value, poly)
    return(0, poly, value)

def evalPoly(value, poly):
    x = Symbol("x")
    return poly.evalf(subs={x:value})

def checkData(X):
    n = len(X)
    if(n < 2):
        return(1, "The set of points must have at least 2 elements.")
    for i in range(n - 1):
        if(len(X[i]) < 2):
            return(1, "Every point must have both X and Y components. Problem found at: " + str(i))
        elif(len(X[i+1]) < 2):
            return(1, "Every point must have both X and Y components. Problem found at: " + str(i+1))
        elif(X[i+1][0] < X[i][0]):
            return(1, "The set of points must be arranged in ascending order with respect to their X component. Problem found at: " + str(i))
        elif(X[i+1][0] == X[i][0]):
            return(1, "All points must be different. Problem found at: " + str(i) + " and " + str(i + 1)) 
    return(0, "Ok.")

#xy = [[0, 0],[1, 1],[2, 1],[3, 0]]
#xy = [[-1, -1, 5],[15, 5, 9]]
xy = [[-1, 15], [4, 5], [5, 9]]
value = 5
poly = neville(5, xy)
#print("The resulting polynomial is: ", poly)
#print("The result of p(%s) is %s" % (value, evalPoly(value, poly)))
