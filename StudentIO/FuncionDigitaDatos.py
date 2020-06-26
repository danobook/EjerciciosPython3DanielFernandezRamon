from StudentIO.claseEstudiante import estudiante
def digitaDatos():


    print(".::Digita los datos dle estudiante::.")
    nombre = input("Nombre:")
    edad = input("Edad:")
    correo = input("Correo:")
    sexo = input("Sexo:")
    estado = input("Estado:")

    datos = estudiante(nombre, edad, correo, sexo, estado)
    print(".::Imprimiendo datos sin formato Shelve::.")
    print(f"Nombre:{datos.nombre}")
    print(f"Edad:{datos.edad}")
    print(f"Correo:{datos.correo}")
    print(f"Sexo:{datos.sexo}")
    print(f"Estado:{datos.estado}")

    return datos

