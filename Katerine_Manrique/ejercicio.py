from abc import ABC,abstractmethod
#Crearemos la clase abstracta
class Figura(ABC):
    @abstractmethod
    def calcular_area(self):#Este metodo es obligatorio colocarlos en todas las subclases
     pass
#Ahora crearemos las clases hijas de la figura
class Circulo(Figura):
    def __init__(self,radio):
      self.radio = radio
    def calcular_area(self):
        return ((self.radio**2)*3.1416)
class Cuadrado(Figura):
  pass
class Rectangulo(Figura):
  pass
class Cilindro(Figura):
  pass
#Vamos a ejecutar
def mostrar_area(Figura:Figura):
    print(f"Area:{Figura.calcular_area():.2f}")
def main():
    radio1 = float(input("Ingrese el radio del circulo:"))    
    circulo1 = Circulo(radio1)
    mostrar_area(circulo1)
if __name__=="__main__":
    main()    
