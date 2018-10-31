#!/bin/python3

from copy import deepcopy, copy
from pandas import DataFrame

class Total_pivoting:
    marks = []

    def stepped(self, A, b):
        global marks
        aux = deepcopy(A)
        Ab = self.aumMatrix(A, b)
        n = len(Ab)
        marks = []
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
                for x in range(i):
                    aux.pop(x)
                for y in aux:
                    for w in range(i):
                        y.pop(w)
            cont += 1
        return Ab

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
        print(marks)
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
        return vector

totalpiv = Total_pivoting()

m = [[1, 2.3, 4],[0.5, 2, 1], [4,5,6]]
b = [1,1,1,1]
#m = [[-7,2,-3,4], [5,-1,14,-1], [1,9,-7,13], [-12,13,-8,-4]]
#b = [-12,13,31,-32]
matrix = totalpiv.stepped(m, b)
print(DataFrame(matrix))
print("\nMarcas:")
print(marks)
vector = totalpiv.clear(matrix, marks)
print("Las variables están en el vector de manera decendente: x4, x3, x2, x1 a menos que el vector de marcas haya cambiado\n")
print(vector)
