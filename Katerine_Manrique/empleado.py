from abc import ABC,abstractmethod
#CREAMOS LA CLASE ABSTRACTA
class Empleado(ABC):
    def __init__(self, nombre: str) -> None:
        self._nombre = None #Queda al atributo nombre como privado
        self._nombre = nombre #Aqui llamamos al SETTER automaticamente
     #creamos los GETTER
    @property   
    def nombre(self) -> str:
     #tendra acceso seguro al nombre del empleado
        return self._nombre
    @nombre.setter
    def nombre(self,valor:str)->None: #SETTER profesional con la validacion basica
     #validamos que sea cadena 
     if isinstance(valor,str) and valor.strip():
        self._nombre =valor.strip()

     else:
         raise ValueError("El nombre debe ser de tipo texto.")
    @abstractmethod
    def trabajar(self) ->None:
     #Este metoso es obligatorio en todas las clases por tener @abstractmethod
        pass
#creamos las clases hijas
class Gerente(Empleado):
    def trabajar(self) -> None:
        print(f"{self.nombre} esta administrando toda la empresa.")

class Desarrollador(Empleado):
     def trabajar(self)->None:
        print(f"{self.nombre} esta escribiendo pagina en PYTHON.")
#creamos un polimorfismo activos 
def ejecutar_tarea(empleado:Empleado):
    empleado.trabajar()

#EJECUCION DIDACTICA
def main():
     #creamos los objetos
     gerente1 = Gerente("Jesus")  
     desarrollador1 = Desarrollador("Cristian valero")   
     print("*********==POLIMORFISMO CON GETTER Y SETTER==**************")
     ejecutar_tarea(gerente1)
     ejecutar_tarea(desarrollador1)
     print("\n********==POLIMORFISMO CON SETTER==************")
     desarrollador1.nombre = "Ñaño rionez"
     gerente1.nombre = "Alberto plaza"
if __name__=="__main__":
   main()


        