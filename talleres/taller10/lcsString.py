import numpy as np
def lcsDPseq(A : str,B : str) -> str:
    m,n = len(A)+1, len(B)+1
    tabla = np.zeros((m,n))

    for i in range(0,n): # cond parada
        tabla[0][i] = 0

    for j in range(0,m): # cond parada
        tabla[j][0] = 0

    for i in range(1,m): # cond recursiva
        for j in range(1,n):
            if A[i-1] == B[j-1]:
                tabla[i][j] = 1 + tabla[i-1][j-1]
            else:
                tabla[i][j] = max(tabla[i-1][j], tabla[i][j-1])

        cadena = ""
        i, j = m-1, n-1

        while i != 0 and j != 0:
            if A[i-1] == B[j-1]:
                cadena = A[i-1] + cadena
                i, j = i-1, j-1
            else:
                if i == 0:
                    i, j = i, j-1
                elif j == 0:
                    i, j = i-1, j
                else:
                    maximo = max(tabla[i-1][j], tabla[i][j-1])
                    if tabla[i-1][j] == maximo:
                        i, j = i-1, j
                    else:
                        i, j = i, j-1
        return cadena

def main():
    A = "acedf"
    B = "cdajd"
    print(lcsDPseq(A,B))

main()
