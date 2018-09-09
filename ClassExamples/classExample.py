#!/bin/python3
import math, sympy
from prettytable import PrettyTable
from decimal import Decimal

print("Para ingresar las funciones tome en cuenta la documentación de la biblioteca Math para \
Python 3 y, además de ello, verifique que, en caso de usar una función de esa biblioteca esté\
escrita en el formato math.<function> : ")
function = input("Ingrese la función: ")
x0 = input("Ingrese un x0: ")
delta = input("Ingrese un delta: ")
itera = input("Ingrese el número de iteraciones: ")
name = input("Ingrese el nombre del archivo en el que quiere se guarde el resultado.\
\nDebe tener en cuenta el archivo se guardará automáticamente con extensión .txt:")

searches = open(name + ".txt", "w")

def f(function, x):
    #fx = math.exp((3*number)-12) + (number * math.cos(3*number)) - (number**2) + 4
    #fx = (2 * (number**2)) + (3 * number) - 3
    #fx = (number*(math.exp(number))) - (number**2) - (5*number) -3
    fx = eval(function)
    #(math.exp(-number)) - math.cos(4*number)
    return fx


def incremental_searches(x0, delta, iterations, function):
    global searches
    table = PrettyTable(['Iteration','Xi','f(Xi)', 'Error'])
    fx = f(function, x0)
    root = 0
    roots = []
    if fx == 0:
        root = x0
        roots.append(x0)
    else:
        x1 = x0 + delta
        cont = 1
        fx1 = f(function, x1)
        table.add_row([cont, x0, fx, "Doesnt exist"])
        while cont < iterations:
            x0 = x1
            fx = fx1
            x1 = x0 + delta
            fx1 = f(function, x1)
            cont += 1
            error = abs(fx1 - fx)
            table.add_row([cont, x0, fx, '%.2E' % Decimal(str(error))])
            if fx1 == 0:
                root = x1
                roots.append(x1)
            elif fx * fx1 < 0:
                root = (x0,x1)
                roots.append(root)
            else:
                root = None  
    searches.write(str(table))      
    return roots


searches.write("\n" + str(incremental_searches(float(x0), float(delta), int(itera), function)))
print("Por favor revise el archivo " + name + ".txt " + "para ver el resultado")
