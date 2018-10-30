#!/bin/python3

from prettytable import PrettyTable

def newJacobi(x0):
    return x0

def norma(x0, x1):
    error = 0
    return error

def jacobi(tolerance, x0, iterations):
    title = ['n']
    aux = 0
    cont = 0
    while aux < len(x0):
        title.append("x"+str(aux))
        aux += 1
    title.append("Error")
    table = PrettyTable(title)
    table.add_row([cont] + x0 + ["Doesn't exist"])
    error = tolerance + 1
    while error < tolerance and cont < iterations:
        x1 = newJacobi(x0)
        error = norma(x0, x1)
        table.add_row([cont] + x1 + [error])
        x0 = x1
        cont += 1
    print(table)

jacobi(1, [0,0,0], 10)
    