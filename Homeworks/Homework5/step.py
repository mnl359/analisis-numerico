#!/bin/python3

def stepped(A):
    n = len(A) 
    if n != len(A[0]):
        print("The matrix has to be squared")
        exit(-1)
    for i in range (0, n):
        for j in range (i, n):
            if i == j:
                column = [row[i] for row in A]
                lenColumn = len(column)
                if all(v == 0 for v in column):
                    continue
                if A[i][i] == 0 and i < n - 1:
                    for k in range(i + 1, lenColumn):
                        if 1 in column:
                            swapping(A, column, i)
                            break
                        elif column[k] != 0:
                            aux = A[k]
                            A[k] = A[i]
                            A[i] = aux
                            break
                
                helper = A[i][i]
                if helper != 1: 
                    if helper == 0 and i == n - 1:
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

def swapping(A, column, i):
    for k in range(i + 1, len(column)):
        if column[k] == 1:
            aux = A[k]
            A[k] = A[i]
            A[i] = aux
            break


B = [[0, 1, 3, 4], [2, 0, 4, 5], [3, 3, 5, 7], [8, 3, 4, 2]]
#print(stepped(B))

name = input("Enter the name of the file you want the answer to be saved. It's going to have '.txt' extension: ")
matrix_rows = int(input("Enter number of rows in the matrix: \
                \nAs this has to be a square matrix, the number of rows is going to be the same number of columns. "))
#matrix_columns = int(input("Enter number of columns in the matrix: "))
matrix = []
print("Enter the %s x %s matrix: "% (matrix_rows, matrix_rows))
print("Separe each number with a space and to change the row press ENTER")
for j in range(matrix_rows):
        matrix.append(list(map(int, input().rstrip().split())))
print("You will find the result in " + name + ".txt")
with open(name + ".txt", "w") as result:
    print("The matrix is:", file=result)
    for x in matrix:
        print(*x, sep=" ", file=result)
    print("\n", file=result)
    A = stepped(matrix)
    for n in A:
        print(*n, sep=" ", file=result)
    print("The stepped matrix is: %s" % str(stepped(matrix)), file=result)

