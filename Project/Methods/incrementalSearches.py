#!/bin/python3


def function(number):
    return (number**2)-1


def incremental_searches(x0, delta, iterations):
    fx = function(x0)
    root = 0
    if fx == 0:
        root = x0
    else:
        x1 = x0 + delta
        cont = 1
        fx1 = function(x1)
        while fx * fx1 > 0 and cont < iterations:
            x0 = x1
            fx = fx1
            x1 = x0 + delta
            fx1 = function(x1)
            cont += 1

        if fx1 == 0:
            root = x1
        elif fx * fx1 < 0:
            root = (x0,x1)
        else:
            root = None
        return root


print(incremental_searches(0, 0.1, 100))
