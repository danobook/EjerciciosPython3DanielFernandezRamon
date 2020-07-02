def existedato(elementos):
    contador = 0
    filtro = input("\n\nDigita el nombre del estudiante a actualizar:").upper()

    estudiante = elementos.objects(nombre = filtro)
    print("\n.::Impresion de elementos con filtro::.")
    for index, p in enumerate(estudiante):
        print(f"\t Elemento {index + 1}\nId:{p.id}\nNombre:{p.nombre}\nEdad:{p.edad}\nCorreo:{p.correo}\nSexo:{p.sexo}\nEstado:{p.estado}")
        contador += 1
        idUpdate = p.id
    if contador==0:
        print("El dato no exiate")
    else:
        print("El dato si exiate")
    return idUpdate


