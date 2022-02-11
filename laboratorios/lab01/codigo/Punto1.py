from collections import deque

class Ciudad:
    def __init__(self, size):
        self.nombreVertice = [""]*size
        self.mapaCiudad = [0]*size
        for i in range(0,size):
            self.mapaCiudad[i] = deque()

    def addArc(self, id1, id2, distancia):
        fila = self.mapaCiudad[id1]
        parejaDestinoPeso = (id2, distancia)
        fila.append(parejaDestinoPeso)

    def getWeight(self, id1, id2):
        arreglo = self.mapaCiudad[id1]
        for i in arreglo:
            if i[0] == id2:
                peso = i[1]
        return peso

    def addVertex(self, id, name):
        self.nombreVertice[id] = name

def main():
    g = Ciudad(5)
    g.addVertex(1, "Movies")
    g.addVertex(2, "Snell")
    g.addArc(1, 2, 10)
    print(g.getWeight(1,2))

main()