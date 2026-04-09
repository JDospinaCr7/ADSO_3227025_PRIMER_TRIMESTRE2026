from abc import ABC, abstractmethod

# creremos la clase abstracta
class Figura(ABC):
        @abstractmethod
        
        def calcular_area(self): # este metodo es obligatorio colocarlo en todo las subclases
            pass
# ahora creaaremos las subclases de figura
class Circulo(Figura):
    def __init__ (self,radio):
         self.radio = radio

    def calcular_area(self): 
            return ((self.radio ** 2) * 3.1416)

class Cuadrado(Figura):
    def __init__ (self, lado1, lado2):
         self.lado1 = lado1
         self.lado2 = lado2

    def calcular_area(self):
        return (self.lado1 * self.lado2) 

class Piramide(Figura):
    def __init__ (self, altura, base):
         self.base = base
         self.altura = altura

    def calcular_area(self):
         return ((self.base * self.altura) / 2)

class Rectangulo(Figura):
    def __init__(self, lado3, lado4):
         self.lado3 = lado3 
         self.lado4 = lado4

    def calcular_area(self):
         return (self.lado3 * self.lado4)

class Cilindro(Figura):
    def __init__(self, altura2, volumen):
         self.altura2 = altura2
         self.volumen = volumen

    def calcular_area(self):
         return (((self.altura2 * 3.1416) / self.volumen)** 0.5)

# vamps a ejecutar 

def mostrar_area(figura: Figura):
     print(f"Area:   {figura.calcular_area():.2f}")

def main():

    radio1 = float(input("Ingrese un número para calcular el radio del circulo: "))
    circulo1 = Circulo(radio1)
    mostrar_area(circulo1)

    lado1 = float(input("Ingrese la primera medida del cuadrado para calcular el area: "))
    lado2 = float(input("Ingrese la segunda memida del cuadrado para calcular el area: "))
    cuadrado1 = Cuadrado(lado1, lado2)
    mostrar_area(cuadrado1)

    base = float(input("Ingrese la base del triangulo para calcular el area: "))
    altura = float(input("Ingrese la altura del triangulo para calcular el area: "))
    triangulo1 = Piramide(base, altura)
    mostrar_area(triangulo1)

    lado3 = float(input("Ingrese la primera medida del rectangulo para calcular el area: "))
    lado4 = float(input("Ingrese la segunda medida del rectangulo para calcular el area: "))
    rectangulo1 = Rectangulo(lado3, lado4)
    mostrar_area(rectangulo1)

    altura2 = float(input("Ingrese la altura del cilindro para calcular el area: "))
    volumen = float(input("Ingrese el volumen del cilindro para calcular el area: "))
    cilindo1 = Cilindro(altura2, volumen)
    mostrar_area(cilindo1)

if __name__ == "__main__":
    main()
