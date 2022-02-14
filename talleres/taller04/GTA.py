#Algoritmo para encontar menor costo

import math
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

def costoDelMasCorto(g, inicio:int, final:int):
    arregloDeVisitados = [False]*g.size
    return costoDelMasCortoAux(g, inicio, final, arregloDeVisitados)

def costoDelMasCortoAux(g, inicio:int, final:int, arregloDeVisitados):
    arregloDeVisitados[inicio] = True
    if inicio == final:
        return 0
    else:
        elCostoDelMasCorto = math.inf
        for vecino in g.getSuccessors(inicio):
            if not arregloDeVisitados[vecino]:
                elCostoDelMasCortoDesdeElVecinoHastaD:int = costoDelMasCortoAux(g, vecino, final, arregloDeVisitados)
                elCostoDelMasCortoDesdeOHastaDPasandoPorElVecino = g.getWeight(inicio,vecino) + elCostoDelMasCortoDesdeElVecinoHastaD
                if elCostoDelMasCortoDesdeOHastaDPasandoPorElVecino < elCostoDelMasCorto:
                    elCostoDelMasCorto = elCostoDelMasCortoDesdeOHastaDPasandoPorElVecino
        return elCostoDelMasCorto

def main():
    grafo = GraphAL(5)
    grafo.addArc(0,1,10)
    grafo.addArc(0,2,1)
    grafo.addArc(2,3,2)
    grafo.addArc(3,0,2)
    grafo.addArc(3,4,3)
    print(costoDelMasCorto(grafo, 0, 1))

main()