class Mueble:#crear la clase

    def _init_(self, nombre, material, color, precio, peso):
        self.__nombre = nombre
        self.__material = material
        self.__color = color
        self.__precio = precio
        self.__peso = peso

     #Metodo para mostrar toda la informacion

    def mostrar_info(self):
        print("\nINFORMACION DEL MUEBLE")
        print(f"nombre: {self.__nombre}")
        print(f"material: {self.__material}")
        print(f"color: {self.__color}")
        print(f"precio: {self.__precio}")
        print(f"peso: {self.__peso}")

    #SETTER modificar atributos con validacion

    def set_precio(self, nuevo_precio):
        if isinstance(nuevo_precio, (int, float)) and nuevo_precio > 0:
            print(f"precio actualizado de {self.__precio} a {nuevo_precio}")
            self.__precio = nuevo_precio
        else:
            print("error: Precio invalido")

    def set_material(self, nuevo_material):
        if isinstance(nuevo_material, str) and len(nuevo_material) > 0:
            print(f"material actualizado de {self.__material} a {nuevo_material}")
            self.__material = nuevo_material
        else:
            print("error: Material invalido")

    def set_color(self, nuevo_color):
        if isinstance(nuevo_color, str) and len(nuevo_color) > 0:
            print(f"color actualizado de {self.__color} a {nuevo_color}")
            self.__color = nuevo_color
        else:
            print("error: Color invalido")


def main():
    print("===== SISTEMA DE INFORMACION DE MUEBLES =====")

    #Crear 2 objetos

    mueble1 = Mueble("Silla", "Madera", "Cafe", 150000, 7)
    mueble2 = Mueble("Mesa", "Vidrio", "Negro", 300000, 20)
     
     #Mostrar informacion inicial
    print("\nINFORMACION INICIAL MUEBLE 1")
    mueble1.mostrar_info()

    print("\nINFORMACION INICIAL MUEBLE 2")
    mueble2.mostrar_info()

    #Modificar 3 atributos del mueble1
    print("\nMODIFICANDO ATRIBUTOS DEL MUEBLE 1")
    mueble1.set_precio(180000)
    mueble1.set_color("Blanco")
    mueble1.set_material("Metal")

     #Mostrar cambios

    print("\nDATOS ACTUALIZADOS MUEBLE 1")
    mueble1.mostrar_info()

     #Modificar 3 atributos del mueble2

    print("\nMODIFICANDO ATRIBUTOS DEL MUEBLE 2")
    mueble2.set_precio(350000)
    mueble2.set_color("Gris")
    mueble2.set_material("Madera")

    #Mostrar cambios

    print("\nDATOS ACTUALIZADOS MUEBLE 2")
    mueble2.mostrar_info()

if _name_ == "_main_":
    main()






        
             