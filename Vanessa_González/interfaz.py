from abc import ABC, abstractmethod
from typing import Optional # Es para la libreria de tipado fuerte

# Interfaz 1
class Movible(ABC):
    # Representa animales que pueden moverse por si solos
    @abstractmethod
    def mover (self) -> None:
        pass 
class Animal(ABC):
    def __init__(self, nombre: str) -> None:
        self.__nombre: str = "" # Privado y encapsulado
        self.nombre = nombre # Ya nombre puedo utilizarlo nombre (getter, setter)
        
    # GETTER - Mostrar
    @property
    def nombre(self) -> None: # Permite leer o mostrar el nombre del animal de forma segura, esto es lo que hace esta property
        return self.__nombre
    
    # SETTER - Modifica la instancia del atributo en este caso es el nombre
    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        if isinstance(nuevo_nombre,str) and nuevo_nombre.strip () and nuevo_nombre != "":
            self.__nombre = nuevo_nombre.strip().title() # El strip y el title es para quitar los espacios en blanco
        else:
            raise ValueError("El nombre ingresado debe de ser una cadena de texto valida.")
    @abstractmethod
    def sonido(self) -> None:
        pass
    
# Creamos las clases hijas de los dos ABC
class Perro(Animal):
    def sonido(self) -> None:
        print(f"{self.nombre} El perro hacer guau guau.")
        
class Gato(Animal):
    def sonido(self) -> None:
        print(f"{self.nombre} El gato hace miau miau.")
        
class Vaca(Animal):
    def sonido(self) -> None:
        print(f"{self.nombre} La vaca hace muuuu.")
        
# Creamos clases hijas de dos padres ABC
class Leon(Animal, Movible):
    def sonido(self) -> None:
        print(f"{self.nombre} El leon hace groar.")
    def mover(self) -> None:
        print(f"{self.nombre} El leon se mueve sigilosamente por el SENA.")
        
# Realizamos las funciones polimorfisticas al rojo vivo
def hacer_sonido(animal: Animal) -> None:
    animal.sonido()
    
def desplazar(animal: Movible) -> None:
    animal.mover()
    
def main() ->None:
    try:
        animales = [
        Perro("Rocky"), #0
        Gato("Mia"), #1
        Vaca("Sisi"), #2
        Leon("Simba") #3
        
        ]
        print("==== POLIMORFISMO EN NUESTRO ZOLOGICO ====")
        for animal in animales:
            hacer_sonido(animal)
        print("Animales con movimiento")
        for animal in animales:
            if isinstance(animal, Movible):
                desplazar(animal)
                
# Actualizamos el nombre
        print("Actualizamos el nombre.")
        animales[3].nombre = "Mufaza"
        print(f"El nuevo mobre es: {animales[3].nombre}")
    except ValueError as e:
        print(f"Error, {e}")
        
if __name__ == "__main__":
    main()