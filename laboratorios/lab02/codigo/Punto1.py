from cmath import inf
from collections import deque

class Ciudad:
    def __init__(self, size):
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

    def getId(self, name):
        contador = 0
        for i in self.nombreVertice:
            if i == name:
                return contador
            contador += 1

    def addVertex(self, id, name):
        self.nombreVertice[id] = name
        self.numeroDeVertices += 1

    def permutacionesDeUna(self, cadena):
        return self.permutacionesAux(cadena, "", [])

    def permutacionesAux(self, pregunta, respuesta, lista):
        if len(pregunta)==0:
            lista.append(respuesta)
        else:
            for i in range(0,len(pregunta)):
                nuevaPregunta = pregunta[0:i] + pregunta[i+1:]
                self.permutacionesAux(nuevaPregunta, respuesta+pregunta[i], lista)
        return lista

    def stringVertices(self):
        cadena = ""
        for i in range(1, self.numeroDeVertices+1):
            cadena = cadena + str(i)
        return cadena

    def listaPermutaciones(self, lista, listaFinal):
        lista = self.permutacionesDeUna(self.stringVertices())
        listaAux = []
        for permutaciones in lista:
            for i in range(len(permutaciones)):
                listaAux.append(int(permutaciones[i]))
            listaFinal.append(listaAux.copy())
            listaAux = []
        return listaFinal

    def caminoMasCortoBrutForce(self, vertice):
        lista = self.listaPermutaciones([], [])
        pesoTotal = inf
        idVertice = self.getId(vertice)
        for permutacion in lista:
            pesoInicial = self.getWeightConId(idVertice, permutacion[0])
            Aux = 0
            if permutacion[0]==idVertice:
                pass
            elif permutacion[self.numeroDeVertices-1] != idVertice:
                pass
            elif pesoInicial == None:
                pass
            else:
                Aux = pesoInicial
                for pesoSiguiente in range(1,len(permutacion)):
                    pesoConId = self.getWeightConId(permutacion[pesoSiguiente-1], permutacion[pesoSiguiente])
                    if pesoConId==None:
                        Aux = 0
                        break
                    else:
                        Aux += pesoConId
            if pesoTotal>Aux and Aux != 0:
                pesoTotal = Aux
        return pesoTotal


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
    print(g.caminoMasCortoBrutForce("Movies"))

main()