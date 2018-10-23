#!/bin/python3

from prettytable import PrettyTable

res = []

def bn(iterations):
    global res
    aux = iterations + 1
    y = iterations - 1
    for x in range(1, aux):
        res[iterations][x+1] = (res[iterations-1][x] - res[iterations][x])/(res[y][0] - res[iterations][0])
        y -= 1

def newton(x, matrix):
    global res
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
        mult = mult * (x - matrix[iteration][0])
        pol += (b*mult)
        table.add_row(res[iteration])
    print(table)
    return pol

m = [[2, -4.610943901069350],[2.2, -4.174986500565880],[2.4, -3.376823619358400],[2.6, -2.136261964998310],[2.8, -0.355353228902949]]
value = 1
print(newton(value, m))