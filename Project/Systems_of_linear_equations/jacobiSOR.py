#!/bin/python3

from copy import deepcopy, copy
from pandas import DataFrame
from numpy import linalg
from numpy import diag
from numpy import tril
from numpy import triu
from numpy import transpose
from numpy import matrix
from numpy import asarray
from numpy import matmul
from scipy import linalg as LA
import texttable as tt
from decimal import Decimal

def aumMatrix(A, b):
    cont = 0
    for i in A:
        i.append(b[cont])
        cont += 1
    return A

def jacobi_SOR(A, b, x, w, iter, tol):
    table = tt.Texttable()
    headers = ['Iteration', 'Error']
    table.header(headers)

    n = len(A)
    det = linalg.det(A)
    if det == 0:
        print("The system does not have an unique solution")
        exit(1)
    
    diagonal_matrix = diag(diag(A))
    l_matrix = diagonal_matrix - tril(A)
    u_matrix = diagonal_matrix - triu(A)
    helper = diagonal_matrix - (w * l_matrix)
    helper2 = ((1- w) * diagonal_matrix) + (w * u_matrix)

    power = linalg.matrix_power(helper, -1)
    t_matrix = matmul(power, helper2)
    trans = transpose(b) * w
    c_matrix = matmul(power, trans)

    Z = [[abs(A[i][j]) for i in range(n)] for j in range(n)]
    helper3 = asarray(Z)
    suma = helper3.sum(axis=1)
    a = 0
    
    for i in range(n):      
        aux2 = (2*(Z[i][i]))
        if all(aux2 > suma):
            a = 1 
        else:
            a = 2
    
    if a == 2:
        RE = max(abs(LA.eigvals(t_matrix)))
        if RE > 1:
            print("The spectral radio is larger than 1 (" + str(RE) + "). Method won't converge")
            a = 2
        else:
            print("The method converges and its spectral radio is " + str(RE))
            a = 1
    
    if a == 1:
        cont = 0
        tolerance = tol + 1
        x = transpose(x)
        error_vector = []
        while cont < iter and tolerance > tol:
            xi = (matmul(t_matrix, x)) + c_matrix
            tolerance = linalg.norm(xi - x)
            cont += 1
            x = xi
            error_vector.append(tolerance)
        
        print("The aproximation to X vector with %s iterations is" %cont)
        for i in range(n):
            print("x" + str(i) + " = ", x[i])
            #print(i, x[i])
        print("\n")
        
        R = matmul(A, x)
        print("The best aproximation you can get of vector 'b' is")
        for i in range(n):
            print("b" + str(i) + " = ", R[i])
        
        print("\n")
        error_vector = transpose(error_vector)
        lenError = len(error_vector)
        print("Iteration Error")
        for i in range(lenError):
            m = '%.2E' % Decimal(str(error_vector[i]))
            table.add_row([i, m])
    elif a == 2:
        print("The method does not converge because the matrix is not dominant on its diagonal")
    s = table.draw()
    print(s)
    print("The error in the last iteration (%s) is " %cont, error_vector[lenError - 1])
    return x

A = [[3, -1, 1], [-1, 3, -1], [1, -1, 3]]
b = [-1, 7, -7]
w = 1.25
x = [0, 0, 0]

print(jacobi_SOR(A, b, x, w, 100, 5e-06))

