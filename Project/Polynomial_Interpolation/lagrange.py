#!/bin/python3

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
    for i in range(len(matrix)):
        ln = l(x, i, matrix)
        pol += ln[1]*matrix[i][1]
        pol1 += ln[0]*matrix[i][1]
    print("El polinomio resultante es:")
    print(pol1)
    return pol

m = [[0, 0],[1, 1],[2, 1],[3, 0]]
value = 1
print("El resultado de p(%s) es igual a %s" % (value, lagrange(value, m)))
