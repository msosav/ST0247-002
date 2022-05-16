from cmath import inf
from collections import deque
import pandas as pd

class GraphAL:
    def __init__(self, acoso, distancia_maxima):
        self.acoso = acoso
        self.distancia_maxima = distancia_maxima
        self.vertices = {}
        self.contador = 1

    def addArc(self, vertex, source):
        if vertex not in self.vertices:
            self.vertices[vertex] = self.contador
            self.contador += 1
        if source not in self.vertices:
            self.vertices[source] = self.contador
            self.contador += 1

    def crearDeque(self):
        self.listaInfo = [0]*self.contador
        for i in range(0, self.contador):
            self.listaInfo[i] = deque()

    def addLista(self, vertex, edge, weight, oneWay, acoso):
        if oneWay == False:
            vertice = self.vertices[vertex]
            fila = self.listaInfo[vertice]
            parejaDestinoPeso = (vertex, edge, weight, oneWay, acoso)
            fila.append(parejaDestinoPeso)
            otro_vertice = self.vertices[edge]
            fila_otro_vertice = self.listaInfo[otro_vertice]
            parejaDestinoPeso_otro_vertice = (edge, vertex, weight, oneWay, acoso)
            fila_otro_vertice.append(parejaDestinoPeso_otro_vertice)
        else:
            vertice = self.vertices[vertex]
            fila = self.listaInfo[vertice]
            parejaDestinoPeso = (vertex, edge, weight, oneWay, acoso)
            fila.append(parejaDestinoPeso)

    def getSuccessors(self, vertice):
        arregloAux = []
        arreglo = self.listaInfo[vertice]
        for i in arreglo:
            if i[1] != 0:
                arregloAux.append(i[1])
        return arregloAux

    def getWeight(self, source, destination):
        arreglo = self.listaInfo[source]
        peso = 0
        for i in arreglo:
            if i[1] == destination:
                peso = i[2]
        return peso

    def getAcoso(self, source, destination):
        arreglo = self.listaInfo[source]
        acoso = 0
        for i in arreglo:
            if i[1] == destination:
                acoso = i[4]
        return acoso

    def djikstra_con_acoso(self, inicio, fin):
        tamano=self.contador
        visitados = [False] * tamano
        distancias = [inf] * tamano
        acosos=[0]*tamano
        predecesores = [-1] * tamano
        distancias[self.vertices[inicio]] = 0

        for _ in range(tamano):
            vertice_actual = -1
            for vertice in range(tamano):
                if (not visitados[vertice]) and (vertice_actual==-1 or acosos[vertice]<acosos[vertice_actual]):
                    vertice_actual=vertice
            if acosos[vertice_actual]==inf:
                break
            visitados[vertice_actual] = True
            for vecino in self.getSuccessors(vertice_actual):
                peso=self.getWeight(vertice_actual,vecino)
                acoso=self.getAcoso(vertice_actual,vecino)
                vecino = self.vertices[vecino]
                if distancias[vertice_actual] + distancias < self.distancia_maxima:
                    if acosos[vertice_actual] + acoso < acosos[vecino]:
                        distancias[vecino] = distancias[vertice_actual] + peso
                        acosos[vecino] = acosos[vertice_actual] + acoso
                        predecesores[vecino] = vertice_actual

        return distancias[self.vertices[fin]], acosos[self.vertices[fin]]

def main():
    df = pd.read_csv("calles_de_medellin_con_acoso.csv", delimiter=";")
    lista = df.to_numpy().tolist()
    acoso = 50
    distancia_maxima = 1000
    g = GraphAL(acoso, distancia_maxima)
    for nombre, origen, destino, peso, una_via, acoso, geometry in lista:
        g.addArc(origen, destino)
    g.crearDeque()
    for nombre, origen, destino, peso, una_via, acoso, geometry in lista:
        g.addLista(origen, destino, peso, una_via, acoso)
    print(g.djikstra("(-75.5686884, 6.2063927)", "(-75.5689683, 6.25177)"))

main()