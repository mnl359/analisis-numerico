#!/bin/python3
import math


def f(number):
    #fx = math.exp((3*number)-12) + (number * math.cos(3*number)) - (number**2) + 4
    #fx = (2 * (number**2)) + (3 * number) - 3
    #fx = (number*(math.exp(number))) - (number**2) - (5*number) -3
    fx = (math.exp(-number)) - math.cos(4*number)
    return fx


def incremental_searches(x0, delta, iterations):
    fx = f(x0)
    root = 0
    roots = []
    if fx == 0:
        root = x0
        roots.append(x0)
    else:
        x1 = x0 + delta
        cont = 1
        fx1 = f(x1)
        while cont < iterations:
            x0 = x1
            fx = fx1
            x1 = x0 + delta
            fx1 = f(x1)
            cont += 1
            if fx1 == 0:
                root = x1
                roots.append(x1)
            elif fx * fx1 < 0:
                root = (x0,x1)
                roots.append(root)
            else:
                root = None
    return roots


print(incremental_searches(-6, 1, 9))
