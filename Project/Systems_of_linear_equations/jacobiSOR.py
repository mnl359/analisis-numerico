#!/bin/python3

from pandas import DataFrame
from numpy import linalg, diag, tril, triu, transpose, matrix, asarray, matmul
from scipy import linalg as LA
from decimal import Decimal
from prettytable import PrettyTable

# Retorna 0 (exito), vector resultado, tabla de iteraciones, número de iteraciones, pasos
# Pasos: matriz de transición, radio espectral

def aumMatrix(A, b):
    cont = 0
    for i in A:
        i.append(b[cont])
        cont += 1
    return A

def jacobi_SOR(A, b, x, w, iter, tol):
    title = ['Iteration']
    aux = 0
    while aux < len(x):
        title.append("x"+str(aux))
        aux += 1
        
    title.append("Error")
    table = PrettyTable(title)
    result = [title]

    n = len(A)
    det = linalg.det(A)
    if det == 0:
        return(1, "The system does not have an unique solution. Determinant is ZERO")
    
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
    RE = 0
    if a == 2:
        RE = max(abs(LA.eigvals(t_matrix)))
        if RE > 1:
            #print("The spectral radio is larger than 1 (" + str(RE) + "). Method won't converge", file=toPrint)
            return (1, "The spectral radio is larger than 1 (" + str(RE) + "). Method won't converge\n \
                    The matrix is not dominant on its diagonal")
            #a = 2
        else:
            #print("The method converges and its spectral radio is " + str(RE), file=toPrint)
            a = 1
    
    if a == 1:
        cont = 0
        table.add_row([cont] + x + ["Doesn't exist"])
        result.append([cont] + x + ["Doesn't exist"])
        x = transpose(x)
        tolerance = tol + 1
        while cont < iter and tolerance > tol:
            xi = (matmul(t_matrix, x)) + c_matrix
            tolerance = linalg.norm(xi - x)
            cont += 1
            table.add_row([cont] + xi.tolist() + ['%.2E' % Decimal(str(tolerance))])
            result.append([cont] + xi.tolist() + ['%.2E' % Decimal(str(tolerance))])
            x = xi
        
        #print("The aproximation to X vector with %s iterations is" %cont, file=toPrint)
        #for i in range(n):
        #    print("x" + str(i) + " = ", x[i], file=toPrint)
        #    #print(i, x[i])
        #print("\n", file=toPrint)
        
        #R = matmul(A, x)
        #print("The best aproximation you can get of vector 'b' is", file=toPrint)
        #for i in range(n):
        #    print("b" + str(i) + " = ", R[i], file=toPrint)
        
    #elif a == 2:
    #    print("The method does not converge because the matrix is not dominant on its diagonal", file=toPrint)
    return 0, x.tolist(), result, cont, t_matrix, RE


#A = [
#    [9.1622,    0.4505,    0.1067,    0.4314,    0.8530,    0.4173,    0.7803,    0.2348,    0.5470,    0.5470],
#    [0.7943,    9.0838,    0.9619,    0.9106,    0.6221,    0.0497,    0.3897,    0.3532,    0.2963,    0.7757],
#    [0.3112,    0.2290,    9.0046,    0.1818,    0.3510,    0.9027,    0.2417,    0.8212,    0.7447,    0.4868],
#    [0.5285,    0.9133,    0.7749,    9.2638,    0.5132,    0.9448,    0.4039,    0.0154,    0.1890,    0.4359],
#    [0.1656,    0.1524,    0.8173,    0.1455,    9.4018,    0.4909,    0.0965,    0.0430,    0.6868,    0.4468],
#    [0.6020,    0.8258,    0.8687,    0.1361,    0.0760,    9.4893,    0.1320,    0.1690,    0.1835,    0.3063],
#    [0.2630,    0.5383,    0.0844,    0.8693,    0.2399,    0.3377,    9.9421,    0.6491,    0.3685,    0.5085],
#    [0.6541,    0.9961,    0.3998,    0.5797,    0.1233,    0.9001,    0.9561,    9.7317,    0.6256,    0.5108],
#    [0.6892,    0.0782,    0.2599,    0.5499,    0.1839,    0.3692,    0.5752,    0.6477,    9.7802,    0.8176],
#    [10.0000,    0.4427,    0.8001,    0.1450,    0.2400,    0.1112,    0.0598,    0.4509,    0.0811,   20.0000]  
#    ]
#
#
#b = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#tol=1e-07 
#w=1.4000
#X0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#fileToPrint = "jacobiSOR.txt"
#with open(fileToPrint, "w") as result:
#    print(jacobi_SOR(A, b, X0, w, 1000, tol, result), file=result)

