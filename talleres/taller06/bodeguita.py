def devolver(denominaciones : list, cantidad : int):
    denominaciones.sort(reverse = True) # O(n log n)
    for denominacion in denominaciones: # O(n)
        numeroDeMonedas = cantidad // denominacion
        cantidad = cantidad % denominacion
        print(str(numeroDeMonedas) + " de " + str(denominacion))
#+ __________
#  O(n log n)
def main():
    devolver([200,500,100,50],2300)
main()