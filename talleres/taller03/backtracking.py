def seAtacanHastaI(tablero, i):
    for j in range(0, i+1):
        for k in range(j+1, i+1):
            if abs(tablero[j]-tablero[k]) == abs(j-k) or tablero[j] == tablero[k]:
                return True
    return False

def nReinas(n:int) -> None:
    print("Lista")
    print(nReinasAuxLista(n, 0, [0]*n, []))
    print("---------------------------")
    print("Imprime todas las opciones validas")
    nReinasAuxPrint(n, 0, [0]*n)
    print("---------------------------")
    print("Imprime la primera opcion y para")
    print(nReinasAuxPrimero(n, 0, [0]*n, []))

def nReinasAuxLista(n:int, col:int, lista:list, nuevaLista:list) -> None:
    if col == n:
        nuevaLista.append(lista.copy())
        return
    for f in range(n):
        lista[col] = f
        if seAtacanHastaI(lista, col):
            pass
        else:
            nReinasAuxLista(n, col+1, lista, nuevaLista)
    return nuevaLista

def nReinasAuxPrint(n:int, col:int, lista:list) -> None:
    if col == n:
        print(lista)
        return
    for f in range(n):
        lista[col] = f
        if seAtacanHastaI(lista, col):
            pass
        else:
            nReinasAuxPrint(n, col+1, lista)

def nReinasAuxPrimero(n:int, col:int, lista:list, primero:list) -> None:
    if col == n:
        primero.append(lista.copy())
        return 
    else:
        for f in range(n):
            lista[col] = f
            if seAtacanHastaI(lista, col):
                pass
            else:
                nReinasAuxPrimero(n, col+1, lista, primero)
            if primero == []:
                pass
            else:
                return primero


def main():
    nReinas(4)

main()