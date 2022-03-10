from cmath import inf
from collections import deque

class Ciudad:
    def __init__(self, size):
        self.size = size
        self.nombreVertice = [""]*size
        self.mapaCiudad = [0]*size
        self.numeroDeVertices = 0
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

    def getWeightConId(self, id1, id2):
        peso = 0
        arreglo = self.mapaCiudad[id1]
        for i in arreglo:
            if i[0] == id2:
                peso = i[1]
        return peso

    def getSuccessors(self, vertice):
        lista = []
        arreglo = self.mapaCiudad[vertice]
        for i in arreglo:
            if i[1] != 0:
                lista.append(i[0])
        return lista

    def getId(self, name):
        contador = 0
        for i in self.nombreVertice:
            if i == name:
                return contador
            contador += 1

    def addVertex(self, id, name):
        self.nombreVertice[id] = name
        self.numeroDeVertices += 1

    def backtracking(self, inicio1, fin1):
        inicio = self.getId(inicio1)
        fin = self.getId(fin1)
        visitado = [False]*self.size
        lista = self.backtrackingAux(inicio, fin, visitado, [], 0)
        return self.menor(lista)

    def menor(self, lista):
        print(max(lista))


    def backtrackingAux(self, inicio, fin, visitado, lista, peso):
        visitado[inicio] = True
        if inicio == fin:
            lista.append(peso)
            return
        for vecino in self.getSuccessors(inicio):
            if not visitado[vecino]:
                pesoAux = self.getWeightConId(inicio, vecino)
                self.backtrackingAux(vecino, fin, visitado, lista, peso = peso + pesoAux)
        return lista

def main():
    g = Ciudad(5)
    g.addVertex(1, "Movies")
    g.addVertex(2, "Snell")
    g.addVertex(3, "Hospital")
    g.addArc("Movies", "Snell", 10)
    g.addArc("Movies", "Hospital", 40)
    g.addArc("Snell", "Hospital", 10)
    g.addArc("Hospital", "Snell", 20)
    g.addArc("Hospital", "Movies", 20)
    print(g.backtracking("Movies", "Hospital"))

main()
