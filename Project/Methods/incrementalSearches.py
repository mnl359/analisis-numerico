#!/bin/python3
import math


def f(number):
    fx = math.exp((3*number)-12) + (number * math.cos(3*number)) - (number**2) + 4
    return fx


def incremental_searches(x0, delta, iterations):
    fx = f(x0)
    root = 0
    if fx == 0:
        root = x0
    else:
        x1 = x0 + delta
        cont = 1
        fx1 = f(x1)
        while fx * fx1 > 0 and cont < iterations:
            x0 = x1
            fx = fx1
            x1 = x0 + delta
            fx1 = f(x1)
            cont += 1

        if fx1 == 0:
            root = x1
        elif fx * fx1 < 0:
            root = (x0,x1)
        else:
            root = None
    return root


print(incremental_searches(-10, 1, 20))
