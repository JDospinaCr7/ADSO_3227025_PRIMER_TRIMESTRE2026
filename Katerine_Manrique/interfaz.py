from abc import ABC, abstractmethod
from typing import Optional

#1 interfaz 
class Movible(ABC):
    #REPRESENTA animales que puedem desplazarse por si solos 
    @abstractmethod
    def mover(self) -> None:
        pass
class Animal(ABC):
    def __init__(self, nombre: str) -> None:
        self.__nombre: str =""  #privado y encapsulado
        self.nombre = nombre #ya nombre puede utilizarlo nommbre (getter y setter)
    #GETTER - MOSTRAR
    @property
    def nombre(self) -> None:   #permite leer o mostrar el nombre del animal de forma segura 
        return self.__nombre
        #SETTER - MODIFICA LA INSTANCIA DEL ATRIBUTO EN ESTE CASO DEL NOMBRE
    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        if isinstance(nuevo_nombre, str) and nuevo_nombre.strip() and nuevo_nombre !="":
            self.__nombre = nuevo_nombre.strip().title()
        else:
            raise ValueError("El nombre ingresado debe ser una cadena de texto valida")
    @abstractmethod
    def sonido(self) -> None:
        pass
#crearemos clases hijas para las dos ABC
class Perro(Animal):
    def sonido(self) -> None:
        print(f"{self.nombre} El perro hace Gua Gua")
class Gato(Animal):
    def sonido(self) -> None:
        print(f"{self.nombre} El gato hace Miau Miau")
class Vaca(Animal):
    def sonido(self) -> None:
        print(f"{self.nombre} La vaca hace Muu Muu")
#crearemos clases hijas de las dos clases ABC
class Leon(Animal, Movible):
    def sonido(self) -> None:
        print(f"{self.nombre} El leon dice: Roonar")
    def mover(self) -> None:
        print(f"{self.nombre} El leon se mueve sigilosamente por el SENA...")
#realizaremos las funciones polimorficas al rojo vivo
def hacer_sonido(animal: Animal) -> None:
    animal.sonido()

def desplazar(animal: Movible) -> None:
    animal.mover()

def main() -> None:
    try:
        animales = [
            Perro("Rocky"), #0
            Gato("Misu"), #1
            Vaca("Lola"), #2
            Leon("Simba"), #3
        ]

        print("===POLIMORFISMO EN NUESTRO ZOOLOGICO===")
        for animal in animales:
            hacer_sonido(animal )
        print("animales con movimiento")
        for animal in animales:
            if isinstance(animal, Movible):
                desplazar(animal)
#actualizacion del  nombre 
        print("Actualizacion del nombre")
        animales[3].nombre = "Mufaza"
        print(f"El nuevo nombre es: {animales[3].nombre}")

    except ValueError as e:
        print(f"Error, {e}")

if __name__ =="__main__":
    main()


    