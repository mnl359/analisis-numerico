import numpy as np
class TransitionMatrix:

    #Gauss Seidel
    def tg(self, A, b):
        Tg = np.zeros((len(A), len(A)))
        Cg = np.zeros(len(A))
        D = np.zeros((len(A), len(A)))
        np.fill_diagonal(D, np.diag(A))
        L = -1*np.tril(A)
        np.fill_diagonal(L, 0)
        U = -1*np.triu(A)
        np.fill_diagonal(U, 0)
        DL = np.subtract(D, L)
        invDL = np.linalg.inv(DL)
        Tg = np.matmul(invDL, U)
        print("\nTg")
        print(Tg)
        print("\nCg")
        Cg = np.matmul(invDL, b)
        print(Cg)
        print("Valores propios: ")
        eig = np.linalg.eigvals(Tg)
        print(eig)
        if max(abs(eig)) < 1:
            print("Converge con: ", complex(max(abs(eig))))

    #Jacobi
    def tj(self, A, b):
        Tj = np.zeros((len(A), len(A)))
        Cj = np.zeros(len(A))
        D = np.zeros((len(A), len(A)))
        np.fill_diagonal(D, np.diag(A))
        L = -1*np.tril(A)
        np.fill_diagonal(L, 0)
        U = -1*np.triu(A)
        np.fill_diagonal(U, 0)
        LU = np.add(L, U)
        invD = np.linalg.inv(D)
        Tj = np.matmul(invD, LU)
        print("\nTj")
        print(Tj)
        print("\nCj")
        Cj = np.matmul(invD, b)
        print(Cj)
        print("Valores propios: ")
        eig = np.linalg.eigvals(Tj)
        print(eig)
        if max(abs(eig)) < 1:
            print("Converge con: ", complex(max(abs(eig))))
    
    #SOR
    def tw(self, A, b, w):
        Tw = np.zeros((len(A), len(A)))
        Cw = np.zeros(len(A))
        D = np.zeros((len(A), len(A)))
        np.fill_diagonal(D, np.diag(A))
        L = -1*np.tril(A)
        np.fill_diagonal(L, 0)
        U = -1*np.triu(A)
        np.fill_diagonal(U, 0)
        wL = w*L
        wU = w*U
        wD = (1-w)*D
        DwL = np.linalg.inv(D-wL)
        wDU = np.add(wD, wU)
        Tw = np.matmul(DwL, wDU)
        print("\nTw")
        print(Tw)
        wDwL = w*DwL
        Cw = np.matmul(wDwL, b)
        print("\nCw")
        print(Cw)
        print("Valores propios: ")
        eig = np.linalg.eigvals(Tw)
        print(eig)
        if max(abs(eig)) < 1:
            print("Converge con: ", complex(max(abs(eig))))



t = TransitionMatrix()
A = [ [8, 3, 5],
      [-2, 7, 3],
      [4, -5, 18] ]
b = [21, 7, 42]
t.tg(A, b)
#t.tj(A, b)
#t.tw(A, b, 1)