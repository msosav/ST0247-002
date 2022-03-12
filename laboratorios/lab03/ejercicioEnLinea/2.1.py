from collections import deque
from cmath import inf

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

def userInput():
    caminoCorto = []
    pesoMin = [inf]
    firstLine = str(input("Ingrese el numero de vertices y el numero de arcos separados por un espacio"))
    indice_ = firstLine.index(" ")
    n = int(firstLine[:indice_])
    m = int(firstLine[indice_+1:])
    grafo = GraphAL(n)
    for edge in range(m):
        iEdge = str(input("Ingrese el arco"))
        indice1 = iEdge.index(" ")
        indice2 = iEdge.rindex(" ")
        v1 = int(iEdge[:indice1])
        v2 = int(iEdge[indice1+1: indice2])
        p = int(iEdge[indice2+1:])
        grafo.addArc(v1,v2,p)
        grafo.addArc(v2,v1,p)
    print(caminos(grafo, n,0,n-1, pesoMin, caminoCorto))
    

def caminosAux(grafo,verticeAhora, destino, visitados, camino, PesoMin, caminoCorto):
        pesoAhora = 0
        visitados[verticeAhora]= True
        camino.append(verticeAhora)
        if len(camino) >= 2:
            for j in range(len(camino)-1):
                pesoAhora += grafo.getWeight(camino[j],camino[j+1])
        if verticeAhora == destino and pesoAhora < PesoMin[0]:
            PesoMin[0] = pesoAhora
            if len(caminoCorto) >= 1:
                caminoCorto.pop()
            caminoCorto.append(camino.copy())
        else:
            for i in grafo.getSuccessors(verticeAhora):
                if visitados[i]== False and pesoAhora < PesoMin[0]:
                    caminosAux(grafo, i, destino, visitados, camino, PesoMin, caminoCorto)
        camino.pop()
        visitados[verticeAhora]= False
        return caminoCorto, PesoMin

def caminos(grafo, numVertices, origen, destino, PesoMin, caminoCorto):
        visitados =[False]*(numVertices)
        camino = []
        return caminosAux(grafo,origen, destino, visitados, camino, PesoMin, caminoCorto)

def main():
    userInput()

main()