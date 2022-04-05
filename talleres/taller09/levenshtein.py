import numpy as np
def levenshtein(string1, string2):

    filas = len(string1)+1
    columnas = len(string2)+1
    operaciones = np.zeros((filas,columnas))

    
    for i in range(1, filas):
        operaciones[i][0] = i


    for i in range(1, columnas):
        operaciones[0][i] = i
        
    for columna in range(1, columnas):
        for fila in range(1, filas):
            if string1[fila-1] == string2[columna-1]:
                cost = 0
            else:
                cost = 1
            operaciones[fila][columna] = min(operaciones[fila-1][columna] + 1, operaciones[fila][columna-1] + 1, operaciones[fila-1][columna-1] + cost) 

    return int(operaciones[fila][columna])

print(levenshtein("sosa", "chosa"))