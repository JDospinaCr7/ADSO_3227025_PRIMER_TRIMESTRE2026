from abc import ABC, abstractmethod

# Creamos la clase abstracta
class Empleado:
      @abstractmethod
      def __init__(self, nombre: str) -> None:
          self._nombre = None # Queda el atributo nombre como privado
          self.nombre = nombre # Aqui llamamos al SETTEr automaticamente    
          
# Creamos los GETTERS
@property 
def nombre (self) -> str:
    # Tendra acceso seguro del nombre del empleado
    return self._nombre

@nombre.setter
# Setter profesional con validacion basica
def nombre (self, valor: str) -> None:
    if isinstance(valor, str) and valor.strip(): # Strip() quita espacios en blanco al principio y al final
        self._nombre = valor.strip()
    else:
        raise ValueError("El nombre debe de ser tipo texto")
def trabajar (self) -> None:
    # Este metodo es obligatorio en todas las clases hijas por tener @abstractmethod
    pass

# Arora creamos las clases hijas
class Gerente(Empleado):
    def trabajar(self) -> None:
        print(f"{self.nombre} Esta administrando toda la empresa.")
        
class Desarrollador(Empleado):
    def trabajar(self) -> None:
        print(f"{self.nombre} Esta escribiendo código en PHYTON.")
        
# Ahora creamos un polimorfismo activo
def ejecutar_tarea(empleado: Empleado):
    empleado.trabajar()
    
    
# Ejecucion didactica
def main():
    # Creamos los objetos
    gerente1 = Gerente("Sebastian H.")
    desarrollador1 = Desarrollador  ("Chiatian V.")
    print("****** === Polimorfismo con GETTERS === ******")
    
    ejecutar_tarea(gerente1)
    ejecutar_tarea(desarrollador1)
    
    print("****** === Polimorfismo con SETTERS === ******")
    desarrollador1.nombre = "Ñaño"
    gerente1.nombre = "Chis"
if __name__ == "__main__":
    main() 
    