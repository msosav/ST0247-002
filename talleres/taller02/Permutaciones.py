def permutaciones(cadena):
    permutacionesAux(cadena,"")

def permutacionesAux(pregunta, respuesta):
    if len(pregunta)==0:
        print(respuesta)
    else:
        for i in range(0,len(pregunta)):
            nuevaPregunta = pregunta[0:i]+pregunta[i+1:]
            permutacionesAux(nuevaPregunta , respuesta+pregunta[i])


def main():
    permutaciones("123")
main()