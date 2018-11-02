#!/bin/python3

from prettytable import PrettyTable
from sympy import Symbol, expand, simplify, factor, init_printing

res = []

def bn(iterations):
    global res
    aux = iterations + 1
    y = iterations - 1
    for x in range(1, aux):
        res[iterations][x+1] = (res[iterations-1][x] - res[iterations][x])/(res[y][0] - res[iterations][0])
        y -= 1

def newton(value, matrix, txt):
    global res
    init_printing(use_unicode=True)
    x = Symbol("x")
    title = ['Xi','F[x]']
    n = len(matrix)
    cont = 1
    for i in matrix:
        aux = i + ([0]*(n-1))
        res.append(aux)
        if cont != n:
            title.append(str(cont))
            cont += 1
    table = PrettyTable(title)
    b0 = matrix[0][1]
    mult = 1
    pol = b0
    table.add_row(res[0])
    for iteration in range(1,n):
        bn(iteration)
        b = res[iteration][iteration+1]
        print(mult * (x - matrix[iteration-1][0]))
        mult = expand(mult * (x - matrix[iteration-1][0]))
        pol += (b*mult)
        table.add_row(res[iteration])
    print(table, file=txt)
    print("El polinomio resultante es:\n %s" % pol, file=txt)
    result = pol.evalf(subs={x:value})
    print("El resultado de p(%s) es igual a %s" % (value, result), file=txt)
    return result, pol

X =[
    [1.0000, 0.5949],
    [2.0000, 0.2622],
    [3.0000, 0.6028],
    [4.0000, 0.7112],
    [5.0000, 0.2217],
    [6.0000, 0.1174],
    [7.0000, 0.2967],
    [8.0000, 0.3188],
    [9.0000, 0.4242],
   [10.0000, 0.5079]]
value = 0.5
#X = [[-4, -2.59625884456571],[-2, -0.696958389857672],[-1, 0.908181747039582]]
with open("newton.txt", "w") as result:
    newton(value, X, result)[1]