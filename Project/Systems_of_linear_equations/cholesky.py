from math import sqrt
import numpy as np
from pprint import pprint

def cholesky_simon(A):
  L = np.zeros_like(A).tolist()
  for i in range(len(A)):
    for j in range(i+1):
      s = sum(L[i][k] * L[j][k] for k in range(j))
      if i == j:
        L[i][j] = sqrt(A[i][i] - s) #Diagonales
      else:
        L[i][j] = (1.0 / L[j][j] * (A[i][j] - s)) #No diagonales
  return L


def cholesky(A):
  L = np.zeros_like(A)
  U = np.zeros_like(A)
  for k in range(len(A)):
    contk = 0
    for p in range(k):
      contk += L[k][p] * U[p][k]
    L[k][k] = np.sqrt(A[k][k] - contk)
    U[k][k] = np.sqrt(A[k][k] - contk)
    for i in range(k + 1, len(A)):
      conti = 0
      for p in range(k):
        conti += L[i][p] * U[p][k]
      L[i][k] = float(A[i][k] - conti) / U[k][k]
    for j in range(k + 1, len(A)):
      contj = 0
      for p in range(k):
        contj += L[k][p] * U[p][j]
      U[k][j] = float(A[k][j] - contj) / L[k][k]
  return L, U
  

m1 = [[25, 15, -5],
      [15, 18,  0],
      [-5,  0, 11]]

m1 = [[6, 3, 4, 8], [3, 6, 5, 1], [4, 5, 10, 7], [8, 1, 7, 25]]
m1 = [
    [9.1622,    0.4505,    0.1067,    0.4314,    0.8530,    0.4173,    0.7803,    0.2348,    0.5470,    0.5470],
    [0.7943,    9.0838,    0.9619,    0.9106,    0.6221,    0.0497,    0.3897,    0.3532,    0.2963,    0.7757],
    [0.3112,    0.2290,    9.0046,    0.1818,    0.3510,    0.9027,    0.2417,    0.8212,    0.7447,    0.4868],
    [0.5285,    0.9133,    0.7749,    9.2638,    0.5132,    0.9448,    0.4039,    0.0154,    0.1890,    0.4359],
    [0.1656,    0.1524,    0.8173,    0.1455,    9.4018,    0.4909,    0.0965,    0.0430,    0.6868,    0.4468],
    [0.6020,    0.8258,    0.8687,    0.1361,    0.0760,    9.4893,    0.1320,    0.1690,    0.1835,    0.3063],
    [0.2630,    0.5383,    0.0844,    0.8693,    0.2399,    0.3377,    9.9421,    0.6491,    0.3685,    0.5085],
    [0.6541,    0.9961,    0.3998,    0.5797,    0.1233,    0.9001,    0.9561,    9.7317,    0.6256,    0.5108],
    [0.6892,    0.0782,    0.2599,    0.5499,    0.1839,    0.3692,    0.5752,    0.6477,    9.7802,    0.8176],
    [10.0000,    0.4427,    0.8001,    0.1450,    0.2400,    0.1112,    0.0598,    0.4509,    0.0811,   20.0000]
    ]
print("L")
pprint(np.array(cholesky(m1)[0]), width=120)

print("U")
pprint(np.array(cholesky(m1)[1]), width=120)

print("NUMPYYY")
pprint(np.linalg.cholesky(m1))