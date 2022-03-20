from cmath import inf
import pandas as pd
import numpy as np

from collections import deque

class GraphAL:
    def __init__(self, size, df):
        self.df = df
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
        peso = 0
        for i in arreglo:
            if i[0] == destination:
                peso = i[1]
        return peso

    def djikstra(self, inicio:int, final) -> list:
        inicio = self.df.index[self.df["origin"] == inicio].tolist()
        inicio = inicio[0]
        final = self.df.index[self.df["destination"] == final].tolist()
        final = final[0]
        distancias = [inf]*self.size
        distancias[inicio] = 0
        predecesores = [-1]*self.size
        visitados = [False]*self.size
        visitados[inicio] = True
        vertice = inicio
        for _ in range(self.size):
            vertice = self.elMasCercaNoVisitado(vertice, distancias, predecesores, visitados)
            visitados[vertice] = True
            self.actualizarLaTabla(vertice, distancias, predecesores)
            if vertice == final:
                return (distancias, predecesores)
        return (distancias, predecesores)

    def elMasCercaNoVisitado(self, vertice, distancia, predecesor, visitados):
        print(vertice)
        losVecinosDeV = self.getSuccessors(vertice)
        elMasCerca = 0
        pesoElMasCerca = inf
        peso = 0
        for vecino in losVecinosDeV:
            print(vecino)
            peso = self.getWeight(vertice, vecino)
            vecino = self.df.index[self.df["origin"] == vecino].tolist()
            vecino = vecino[0]
            if peso <= pesoElMasCerca and not visitados[vecino]:
                elMasCerca = vecino
                pesoElMasCerca = peso
                predecesor[elMasCerca] = vertice
                distancia[elMasCerca] = peso + distancia[vertice]
        return elMasCerca

    def actualizarLaTabla(self, vertice, distancia, predecesor) -> None:
        losVecinosDeV = self.getSuccessors(vertice)
        for vecino in losVecinosDeV:
            elPesoDeVAlVecino = self.getWeight(vertice, vecino)
            vecino = self.df.index[self.df["origin"] == vecino].tolist()
            vecino = vecino[0]
            if (distancia[vertice] + elPesoDeVAlVecino) < distancia[vecino]:
                distancia[vecino] = distancia[vertice] + elPesoDeVAlVecino
                predecesor[vecino] = vertice

def main():
    df = pd.read_csv("lol.csv", sep=";")
    lista = df.to_numpy()
    g = GraphAL(len(df), df)
    for id in range(len(df)):
        g.addArc(id, lista[id][1], lista[id][2])
    print(g.djikstra("a", "d"))
    
main()