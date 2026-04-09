class Libro:   #Clase
    def __init__(self, titulo, precio): #Constructor
     self.__titulo = titulo #Atributos, __ que es privado
     self.__precio = precio  
# construccion de metodos   
    # gestor, devuelve el valor de el atributo solicitado, get
    def get_titulo(self): # identifica que va a devolver un valor y solo lo muestra
       return self.__titulo
    def get_precio(self):
       return self.__precio 
    def mostrar_informacion(self):
       print(f"\nEl titulo es: {self.__titulo}, y el precio es : {self.__precio}\n")

    # vamos a crear un metodo para cambiar el precio

    # utilizamos el Setter, (set), para realizar el cambio de el valor contenido en el 
    # atributo
    def set_precio(self, nuevo_precio):
       if isinstance (nuevo_precio, (int, float)) and nuevo_precio > 0:
          self.__precio = nuevo_precio
       else: print("Recuerde debe ingresar un número valido")
    # en el siguiente metodo vamos a cambiar el valor del atributo titulo utilizando set
    def set_titulo(self, nuevo_titulo):
       if isinstance (nuevo_titulo, str) and len(nuevo_titulo) > 0: # debe ser string y tener al menos una letra
          self.__titulo = nuevo_titulo  # Actualiza el atributo con el nuevo valor 

def main():
        # aqui invoco los metodos
        print("=====ESTIMADO APRENDIZ BIENVENIDO AL PROGRAMA DE LIBRO====\n")
        
    # VAMOS A CREAR 2 OBJETOS LIBRO, UNO ES HTML, Y PRECIO $200000
    # EL SEGUNDO LIBRO SERA JAVASCRP, PRECIO $186000
        libro1 = Libro("HTMl", 200000)
        libro2 = Libro("JAVASCRIP", 186000)
        
    # AHORA VAMOS A MOSTRAR LOS VALORES INICIALES DEL LIBRO 1
        print("\nINFORMACION DEL PRIMER LIBRO METODO SEPARADOS ")
        print(f" El titulo es: {libro1.get_titulo()}")
        print(f" El precio es: {libro1.get_precio()}")

    # VAMOS A MOSTRAR LO ANTERIOR PERO CON TODO EL METODO MOSTRAR 
        print("\nINFORMACION DEL PRIMER LIBRO UN METODO ")
        libro1.mostrar_informacion()
        
    # ahora actualizaremoe el nombre del libro
        print("\n ACTUALIZACION DEL nombre DEL PRIMER LIBRO") 
        nuevo_titulo = input("Ingrese el nuevo titulo: ")
        libro1.set_titulo(nuevo_titulo)
        print("El nuevo nombre actualizado del libro1 es")
        libro1.get_titulo()

        print("\nLos datos actualizados son del libro1 son: ")
        libro1.mostrar_informacion()   
        
        
        
if __name__ == "__main__":
    main()  
       