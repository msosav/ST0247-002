import numpy as np


class GraphAM:

    def __init__(self, size):
        dimensiones = (size, size)
        self.matriz = np.zeros((size, size))

    def getWeight(self, source, destination):
        return self.matriz[source][destination]

    def addArc(self, source, destination, weight):
        self.matriz[source][destination] = weight

    def getSuccessors(self, vertex):
        lista = []
        for i in range(len(self.matriz[0])):
            if self.matriz[vertex][i] != 0:
                lista.append(i)
        return lista