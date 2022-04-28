from cmath import inf
from collections import deque
import pandas as pd

class GraphAL:
    def __init__(self, promedio):
        self.promedio = promedio
        self.ArregloDeListas = {}
        self.distancias = {}
        self.predecesores = {}
        self.visitados = {}
        self.contador = 0
        self.listaInfo = []
        self.listaRecorridos = []

    def addArc(self, vertex):
        if vertex not in self.ArregloDeListas:
            self.ArregloDeListas[vertex] = self.contador
            self.visitados[vertex] = False
            self.distancias[vertex] = 0
            self.predecesores[vertex] = ""
            self.contador += 1

    def crearDeque(self):
        self.listaInfo = [0]*self.contador
        for i in range(0, self.contador):
            self.listaInfo[i] = deque()

    def addLista(self, vertex, edge, weight, oneWay, acoso):
        vertice = self.ArregloDeListas[vertex]
        fila = self.listaInfo[vertice]
        parejaDestinoPeso = (vertex, edge, weight, oneWay, acoso)
        fila.append(parejaDestinoPeso)

    def getSuccessors(self, vertice):
        arregloAux = []
        vertex = self.ArregloDeListas[vertice]
        arreglo = self.listaInfo[vertex]
        for i in arreglo:
            if i[1] != 0:
                arregloAux.append(i[1])
        return arregloAux

    def getWeight(self, source, destination):
        vertice = self.ArregloDeListas[source]
        arreglo = self.listaInfo[vertice]
        peso = 0
        for i in arreglo:
            if i[1] == destination:
                peso = i[2]
        return peso

    def djikstra(self, inicio, fin) -> list:
        distanciasAux = self.distancias.copy()
        distanciasAux[inicio] = 0
        predecesoresAux = self.predecesores.copy()
        visitadosAux = self.visitados.copy()
        visitadosAux[inicio] = True
        vertice = inicio
        for _ in range(len(self.ArregloDeListas)):
            vertice = self.elMasCercaNoVisitado(vertice, distanciasAux, predecesoresAux, visitadosAux, fin)
            visitadosAux[vertice] = True
            
            self.listaRecorridos.append[vertice]
            self.actualizarLaTabla(vertice, distanciasAux, predecesoresAux)
            if fin == vertice:
                lista = list(distanciasAux.values())
                return (max(lista))
        return (max(list(distanciasAux)))

    def elMasCercaNoVisitado(self, vertice, distancia, predecesor, visitados, fin):
        losVecinosDeV = self.getSuccessors(vertice)
        elMasCerca = 0
        pesoElMasCerca = inf
        peso = 0
        for vecino in losVecinosDeV:
            peso = self.getWeight(vertice, vecino)
            if vecino == fin:
                elMasCerca = vecino
                pesoElMasCerca = peso
                predecesor[elMasCerca] = vertice
                distancia[elMasCerca] = peso + distancia[vertice]
                break
            elif peso <= pesoElMasCerca and visitados[vecino] == False:
                elMasCerca = vecino
                pesoElMasCerca = peso
                predecesor[elMasCerca] = vertice
                distancia[elMasCerca] = peso + distancia[vertice]
        return elMasCerca

    def actualizarLaTabla(self, vertice, distancia, predecesor) -> None:
        losVecinosDeV = self.getSuccessors(vertice)
        for vecino in losVecinosDeV:
            elPesoDeVAlVecino = self.getWeight(vertice, vecino)
            if (distancia[vertice] + elPesoDeVAlVecino) < distancia[vecino]:
                distancia[vecino] = distancia[vertice] + elPesoDeVAlVecino
                predecesor[vecino] = vertice

def main():
    df = pd.read_csv("calles_de_medellin_con_acoso.csv", delimiter=";")
    lista = df.to_numpy().tolist()
    promedio = 14
    g = GraphAL(promedio)
    for i in lista:
        g.addArc(i[1])
    g.crearDeque()
    for i in lista:
        g.addLista(i[1], i[2], i[3], i[4], i[5])
    print(g.djikstra("(-75.5686884, 6.2063927)", "(-75.5685931, 6.2073652)"))

main()