#!/bin/python3

from copy import deepcopy, copy
from pandas import DataFrame
from numpy import linalg as LA

# Retorna 0 (exitoso), matriz escalonada y vector resultado. 
# El metodo que retorna lo anterior es 'main'

class Gauss:
    def stepped(self, A, b):
        if LA.det(A) == 0:
            return 0
        try:
            LA.inv(A)
        except LA.LinAlgError:
            return -1
        Ab = self.aumMatrix(A, b)
        n = len(Ab)
        for i in range(0, n):
            for j in range(i, n):
                if i == j:
                    column = [row[i] for row in Ab]
                    lenColumn = len(column)
                    if Ab[i][i] == 0:
                        for k in range(i, lenColumn):
                            if column[k] != 0:
                                aux = Ab[k]
                                Ab[k] = Ab[i]
                                Ab[i] = aux
                                break

                    helper = Ab[i][i]
                    if helper == 0:
                        return 1

                else:
                    helper = Ab[j][i]
                    mult = helper / Ab[i][i]
                    row1 = Ab[i]
                    row2 = Ab[j]
                    for k in range(0, len(row2)):
                        row2[k] -= (mult * row1[k])
                    Ab[j] = row2
        return Ab

    def aumMatrix(self, A, b):
        cont = 0
        for i in A:
            i.append(b[cont])
            cont += 1
        return A

    def clear(self, stepMat, n):
        vector = []
        for x in range(n):
            vector.append(0)
        vector[n - 1] = stepMat[n - 1][n] / stepMat[n - 1][n - 1]
        i = n - 2
        while i >= 0:
            result = 0
            p = len(vector) - 1
            while p >= 0:
                result += (stepMat[i][p] * vector[p])
                p -= 1
            vector[i] = (stepMat[i][n] - result) / stepMat[i][i]
            i -= 1
        return vector

    def main(self, A, b):
        matrix = self.stepped(A, b)
        if matrix == -1:
            return 1, "Matrix is not invertible"
        elif matrix == 1:
            return 1, "It's not possible to step the matrix"
        elif matrix == 0:
            return 1, "The matrix is not well conditioned. Determinant is ZERO"
        n = len(matrix)
        vector = self.clear(matrix, n)
        return 0, matrix, vector

# gauss = Gauss()
# name = input("Enter the name of the file you want the answer to be saved. It's going to have '.txt' extension: ")
# matrix_rows = int(input("As this has to be a square matrix, the number of rows is going to be the same number of columns. \
#                 \nEnter number of rows in the matrix: "))
# matrix = []
# vector = []
# print("Enter the %s x %s matrix: "% (matrix_rows, matrix_rows))
# print("Separe each number with a space and to change the row press ENTER")
# for j in range(matrix_rows):
#         matrix.append(list(map(float, input().rstrip().split())))
# print("Enter de vector. Separe each number with a space")
# vector.append(list(map(float, input().rstrip().split())))
# vector = vector[0]
# print("You will find the result in " + name + ".txt")
# matrix_aux = deepcopy(matrix)
# vector_aux = copy(vector)
# with open(name + ".txt", "w") as result:
#     A = gauss.clear(gauss.stepped(matrix_aux, vector_aux), len(matrix))
#     num = 1
#     for x in A:
#         print("x" + str(num) + " = " + str(x), file=result)
#         num += 1
#     print("\n", file=result)
#     print("The matrix was:" , file=result)
#     print(DataFrame(aumMatrix(matrix, vector)), file=result)
