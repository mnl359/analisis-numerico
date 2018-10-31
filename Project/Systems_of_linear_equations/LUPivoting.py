#!/bin/python3

from copy import deepcopy, copy
from pandas import DataFrame

class LU_pivoting:
    mults = []
    marks = []

    def create_matrix(self, arr, lenMatrix):
        arr = [[0 for x in range(lenMatrix)] for y in range(lenMatrix)]
        return arr

    def aumMatrix(self, A, b):
        cont = 0
        for i in A:
            i.append(b[cont])
            cont += 1
        return A

    def exchange_rows(self, i, k, A):
        aux = A[i]
        A[i] = A[k]
        A[k] = aux
        return A

    def multiply(self, m, n):
        if len(m[0]) != len(n):
            print("Dimensions are not compatible")
            exit(1)
        result = []
        for col in range(len(m)):
            aux = []
            column = 0
            while column != 1:
                pos = 0
                row = 0
                while row != len(n):
                    pos += m[col][row] * n[row]
                    row += 1
                aux.append(pos)
                column += 1
            result.append(aux)

        return result

    def upper_triangular(self, A):
        global mults
        global marks

        n = len(A)
        mults = self.create_matrix(mults, n)
        marks = self.create_matrix(marks, n)

        for i in range(n):
            marks[i][i] = 1

        for i in range(n):
            for j in range(i, n):
                if i == j:
                    # mults[i][i] = 1
                    column = [row[i] for row in A]
                    lenColumn = len(column)
                    helper = abs(A[i][i])
                    cont = i
                    for k in range(i, lenColumn):
                        if abs(column[k]) > helper:
                            helper = abs(column[k])
                            cont = k
                    A = self.exchange_rows(i, cont, A)
                    marks = self.exchange_rows(i, cont, marks)
                    mults = self.exchange_rows(i, cont, mults)

                    if A[i][i] == 0:
                        print("WARNING! It's not possible to step the matrix. Error in row ", i)
                        exit(1)

                else:
                    helper = A[j][i]
                    mult = helper / A[i][i]
                    mults[j][i] = round(mult, 15)
                    row1 = A[i]
                    row2 = A[j]
                    for k in range(n):
                        row2[k] -= (mult * row1[k])
                        row2[k] = round(row2[k], 10)
                    A[j] = row2

        for i in range(n):
            mults[i][i] = 1

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

    def lu_pivoting(self, A, vector, toPrint):
        u_matrix = self.upper_triangular(A)
        print("The U matrix is:", "\n", DataFrame(u_matrix), "\n", file=toPrint)
        l_matrix = mults
        print("The L matrix is:", "\n", DataFrame(l_matrix), "\n", file=toPrint)
        aux = self.multiply(marks, vector)
        helper = [aux[i][0] for i in range(len(aux))]
        # print(helper, "\n")
        Lz = self.aumMatrix(l_matrix, helper)
        vector_z = self.progressive_substitution(Lz)
        # print(vector_z, "\n")
        Ux = self.aumMatrix(u_matrix, vector_z)
        result = self.regressive_substitution(Ux)
        return result

#A = [[-7, 2, -3, 4], [5, -1, 14, -1], [1, 9, -7, 5], [-12, 13, -8, -4]]
#b = [-12, 13, 31, -32]

#A = [[2, -3, 4, 1], [-4, 2, 1, -2], [1, 3, -5, 3], [-3, -1, 1, -1]]
#b = [10, -10, 32, -21]

#print(lu_pivoting(A, b))

lupivot = LU_pivoting()

name = input("Enter the name of the file you want the answer to be saved. It's going to have '.txt' extension: ")
matrix_rows = int(input("As this has to be a square matrix, the number of rows is going to be the same number of columns. \
                \nEnter number of rows in the matrix: "))
matrix = []
vector = []
print("Enter the %s x %s matrix: "% (matrix_rows, matrix_rows))
print("Separe each number with a space and to change the row press ENTER")
for j in range(matrix_rows):
        matrix.append(list(map(float, input().rstrip().split())))
print("Enter de vector. Separe each number with a space")
vector.append(list(map(float, input().rstrip().split())))
vector = vector[0]
print("You will find the result in " + name + ".txt")
matrix_aux = deepcopy(matrix)
vector_aux = copy(vector)
with open(name + ".txt", "w") as result:
    print("The augmented matrix is:" , file=result)
    print(DataFrame(lupivot.aumMatrix(matrix, vector)), file=result)
    print("\n", file=result)
    A = lupivot.lu_pivoting(matrix_aux, vector_aux, result)
    print("The result of each variable is: ", file=result)
    num = 1
    for x in A:
        print("x" + str(num) + " = " + str(x), file=result)
        num += 1
