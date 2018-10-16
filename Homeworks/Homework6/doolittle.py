from math import sqrt
import numpy as np
from pandas import DataFrame

def doolittle(A):
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
  return U, L

A = [[-4, 1, 0, 2], [3, 1, 2, -8], [14, 2, -4, 6], [-7, 0, 5, 7]]
U = doolittle(A)[0]
L = doolittle(A)[1]

print(DataFrame(U))
print(DataFrame(L))