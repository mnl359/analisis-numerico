#!/bin/python3

from pandas import DataFrame
from copy import deepcopy

def crout(matrix):
    l = []
    u = []
    ucont = 0
    for i in range(len(matrix)):
        laux = []
        uaux = []
        for j in range(len(matrix)):
            if j == ucont:
                uaux.append(1)
            else:
                uaux.append(0)
            laux.append(0)
        ucont += 1
        l.append(laux)
        u.append(uaux)
    n = len(matrix)
    for j in range(n):
        for i in range(j,n):
            sum = 0
            for k in range(j):
                sum = sum + l[i][k]*u[k][j]
            l[i][j] = matrix[i][j] - sum
        
        for i in range(j,n):
            sum = 0
            for k in range(j):
                sum = sum + l[j][k] * u[k][i]
            if l[j][j] == 0:
                print("Divided by 0")
                exit(1)
            u[j][i] = (matrix[j][i] - sum)/ l[j][j]
    
    return l, u

# name = input("Enter the name of the file you want the answer to be saved. It's going to have '.txt' extension: ")
# matrix_rows = int(input("As this has to be a square matrix, the number of rows is going to be the same number of columns. \
#                 \nEnter number of rows in the matrix: "))
# matrix = []
# print("Enter the %s x %s matrix: "% (matrix_rows, matrix_rows))
# print("Separe each number with a space and to change the row press ENTER")
# for j in range(matrix_rows):
#         matrix.append(list(map(float, input().rstrip().split())))
# matrix_aux = deepcopy(matrix)
# with open(name + ".txt", "w") as result:
#     mat = crout(matrix)
#     print("The L matrix is:" , file=result)
#     print(DataFrame(mat[0]), file=result)
#     print("\n", file=result)
#     print("The U matrix is:" , file=result)
#     print(DataFrame(mat[1]), file=result)
#     print("\n", file=result)