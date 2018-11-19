#!/bin/python3

from prettytable import PrettyTable
from sympy import Symbol, expand, simplify, factor, init_printing
from numpy import linalg as LA 

# El método principal es Newton
# Retorna 0 (exitoso), el resultado del polinomio en el número que se quiere evaluar, 
# el polinomio en términos de x, la tabla de diferencias divididas y el número de iteraciones


res = []
zero = 0

def bn(iterations):
    global res
    global zero
    aux = iterations + 1
    y = iterations - 1
    for x in range(1, aux):
        den = res[y][0] - res[iterations][0]
        if den == 0:
            print(den, x)
            zero = -1
            break
        res[iterations][x+1] = (res[iterations-1][x] - res[iterations][x])/den
        y -= 1

def newton(value, matrix):
    #try:
    #    LA.inv(matrix)
    #except LA.LinAlgError:
    #    return 1, "Matrix is not invertible"
    global res
    global zero
    n = len(matrix) - 1
    for i in range(n):
        if(matrix[i+1][0] < matrix[i][0]):
            return(1, "The set of dots must be arranged in ascending order with respect to their X component. Problem found at: " + str(i)) 
        elif(matrix[i+1][0] == matrix[i][0]):
            return(1, "All dots must be different. Problem found at: " + str(i) + " and " + str(i + 1))
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
    tableList = [title]
    b0 = matrix[0][1]
    mult = 1
    pol = b0
    table.add_row(res[0])
    tableList.append(res[0])
    for iteration in range(1,n):
        if zero == -1:
            return 1, "Division by zero"
        bn(iteration)
        b = res[iteration][iteration+1]
        #print(mult * (x - matrix[iteration-1][0]))
        mult = expand(mult * (x - matrix[iteration-1][0]))
        pol += (b*mult)
        table.add_row(res[iteration])
        tableList.append(res[iteration])
    #print(table, file=txt)
    #print("El polinomio resultante es:\n %s" % pol, file=txt)
    result = pol.evalf(subs={x:value})
    #print("El resultado de p(%s) es igual a %s" % (value, result), file=txt)
    return 0, result, pol, tableList, iteration

#X =[
#    [1.0000, 0.5949],
#    [2.0000, 0.2622],
#    [3.0000, 0.6028],
#    [4.0000, 0.7112],
#    [5.0000, 0.2217],
#    [6.0000, 0.1174],
#    [7.0000, 0.2967],
#    [8.0000, 0.3188],
#    [9.0000, 0.4242],
#   [10.0000, 0.5079]]
#value = 0.5
#
#print(newton(value, X))
#X = [[-4, -2.59625884456571],[-2, -0.696958389857672],[-1, 0.908181747039582]]
#with open("newton.txt", "w") as result:
#    newton(value, X, result)[1]