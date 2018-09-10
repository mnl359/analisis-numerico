#!/bin/python3


def f(x):
    return x


def aitken(x0, tolerance, iterations):

    cont = 0
    while error > tolerance and cont < iterations:
        x1 = f(x0)
        x2 = f(x1)

        denominator = (x2-x1) - (x1-x0)
        aux = x2-(((x2-x1)**2)/denominator)
        error = abs(aux-x2)
        x0 = aux
        cont += 1
