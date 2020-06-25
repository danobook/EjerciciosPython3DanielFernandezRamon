import pickle


def guardarDatos(nombre,edad,correo,sexo,estado):

    pickled_file = open('../pickled_file.pickle', 'wb')
    data = {'name': nombre, 'edad': edad, 'correo': correo, 'sexo': sexo,'estado':estado}
    pickle.dump(data, pickled_file)
    return pickled_file
