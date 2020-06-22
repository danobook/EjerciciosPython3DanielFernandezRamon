from Modulos.FuncionValidar import ValidaDato
from Modulos.FuncionSigno import DeterminaSigno
from Modulos.FuncionPar import  DeterminaParImpar
from Modulos.FuncionPrimo import DeterminarPrimo
from Modulos.FuncionTiempo import DeterminarAnio
print("Determinar el singno")
dato = ValidaDato()
DeterminaSigno(dato)
print("Determinar si es par o impar")
dato = ValidaDato()
DeterminaParImpar(dato)
print("Determinar si el numero es primo")
dato = ValidaDato()
DeterminarPrimo(dato)
print("Determinar si un anio es bisiesto")
dato = ValidaDato()
DeterminarAnio(dato)

