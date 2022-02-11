from collections import deque
import string

class Ciudad:
    def __init__(self, size):
        self.nombreVertice = [""]*size
        self.idVertice = [0]*size
        for i in range(0,size):
            self.nombreVertice[i] = deque()
            self.idVertice[i] = deque()

    def addArc(self, nombre1:str, nombre2:str, distancia):
        id1 = self.nombreVertice.index(nombre1)
        fila = self.idVertice[id1]
        parejaDestinoPeso = (nombre2, distancia)
        fila.append(parejaDestinoPeso)

    def getWeight(self, nombre1:str, nombre2:str):
        id1 = self.nombreVertice.index(nombre1)
        id2 = self.nombreVertice.index(nombre2)
        arreglo = self.idVertice[id1]
        for i in arreglo:
            if i[0] == id2:
                peso = i[1]
        return peso

    def addVertex(self, id, name):
        self.nombreVertice[id] = name
        self.idVertice[id] = id

def main():
    g = Ciudad(5)
    g.addVertex(1, "Movies")
    g.addVertex(2, "Snell")
    g.addArc("Movies", "Snell", 10)
    print(g.getWeight("Movies","Snell"))

main()