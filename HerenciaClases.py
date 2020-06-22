# Programa para obtener el area y perimetro de un rectangulo y un triangulo rectagulo.
import math
class figura:
    def __init__(self,lados):
        self.lados = lados

    def validar(self):
        self.lados = self.lados
        if self.lados != 3 and self.lados != 4:
            return print("La figura no es valida")

class rectangulo(figura):
    def __init__(self,lado1,lado2):
        figura.__init__(self,lados)
        self.lado1 = lado1
        self.lado2 = lado2

    def perimetro(self):
        return (print(f"EL perimetro del rectangulo vale {(2*self.lado1) + (2*self.lado2)}"))

    def area(self):
        return (print(f"EL area del rectangulo vale {(self.lado1) * (self.lado2)}"))

class triangulo(figura):
    def __init__(self,lado1,lado2,lado3):
        figura.__init__(self,lados)
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def perimetro(self):
        return (print(f"EL perimetro del triangulo vale {(self.lado1) + (self.lado2) + (self.lado3)}"))

    def area(self):
        return (print(f"EL area del triangulo vale {(self.lado1) * (self.lado2) / 2}"))

print("Programa para obtener el area y perimetro de las figuras geometricas: rectangulo y triangulo rectagulo.")
lados = int(input("Digita el numero de lados:"))
r = figura(lados)
r.validar()
if lados==4:
    base = int(input("Digita la base  del rectangulo:"))
    altura = int(input("Digita la altura del rectangulo :"))
    j = rectangulo(base,altura)
    # Imprime area y perimetro de un cuadrado
    j.perimetro()
    j.area()
if lados==3:
    base = int(input("Digita la base  del triangulo:"))
    altura = int(input("Digita la altura del triangulo :"))
    hipotenusa = round(math.sqrt(base**2+altura**2),2)
    respuesta = input(f"La hipotenusa del trianuglo vale {hipotenusa} S/N:")
    if (respuesta != 's' and respuesta != 'S'):
        print("No se puede obtener el area, la figura no es un triangulo rectangulo")
    else:
        j = triangulo(base,altura,hipotenusa)
        # Imprime area y perimetro de un cuadrado
        j.perimetro()
        j.area()

