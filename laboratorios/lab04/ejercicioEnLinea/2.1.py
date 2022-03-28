def Userinput():
    while(True):
        primeraLinea = str(input("Digite numero de rutas, duracion total, tarifa: "))
        numeroConductores = int(primeraLinea[:primeraLinea.index(" ")])
        duracionMax = int(primeraLinea[primeraLinea.index(" ") + 1:primeraLinea.rindex(" ")])
        tarifa = int(primeraLinea[primeraLinea.rindex(" ") + 1:])
        

        if numeroConductores==0 and duracionMax==0 and tarifa==0:
            break

        rutaManana = str(input("Digite las duraciones de las rutas de la manana: "))
        rutaTarde = str(input("Digite las duraciones de las rutas de la tarde: "))

        duracionRutasManana = [0]*numeroConductores
        duracionRutasTarde = [0]*numeroConductores
        
        rutaMananaAux = rutaManana
        for i in range(numeroConductores):
            if " " in rutaMananaAux:
                numM = int(rutaMananaAux[:rutaMananaAux.index(" ")])
            else: numM = int(rutaMananaAux)
            duracionRutasManana[i] = numM
            if i < numeroConductores-1:
                rutaMananaAux = rutaMananaAux[rutaMananaAux.index(" ") + 1:]
        
        rutaTardeAux = rutaTarde
        for j in range(numeroConductores):
            if " " in rutaTardeAux:
                numT = int(rutaTardeAux[:rutaTardeAux.index(" ")])
            else: numT = int(rutaTardeAux)
            duracionRutasTarde[j] = numT
            if j < numeroConductores-1:
                rutaTardeAux = rutaTardeAux[rutaTardeAux.index(" ") + 1:]

        print(rutas(numeroConductores,duracionMax,tarifa,duracionRutasManana,duracionRutasTarde))


def rutas(numeroConductores, duracionMax , tarifa, duracionRutasManana, duracionRutasTarde):
    duracionRutasManana.sort()
    duracionRutasTarde.sort()

    mSize = len(duracionRutasManana) - 1
    inicio = 0

    conductores = [0]*numeroConductores
    for i in range(len(conductores)):
        conductores[i] = duracionRutasManana[mSize] + duracionRutasTarde[inicio]
        inicio += 1
        mSize -= 1
    
    excedente = 0
    for j in range(len(conductores)):
        if conductores[j] > duracionMax:
            residuo = conductores[j] - duracionMax
            excedente += residuo
    return excedente * tarifa

def main():
    Userinput()

main()