class Estudiante():
    nombre = ""
    email = ""
    __password = ""

    def __init__(self, nombre, email, password):
        self.nombre = nombre
        self.email = email
        self.__password = password
    def ingresarDatos(self):
        self.nombre = input("Digita el nombre:")
        self.email = input("Digita el email:")
        self.__password = input(("Digital la contraseña:"))

    def mostrarNombre(self):
        print("Nombre:",self.nombre)
    def mostrarEmail(self):
        print("Email:",self.email)
    def mostrarPassword(self):
        print("Contraseña :",self.__password)
