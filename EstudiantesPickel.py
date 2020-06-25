from StudentIO import ClaseEstudiantes
from StudentIO.FuncionPickelGuardar import guardarDatos
from StudentIO.FuncionPickelLeer import leerDatos
from StudentIO.FuncionActualizar import actualizarDatos

nombre = ""
edad = ""
correo = ""
sexo = ""
estado = ""

estudiantes = ClaseEstudiantes.Estudiante(nombre, edad, correo, sexo, estado)
while True:
    #Funcion ingresarDatos
    print("\n\t.::Ingresar datos de estudiante::.")
    estudiantes.ingresarDatos()
    nombre = estudiantes.nombre
    edad = estudiantes.edad
    correo = estudiantes.correo
    sexo = estudiantes.sexo
    estado = estudiantes.estado
    guardar = input("Desea guaradar los datos del estudiante S/N: ")
    #Se crea base de datos con pickel
    if guardar == 's' or guardar == 'S':
        guardarDatos(nombre,edad,correo,sexo,estado)
        mostrar = input("Desea mostrar los datos S/N:")
        if mostrar == 's' or mostrar == 'S':
            # Se muestran los datos en consola
            leerDatos()
    else:
        print("Los datos no se guardaron")
        break
    continuar = input("Desea modificar los datos del estudiante S/N:")
    if continuar == 's' or continuar == 'S':
        actualizarDatos()
        print(".::Datos actualziados::.")
        leerDatos()
        break
    else:
        break




