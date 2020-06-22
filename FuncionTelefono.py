# Determinar si un numero es un numero telefonico valido
def ValidaTelefono():
    import re
    numero = input("Digita un numero telefonico:")
    print(numero)
    # Se utiliza determina los formatos a encontrar
    coincidencia1 = re.match(r"^(\d\d\d\d\d\d\d\d\d\d)$",numero)
    coincidencia2 = re.match(r"^(\(\d\d\)\d\d\d\d\d\d\d\d)$",numero)
    coincidencia3 = re.match(r"^(\(\d\d\d\)\d\d\d\d\d\d\d)$",numero)
    coincidencia4 = re.match(r"^(\(\d\d\)(\s|-)\d\d\d\d(\s|-)\d\d\d\d)$",numero)
    coincidencia5 = re.match(r"^(\(\d\d\d\)(\s|-)\d\d\d(\s|-)\d\d\d\d)$",numero)
    coincidencia6 = re.match(r"^(\d\d\d(\s|-)\d\d\d(\s|-)\d\d\d\d)$",numero)

    if (coincidencia1 or coincidencia2 or coincidencia3 or coincidencia4 or coincidencia4 or coincidencia5 or coincidencia6):
        print("El numero telefonico es valido")
    else:
        print("El numero telefonico no es valido,no tiene el formato correcto")
