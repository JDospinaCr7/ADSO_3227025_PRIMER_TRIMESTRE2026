from abc import ABC, abstractmethod
from typing import Optional

#1 Interfas
class movible(ABC):
    #Representa animales que pueden moverse por si solos
    @abstractmethod
    def mover(self) -> None:
        pass

class Animal(ABC):
    def __init__(self, nombre: str) -> None:
        self.__nombre: str = ""
        self.nombre = nombre # yo nombre puedo utilizaro (getter y setter)
    #Getter - mostrar
    @property
    def nombre (self) -> None:
        return self.__nombre
    
    #Setter - modifica la instancia del atributo en este caso el nombre
    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        if isinstance(nuevo_nombre, str) and nuevo_nombre.strip() and nuevo_nombre !="":
            self.__nombre = nuevo_nombre.strip().title()
        else:
            raise ValueError("El nombre ingresado debe ser una cadena de texto vvalida")
        
    @abstractmethod
    def sonido(self) -> None:
        pass

#Crearemos las clases hijas para las dos ABC
class Perro(Animal):
    def sonido(self) -> None:
        print(f"{self.nombre} El perro ladra")

class Gato(Animal):
    def sonido(self) -> None:
        print(f"{self.nombre} El gato hace miau")

class Vaca(Animal):
    def sonido(self) -> None:
        print(f"{self.nombre} La vaca hace mu")

class Leon(Animal, movible):
    def sonido(self) -> None:
        print(f"{self.nombre} El leon dice: Roooar")
    def mover(self) -> None:
        print(f"{self.nombre} el leon se mueve sigilosamente por el SENA")


#Realizamos las funciones polimorficas al rojo vivo
def hacer_sonido(animal: Animal) -> None:
    animal.sonido()

def desplazar(animal: movible) -> None:
    animal.mover()

def main() -> None:
    try:
        animales = [
            Perro("Rocky"),
            Gato("Misu"),
            Vaca("Lola"),
            Leon("Simba")
        ]
        print(f" ====== Polimorfismo en nuestro zoologico ======")
        for animal in animales:
            hacer_sonido(animal)
        print("Animales en movimiento")
        for animal in animales:
            if isinstance (animal, movible):
                desplazar(animal)
#Actualizar el nombre
        print("Actualizacion del nombre")
        animales[3].nombre = "mufasa"
        print(f"El nuevo nombre es: {animales[3].nombre}")
        
    except ValueError as e:
        print(f"Error, {e}")

if __name__ == "__main__":
    main()