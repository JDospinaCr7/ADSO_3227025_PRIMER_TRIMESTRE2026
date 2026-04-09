from abc import ABC, abstractmethod
from typing import List # importamos listas para usar notaciones de lista de objetos
#===========================================
#1. crearemos la clase abstracta persona
#===========================================

class persona(ABC): #Declaramos la super clase persona como abstracta
    def __init__(self,nombre: str) -> None:
        self.nombre = nombre
    @property
    def nombre(self) -> str: # Getter para el nombre de la persona
        return self.__nombre # Atributo privado _nombre,devuelve el nombre almacenado en el objeto
    
    @nombre.setter
    def nombre(self,nuevo_nombre: str) -> None :
        # ahora validamos el nuevo nombre_nombre que sea str
        if isinstance(nuevo_nombre,str) and nuevo_nombre.strip(): #validamos que strip() elimine espacios en blanco 
            self.__nombre = nuevo_nombre
        else:
             # si no cumples las condiciones del si realizamos esta excepcion para evitar estados invalidos 
             raise ValueError(" El nombre debe ser una cadena de caracteres")
    @abstractmethod
    def presentar(self) -> None: # Este metodo debe declararse en todas las clases hijas de persona
        pass
#===========================================
# CREAMOS LAS CLASES HIJAS 
#===========================================
class cliente(persona): # El cliente hereda de persona ( ahora es una subclase)
    def presentar(self) -> None: # Implementamos el metodo abstracto presentar()
            print(f"El cliente {self.nombre} ha llegado al restaurante")

class Empleado(persona): # El cliente hereda de persona (ahora es una subclase)
    @abstractmethod
    def trabajar(self) -> None: # Metodo definido dentro es esta clase,toda subclase de empleado debe implementarlo
            pass

class Mesero(Empleado): 
         def presentar(self) -> None:
            print(f"El mesero {self.nombre} esta atendiendo a los comensales")
         def trabajador(self) -> None: 
                print(f" El mesero {self.nombre} esta tomando pedidos")

class chef(Empleado):
          def presentar(self) -> None:
            print(f"El chef {self.nombre} esta en la cocina")
          def trabajar(self) -> None: #Implementamos en el metodo abstracto presentar() y trabajar()
                 print(f"El chef {self.nombre} esta preparando platos deliciosos")
           
#=============================================
# creamos la clase cocina (),pero esta no es ABC
# ============================================
class Cocina():
     def __init__(self,chefs:list[chef]) -> None: #este constructor recibe los objetos chef y los #almacena  en una lista 
          self.chefs = chefs 
     @property
     def chefs(self,) -> list[chefs]: #retornamos la lista privada de _chefs
          return self.chefs
     @chefs.setter
     def chefs(self,lista_chefs: list[chef]) -> None:
          #validamos que lista chefs y que todos los elementos sean insta
          if isinstance(lista_chefs,list) and all(isinstance(c,chef)for c in lista_chefs):
               self.chefs = lista_chefs # si la lista cumple lo anterior se almacena
          else:
               raise ValueError("Debe proporcionar una lista con elementos validos del chef")
     def operar(self) -> None:
          #Mostramos el trabajo de todos los chefs
          for chef in self.chefs: #Recorremos la lista chefs
               chef.trabajar() #llama a el metodo trabajar() de cada objeto chef

class restaurante():
     def __init__(self,nombre:str) -> None:
           self.nombre = nombre
           self.clientes : list[cliente] = []
           self.cocina = self.cocina([chef("Manos sucias"),chef("El chino cochina")])
     @property
     def nombre(self) -> str:
           return self.nombre
     @nombre.setter
     def nombre(self,nuevo_nombre:str) -> None:
          if isinstance(nuevo_nombre,str) and nuevo_nombre.strip():
            self.nombre = nuevo_nombre
          else:
            raise ValueError("El nombre del restaurante debe ser un nombre valido")
     def iniciar_servicio(self) -> None:
           #simularemos el servicio del restaurante
           print(f"\n==========Restaurante {self.nombre}iniciando servicio==========")
           print("\nAtendiendo clientes")
           for cliente in self.clientes:#llamamos el metodo presentar,generar polimorfismo
               cliente.presentar()
           print("\nCocina en operacion:")
           self.cocina.operar()


          
          

    
     
     
  