def DeterminarPrimo(dato):
    numeros = 1
    aux = 0
    while numeros<=dato and dato>1:
        if dato%numeros==0:
            aux = aux + 1
        numeros = numeros + 1
    if dato <= 1:
        print("Los numeros primos comienzan desde apartir del 2")
        aux=3
    if aux>2:
        print("El dato no es primo")
    else:
        print("El dato es primo")