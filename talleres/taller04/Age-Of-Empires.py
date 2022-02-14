from collections import deque
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

def hayCamino(g, inicio, final):
    tablaHashDeVisitados = [False]*g.size
    return hayCaminoAux(g, inicio, final, tablaHashDeVisitados)

#Sea inicio el origen y final el destino
def hayCaminoAux(g, inicio:int, final:int, tablaHashDeVisitados) -> bool:
    tablaHashDeVisitados[inicio] = True #Digo que ya visité a inicio
    if inicio == final: #Si el inicio es igual al final
        return True
    else:
        for vecino in g.getSuccessors(inicio): #Para cada vecino en los sucesores de inicio
            if not tablaHashDeVisitados[vecino]: #Si no está visitado el vecino en la tabla
                hayCaminoDelVecinoAd = hayCaminoAux(g, vecino, final, tablaHashDeVisitados)
                if hayCaminoDelVecinoAd:
                    return True
        return False #Si nunca dio verdadero es falso

def main():
    grafo = GraphAL(5)
    grafo.addArc(0,1,10)
    grafo.addArc(0,2,1)
    grafo.addArc(2,3,2)
    grafo.addArc(3,0,2)
    grafo.addArc(3,4,3)
    print(hayCamino(grafo, 0, 4))
    print(hayCamino(grafo, 1,4))
main()
