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
        for i in arreglo:
            if i[0] == destination:
                peso = i[1]
        return peso

def estaBienPintado(listaColores:list, i:int, grafo) -> bool:
    for vertice in range(0, i+1):
        colorVertice = listaColores[vertice]
        for sucesor in grafo.getSuccessors(vertice):
            if sucesor <= i:
                colorSucesor = listaColores[sucesor]
                if colorVertice == colorSucesor:
                    return False
    return True

def sePuedePintarConMColores(grafo, numeroColores:int) -> bool:
    return pintarAuxTodos(grafo, [0]*grafo.size, numeroColores, 0, [])

def pintarAux(grafo, arregloColores:list, numeroColores:int, i:int):
    if i == len(arregloColores):
        print(arregloColores)
        return True
    for color in range(0, numeroColores):
        arregloColores[i] = color
        if estaBienPintado(arregloColores, i, grafo):
            pudePintarDeIMasUnoEnAdelante = pintarAux(grafo, arregloColores, numeroColores, i+1)
            if pudePintarDeIMasUnoEnAdelante:
                print(arregloColores)
                return True
    return False

def pintarAuxTodos(grafo, arregloColores:list, numeroColores:int, i:int, lista):
    if i == len(arregloColores):
        lista.append(arregloColores.copy())
        return 
    for color in range(numeroColores):
        arregloColores[i] = color
        if not estaBienPintado(arregloColores, i, grafo):
            pass
        else:
            pintarAuxTodos(grafo, arregloColores, numeroColores, i+1, lista)
    return lista

def main():
    grafo = GraphAL(7)
    grafo.addArc(0,1,1), grafo.addArc(1,0,1)
    grafo.addArc(1,2,1), grafo.addArc(2,1,1)
    grafo.addArc(1,6,1), grafo.addArc(6,1,1)
    grafo.addArc(2,3,1), grafo.addArc(3,2,1)
    grafo.addArc(2,4,1), grafo.addArc(4,2,1)
    grafo.addArc(2,5,1), grafo.addArc(5,2,1)
    grafo.addArc(3,1,1), grafo.addArc(1,3,1)
    grafo.addArc(3,2,1), grafo.addArc(2,3,1)
    grafo.addArc(3,6,1), grafo.addArc(6,3,1)
    grafo.addArc(4,2,1), grafo.addArc(2,4,1)
    grafo.addArc(4,5,1), grafo.addArc(5,4,1)
    grafo.addArc(4,6,1), grafo.addArc(6,4,1)
    print(estaBienPintado([0,0,1,0,0,0,0], 2, grafo))
    print(sePuedePintarConMColores(grafo, 3))

main()