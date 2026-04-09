from abc import ABC, abstractmethod
# CRAREMOS LA CLASE ABSTRACTA
class Empleado(ABC):
    def __init__(self, nombre: str) -> None:
        self._nombre = None # queda el atributo nombre como privado
        self.nombre = nombre # aqui llamamos al SETTER automaticamente
    # craremos los GETTER
    @property
    def nombre(self) -> str:
        # tendra acceso seguro al nombre del empleado
            return self._nombre
    
    @nombre.setter
    def nombre(self, valor: str) -> None: # SETTER profesional con validacion basica
            # valida que sea cadena
        if isinstance(valor, str) and valor.strip(): #strip() quita los espacios en blanco al principio y al final
             self._nombre = valor.strip()
        else: raise ValueError("El nombre debe ser de tipo texto. ".center(50))

    @abstractmethod
    def trabajar(self) -> None:
         # este metodo es obligatorio en todas las clases hijas por tener @abstractmethod
         pass 
    # crearemos las clases hijas
class Gerente(Empleado):
    def trabajar(self) -> None:
        print(f"{self.nombre} esta administrando la empresa. ")

class Desarrollador(Empleado):
    def trabajar(self) -> None:
        print(f"{self.nombre} esta escribiendo codigo en PYTHON. ")

class Vendedor(Empleado):
     def trabajar(self) -> None:
          print(f"{self.nombre} esta vendiendo petuches. ")

class Tecnico(Empleado):
     def trabajar(self) -> None:
          print(f"{self.nombre} esta arreglando la pc de Diddy")

# CREAREMOS UN POLIMORFISMO ACTIVO
def ejecutar_tarea(empleado: Empleado):
     empleado.trabajar()

# ejecucion didactica
def main():
     # craremos los objetos
     gerente1 = Gerente("jefrey eipstein")
     desarrollador1 = Desarrollador("Diddy")
     vendedor1 = Vendedor("El mencho")
     tecnico1 = Tecnico("Justin biber")

     print("********************* === POLIMORFISMO CON GETTER Y SETTER === *********************".center(50))

     ejecutar_tarea(gerente1)
     ejecutar_tarea(desarrollador1)
     ejecutar_tarea(vendedor1)
     ejecutar_tarea(tecnico1)
     
     print("\n********************* ==== POLIMORFISMO CON SETTER === *********************".center(50))

     desarrollador1.nombre = "Michael jackson"
     gerente1.nombre = "Pastrana"
     vendedor1.nombre = "El piratita"
     tecnico1.nombre = "Jaden Smith"

     print("\n************************ Nombres cambiados ************************".center(50))

     ejecutar_tarea(gerente1)
     ejecutar_tarea(desarrollador1)
     ejecutar_tarea(vendedor1)
     ejecutar_tarea(tecnico1)

if __name__ == "__main__":
     main()
