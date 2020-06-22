def ValidaDato():
    while True:
        try:
            dato = int(input("Digita un numero entero:"))
            return dato
            break
        except ValueError:
            print("ATENCIÓN: Debe ingresar un número entero.")

