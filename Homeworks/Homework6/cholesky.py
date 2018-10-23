from math import sqrt
import numpy as np
from pandas import DataFrame

def cholesky(A):
  L = np.zeros_like(A).tolist()
  for i in range(len(A)):
    for j in range(i+1):
      s = sum(L[i][k] * L[j][k] for k in range(j))
      if i == j:
        if (A[i][i] - s) >= 0:
          L[i][j] = sqrt(A[i][i] - s) #Diagonales
        else:
          print("Raiz de negativo")
      else:
        if not (L[j][j] * (A[i][j] - s)) == 0:
          L[i][j] = (1.0 / L[j][j] * (A[i][j] - s)) #No diagonales
        else:
          print("Division por 0")
  Lmat = np.array(L)
  Ltrans = Lmat.transpose()
  print(DataFrame(Ltrans))
  return L
  

m1 = [[25, 15, -5],
      [15, 18,  0],
      [-5,  0, 11]]
 
#A = [[-4, 1,0, 2], [3, 1, 2, -8], [14, 2, -4, 6], [-7, 0, 5, 7]]
A = [[3, 4, -2], [4, 8, -2], [-2, -2, 4]]

print("\n", DataFrame(cholesky(A)))

 