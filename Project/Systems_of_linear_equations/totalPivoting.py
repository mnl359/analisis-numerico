#!/bin/python3

from copy import deepcopy, copy
from pandas import DataFrame
from numpy import linalg as LA

# La función principal es main
# Esta función retorna 0 (exitoso), la matriz escalonada, el vector de marcas y el vector resultado

class Total_pivoting:
    marks = []

    def stepped(self, A, b):
        if LA.det(A) == 0:
            return 0, 0
        try:
            LA.inv(A)
        except LA.LinAlgError:
            return -1, -1
        marks = []
        aux = deepcopy(A)
        Ab = self.aumMatrix(A, b)
        n = len(Ab)
        cont = 0
        for x in range(1, len(aux[0]) + 1):
            marks.append(x)
        for i in range(1, n):
            biggest = self.biggestNumber(Ab, cont, cont)
            mult = Ab[biggest[0]][biggest[1]]
            if biggest[0] != 0:
                Ab = self.changeRows(Ab, biggest[0], cont)
            if biggest[1] != 0:
                Ab = self.changeColumns(Ab, biggest[1], cont)
                marks = self.changeMarks(marks, biggest[1], cont)
            Ab = self.multiply(Ab, mult, i)
            aux = deepcopy(Ab)
            k = len(aux)
            if len(aux) - 1 > i:
                for m in aux:
                    m.pop(k)       
                x = 0
                helper = i - x
                while x < helper:
                    aux.pop(x)
                    x += 1
                    helper = i - x
                for y in aux:
                    w = 0
                    helper = i - w
                    while w < helper:
                        y.pop(w)
                        w += 1
                        helper = i - w
            cont += 1
        return Ab, marks

    def biggestNumber(self, A, row_min, col_min):
        biggest = 0
        biggest_row = 0
        biggest_col = 0
        for i in range(row_min, len(A)):
            for j in range(col_min, len(A[0]) - 1):
                if abs(A[i][j]) > biggest:
                    biggest = abs(A[i][j])
                    biggest_col = j
                    biggest_row = i
        return biggest_row, biggest_col

    def multiply(self, Ab, multi, i):
        i -= 1
        for j in range(i + 1, len(Ab)):
            helper = Ab[j][i]
            mult = helper / multi
            row1 = Ab[i]
            row2 = Ab[j]
            for k in range(0, len(row2)):
                aux = round(mult * row1[k], 9)
                row2[k] = round(row2[k], 9) - aux
            Ab[j] = row2
        return Ab

    def changeRows(self, Ab, biggest_row, i):
        aux = Ab[biggest_row]
        Ab[biggest_row] = Ab[i]
        Ab[i] = aux
        return Ab

    def changeColumns(self, Ab, biggest_col, i):
        for x in Ab:
            aux = x[i]
            x[i] = x[biggest_col]
            x[biggest_col] = aux
        return Ab

    def changeMarks(self, marks, biggest_col, i):
        aux = marks[i]
        marks[i] = marks[biggest_col]
        marks[biggest_col] = aux
        return marks

    def aumMatrix(self, A, b):
        cont = 0
        for i in A:
            i.append(b[cont])
            cont += 1
        return A

    def clear(self, stepMat, marks):
        vector = []
        n = len(stepMat)
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
        print(vector)
        print(marks)
        helper = [0 for i in range(len(vector))]  
        for i in range(len(marks)):
            helper[marks[i] - 1] = vector[i]

        return helper

    def main(self, A, b):
        matrix, marks = self.stepped(A, b)
        if matrix == -1:
            return 1, "The matrix is not invertible"
        elif matrix == 0:
            return 1, "The matrix is not well conditioned. Determinant is ZERO"
        vector = self.clear(matrix, marks)
        print(vector)
        return 0, matrix, marks, vector


#totalpiv = Total_pivoting()

#m = [[1, 2.3, 4],[0.5, 2, 1], [4,5,6]]
#b = [1,1,1,1]
#A = [[2, -3, 4, 1], [-4, 2, 1, -2], [1, 3, -5, 3], [-3, -1, 1, -1]]
#b = [10, -10, 32, -21]

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
#b = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#
#
#fileToPrint = "totalPivoting.txt"
#with open(fileToPrint, "w") as result:
#    matrix = totalpiv.stepped(A, b)
#    print(DataFrame(matrix), "\n", file=result)
#    vector = totalpiv.clear(matrix, marks)
#    print(vector, file=result)


# m = [[1, 2.3, 4],[0.5, 2, 1], [4,5,6]]
# b = [1,1,1,1]
# #m = [[-7,2,-3,4], [5,-1,14,-1], [1,9,-7,13], [-12,13,-8,-4]]
# #b = [-12,13,31,-32]
# matrix = totalpiv.stepped(m, b)
# print(DataFrame(matrix))
# print("\nMarcas:")
# print(marks)
# vector = totalpiv.clear(matrix, marks)
# print("Las variables están en el vector de manera decendente: x4, x3, x2, x1 a menos que el vector de marcas haya cambiado\n")
# print(vector)
