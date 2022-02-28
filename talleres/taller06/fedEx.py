from collections import deque
from math import inf
## Algortimo para verificar si hay camino
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


def cicloHamiltonianoCostoMinimo(grafo):
    lista = [False]*grafo.size
    pesof = 0
    elmascerca = 0
    lista[elmascerca] = True
    for vez in range(grafo.size-1):
      peso = inf      
      for sucesor in grafo.getSuccessors(elmascerca):
          if peso > grafo.getWeight(elmascerca, sucesor):
              if not lista[sucesor]:
                  peso = grafo.getWeight(elmascerca, sucesor)
                  sucesorElegido = sucesor
      lista[sucesorElegido] = True
      pesof += peso
      elmascerca = sucesorElegido
    pesof += grafo.getWeight(elmascerca, 0)
    return pesof

def main():
    grafo = GraphAL(3)
    grafo.addArc(0,1,1)
    grafo.addArc(0,2,3)
    grafo.addArc(1,2,4)
    grafo.addArc(1,0,2)
    grafo.addArc(2,1,2)
    grafo.addArc(2,0,3)
    print(cicloHamiltonianoCostoMinimo(grafo))

main()
  
        