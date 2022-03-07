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



def elMasCercaQueNoEsteVisitado(grafo, vertice, visitados, distancias, predecesores):
    losVecinosDeV = grafo.getSuccessors(vertice)
    elPesoDelMasCerca = inf
    elMasCerca = 0
    for vecino in losVecinosDeV:
        peso = grafo.getWeight(vertice, vecino)
        if peso <= elPesoDelMasCerca and not visitados[vecino]:
            elPesoDelMasCerca = peso
            elMasCerca = vecino
    actualizarLaTabla(grafo, vertice, distancias, predecesores)
    return elMasCerca

def actualizarLaTabla(grafo, vertice,distancias, predecesores):
    losVecinosDeV = grafo.getSuccessors(vertice)
    for vecino in losVecinosDeV:
        elpesoDeVAlVecino = grafo.getWeight(vertice, vecino)
        if distancias[vertice] + elpesoDeVAlVecino < distancias[vecino]:
            distancias[vecino] = distancias[vertice] + elpesoDeVAlVecino
            predecesores[vecino] = vertice
    
    
def dijkstra(grafo,origen : int) -> list:
    distancias =  [inf]*grafo.size
    distancias[origen] = 0
    predecesores = [-1]*grafo.size
    visitados = [False]*grafo.size
    visitados[origen] = True
    vertice = origen
    for _ in range(grafo.size):
        vertice = elMasCercaQueNoEsteVisitado(grafo, vertice, visitados, distancias, predecesores)
        visitados[vertice] = True
        #actualizarLaTabla(grafo, vertice, distancias, predecesores)
    return distancias, predecesores

def main():
    grafo = GraphAL(6)
    grafo.addArc(0,1,2)
    grafo.addArc(0,2,4)
    grafo.addArc(1,2,1)
    grafo.addArc(1,3,7)
    grafo.addArc(2,4,3)
    grafo.addArc(4,3,2)
    grafo.addArc(4,5,5)
    grafo.addArc(3,5,1)
    print(dijkstra(grafo,0))
main()
