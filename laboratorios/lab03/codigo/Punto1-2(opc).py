import unittest

class Test(unittest.TestCase):
    def seAtacanHastaI(self, tablero, i):
        for j in range(0, i+1):
            for k in range(j+1, i+1):
                if abs(tablero[j]-tablero[k]) == abs(j-k) or tablero[j] == tablero[k]:
                    return True
        return False

    def nReinas(self, n:int):
        return self.nReinasAuxLista(n, 0, [0]*n, [])

    def nReinasAuxLista(self, n:int, col:int, lista:list, nuevaLista:list) -> None:
        if col == n:
            nuevaLista.append(lista.copy())
            return
        for f in range(n):
            lista[col] = f
            if self.seAtacanHastaI(lista, col):
                pass
            else:
                self.nReinasAuxLista(n, col+1, lista, nuevaLista)
        return nuevaLista

    def test_NReinas(self):
        lista = self.nReinas(4)
        self.assertTrue([2,0,3,1] in lista)
        #self.assertTrue([1,3,2,0] in lista)

if __name__ == "__main__":
    unittest.main()