#!/bin/python3

def stepped(A, b):
    Ab = aumMatrix(A, b)
    n = len(Ab) 
    for i in range (0, n):
        for j in range (i, n):
            if i == j:
                column = [row[i] for row in A]
                lenColumn = len(column)
                if all(v == 0 for v in column):
                    continue
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
                row1 = A[i]
                row2 = A[j]
                for k in range(0, len(row2)):
                    row2[k] -= (mult*row1[k])
                A[j] = row2
    
    return Ab  

def aumMatrix(A, b):
    cont = 0
    for i in A:
        i.append(b[cont])
        cont += 1
    return A

def clear(stepMat):
    n = len(stepMat)
    x = stepMat[]


name = input("Enter the name of the file you want the answer to be saved. It's going to have '.txt' extension: ")
matrix_rows = int(input("As this has to be a square matrix, the number of rows is going to be the same number of columns. \
                \nEnter number of rows in the matrix: "))
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
    A = stepped(matrix)
    for n in A:
        print(*n, sep=" ", file=result)
    print("The stepped matrix is: %s" % str(stepped(matrix)), file=result)

