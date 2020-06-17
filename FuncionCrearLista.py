def CrearLista(elementos):
    Lista = []
    aux = 0
    while aux < elementos:
        elemento = int(input(f"Lista[{aux}]="))
        Lista.append(elemento)
        aux += 1
    print(f"Lista original = {Lista}")
    return Lista