from abc import ABC, abstractmethod
from typing import List # Importamos listas de objetos

#1. Crearemos la clase abstracta persona

class Persona(ABC): #Declaramos la superclase persona como abstracta
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre

    @property
    def nombre(self) -> str:
        return self.nombre #Atributo privado nombre, devielve el nombre almacenado en el objeto
    
    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        #Ahora validamos el nuevo nombre que sea str
        if isinstance(nuevo_nombre, str) and nuevo_nombre.strip():  #Validamos que strip() elimine espacios
            self._nombre = nuevo_nombre
        else:
            #Si no cumple con las condiciones del si realizamos esta excepcion para evitar estados invalidos
            raise ValueError("El nombre debe ser una cadena de texto valida.")
    @abstractmethod
    def presentar(self) -> None: #Este metodo debe declararse en todas las clases hijas de persona
        pass

    #===================================================
    #Creamos las clases hijas
class Cliente(Persona):
    def presentar(self) -> None: #Implementamos el metodo abstracto presentar()
        print(f"El cliente {self.nombre} ha llegado al restaurante")
        
class Empleado(Persona):
    @abstractmethod
    def trabajar(self) -> None:
        pass

class Mesero(Empleado):
    def presentar(self) -> None:
        print(f"El mesero {self.nombre} esta atendiendo a los comensales")
    def trabajar(self) -> None:
        print(f"El mesero {self.nombre} esta tomando pedidos")
class Chef(Empleado):
    def presentar(self) -> None:
        print(f"El chef {self.nombre} esta en la cocina")
    def trabajar(self) -> None:
        print(f"El chef {self.nombre} esta preparando platos deliciosos")

#================================================================================
#Crearemos la clase Cocina(), pero esta no es ABC
class Cocina():
    def __init__(self, chefs: List[Chef]) -> None: #Este constrictor recibe los objetos de chef y los almacena en una lista
        self.chefs = chefs
    @property
    def chefs(self) -> List[Chef]:
        return self.chefs
    
    @chefs.setter
    def chefs(self, lista_chefs: List[Chef]) -> None:
        #Validamos que lista chefs y qur todos los elementos sean instamcias de lass chef
        if isinstance(lista_chefs, list) and all(isinstance(c, Chef) for c in lista_chefs):
            self.chefs = lista_chefs # Si la lista comple lo anterior lo anterior se almacena
        else:
            raise ValueError("Debe proporcionar una lista con elementos validos de chef")
        
def operar(self) -> None:
    #Mostraremos el trabajo de todos los chef
    for chef in self.chefs:
        chef.trabajar() #Llama el metodo trabajar() de cada objeto chef

class Restaurante():
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.clientes: List[Cliente] = []
        self.cocina = Cocina([Chef("Manos Sucias") ,Chef("El chino cohino")])
    
    @property
    def nombre(self) -> str:
        return self.nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str) and nuevo_nombre.strip():
            self._nombre = nuevo_nombre
        else:
            raise ValueError("El nombre del restaurante debe ser un nombre valido")
        
    def iniciar_servicio(self) -> None:
        #Simularemos el servicio del restaurante
        print(f"\n ====== Restaurante {self.nombre} Iniciando servicio ======")
        print(f"\n Atendiendo clientes")
        for cliente in self.clientes: #Llamamos al metodo presentar, genera el polimorfismo
            cliente.presentar()
        print("\n Cocina en operacion")
        self.cocina.operar()
        

#====================
#Main
#====================
def main():
    #crearemos el restaurante con el nombre "La buena mesa"
    restaurante1 = Restaurante("La buena mesa")
    #Agregaremos un cliente el cliente al restaurante
    restaurante1.agregar.cliente(Cliente("Juan"))
    restaurante1.agregar.cliente(Cliente("Maria"))
    #Simulamos el inicio de operacion
    restaurante1.iniciar_servicio()


if __name__ == "__main__":
    main()