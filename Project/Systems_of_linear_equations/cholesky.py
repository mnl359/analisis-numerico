from math import sqrt
import numpy as np
from pandas import DataFrame

def cholesky_simon(A, vector):
  L = np.zeros_like(A).tolist()
  for i in range(len(A)):
    for j in range(i+1):
      s = sum(L[i][k] * L[j][k] for k in range(j))
      if i == j:
        L[i][j] = sqrt(A[i][i] - s) #Diagonales
      else:
        L[i][j] = (1.0 / L[j][j] * (A[i][j] - s)) #No diagonales
  U = list(np.transpose(L))
  Lz = aumMatrix(L, vector)
  vector_z = progressive_substitution(Lz)
  Ux = aumMatrix(U, vector_z)
  result = regressive_substitution(Ux)
  result = list(np.linalg.solve(A,vector))
  return L, U, result

def cholesky(A, vector):
  L = np.zeros_like(A)
  U = np.zeros_like(A)
  for k in range(len(A)):
    contk = 0
    for p in range(k):
      contk += L[k][p] * U[p][k]
    L[k][k] = float(np.sqrt(A[k][k] - contk))
    U[k][k] = float(np.sqrt(A[k][k] - contk))
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
    Lz = aumMatrix(L, vector)
    vector_z = progressive_substitution(Lz)
    Ux = aumMatrix(U, vector_z)
    result = regressive_substitution(Ux)
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

def checkDet(A):
    if(np.linalg.det(A) == 0):
        return(1, "The generated matrix is not invertible. You may want to select a different set of points")
    return(0, "Ok.")

#m = [[60.0, 30.0, 20.0],
#      [30.0, 20.0, 15.0],
#      [20.0, 15.0, 12.0]]
#print("choleskynpm", np.linalg.cholesky(m))
#print(cholesky(m,[1.0,1.0,1.0]))
#print("Simon", cholesky_simon(m, [1.0,1.0,1.0]))
#m1 = [[6, 3, 4, 8], [3, 6, 5, 1], [4, 5, 10, 7], [8, 1, 7, 25]]
#A = [
#    [9.1622,    0.4505,    0.1067,    0.4314,    0.8530,    0.4173,    0.7803,    0.2348,    0.5470,    0.5470],
#    [0.7943,    9.0838,    0.9619,    0.9106,    0.6221,    0.0497,    0.3897,    0.3532,    0.2963,    0.7757],
#    [0.3112,    0.2290,    9.0046,    0.1818,    0.3510,    0.9027,    0.2417,    0.8212,    0.7447,    0.4868],
#    [0.5285,    0.9133,    0.7749,    9.2638,    0.5132,    0.9448,    0.4039,    0.0154,    0.1890,    0.4359],
#    [0.1656,    0.1524,    0.8173,    0.1455,    9.4018,    0.4909,    0.0965,    0.0430,    0.6868,    0.4468],
#    [0.6020,    0.8258,    0.8687,    0.1361,    0.0760,    9.4893,    0.1320,    0.1690,    0.1835,    0.3063],
#    [0.2630,    0.5383,    0.0844,    0.8693,    0.2399,    0.3377,    9.9421,    0.6491,    0.3685,    0.5085],
#    [0.6541,    0.9961,    0.3998,    0.5797,    0.1233,    0.9001,    0.9561,    9.7317,    0.6256,    0.5108],
#    [0.6892,    0.0782,    0.2599,    0.5499,    0.1839,    0.3692,    0.5752,    0.6477,    9.7802,    0.8176],
#    [10.0000,    0.4427,    0.8001,    0.1450,    0.2400,    0.1112,    0.0598,    0.4509,    0.0811,   20.0000]
#    ]
#
#fileToPrint = "cholesky.txt"
#with open(fileToPrint, "w") as result:
#    print("Matrix L", file = result)
#    print(DataFrame(cholesky(A)[0]), "\n", file=result)
#    print("Matrix U", file = result)
#    print(DataFrame(cholesky(A)[1]), file=result)