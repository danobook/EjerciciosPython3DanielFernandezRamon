import POO


estudiantes = POO.Estudiante("Daniel","padts7@cinvestav.mx","password1")
print(estudiantes)
print(POO.Estudiante)
print("\n\t.:Se muestras datos de ejemplo:.")
estudiantes.mostrarNombre()
estudiantes.mostrarEmail()
estudiantes.mostrarPassword()
print("\n\t.:Se pide ingresar datos y luego se muestran:.")
estudiantes.ingresarDatos()
estudiantes.mostrarNombre()
estudiantes.mostrarEmail()
estudiantes.mostrarPassword()

