from collections import deque
from cmath import inf
class GraphAL:

    def __init__(self,size):
        self.size = size
        self.arregloDeListas =[0]*size
        for i in range(0,size):
            self.arregloDeListas[i] = deque()

    def addArc(self,vertex,edges, weigth): ## Añadir el peso
        fila = self.arregloDeListas[vertex]
        parejaDestinoPeso = (edges, weigth)
        fila.append(parejaDestinoPeso)
    
    def getWeight(self, source, destination):
        arreglo = self.arregloDeListas[source]
        for i in arreglo:
            if i[0] == destination:
                peso = i[1]
        return peso

    def getSuccessors(self, vertice):
        lista = []
        arreglo = self.arregloDeListas[vertice]
        for i in arreglo:
            if i[1] != 0:
                lista.append(i[0])
        return lista

def actualizarLaTabla(g,v,distancias,predecesores) -> None:
    losVecinosDeV = g.getSuccessors(v)
    for vecino in losVecinosDeV:
        elPesoDeVAlVecino = g.getWeight(v,vecino)
        if distancias[v] + elPesoDeVAlVecino < distancias[vecino]: 
            distancias[vecino] = distancias[v] + elPesoDeVAlVecino
            predecesores[vecino] = v

def elMasCercaQueNoEsteVisitado(g,v,visitados) -> int:
    losVecinosDeV = g.getSuccessors(v)
    elPesoDelMasCerca, elMasCerca = inf, 0
    for vecino in losVecinosDeV:
        peso = g.getWeight(v,vecino)
        if peso <= elPesoDelMasCerca and not visitados[vecino]:
            elPesoDelMasCerca, elMasCerca = peso, vecino
    return elMasCerca

def dijkstra(g,s : int) -> list:
    distancias =  [inf]*g.size
    predecesores = [-1]*g.size
    visitados = [False]*g.size
    distancias[s], visitados[s] = 0, True
    v = s
    for _ in range(1,g.size+1):
        v = elMasCercaQueNoEsteVisitado(g,v,visitados)
        visitados[v] = True
        actualizarLaTabla(g,v,distancias,predecesores)
    return (distancias, predecesores)

def main():
    g = GraphAL(6)
    g.addArc(0,1,2)
    g.addArc(0,2,4)
    g.addArc(1,2,1)
    g.addArc(1,3,7)
    g.addArc(2,4,3)
    g.addArc(4,3,2)
    g.addArc(4,5,5)
    g.addArc(3,5,1)
    print(dijkstra(g,0))
main()

