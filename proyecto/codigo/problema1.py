from cmath import inf
import pandas as pd
import numpy as np
from collections import deque

class GraphAL:
    def __init__(self, lista, riesgoAcoso):
        self.riesgoAcoso = riesgoAcoso
        self.listaRecorrido = []
        self.listaRecorrido1 = []
        listaNodos = []
        for i in lista:
            if i[0] not in listaNodos:
                listaNodos.append(i[0])
        self.matrizUnaVia = np.zeros((len(listaNodos), len(listaNodos)))
        self.matrizAcoso = np.zeros((len(listaNodos), len(listaNodos)))
        self.distanciaMasCorta = inf
        self.distancia=0
        self.hasPath =False
        self.visited = [[0 for x in range(len(self.matrizUnaVia[0]))] for y in range(len(self.matrizUnaVia))]
        self.size = len(listaNodos)
        self.arregloDeListas = [0]*len(listaNodos)
        for i in range(0,len(listaNodos)):
            self.arregloDeListas[i] = deque()

    def addArc(self, vertex, edge, weight, oneWay, acoso):
        fila = self.arregloDeListas[vertex]
        parejaDestinoPeso = (edge, weight)
        fila.append(parejaDestinoPeso)
        if oneWay == False:
            self.matrizUnaVia[vertex][edge] = weight
            self.matrizUnaVia[edge][vertex] = weight
            self.matrizAcoso[vertex][edge] = acoso
            self.matrizAcoso[edge][vertex] = acoso
        else:
            self.matrizUnaVia[vertex][edge] = weight
            self.matrizAcoso[vertex][edge] = acoso

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
    
    def encontrarCamino(self, start, end):
        self.visita(start[0], start[1], end)
        if self.hasPath:
            print("Distancia camino más corto:", self.distanciaMasCorta)
            print("Los puntos que se recorrieron:", self.listaRecorrido)
            print("Promedio ponderado acoso:", self.promedioPonderado())
        else:
            print("No hay un camino")

    def visita(self, x, y, end):
        if x==end[0]and y==end[1]:
            if self.distanciaMasCorta > min(self.distancia, self.distanciaMasCorta):
                self.listaRecorrido = self.listaRecorrido1.copy()
                if self.promedioPonderado() < self.riesgoAcoso:
                    self.distanciaMasCorta = min(self.distancia, self.distanciaMasCorta)
                    self.hasPath = True
                else:
                    self.hasPath = False
            return
        self.visited[x][y] = 1
        self.distancia += self.matrizUnaVia[x][y]
        self.listaRecorrido1.append((x,y))
        if self.sePuedeVisitar(x+1, y):
            self.visita(x+1, y, end)
        if self.sePuedeVisitar(x, y+1):
            self.visita(x, y+1, end)
        if self.sePuedeVisitar(x-1, y):
            self.visita(x-1, y, end)
        if self.sePuedeVisitar(x, y-1):
            self.visita(x, y-1, end)
        self.visited[x][y] = 0
        self.distancia -= self.matrizUnaVia[x][y]
        self.listaRecorrido1.remove((x,y))

    def sePuedeVisitar(self, x, y):
        if x<0 or y<0 or x>=len(self.matrizUnaVia[0]) or y>=len(self.matrizUnaVia):
            return False
        if self.matrizUnaVia[x][y]==0 or self.visited[x][y]==1:
            return False
        return True

    def promedioPonderado(self):
        numerador = 0
        denominador = 0
        for pareja in self.listaRecorrido:
            numerador = numerador + self.matrizAcoso[pareja[0]][pareja[1]]*self.matrizUnaVia[pareja[0]][pareja[1]]
            denominador = denominador + self.matrizAcoso[pareja[0]][pareja[1]]
        return numerador/denominador

def main():
    df = pd.read_csv("prueba.csv", delimiter=";")
    lista = df.to_numpy().tolist()
    riesgoAcoso = float(input("Promedio ponderado acoso: "))
    g = GraphAL(lista, riesgoAcoso)
    for i in lista:
        g.addArc(i[0], i[1], i[2], i[3], i[4])
    inicio = (2,3)
    fin = (3,4)
    g.encontrarCamino(inicio,fin)

main()