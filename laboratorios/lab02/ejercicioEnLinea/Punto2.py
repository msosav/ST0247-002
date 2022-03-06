from collections import deque

def seAtacanHastaI(tablero, i):
    for j in range(0, i+1):
        for k in range(j+1, i+1):
            if abs(tablero[j]-tablero[k]) == abs(j-k) or tablero[j] == tablero[k]:
                return True
    return False

def nReinas() -> None:
    while True:
        n = int(input("Ingrese el numero de reinas: "))
        if n == 0:
            return
        print(nReinasAuxLista(n, 0, [0]*n, [], tableroReinas(n)))

def nReinasAuxLista(n:int, col:int, lista:list, nuevaLista:list, matriz) -> None:
    if col == n:
        nuevaLista.append(lista.copy())
        return
    for f in range(n):
        if matriz[col][f] == True: 
            lista[col] = f
        else: continue
        if seAtacanHastaI(lista, col):
            pass
        else:
            nReinasAuxLista(n, col+1, lista, nuevaLista, matriz)
    return len(nuevaLista)

def tableroReinas(n):
    arregloDeListas = [None]*n
    for i in range(0,n):
        arregloDeListas[i] = deque()

    for linea in range(n):
        entrada = input("Ingrese la linea: ")
        for letra in range(n):
            if entrada[letra] == ".":
                arregloDeListas[linea].append(True) 
            else: arregloDeListas[linea].append(False) 
    return arregloDeListas




def main():
    nReinas()

main()