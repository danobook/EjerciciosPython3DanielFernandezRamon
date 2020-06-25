import pickle
from StudentIO import ClaseEstudiantes


def actualizarDatos():
    nombre = ""
    edad = ""
    correo = ""
    sexo = ""
    estado = ""

    estudiantes = ClaseEstudiantes.Estudiante(nombre, edad, correo, sexo, estado)

    estudiantes.ingresarDatos()
    nombre = estudiantes.nombre
    edad = estudiantes.edad
    correo = estudiantes.correo
    sexo = estudiantes.sexo
    estado = estudiantes.estado

    pickled_file = open('../pickled_file.pickle', 'wb')
    data = {'name': nombre, 'edad': edad, 'correo': correo, 'sexo': sexo,'estado':estado}
    pickle.dump(data, pickled_file)
    return pickled_file