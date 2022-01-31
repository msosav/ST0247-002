def nReinas(n):
    cadena=""
    for i in range(n):
        cadena += str(i)
    return(verificar(permutacion(cadena, "", []), []))

def permutacion(pregunta, respuesta, lista):
    if len(pregunta)==0:
        lista.append(respuesta)
    else:
        for i in range(0,len(pregunta)):
            nuevaPregunta = pregunta[0:i] + pregunta[i+1:]
            permutacion(nuevaPregunta, respuesta+pregunta[i], lista)
    return lista

def verificar(lista, nuevaLista):
    for i in lista:
        contador = 0
        for j in range(len(i)):
            for k in range(len(i)):
                if j != k:
                    x = j - k
                    y = int(i[j]) - int(i[k])
                    pendiente = y/x
                    if pendiente == 1 or pendiente == -1:
                        contador += 1
        if contador == 0:
            nuevaLista.append(i)
    return nuevaLista


def main():
    print(nReinas(8))

main()