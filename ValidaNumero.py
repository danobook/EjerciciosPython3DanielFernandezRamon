def ValidaDato():
    while True:
        try:
            elementos = int(input("Digita el numero de elementos de la lista:"))
            if elementos > 0:
                return elementos
                break
            else:
                print("ATENCIÓN: Debe ingresar un número entero positivo.")
        except ValueError:
            print("ATENCIÓN: Debe ingresar un número entero positivo.")




