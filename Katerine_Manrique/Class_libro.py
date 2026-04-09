class Libro:

    # Constructor
    def _init_(self, titulo, precio):
        self.__titulo = titulo
        self.__precio = precio

    # Getter para obtener el título
    def get_titulo(self):
        return self.__titulo

    # Getter para obtener el precio
    def get_precio(self):
        return self.__precio

    # Setter para modificar el título
    def set_titulo(self, nuevo_titulo):
        if isinstance(nuevo_titulo, str) and nuevo_titulo != "":
            self.__titulo = nuevo_titulo
        else:
            print("Error: el título debe ser un texto válido")

    # Setter para modificar el precio
    def set_precio(self, nuevo_precio):
        if isinstance(nuevo_precio, (int, float)) and nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("Error: el precio debe ser un número mayor a 0")

    # Método para mostrar información
    def mostrar_info(self):
        print("Título del libro:", self.__titulo)
        print("Precio: $", self.__precio)


# Programa principal
def main():

    print("===== S.I. de los libros de Complejo Sur =====")

    # Crear objeto
    libro1 = Libro("Pedro Paramo", 70000)

    print("\n===== Información del libro =====")
    libro1.mostrar_info()

    # Mostrar precio actual
    print("\nPrecio actual del libro: $", libro1.get_precio())

    # Cambiar precio
    libro1.set_precio(100000)

    # Mostrar nuevo precio
    print("Precio nuevo del libro: $", libro1.get_precio())

    print("\n+++++ FIN DEL PROGRAMA +++++")


# Ejecutar programa
if __name__ == "_main_":
    main()