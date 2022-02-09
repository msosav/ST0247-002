def hayCamino(grafo, inicio:int, final:int) -> bool:
    if inicio == final:
        return True
    else:
        for vecino in grafo.getSuccesors(inicio):
            hayCaminoDelVecinoAd = hayCamino(grafo, vecino, final)
            if hayCaminoDelVecinoAd:
                return True
    return False #Si nunca dio verdadero es falso