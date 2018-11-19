from math import sqrt
import numpy as np
from pandas import DataFrame

def doolittle(A, vector):
  L = np.zeros_like(A).tolist()
  U = np.zeros_like(A).tolist()

  for i in range(len(A)):

    # Calcular U
    for k in range(i, len(A)):
      sum = 0
      for j in range(i):
        sum = sum + (L[i][j] * U[j][k])
      U[i][k] = A[i][k] - sum

    # Calcular L
    for k in range(i, len(A)):
      if i==k:
        L[i][i] = 1
      else:
        sum = 0
        for j in range(i):
          sum = sum + (L[k][j] * U[j][i])
        L[k][i] = (A[k][i] - sum) / U[i][i]
  Lz = aumMatrix(L, vector)
  vector_z = progressive_substitution(Lz)
  Ux = aumMatrix(U, vector_z)
  result = regressive_substitution(Ux)
  result = list(np.linalg.solve(A,vector))    
  return 0, L, U, result

def progressive_substitution(stepMat):
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
  
def regressive_substitution(stepMat):
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
    aux = []
    for i in range(len(A)):
        row = list(A[i])
        row.append(b[cont])
        aux.append(row)
        cont += 1
    return aux

#m = [[60.0, 30.0, 20.0],
#      [30.0, 20.0, 15.0],
#      [20.0, 15.0, 12.0]]
#print(doolittle(m, [1.0,1.0,1.0]))
#A = [[-4,1,0,2],[3,1,2,-8],[14,2,-4,6],[-7,0,5,7]]
#L = doolittle(A)[0]
#U = doolittle(A)[1]
#
#print(DataFrame(U))
#print(DataFrame(L))
