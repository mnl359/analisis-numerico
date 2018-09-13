#!/bin/python3

from pprint import PrettyPrinter, pprint
        
def multiply(m, n):
    if len(m[0]) != len(n):
        print("Las dimensiones de las matrices no son compatibles")
        exit(1)
    result = []
    for col in range(len(m)):
        aux = []
        column = 0
        while column != len(n[0]):
            pos = 0
            row = 0
            while row != len(n):
                pos += m[col][row] * n[row][column]
                row += 1
            aux.append(pos)
            column += 1
        result.append(aux)
    for x in result:
            print(*x, sep=" ")

first_rows = int(input("Enter number of rows in the first matrix: "))
first_columns = int(input("Enter number of columns in the first matrix: "))
first_matrix = []
print("Enter the %s x %s matrix: "% (first_rows, first_columns))
print("Separe each number with a space and to change the row press ENTER")
for i in range(first_rows):
        first_matrix.append(list(map(int, input().rstrip().split())))
second_rows = int(input("Enter number of rows in the second matrix: "))
second_columns = int(input("Enter number of columns in the second matrix: "))
second_matrix = []
print("Enter the %s x %s matrix: "% (second_rows, second_columns))
print("Separe each number with a space and to change the row press ENTER")
for j in range(second_rows):
        second_matrix.append(list(map(int, input().rstrip().split())))
print("The result matrix is:")
m = multiply(first_matrix, second_matrix)
