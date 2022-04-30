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
        self.distanciaMasCorta = 0

    def addArc(self, vertex, source):
        if vertex not in self.ArregloDeListas:
            self.ArregloDeListas[vertex] = self.contador
            self.visitados[vertex] = False
            self.distancias[vertex] = 0
            self.predecesores[vertex] = ""
            self.contador += 1
        if source not in self.ArregloDeListas:
            self.ArregloDeListas[source] = self.contador
            self.visitados[source] = False
            self.distancias[source] = 0
            self.predecesores[source] = ""
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

    def getAcoso(self, source, destination):
        vertice = self.ArregloDeListas[source]
        arreglo = self.listaInfo[vertice]
        peso = 0
        for i in arreglo:
            if i[1] == destination:
                peso = i[4]
        return peso

    def djikstra(self, inicio, fin):
        distanciasAux = self.distancias.copy()
        distanciasAux[inicio] = 0
        predecesoresAux = self.predecesores.copy()
        visitadosAux = self.visitados.copy()
        visitadosAux[inicio] = True
        vertice = inicio
        for _ in range(len(self.ArregloDeListas)):
            vertice = self.elMasCercaNoVisitado(vertice, distanciasAux, predecesoresAux, visitadosAux, fin)
            visitadosAux[vertice] = True
            self.actualizarLaTabla(vertice, distanciasAux, predecesoresAux)
            if fin == vertice:
                if self.promedio >= self.promedioPonderado():
                    self.distanciaMasCorta = max(list(distanciasAux.values()))
                    print("Distancia camino más corto:", self.distanciaMasCorta)
                    print("Los puntos que se recorrieron:", self.listaRecorridos)
                    print("Promedio ponderado acoso:", self.promedioPonderado())
                else:
                    print("No hay un camino")
                return 
        return

    def elMasCercaNoVisitado(self, vertice, distancia, predecesor, visitados, fin):
            losVecinosDeV = self.getSuccessors(vertice)
            if losVecinosDeV is not None:
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
                        acoso = self.getAcoso(vertice, vecino)
                        self.listaRecorridos.append((vertice, peso, acoso))
                        break
                    elif peso <= pesoElMasCerca and visitados[vecino] == False:
                        elMasCerca = vecino
                        pesoElMasCerca = peso
                        predecesor[elMasCerca] = vertice
                        distancia[elMasCerca] = peso + distancia[vertice]
                acoso = self.getAcoso(vertice, vecino)
                self.listaRecorridos.append([vertice, peso, acoso])
                return elMasCerca

    def actualizarLaTabla(self, vertice, distancia, predecesor) -> None:
        losVecinosDeV = self.getSuccessors(vertice)
        if losVecinosDeV is not None:
            for vecino in losVecinosDeV:
                elPesoDeVAlVecino = self.getWeight(vertice, vecino)
                if (distancia[vertice] + elPesoDeVAlVecino) < distancia[vecino]:
                    distancia[vecino] = distancia[vertice] + elPesoDeVAlVecino
                    predecesor[vecino] = vertice

    def promedioPonderado(self):
        numerador = 0
        denominador = 0
        for pareja in self.listaRecorridos:
            numerador = numerador + pareja[1]*pareja[2]
            denominador = denominador + pareja[2]
        return numerador/denominador


def main():
    df = pd.read_csv("calles_de_medellin_con_acoso.csv", delimiter=";")
    lista = df.to_numpy().tolist()
    promedio = 14
    g = GraphAL(promedio)
    for i in lista:
        g.addArc(i[1], i[2])
    g.crearDeque()
    for i in lista:
        g.addLista(i[1], i[2], i[3], i[4], i[5])
    g.djikstra("(-75.5715105, 6.2063061)", "(-75.5685931, 6.2073652)")

main()