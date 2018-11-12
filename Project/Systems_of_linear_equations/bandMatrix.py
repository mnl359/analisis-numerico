#!/bin/python3

from copy import copy

# El método principal es main
# Retorna 0 (exitoso) y el vector resultado
# No hay matriz porque simplemente se ingresan 4 vectores, a partir de los cuales se hacen los cálculos. 

def band_matrix(a, b, c, d):
    n = len(d)

    for k in range(n - 1):
        m = a[k] / b[k]
        b[k + 1] -= (m * c[k])
        d[k + 1] -= (m * d[k])
    
    return b, d


def regressive_substitution_trid(b, c, d):
    n = len(d)
    x = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        if i == n - 1:
            x[i] = d[i] / b[i]
        else:
            x[i] = (d[i] - (c[i] * x[i + 1])) / b[i]

    return x

def main(a, b, c, d):
    y = band_matrix(a, b, c, d)
    z = regressive_substitution_trid(y[0], c, y[1])
    return (0, z)


#name = input("Enter the name of the file you want the answer to be saved in. It's going to have '.txt' extension: ")
#
#matrix_rows = 4
#a = []
#b = []
#c = []
#d = []
#
#print("You have to enter each vector in this order: a, b, c, d \
#       \nSepare each number with a space and press ENTER to start with the next vector:")
#
#for j in range(matrix_rows):
#    if j == 0:
#        a.append(list(map(float, input().rstrip().split())))
#    elif j == 1:
#        b.append(list(map(float, input().rstrip().split())))
#    elif j == 2:
#        c.append(list(map(float, input().rstrip().split())))
#    elif j == 3:
#        d.append(list(map(float, input().rstrip().split())))
#
#a = a[0]
#b = b[0]
#c = c[0]
#d = d[0]
#
#print("You will find the result in " + name + ".txt")
#
#a_aux = copy(a)
#b_aux = copy(b)
#c_aux = copy(c)
#d_aux = copy(d)
#
#with open(name + ".txt", "w") as result:
#    print("The result of each variable is: ", file=result)
#    vector = main(a_aux, b_aux, c_aux, d_aux)
#    num = 1
#    for x in vector:
#        print("x" + str(num) + " = " + str(x), file=result)
#        num += 1
#