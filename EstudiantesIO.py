from StudentIO.FuncionDigitaDatos import digitaDatos
from StudentIO.FuncionGuardarShelve import guardarDatos
from StudentIO.FuncionLeerShelve import leerDatos

# Funcion para ingresar datos sin formato shelve
datosestudiante = digitaDatos()

# Funcion para  guardar los datos en formato shelve
datosguardados = guardarDatos(datosestudiante)

# Funcion para leer los datos que tienen formato shelve
leerdatos =  leerDatos(datosguardados)