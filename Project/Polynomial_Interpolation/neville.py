#!/bin/python3

from sympy import Symbol, expand, simplify, factor, init_printing
import numpy as np

def neville(xy):
    x = Symbol("x")
    n = len(xy[0])
    polys = []
    for i in range(n):
        row = [None]*n
        polys.append(row)
    for i in range(n):
        polys[i][i] = xy[1][i]

    for j in range(1,n):
        for i in range(n-j):
            xi = xy[0][i]
            xj = xy[0][j + i]
            polij = expand(((x - xi) * polys[i+1][j + i] - (x - xj) * polys[i][j-1+i]) / (xj - xi))
            polys[i][j+i] = polij

    return(polys[0][n-1])

def evalPoly(value, poly):
    x = Symbol("x")
    return poly.evalf(subs={x:value})

#xy = [[0, 0],[1, 1],[2, 1],[3, 0]]
xy = [[-1, 4, 5],[15, 5, 9]]
value = 5
poly = neville(xy)
print("The resulting polynomial is: ", poly)
print("The result of p(%s) is %s" % (value, evalPoly(value, poly)))
