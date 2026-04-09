class Catalogo:
    def __init__(self, precio, descripcion, cantidad, categoria, estado, Id_Producto):
        self.__precio = precio 
        self.__descripcion = descripcion
        self.__cantidad = cantidad
        self.__categoria = categoria
        self.__estado = estado
        self.__Id_Producto = Id_Producto

    def get_precio(self):
        return self.__precio
    
    def get_descripcion(self):
        return self.__descripcion
    
    def get_cantidad(self):
        return self.__cantidad
    
    def get_categoria(self):
        return self.__categoria
    
    def get_estado(self):
        return self.__estado
    
    def get_Id_Producto(self):
        return self.__Id_Producto
    

    def set_precio(self, nuevo_precio):
        if isinstance(nuevo_precio, (int, float)) and nuevo_precio >0:
            self.__precio = nuevo_precio
        else: print("Error en el precio ingresado, debe ser un precio valido. ")

    def set_descripcion(self, nueva_descripcion):
        if isinstance(nueva_descripcion, str) and nueva_descripcion != "":
            self.__descripcion = nueva_descripcion
        else: print("Error en la descricion ingresado, debe ser un texto valido.")

    def set_cantidad(self, nueva_cantidad):
        if isinstance(nueva_cantidad, (int, float)) and nueva_cantidad >0 :
            self.__cantidad = nueva_cantidad
        else: print("Error en la cantidad ingresada, debe ser una cantidad valido.")
    
    def set_categoria(self, nueva_categoria):
        if isinstance(nueva_categoria, str) and nueva_categoria != "":
            self.__categoria = nueva_categoria
        else: print("Error en la categoria ingresada, debe ser un texto valido.")
    
    def set_estado(self, nuevo_estado):
        if isinstance(nuevo_estado, str) and nuevo_estado != "":
            self.__estado = nuevo_estado
        else: print("Error en el estado ingresado, debe ser un texto valido.")
    
    def set_Id_Producto(self, nuevo_Id_Producto):
        if isinstance(nuevo_Id_Producto, str) and nuevo_Id_Producto != "":
            self.__Id_Producto = nuevo_Id_Producto
        else: print("Error en el titulo ingresado, debe ser un texto valido.")

    
    def mostrar_info(self):
        print(f"El precio del producto es: ${self.__precio}")
        print(f"La descripción del producto es: {self.__descripcion}")
        print(f"La cantidad del producto es: {self.__cantidad}")
        print(f"La categoria del producto es: {self.__categoria}")
        print(f"El estado del producto es: {self.__estado}")
        print(f"El Id del producto es: {self.__Id_Producto}")


def main():

    print("======EMPRESA NOTCH=======".center(50))
    catalogo1 = Catalogo(15000, "Encantamiento de Reparación", 2, "Encantamientos", "Casi agotado", "EN-25")
    catalogo2 = Catalogo(10000, "Espada de Hierro", 5, "Armamento", "En producción", "AR-10")
    catalogo3 = Catalogo(20000, "Poción de Fuerza", 10, "Pociones", "Lleno en almacen", "AL-1")

    print("======Información del catalogo======".center(50))
    catalogo1.mostrar_info()
    print("==================================================")
    catalogo2.mostrar_info()
    print("==================================================")
    catalogo3.mostrar_info()
    print("==================================================")



    print("==================================================")

    print("\n Actualización del estado del tercer producto".center(50))
    nuevo_estado = input("Ingrese el nuevo estado: ")
    catalogo3.set_estado(nuevo_estado)
    catalogo3.get_estado()

    print("\n Los datos actualizados del catalogo3 son: ".center(50))
    catalogo3.mostrar_info()

    print("==================================================")

if __name__ == "__main__":
    main()
