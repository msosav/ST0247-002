from collections import deque
from cmath import inf

class GraphAL:
    def __init__(self, size):
        self.size = size
        self.arregloDeListas = [0]*size
        for i in range(0,size):
            self.arregloDeListas[i] = deque()

    def addArc(self, vertex, edge, weight):
        fila = self.arregloDeListas[vertex]
        parejaDestinoPeso = (edge, weight)
        fila.append(parejaDestinoPeso)
    def getSuccessors(self, vertice):
        lista = []
        arreglo = self.arregloDeListas[vertice]
        for i in arreglo:
            if i[1] != 0:
                lista.append(i[0])
        return lista

    def getWeight(self, source, destination):
        arreglo = self.arregloDeListas[source]
        for i in arreglo:
            if i[0] == destination:
                peso = i[1]
        return peso

def prims(grafo):
    duplasDeVertices = []
    totalAcumulado= 0
    origen = 0
    verticesBusquedaMenor = []
    visitados =  [False]*grafo.size
    visitados[origen] = True
    vertice = origen
    verticesBusquedaMenor.append(vertice)
    for _ in range(grafo.size-1):
        vertice = elMasCercaQueNoEsteVisitado(grafo, visitados, verticesBusquedaMenor, duplasDeVertices)
        visitados[vertice] = True
    for v in range (len(duplasDeVertices)):
        totalAcumulado += grafo.getWeight(duplasDeVertices[v][0], duplasDeVertices[v][1])
    return totalAcumulado


def elMasCercaQueNoEsteVisitado(grafo, visitados, verticesBusquedaMenor, duplasDeVertices):
    elPesoDelMasCerca = inf
    elMasCerca = 0
    for v in verticesBusquedaMenor:
        losVecinosDeV = grafo.getSuccessors(v)
        for vecino in losVecinosDeV:
            peso = grafo.getWeight(v, vecino)
            if peso <= elPesoDelMasCerca and not visitados[vecino]:
                elPesoDelMasCerca = peso
                elMasCerca = vecino
                vertice = v
    verticesBusquedaMenor.append(elMasCerca)
    duplasDeVertices.append((vertice,elMasCerca))

    return elMasCerca

def main():
    grafo = GraphAL(7)
    grafo.addArc(0,5,10)
    grafo.addArc(5,0,10)

    grafo.addArc(0,1,28)
    grafo.addArc(1,0,28)
    
    grafo.addArc(5,4,25)
    grafo.addArc(4,5,25)
    
    grafo.addArc(4,6,24)
    grafo.addArc(6,4,24)

    grafo.addArc(4,3,22)
    grafo.addArc(3,4,22)

    grafo.addArc(3,6,18)
    grafo.addArc(6,3,18)

    grafo.addArc(3,2,12)
    grafo.addArc(2,3,12)

    grafo.addArc(1,2,16)
    grafo.addArc(2,1,16)

    grafo.addArc(1,6,14)
    grafo.addArc(6,1,14)


    print(prims(grafo))
main()