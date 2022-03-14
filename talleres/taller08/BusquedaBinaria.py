def busquedaBinaria(arreglo: list, valor: int)-> int:
    return busquedaBinariaAux(arreglo, valor, 0 , len(arreglo)-1)

def busquedaBinariaAux(arreglo: int, valor: int, elIndiceDeMasALaIzquierda: int, elIndiceDeMasALaDerecha: int):
    mitad = (elIndiceDeMasALaDerecha + elIndiceDeMasALaIzquierda)//2
    if elIndiceDeMasALaIzquierda > elIndiceDeMasALaDerecha:
        return -1
    if valor == arreglo[mitad]:
        return mitad
    if valor < arreglo[mitad]:
        return busquedaBinariaAux(arreglo, valor, elIndiceDeMasALaIzquierda, mitad-1)
    else:
        return busquedaBinariaAux(arreglo, valor, mitad+1, elIndiceDeMasALaDerecha)
        ## Complejidad: 1 llamado recursivo n/2.    O(log2 n)

def main():
    arreglo = [10,20,30,40,50,55,60]
    print(busquedaBinaria(arreglo,10))
    print(busquedaBinaria(arreglo,60))
    print(busquedaBinaria(arreglo,30))
    print(busquedaBinaria(arreglo,25))
    print(busquedaBinaria(arreglo,80))
    print(busquedaBinaria(arreglo,41))
main()
