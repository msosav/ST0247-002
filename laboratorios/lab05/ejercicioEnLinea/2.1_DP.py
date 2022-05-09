import numpy as np
import itertools

class GraphAM:
    def __init__(self, size):
        self.matriz = np.zeros((size, size))

    def addArc(self, source, destination, weight):
        self.matriz[source][destination] = weight
        self.matriz[destination][source] = weight

def graphCreate(g, numV,arrayPos):
    numArc = int((numV*(numV-1))/2)
    x = 0
    for arcs in range(numArc):
        x = x + 1
        for i in range(x,numV):
            rowW = abs(arrayPos[arcs][0] - arrayPos[i][0])
            colW = abs(arrayPos[arcs][1] - arrayPos[i][1])
            weight = rowW + colW
            g.addArc(arcs, i, weight)

def held_karp(dists):
    n = len(dists)

    C = {}

    for k in range(1, n):
        C[(1 << k, k)] = (dists[0][k], 0)

    for subset_size in range(2, n):
        for subset in itertools.combinations(range(1, n), subset_size):
            bits = 0
            for bit in subset:
                bits |= 1 << bit

            for k in subset:
                prev = bits & ~(1 << k)

                res = []
                for m in subset:
                    if m == 0 or m == k:
                        continue
                    res.append((C[(prev, m)][0] + dists[m][k], m))
                C[(bits, k)] = min(res)

    bits = (2**n - 1) - 1

    res = []
    for k in range(1, n):
        res.append((C[(bits, k)][0] + dists[k][0], k))
    opt = min(res)
    opt = opt[0]

    return opt

def main():
    arrayPos = []
    numEscenarios = int(input("Ingrese el numero de escenarios a resolver "))
    for j in range(numEscenarios):
        dimensiones = input("Ingrese las dimensiones ")
        posInicial = input("Ingrese la posicion inicial ")
        numP = posInicial[:posInicial.index(" ")]
        numF = posInicial[posInicial.index(" ")+1:]
        arrayPos.append((int(numP),int(numF)))
        numRadio = int(input("Ingrese el numero de desechos radioactivos "))
        for radio in range (numRadio):
            posRadio = input("Ingrese las cordenadas del desecho ")
            num1 = posRadio[:posRadio.index(" ")]
            num2 = posRadio[posRadio.index(" ")+1:]
            arrayPos.append((int(num1),int(num2)))
        g = GraphAM(numRadio+1)
        graphCreate(g, numRadio+1, arrayPos)
        graph = g.matriz
        print(held_karp(graph))

main()







