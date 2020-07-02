from ClaseEstudiantes import estudianteDatos
from mongoengine import *

def mostrardatos(Estudiantes):

    estudiantes = Estudiantes.objects

    print("\n.::Impresion de elementos de la base de datos::.")
    for index,p in enumerate(estudiantes):
        print(f"\tElemento {index+1}\nNombre:{p.nombre}\nEdad:{p.edad}\nCorreo:{p.correo}\nSexo:{p.sexo}\nEstado:{p.estado}")
    return estudiantes