#!/bin/python3

"""Tubi, lindura holi este método debe devolver el polinomio de la lagrange y el polinomio evaluado
    evaluado en un valor, así que retorna [0, polinomio, resultado]"""

from sympy import Symbol, expand, simplify, factor, init_printing

def l(value, i, matrix):
    init_printing(use_unicode=True)
    x = Symbol("x")
    z = 0
    num = 1
    y = 0
    den = 1
    while y < len(matrix):
        if y != i:
            den = den * (matrix[i][0] - matrix[y][0])
        y+=1
    while z < len(matrix):
        if z != i:
            aux = expand(x - matrix[z][0])
            num = expand(num * aux)
        z+=1
    aux = factor(num/den)
    ln = aux.evalf(subs={x:value})
    return aux, ln

def lagrange(x, matrix):
    pol = 0
    pol1 = 0
    check = checkData(matrix)
    if(check[0] == 1):
        return(check)
    for i in range(len(matrix)):
        ln = l(x, i, matrix)
        pol += ln[1]*matrix[i][1]
        pol1 += ln[0]*matrix[i][1]
    return 0, pol1, pol

def checkData(X):
    n = len(X)
    if(n < 2):
        return(1, "The set of dots must have at least 2 elements.")
    for i in range(n - 1):
        if(len(X[i]) < 2):
            return(1, "Every dot must have both X and Y components. Problem found at: " + str(i))
        elif(len(X[i+1]) < 2):
            return(1, "Every dot must have both X and Y components. Problem found at: " + str(i+1))
        elif(X[i+1][0] < X[i][0]):
            return(1, "The set of dots must be arranged in ascending order with respect to their X component. Problem found at: " + str(i)) 
        elif(X[i+1][0] == X[i][0]):
            return(1, "All dots must be different. Problem found at: " + str(i) + " and " + str(i + 1))
    return(0, "Ok.")