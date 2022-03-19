from cmath import inf
import pandas as pd

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
        peso = 0
        for i in arreglo:
            if i[0] == destination:
                peso = i[1]
        return peso

def rellenar(lista, df, nombreCol):
    for i in len(df[nombreCol]):
        lista[i]=(df["name"], df["origin"], df["destination"], df["length"], df["oneway"], df["harassmentRisk"],)
    return lista

def idDestino(df, destino, nombres):
    contador = 0
    for i in df["origin"]:
        if i == destino:
            return contador
        contador += 1

def djikstra(grafo, inicio:int) -> list:
    distancias = [inf]*grafo.size
    distancias[inicio] = 0
    predecesores = [-1]*grafo.size
    visitados = [False]*grafo.size
    visitados[inicio] = True
    vertice = inicio
    for _ in range(grafo.size):
        vertice = elMasCercaNoVisitado(grafo, vertice, distancias, predecesores, visitados)
        visitados[vertice] = True
        actualizarLaTabla(grafo, vertice, distancias, predecesores)
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
        if (distancia[vertice] + elPesoDeVAlVecino) < distancia[vecino]:
            distancia[vecino] = distancia[vertice] + elPesoDeVAlVecino
            predecesor[vecino] = vertice

def main():
    df = pd.read_csv("calles_de_medellin_con_acoso.csv", sep=";")
    lista = rellenar([0]*len(df["name"]), df, "name")
    g = GraphAL(len(df["name"]))
    for i in lista:
        print(i)

"""df = pd.read_csv("calles_de_medellin_con_acoso.csv", sep=";")
print(df)"""

main()