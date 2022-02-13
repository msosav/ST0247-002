from collections import deque

class Ciudad:
    def __init__(self, size):
        self.nombreVertice = [""]*size
        self.mapaCiudad = [0]*size
        for i in range(0,size):
            self.mapaCiudad[i] = deque()

    def addArc(self, name1, name2, distancia):
        id1 = self.getId(name1)
        id2 = self.getId(name2)
        fila = self.mapaCiudad[id1]
        parejaDestinoPeso = (id2, distancia)
        fila.append(parejaDestinoPeso)

    def getWeight(self, name1, name2):
        id1 = self.getId(name1)
        id2 = self.getId(name2)
        arreglo = self.mapaCiudad[id1]
        for i in arreglo:
            if i[0] == id2:
                peso = i[1]
        return peso

    def getId(self, name):
        contador = 0
        for i in self.nombreVertice:
            contador += 1
            if i == name:
                return contador

    def addVertex(self, id, name):
        self.nombreVertice[id] = name