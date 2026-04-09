from abc import ABC, abstractmethod
from typing import List # Importamos listas para usar notaciones de listas de objetos
#==========================================
#1. Creamos la clase abstracta persona
#==========================================

class Persona(ABC): # Declaramos la super clase persona como abstracta
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
    @property
    def nombre(self) -> str: # GETTER para el nombre de la persona
        return self._nombre # Atributo privaso _nombre, devuelve el nombre almacenado en el objecto
    
    
    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        # Ahora validamos que el nuevo_nommbre sea str
        if isinstance(nuevo_nombre, str) and nuevo_nombre.strip(): # Validamos que strip() elimine espacios
            self._nombre = nuevo_nombre
        else:
            # Si no cumple las condiciones del si realizamos esta excepcion para evitar estados invalidos
            raise ValueError("El nombre debe de ser una cadena de caracteres.")
    @abstractmethod
    def presentar(self) -> None: #Este metodo debe de declararse en todas las clases hijas de persona
        pass
    #======================================
    # CREAMOS LAS CLASES HIJAS
    #======================================
class Cliente(Persona):  # El cliente hereda de persona ( ahora es una subclase)
    def presentar(self) -> None: # Implementamos el metodo abstracto presentar()
        print(f"El cliente {self.nombre} ha llegado al restuarante.") 
            
class Empleado(Persona): # El cliente hereda de persona ( ahora es una subclase)
    @abstractmethod
    def trabajar(self) -> None:
        pass
    
class Mesero(Empleado):
    def presentar(self) -> None:
        print(f"El Mesero {self.nombre} esta atendiendo a los comensales.")
    def trabajar(self) -> None:
        print(f"El Mesero {self.nombre} esta toamndo pedidos.")
        
class Chef(Empleado):
    def presentar(self) -> None:
        print(f"El Chef {self.nombre} esta en la cocina.")
    def trabajar(self) -> None: # Implementamos el metodo abstracto presentar() y trabajar()
        print(f"El Chef {self.nombre} esta preparando platos deliciosos.")
#=====================================================
    # CREAMOS LA CLASSE COCINA(), PERO ESTA NO ES ABC
#=====================================================
class Cocina():
    def __init__(self, chefs: List[Chef]) -> None: # Eeste constructor recibe los objetos del chef y los almacena
        self.chefs = chefs # Aqui realiza internamente @chefs.setter
    @property
    def chefs(self) -> List[Chef]: #Retornamos la lista privada de _chefs
        return self.chefs
    @chefs.setter
    def chefs(self, lista_chefs: List[Chef]) -> None:
        # Validamos que lista_chefs y que todos los elementos sean instancias de class chef
        if isinstance(lista_chefs, list) and all(isinstance(c, Chef) for c in lista_chefs):
            self.chefs = lista_chefs # Si la lista cumple con lo anterio se almacena
        else:
            raise ValueError("Debe proporcionar una lista con elementos validos para el chef")
    def operar(self) -> None:
        for chef in self.Chefs:
            chef.trabajar()
            
class Restaurante():
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.clientes: List[Cliente] = []
        self.cocina = Cocina([Chef("Manos Sucias"), Chef("El chico cochina")])
    @property
    def nombre(self) -> str:
        return self.nombre
    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        if isinstance(nuevo_nombre, str) and nuevo_nombre.strip():
            self._nombre = nuevo_nombre
        else:
            raise ValueError("El nombre del restaurante debe de ser un nombre valido.")
    def agregar_Cliente(self, cliente: Cliente) -> None:
        if isinstance(cliente, Cliente):
            self.cliente.append(cliente) # Append agrega el cliente a la lista
        else:
            raise ValueError("El nombre del cliente debe ser un nombre valido.")
    def iniciar_servicio(self) -> None:
        # Simuladoremos el servicio del restaurante 
        print(f"\n======= Restaurante {self.nombre} iniciando servicio =======")
        print("\nArendiendo clientes")
        for cliente in self.clientes: # Llamamos al metodo presentar, generar el polimorfismo
            cliente.presentar()
        print("\n COCINA EN OPERACION:")
        self.cocina.operar()
#====================================
# Main
#====================================
def main() -> None:
    # Crearemos el restuarante con el nombre "La Buena Masa"
    restaurante1 = Restaurante("La Buena Masa")
    # Agregarenos DOS clientes al restaurante
    restaurante1.agregar.cliente(Cliente("Juan"))
    restaurante1.agregar.cliente(Cliente("Maria"))
    # SIMULAREMOS INICIO DE OPERACION
    restaurante.iniciar_servicio()

if __name__ == "__main__":
    main()
    
    

