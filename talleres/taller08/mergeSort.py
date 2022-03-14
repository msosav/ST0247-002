def mergeSort(arreglo):
    resultado = []
    if( len(arreglo) == 1):
        return arreglo;
    mitad  = len(arreglo) // 2
    izquierda = mergeSort(arreglo[:mitad])
    derecha = mergeSort(arreglo[mitad:])
    len_izquierda = len(izquierda)
    len_derecha = len(derecha)
    i = 0
    j = 0
    while i != len_izquierda or j !=len_derecha:
        if( i != len_izquierda and (j == len_derecha or izquierda[i] < derecha[j])):
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    return resultado

def main():
    arreglo = [24,30,50,1,5,3,8,6,8,3]
    print(mergeSort(arreglo))

main()