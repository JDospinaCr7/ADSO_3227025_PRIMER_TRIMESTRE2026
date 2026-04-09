class Libro:
    def __init__(self, titulo, precio):
        self.__titulo = titulo
        self.__precio = precio
        
#Vamos a crear los getter, pertmite acceder al valor de forma segura.
    def get_titulo(self):
        return self. __titulo
    def get_precio(self):
        return self. __precio
    
#Vamos a controlar, validar los valores antes de ser modificados
    def set_titulo(self, nuevo_titulo):
        if isinstance(nuevo_titulo, str) and nuevo_titulo != "":
            self.__titulo = nuevo_titulo
        else:
            print("Error en el titulo ingresado, debe ser un texto valido")
            
    def set_precio(self, nuevo_precio):
        if isinstance(nuevo_precio, (int, float)) and nuevo_precio >=0:
            self.__precio = nuevo_precio
        else:
            print("Error en el precio ingresado, debe ser un numero valido")

    def mostrar_info(self):
        print(f"Titulo del libro: {self.__titulo}")
        print(f"precio: {self.__precio}")
    
def main():
    print("S.I. De libros del complejo sur")
    Libro1 = Libro("Pedro Paramo", 70000) #Creamos el objeto libro
    print("====== Informacion del libro ======")
    Libro1.mostrar_info()
    
#Mostrar el precio actual
    print("\nPrecio actual del libro: $ ", Libro1.get_precio())
    Libro1.set_precio(100000) #Nuevo precio
    #mostrar el precio nuevo
    print("\nPrecio Nuevo del libro: $", Libro1.get_precio())
    print("********* Fin del programa *********")
    
    
if __name__ == "__main__":
    main()
    