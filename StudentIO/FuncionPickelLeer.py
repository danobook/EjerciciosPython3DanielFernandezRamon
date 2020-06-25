import pickle


def leerDatos():
    pickled_file = open('../pickled_file.pickle', 'rb')
    data = pickle.load(pickled_file)

    Nombre = data["name"]
    Edad = data["edad"]
    Correo = data["correo"]
    Sexo = data["sexo"]
    Estado = data["estado"]

    print(f"Nombre:{Nombre} ")
    print(f"Edad:{Edad}")
    print(f"Correo:{Correo}")
    print(f"Sexo:{Sexo}")
    print(f"Estado:{Estado}")
