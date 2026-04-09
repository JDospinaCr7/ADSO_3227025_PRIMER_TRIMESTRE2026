from abc import ABC, abstractmethod

# Creamos la clase abstracta
class Figura(ABC):
      @abstractmethod
      def calcular_area(self): # Este metoido que cree es obligatorio colocarlo en todas las subclases 
          pass
      
# Ahora crearemos las clases hijas de Figura 
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    def calcular_area(self):
        return ((self.radio ** 2) * 3.1416)
    
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
    def calcular_area(self):
        return self.lado ** 2

class Rectangulo(Figura):
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2
    def calcular_area(self):
        return self.lado ** 2

class Triangulo(Figura):
     

class Cilindro(Figura):
    pass

# Vamos a ejecutar 
def mostrar_area(figura: Figura):
    print(f"Area: {figura.calcular_area():.2f}")
    
def main():
    radio1 = float(input("Ingrese el radio del circulo: "))
    circulo1 = Circulo(radio1)
    lado = float(input("Ingrese el lado del cuadrado: "))
    cuadrado1 = Cuadrado(lado)
    mostrar_area(circulo1)
    
    
    
if __name__ == "__main__":
    main()