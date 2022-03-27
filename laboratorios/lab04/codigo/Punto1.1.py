from cmath import inf

from collections import deque

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

def djikstra(grafo, inicio:int, fin:int) -> list:
    distancias = [0]*grafo.size
    distancias[inicio] = 0
    predecesores = [-1]*grafo.size
    visitados = [False]*grafo.size
    visitados[inicio] = True
    vertice = inicio
    for _ in range(grafo.size):
        vertice = elMasCercaNoVisitado(grafo, vertice, distancias, predecesores, visitados)
        visitados[vertice] = True
        actualizarLaTabla(grafo, vertice, distancias, predecesores)
        if vertice == fin:
            return (max(distancias), predecesores)
    return (distancias, predecesores)

def elMasCercaNoVisitado(grafo, vertice, distancia, predecesor, visitados):
    losVecinosDeV = grafo.getSuccessors(vertice)
    elMasCerca = 0
    pesoElMasCerca = inf
    peso = 0
    for vecino in losVecinosDeV:
        peso = grafo.getWeight(vertice, vecino)
        if peso <= pesoElMasCerca and not visitados[vecino]:
            elMasCerca = vecino
            pesoElMasCerca = peso
            predecesor[elMasCerca] = vertice
            distancia[elMasCerca] = peso + distancia[vertice]
    return elMasCerca

def actualizarLaTabla(grafo, vertice, distancia, predecesor) -> None:
    losVecinosDeV = grafo.getSuccessors(vertice)
    for vecino in losVecinosDeV:
        elPesoDeVAlVecino = grafo.getWeight(vertice, vecino)
        if (distancia[vertice] + elPesoDeVAlVecino) == 0:
            distancia[vecino] = distancia[vertice] + elPesoDeVAlVecino
            predecesor[vecino] = vertice
        elif (distancia[vertice] + elPesoDeVAlVecino) < distancia[vecino]:
            distancia[vecino] = distancia[vertice] + elPesoDeVAlVecino
            predecesor[vecino] = vertice

def main():
    grafo = GraphAL(5)
    grafo.addArc(0,1,10)
    grafo.addArc(0,2,13)
    grafo.addArc(0,3,15)
    grafo.addArc(2,3,8)
    grafo.addArc(3,1,12)
    grafo.addArc(3,4,20)
    grafo.addArc(1,4,7)
    print(djikstra(grafo,0,4))

main()