from CapturaDatosMongoEngine import escrituradatos
from MuestraDatosMongoEngine import mostrardatos
from MuestraSiExsiteDato import existedato
from ClaseEstudiantes import estudianteDatos
from ActualizaDatosEngine import datosnuevos
# Se capturan los elementos d la base de datos
Estudiantes = escrituradatos()
# Se muestran los elementos de la base de datos
datos = mostrardatos(Estudiantes)
# Determina si hay un elementos de la base de datos que se desea actualziar
datoexistente = existedato(Estudiantes)

# Se envia el estudiane como parametro a la funcion y se regresa el dato actualizado
#datoactualizado = datosnuevos(Estudiantes)



