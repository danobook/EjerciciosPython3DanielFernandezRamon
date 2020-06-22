def ValidarEmail():
    import re

    correo = input("Digita la direccion de e-mail:")
    bandera = correo.count("@")
    patron1 = "@padts.mx$"
    patron2 = "@padts.com.mx$"
    patron3 = "@python.padts.mx$"

    if bandera == 1:
        correo = correo.replace(" ", "")
        bloques = correo.partition("@")
        coincidencia1 = re.match(patron1, bloques[1]+bloques[2])
        coincidencia2 = re.match(patron2, bloques[1]+bloques[2])
        coincidencia3 = re.match(patron3, bloques[1]+bloques[2])
        if coincidencia1 or coincidencia2 or coincidencia3:
            print(correo)
            print("El correo electronico es valido")
            print(f"Usuario:{bloques[0]}")
            print(f"Compania:{bloques[2]}")
        else:
            print("El correo electronico no es valido")



    else:
        print("El correo electronico no es valido")
