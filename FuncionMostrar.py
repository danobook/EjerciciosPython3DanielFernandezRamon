def mostrardatos(Estudiante):
    estudiante = Estudiante.objects
    print("\n.::Impresion de elementos de la base de datos::.")
    for index,p in enumerate(estudiante):
        print(f"\tElemento {index+1}\nNombre:{p.nombre}\nCorreo:{p.correo}\nContrasena:{p.contrasena}")
