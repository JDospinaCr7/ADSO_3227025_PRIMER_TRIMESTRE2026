from abc import ABC, abstractmethod
#Creamos la clase abstracta
class Empleado(ABC):
    def __init__(self, nombre: str) -> None:
        self._nombre = None #Queda el atributo nombre como privado
        self.nombre = nombre # Aqui llamamos al setter automaticamente

    #Crearemos los getter

    @property
    def nombre(self) -> str:
        #Tendra acceso seguro al nombre del empleado
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor: str) -> None: # Setter profecional con validacion basica
        if isinstance(valor, str) and valor.strip():
            self._nombre = valor.strip()
        else:
            raise ValueError("El nombre debe ser de tipo texto")
    
    @abstractmethod
    def trabajar(self) -> None:
        #Este metodo es obligatorio en todas las clases
     
        pass
#Creaaremos las clases hijas

class Gerente(Empleado):
    def trabajar(self) -> None:
        print(f"{self.nombre} Esta administrando toda la empresa")

class Desarrollador(Empleado):
    def trabajar(self) -> None:
        print(f"{self.nombre} Esta escribiendo código en python")

class Vendedor(Empleado):
    def trabajar(self):
        print(f"{self.nombre} Esta vendiendo Avon")

class Tecnico(Empleado):
    def trabajar(self):
        print(f"{self.nombre} esta con falla en el sistema")

#Creamos polimorfismo activo
def ejecutar_tarea(empleado: Empleado):
    empleado.trabajar()

def main():
    #creamos los objetos
    gerente1 = Gerente("Sebastian Herradura ")
    desarrollador1 = Desarrollador("Cristian Valero")
    vendedor1 = Vendedor("Pablo neruda")
    tecnico1 = Tecnico("Luis Perez")

    print("****** Polimorfismo con getter y Setter ******")

    ejecutar_tarea(gerente1)
    ejecutar_tarea(desarrollador1)
    ejecutar_tarea(vendedor1)
    ejecutar_tarea(tecnico1)

    print("************ Polimorfismo con setter ************")
    gerente1.nombre = "Mencho"
    desarrollador1.nombre = "Menchora"
    vendedor1.nombre = "Pedro Picapiedra"
    tecnico1.nombre = "Pablo Emilio"

    ejecutar_tarea(gerente1)
    ejecutar_tarea(desarrollador1)
    ejecutar_tarea(vendedor1)
    ejecutar_tarea(tecnico1)

if __name__ == "__main__":
    main()