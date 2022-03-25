from cmath import inf
from numpy import append
import pandas as pd

class GraphAL:
    def __init__(self, promedio):
        self.promedio = promedio
        self.ArregloDeListas = {}
        self.distancias = {}
        self.predecesores = {}
        self.visitados = {}

    def addArc(self, vertex, edge, weight, oneWay, acoso):
        if vertex in self.ArregloDeListas:
            self.ArregloDeListas[vertex] = (edge, weight, oneWay, acoso), (self.ArregloDeListas[vertex])
        else:
            self.ArregloDeListas[vertex] = (edge, weight, oneWay, acoso)
            self.distancias[(vertex)] = inf
            self.predecesores[(vertex)] = -1
            self.visitados[(vertex)] = False
            self.listaRecorridos = []

    def getSuccessors(self, vertice):
        contador = 0
        arregloAux = []
        if self.ArregloDeListas[vertice][0][0]=="(":
            arregloAux.append(self.ArregloDeListas[vertice][0])
        else:
            try:
                for destino, peso, oneWay, acoso in self.ArregloDeListas[vertice]:
                    arregloAux.append(destino)
                    contador += 1
            except ValueError:
                print("xd")
                for destino, peso, oneWay, acoso in self.ArregloDeListas[vertice][contador:]:
                    arregloAux.append(destino)
        return arregloAux

    def getWeight(self, source, destination):
        if self.ArregloDeListas[source][0]==destination:
            return self.ArregloDeListas[source][1]
        else:
            for destino, peso, oneWay, acoso in self.ArregloDeListas[source]:
                if destino==destination:
                    return peso

    def imprimirDiccionario(self):
        print(self.ArregloDeListas)

    def djikstra(self, inicio, fin) -> list:
        distanciasAux = self.distancias.copy()
        distanciasAux[inicio] = 0
        predecesoresAux = self.predecesores.copy()
        visitadosAux = self.visitados.copy()
        visitadosAux[inicio] = True
        vertice = inicio
        for _ in range(len(self.ArregloDeListas)):
            vertice = self.elMasCercaNoVisitado(vertice, distanciasAux, predecesoresAux, visitadosAux)
            visitadosAux[vertice] = True
            self.actualizarLaTabla(vertice, distanciasAux, predecesoresAux)
            if fin == vertice:
                """if self.promedio <= self.promedioPonderado():
                    print("Distancia camino más corto:", self.distanciaMasCorta)
                    print("Los puntos que se recorrieron:", self.listaRecorrido)
                    print("Promedio ponderado acoso:", self.promedioPonderado())
                else:
                    print("No hay un camino")"""
                lista = list(distanciasAux.values())
                return (max(lista))
        return (max(list(distanciasAux)))

    def elMasCercaNoVisitado(self, vertice, distancia, predecesor, visitados):
        losVecinosDeV = self.getSuccessors(vertice)
        elMasCerca = 0
        pesoElMasCerca = inf
        peso = 0
        for vecino in losVecinosDeV:
            peso = self.getWeight(vertice, vecino)
            if peso <= pesoElMasCerca and visitados[vecino]!=True:
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

    def getHarrasment(self, source, destination):
        if self.ArregloDeListas[source][0]==destination:
            return self.ArregloDeListas[source][3] 
        else:
            for destino, peso, oneWay, acoso in self.ArregloDeListas[source]:
                if destino==destination:
                    return acoso

    def imprimirTuplas(self, vertex):
        for i in self.ArregloDeListas[vertex]:
            print(i)

    def promedioPonderado(self):
        numerador = 0
        denominador = 0
        for pareja in self.listaRecorridos:
            print(list(self.ArregloDeListas).index(pareja))
            numerador = numerador + self.ArregloDeListas[pareja][3]*self.ArregloDeListas[pareja][1]
            denominador = denominador + self.ArregloDeListas[pareja][3]
        return numerador/denominador

def main():
    df = pd.read_csv("calles_de_medellin_con_acoso.csv", delimiter=";")
    lista = df.to_numpy().tolist()
    promedio = 1
    g = GraphAL(promedio)
    for i in lista:
        g.addArc(i[1], i[2], i[3], i[4], i[5])
    #g.imprimirDiccionario()
    print(g.djikstra("(-75.5713302, 6.2083717)", "(-75.5742281, 6.2094339)"))
    #print(g.getHarrasment("(1,2)", "(3,4)"))

main()