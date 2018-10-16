from math import sqrt
import numpy as np
from pprint import pprint

def cholesky(A):
  L = np.zeros_like(A).tolist()
  for i in range(len(A)):
    for j in range(i+1):
      s = sum(L[i][k] * L[j][k] for k in range(j))
      if i == j:
        L[i][j] = sqrt(A[i][i] - s) #Diagonales
      else:
        L[i][j] = (1.0 / L[j][j] * (A[i][j] - s)) #No diagonales
  return L
  

m1 = [[25, 15, -5],
      [15, 18,  0],
      [-5,  0, 11]]

pprint(cholesky(m1), width=120)

 
