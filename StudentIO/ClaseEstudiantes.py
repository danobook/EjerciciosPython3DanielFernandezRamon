class Estudiante():


    def __init__(self, nombre, edad, correo, sexo ,estado ):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.sexo = sexo
        self.estado = estado

    def ingresarDatos(self):
        self.nombre = input("Digita el nombre:")
        self.edad = input("Digita la edad:")
        self.correo = input("Digita el correo:")
        self.sexo = input("Digita el sexo:")
        self.estado = input("Digita el estado:")

