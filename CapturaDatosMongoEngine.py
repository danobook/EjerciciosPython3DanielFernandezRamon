from ClaseEstudiantes import estudianteDatos
from mongoengine import *
def escrituradatos():
    connect('padts')
    nombre = ""
    edad = ""
    correo = ""
    sexo = ""
    estado = ""
    datosestudiantes = estudianteDatos(nombre,edad,correo,sexo,estado)

    #Esquema/Modelo
    class Estudiantes(Document):
        nombre = StringField(required=True)
        edad = StringField(required=True)
        correo = StringField(required=True)
        sexo = StringField(required=True)
        estado = StringField(required=True)

        datosestudiantes.ingresarDatos()

    estudiantes = Estudiantes(
        nombre = datosestudiantes.nombre,
        edad =datosestudiantes.edad ,
        correo = datosestudiantes.correo ,
        sexo=datosestudiantes.sexo,
        estado = datosestudiantes.estado
        )

    estudiantes.save()

    return Estudiantes
