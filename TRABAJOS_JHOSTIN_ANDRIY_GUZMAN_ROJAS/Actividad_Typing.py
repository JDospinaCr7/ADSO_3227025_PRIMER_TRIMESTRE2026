from abc import ABC, abstractmethod

from typing import Optional

# 1 interfaz

class Movible(ABC):
    # Representa animales que pueden desplazarse por si solos  
    @abstractmethod
    def mover (self) -> None:
        pass
    
class Animal(ABC):
    def __init__ (self, nombre: str) -> None:
        self.__nombre: str = "" # privado y encapsulado
        self.nombre = nombre  # Ya nombre puedo utilizarlo nombre ( getter, setter)
        
# GETTER - MOSTRAR
    @property
    def nombre(self) -> None: #permite leer o mostrar el nombre del animal de ofrma segura
        return self.__nombre

# SETTER - modifica el la instancia del atributo en este caso el nombre
    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        if isinstance(nuevo_nombre, str) and nuevo_nombre.strip() and nuevo_nombre != "":
            self.__nombre = nuevo_nombre.strip().title()
        else: 
            raise ValueError("El nombr ingresado debe ser una cadena de texto valida")
    @abstractmethod
    def sonido(self) -> None:
        pass 

# crearemos clases hijas para las dos ABC

class Perro(Animal):
    def sonido(self) -> None:
     print(f"{self.nombre} hace guau")
     
class Paloma(Animal):
    def sonido(self) -> None:
        print(f"{self.nombre} dice yo la queria")

# crearemos clases hijas de las dos clases ABC        
class Leon(Animal, Movible):
    def sonido(self) -> None:
        print(f"{self.nombre} el leon hace Rooar")
    def mover(self) -> None:
        print(f"{self.nombre} la mueve sin tocarla")

# realizaremos is funciones polimorficas al rojo vivo
     
def hacer_sonido(animal: Animal) -> None:
    animal.sonido()
    
def desplazar (animal: Movible) -> None:
    animal.mover()
    
         
def main():
    
    try: 
        animales = [
            Perro("Dylan"),
            Paloma("Misu"),
            Leon("Pelu")
        ]
        
        print("=== POLIMORFISMO EN NUESTRO ZOOLOGIOC ===".center(50))
        
        for animal in animales:
            hacer_sonido(animal)
        print("animales con movimiento")
        for animal in animales:
            if isinstance(animal, Movible):
                desplazar(animal)

# actualizacion del nombre
        print("Actualizacion del nombre") 
        animales[2].nombre = "Mufaza"
        print(f"El nombre es: {animales[2].nombre}")
            
    except ValueError as e:
        print(f"Error, {e}")
    
if __name__ == "__main__":
    main()