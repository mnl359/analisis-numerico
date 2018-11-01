#!/bin/python3

from pandas import DataFrame
from copy import deepcopy, copy

class LU_gauss:
    mults = []

    def create_matrix_L(self, lenMatrix):
        global mults
        mults = [[0 for x in range(lenMatrix)] for y in range(lenMatrix)]

    def lower_triangular(self, A):
        n = len(A)
        if n != len(A[0]):
            print("The matrix has to be squared")
            exit(-1)
        for i in range(n - 1, -1, -1):
            for j in range(i, -1, -1):
                if i == j:
                    column = [row[i] for row in A]
                    if A[i][i] == 0:
                        for k in range(i - 1, -1, -1):
                            if 1 in column:
                                self.swapping_lower(A, column, i)
                                break
                            elif column[k] != 0:
                                aux = A[k]
                                A[k] = A[i]
                                A[i] = aux
                                break

                    helper = A[i][i]
                    if helper != 1:
                        if helper == 0:
                            print("WARNING! It's not possible to step the matrix. Error in row", i)
                            exit(1)
                        row = A[i]
                        for k in range(0, len(row)):
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

    def swapping_lower(self, A, column, i):
        for k in range(0, i):
            if column[k] == 1:
                aux = A[k]
                A[k] = A[i]
                A[i] = aux
                break

    def upper_triangular(self, A):
        global mults
        n = len(A)
        self.create_matrix_L(n)
        for i in range(0, n):
            for j in range(i, n):
                if i == j:
                    mults[i][i] = 1
                    column = [row[i] for row in A]
                    lenColumn = len(column)
                    if A[i][i] == 0:
                        for k in range(i, lenColumn):
                            if column[k] != 0:
                                aux = A[k]
                                A[k] = A[i]
                                A[i] = aux
                                break

                    helper = A[i][i]
                    if helper == 0:
                        print("WARNING! It's not possible to step the matrix. Error in row", i)
                        exit(1)

                else:
                    helper = A[j][i]
                    mult = helper / A[i][i]
                    mults[j][i] = mult
                    row1 = A[i]
                    row2 = A[j]
                    for k in range(0, len(row2)):
                        row2[k] -= (mult * row1[k])
                    A[j] = row2
        return A

    def progressive_substitution(self, stepMat):
        vector = []
        n = len(stepMat)
        for x in range(n):
            vector.append(0)
        vector[0] = stepMat[0][n] / stepMat[0][0]
        i = 1
        while i <= n - 1:
            result = 0
            p = 0
            while p <= len(vector) - 1:
                result += (stepMat[i][p] * vector[p])
                p += 1
            vector[i] = stepMat[i][n] - result / stepMat[i][i]
            i += 1
        return vector

    def regressive_substitution(self, stepMat):
        n = len(stepMat)
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

    def aumMatrix(A, b):
        cont = 0
        for i in A:
            i.append(b[cont])
            cont += 1
        return A

    def lu_gauss(self, A, vector):
        u_matrix = self.upper_triangular(A)
        print("The U matrix is: ", "\n", DataFrame(u_matrix), "\n", file=toPrint)
        l_matrix = mults
        print("The L matrix is: ", "\n", DataFrame(l_matrix), "\n", file=toPrint)
        Lz = self.aumMatrix(l_matrix, vector)
        vector_z = self.progressive_substitution(Lz)
        Ux = self.aumMatrix(u_matrix, vector_z)
        result = self.regressive_substitution(Ux)
        return l_matrix, u_matrix, result

#A = [[2, -3, 4, 1], [-4, 2, 1, -2], [1, 3, -5, 3], [-3, -1, 1, -1]]
#b = [10, -10, 32, -21]
#A = [[-7, 2, -3, 4], [5, -1, 14, -1], [1, 9, -7, 5], [-12, 13, -8, -4]]
#b = [-12, 13, 31, -32]
#print(lu_gauss(A, b))

# lugauss = LU_gauss()
#
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
#     print("The augmented matrix is:" , file=result)
#     print(DataFrame(lugauss.aumMatrix(matrix, vector)), file=result)
#     print("\n", file=result)
#     A = lugauss.lu_gauss(matrix_aux, vector_aux, result)[2]
#     print("The result of each variable is: ", file=result)
#     num = 1
#     for x in A:
#         print("x" + str(num) + " = " + str(x), file=result)
#         num += 1
    