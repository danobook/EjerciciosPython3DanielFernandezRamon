from estudiante import Estudiante
from mongoengine import *
connect('padts')


def ingresaDatos():
    nombre = Estudiante.nombre(Estudiante)
    correo = Estudiante.correo(Estudiante)
    contrasena = Estudiante.contrasena(Estudiante)


    class estudiante(Document):
        nombre = StringField(required=True)
        correo = StringField(required=True)
        contrasena = StringField(required=True)


    estudiantedatos = estudiante(
        nombre = nombre,
        correo = correo ,
        contrasena=contrasena
        )

    estudiantedatos.save()

    return estudiante
