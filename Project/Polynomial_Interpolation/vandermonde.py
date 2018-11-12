#!/bin/python3

from numpy import polynomial
from numpy import vander
from pandas import DataFrame

# El método principal es main
# Devuelve la matriz de Vandermonde, la matriz final después de 
# toda la eliminación gaussiana y por último el vector que tiene
# los coeficientes del polinomio

def create_array(arr, length):
    arr = [0 for x in range(length)]
    return arr

def aumMatrix(A, b):
    cont = 0
    for i in A:
        i.append(b[cont])
        cont += 1
    return A

def swapping_lower(A, column, i):
    for k in range(0, i):
        if column[k] == 1:
            aux = A[k]
            A[k] = A[i]
            A[i] = aux
            break

def lower_triangular(A):
    rows = len(A) 
    columns = len(A[0])

    x = 0
    y = 0
    if rows == columns:
        x = columns - 1
        y = x - 1
    else:
        x = columns - 2
        y = x 

    for i in range (x, -1, -1):
        for j in range (y, -1, -1):
            if i == j:
                column = [row[i] for row in A]
                if A[j][i] == 0:
                    for k in range(i - 1, -1 , -1):
                        if 1 in column:
                            swapping_lower(A, column, i)
                            break
                        elif column[k] != 0:
                            aux = A[k]
                            A[k] = A[i]
                            A[i] = aux
                            break
                
                helper = A[i][j]
                if helper != 1: 
                    if helper == 0:
                        print("WARNING! It's not possible to step the matrix. Error in row", i)
                        exit(1)
                    row = A[i]             
                    for k in range(len(row)):
                        row[k] = row[k] / helper
                    A[i] = row
            else:
                helper = A[j][i]
                if helper != 0:
                    row1 = A[i]
                    row2 = A[j]
                    for k in range(0, len(row2)):
                        row2[k] += ((-1 * helper) * row1[k])
                    A[j] = row2

    return A

def upper_triangular(A):
    rows = len(A) 
    columns = len(A[0])
    for i in range (columns):
        for j in range (i, rows):
            if i == j:
                column = [row[i] for row in A]
                lenColumn = len(column)
                if A[i][i] == 0:
                    for k in range(i, lenColumn):
                        if column[k] != 0:
                            aux = A[k]
                            A[k] = A[i]
                            A[i] = aux
                            break
                helper = A[i][j]
                if helper != 1: 
                    if helper == 0:
                        print("WARNING! It's not possible to step the matrix. Error in row", i)
                        exit(1)
                    row = A[i]             
                    for k in range(len(row)):
                        row[k] = row[k] / helper
                    A[i] = row

            else:
                helper = A[j][i]
                mult = helper / A[i][i]
                row1 = A[i]
                row2 = A[j]
                for k in range(0, len(row2)):
                    row2[k] -= (mult*row1[k])
                A[j] = row2
    return A


def clear(stepMat, n):
    vector = []
    vector = create_array(vector, n)
    vector[n-1]=stepMat[n-1][n]/stepMat[n-1][n-1]
    i = n-2
    while i >= 0:
        result = 0
        p = len(vector)-1
        while p >= 0:
            result += (stepMat[i][p]*vector[p])
            p -= 1
        vector[i] = (stepMat[i][n]-result)/stepMat[i][i]
        i -= 1
    return vector


def vandermonde(A):
    for i in range(len(A)):
        if len(A[i]) != 2:
            return(1, "Error, you have not given points to create the polynomial")
    #V = polynomial.polynomial.polyvander(A, deg)
    rows = len(A)
    columns = len(A[0])
    x_points = []
    y_points = []
    x_points = create_array(x_points, rows)
    y_points = create_array(y_points, rows)

    for i in range(columns):
        for j in range(rows):
            if i == 0:
                x_points[j] = A[j][i]
            else:
                y_points[j] = A[j][i]

    V = vander(x_points)
    V = V.tolist()
    
    augmented = aumMatrix(V, y_points)
    res = upper_triangular(augmented)
    res = lower_triangular(res)

    return res, augmented
    
def main(A):
    augMatrix = vandermonde(A)[1]
    resMatrix = vandermonde(A)[0]
    vector = clear(resMatrix, len(resMatrix))

    return augMatrix, resMatrix, vector   



# name = input("Enter the name of the file you want the answer to be saved. It's going to have '.txt' extension: ")
# matrix_rows = int(input("Please, enter the amount of points you want to use to create the polynomial: "))
# matrix = []
# print("Enter the %s x %s matrix: "% (matrix_rows, 2))
# print("Separe each number with a space and press ENTER to change the row ")
# for j in range(matrix_rows):
#         matrix.append(list(map(float, input().rstrip().split())))
# print("You will find the result in " + name + ".txt")
# with open(name + ".txt", "w") as result:
#     print("The matrix you entered is:", file=result)
#     print(DataFrame(matrix), file=result)
#     print("\n", file=result)
#     A = vandermonde(matrix, result)
#     print("\n", file=result)
#     print("The resulting matrix after Gaussian elimination is: \n",file=result)
#     print(DataFrame(A), file=result)
#     vector = clear(A, len(A))
#     cont = len(vector) - 1
#     str_res = "p(x) = "
#     for i in range(len(vector)):
#         if cont == 0:
#             if vector[i] > 0:
#                 str_res += "+" + str(vector[i])
#             else:
#                 str_res += str(vector[i])
#         elif vector[i] > 0:
#             str_res += "+" + str(vector[i]) + "x^" + str(cont) + " "
#         else:
#             str_res += str(vector[i]) + "x^" + str(cont) + " "
#         cont -= 1
#
#     print("\n", str_res, "\n", file=result)
