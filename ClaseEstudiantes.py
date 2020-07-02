class estudianteDatos():


    def __init__(self, nombre, edad, correo, sexo ,estado ):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.sexo = sexo
        self.estado = estado

    def ingresarDatos(self):
        self.nombre = input("Digita el nombre:").upper()
        self.edad = input("Digita la edad:").upper()
        self.correo = input("Digita el correo:").upper()
        self.sexo = input("Digita el sexo:").upper()
        self.estado = input("Digita el estado:").upper()


