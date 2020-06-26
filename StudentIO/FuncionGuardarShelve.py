import shelve

def guardarDatos(datos):

    name = datos.nombre
    age = datos.edad
    email = datos.correo
    sex = datos.sexo
    state = datos.estado

    #Aqui los datos se cambian a formato .db para contruir la base de datos
    with shelve.open('test_shelf.db') as s:
        s['key1'] = {
            'Nombre': name,
            'Edad': age,
            'Correo': email,
            'Sexo': sex,
            "Estado": state,
        }

    print("Los datos se han guardado correctamente")
    return s

