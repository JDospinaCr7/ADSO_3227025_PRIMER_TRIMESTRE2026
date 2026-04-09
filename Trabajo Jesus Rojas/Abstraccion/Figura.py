from abc import ABC, abstractmethod
#Crearemos la clase abstracta
class Figura(ABC):
    @abstractmethod
    def calcular_area(): #Este metodo es obligatorio colocarlo en todas las subclases(Hijos)
        pass

#Ahora crearemos las clases hijas de figura
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return ((self.radio ** 2) * 3.1416)
    
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado1 = lado

    def calcular_area(self):
        return(self.lado1 ** 2)

class Triangulo(Figura):
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2
    
    def calcular_area(self):
        return((self.lado1 * self.lado2) / 2)

class Rectangulo(Figura):
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2

    def calcular_area(self):
        return(self.lado1 * self.lado2)

class Cilindro(Figura):
    pass



def mostrar_area(figura: Figura):
    print(f"Area del circulo: {figura.calcular_area():.2f} :")

def area_cuadrado(cuadrado: Figura):
    print(f"Area del cuadrado: {cuadrado.calcular_area():.2f}")

def area_rectangulo(rectangulo: Figura):
    print(f"Area del rectangulo : {rectangulo.calcular_area():.2f}")

def area_triangulo(triangulo: Figura):
    print(f"Area del triangulo : {triangulo.calcular_area():.2f}")



def main():
    radio1 = float(input("Ingrese el radio del circulo: "))
    circulo1 = Circulo(radio1)
    mostrar_area(circulo1)

    lado = float(input("Ingrese el ancho del cuadrado: "))
    cuadrado1 = Cuadrado(lado)
    area_cuadrado(cuadrado1)

    lado1 = float(input("Ingrese el ancho del cuadrado: "))
    lado2 = float(input("Ingrese el alto del cuadrado: "))
    rectangulo1 = Rectangulo(lado1, lado2)
    area_rectangulo(rectangulo1)

    lado1 = float(input("Ingrese el alto del triangulo: "))
    lado1 = float(input("Ingrese el ancho del triangulo: "))
    triangulo1 = Triangulo(lado1, lado2)
    area_triangulo(triangulo1)

if __name__ == "__main__":
    main()