from abc import ABC, abstractmethod
from typing import List # importamos listas para usar notaciones de listas de objetos
#================================================================

#1. creamos la clase abstracta persona

#================================================================

class Persona(ABC): # Declaramos la superclase persona como abstracta
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        
    @property
    def nombre (self) -> str: # GETteR para el nombre de la persona 
        return self.nombre # atributo privado,_nombre, devuleve el nombre almacenado en el objeto
    
    @nombre.setter
    def  nombre(self, nuevo_nombre: str) -> None:
        # ahora validamos el nuevo_nombre que sea str
        if isinstance(nuevo_nombre, str) and nuevo_nombre.strip(): # validamos que strip() elimine espacios
            self._nombre = nuevo_nombre
        else:
            # si no cumple las condiciones del si realizamos esta excepcion para evitar estados invalidos 
            raise ValueError("El nombre debe ser una cadena de caracteres")
        
    @abstractmethod
    def presentar(self) -> None: # Este metodo debe declararse en todas las clases hijas de Persona 
        pass
    
# =============================================================

# CREAMOS LAS CLASES HIJAS

# =============================================================

class Cliente(Persona): # El cliente hereda de persona (ahora es una subclase)
    def presentar(self) -> None: # Imlplementamos el metodo abstarcto presentar()
        print(f"El cliente {self.nombre} ha llegado al restaurante")
        
class Empleado(Persona):
    @abstractmethod
    def trabajar(self) -> None: # Metodo definido dentro es esta clase, toda subclase de empleado debe 
        pass 
    
class Mesero(Empleado):
    def presentar(self) -> None: 
        print(f"El Mesero {self.nombre} esta atendiendo a los comensales")
    def trabajar(self) -> None: 
        print(f"El Mesero {self.nombre} esta tomando pedidos")
        
class Chef(Empleado):
    def presentar(self) -> None: 
        print(f"El Chef {self.nombre} esta em la cocina")
    def trabajar(self) -> None: 
        print(f"El Mesero {self.nombre} esta preparando platos deliciosos")
    
# ==================================================================

# crearemos la clase Cocina(), pero esta no es ABC

#===================================================================

class Cocina():
    def __init__(self, chefs: List[Chef]) -> None: # este constructor recibe los objetos y los
        self.chefs = chefs                                          # almacena en una lista
    @property
    def chefs(self) -> List[Chef]:
        return self.chefs
    @chefs.setter
    def chefs (self, lista_chefs: List[Chef]) -> None: 
        # validamos que lista_chefs y que todos los elementos sena instancias de class chef
        if isinstance(lista_chefs, List) and all(isinstance (c, Chef) for c in lista_chefs):
            self.chefs = lista_chefs # si la lista cimple lo anterior se almacena 
        else:
            raise ValueError("Debe proporcionar una lista con elementos validos de chef") 
        
    def operar(self) -> None:
        # mostraremos el trabajo de todos los chefs
        for chef in self.chefs: # recorremos la lista chefs 
            chef.trabajar() # Llama el metodo trabajar() de cada objeto chef    
            
class Restaurante():
    def __init__ (self, nombre: str) -> None:
        self.nombre = nombre
        self.clientes: List[Cliente] = []
        self.cocina = Cocina([Chef("El mencho"), Chef("El piratita")])
    @property
    def nombre(self) -> str:
        return self.nombre 
    @nombre.setter
    def nombre(self, nuevo_nombre :str) -> None:
        if isinstance(nuevo_nombre, str) and nuevo_nombre.strip():
            self._nombre = nuevo_nombre
        else: 
            raise ValueError("El nombre del restaurante debe ser un nombre valido")
        
    def agregar_cliente(self, cliente: Cliente) -> None:
        if isinstance(cliente, Cliente):
            self.clientes.append(cliente) # append agrega el cliente a la lista
        else:
            raise ValueError("El nombre del cliente debe ser un nombre valido")

    def iniciar_servicio(self) -> None: 
        #simularemos el servicio del restaurante
        print(f"\n===== Restaurante {self.nombre} iniciando servicio =====")
        print("\n Atendiendo clientes")
        for cliente in self.clientes: # llamammos al metodo presentar, genera el polimorfismo
            cliente.presentar()
        print("\n COCINA EN OPERACION")
        self.cocina.operar()
        
# ==================================================== 

# main

# ====================================================
       
            
def main():        
        
    # crearemos el restaurante con el nombre "La Buena Mesa"
    restaurante1 = Restaurante ("La carne en tus manos")
    # Agregamos Dos clientes al restaurante
    restaurante1.agregar.cliente(Cliente("Juan"))
    restaurante1.agregar.cliente(Cliente("Maria"))
    # simularemos inicio de operacion 
    restaurante1.iniciar_servicio()    
          
if __name__ == "__main__":
    main()