def permutacionRepeticion(cadena):
    permutacionAux(cadena,"")

def permutacionAux(pregunta, respuesta):
    if len(pregunta) == len(respuesta):
        print(respuesta)
    else:
        for i in range(0,len(pregunta)):
            permutacionAux(pregunta, respuesta+pregunta[i])


def main():
    permutacionRepeticion("123")
main()