import pandas as pd
import numpy as np

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

def main():
    df = pd.read_csv("calles_de_medellin_con_acoso.csv", sep=";")
    lista = df.to_numpy().tolist()
    g = GraphAL(len(df))
    for id in range(len(df)):
        id2 = df.index[df["origin"] == lista[id][2]].tolist()
        g.addArc(id, lista[id][2], lista[id][3])
    print(g.getSuccessors(1))
    
main()