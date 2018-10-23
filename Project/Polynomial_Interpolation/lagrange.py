#!/bin/python3

res = []

def l(value, i, matrix):
    global res
    x = 0
    num = 1
    while x < len(matrix):
        if x != i:
            num = num * (value - matrix[x][0])
        x+=1
    print(num)
    y = 0
    den = 1
    while y < len(matrix):
        if x != i:
            num = num * (matrix[i][0] - matrix[y][0])
        y+=1
    return num/den

def lagrange(x, matrix):
    pol = 0
    for i in range(len(matrix)):
        ln = l(x, i, matrix)
        pol += ln*matrix[i][1]
    return pol

m = [[2, -4.610943901069350],[2.2, -4.174986500565880],[2.4, -3.376823619358400],[2.6, -2.136261964998310],[2.8, -0.355353228902949]]
value = 2.5
print(lagrange(value, m))
