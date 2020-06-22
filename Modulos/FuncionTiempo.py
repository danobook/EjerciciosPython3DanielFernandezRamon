# Funcion que valida si un anio es bisiesto
def DeterminarAnio(dato):
    if dato<=0:
        print("No es un ano valido")
    else:
        if dato%400 == 0:
            print("El anio es bisiesto")
        elif dato%100 != 0 and dato%4 == 0:
            print("El anio es bisiesto")
        else:
            print("El anio no es bisiesto")
