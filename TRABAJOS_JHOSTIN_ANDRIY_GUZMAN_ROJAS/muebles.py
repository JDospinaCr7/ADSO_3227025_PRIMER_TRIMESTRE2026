class mueble: 
    def __init__(self, nombre, material, color, precio, origen):
        self.__nombre = nombre
        self.__material = material
        self.__color = color
        self.__precio = precio
        self.__origen = origen  

    def get_nombre(self):
        return self.__nombre
    def get_material(self):
        return self.__material
    def get_color(self):
        return self.__color
    def get_precio(self):
        return self.__precio
    def get_origen(self):
        return self.__origen
    
    def mostrar_info(self):
        print(f"\n El nombre del mueble es : {self.__nombre}, el material es: {self.__material}, el color es: {self.__color}, el precio es: ${self.__precio} y el origen del mueble es: {self.__origen}")

    def set_nombre (self, nuevo_nombre):
        if isinstance (nuevo_nombre, str) and len(nuevo_nombre) > 0:
            self.__nombre = nuevo_nombre

    def set_material (self, nuevo_material):
        if isinstance(nuevo_material, str) and len(nuevo_material) > 0:
            self.__material = nuevo_material

    def set_color (self, nuevo_color):
        if isinstance(nuevo_color, str) and len(nuevo_color) > 0:
            self.__color = nuevo_color

    def set_precio(self, nuevo_precio):
        if isinstance (nuevo_precio, (int, float)) and nuevo_precio > 0:
            self.__precio = nuevo_precio
        else: print("Recuerde que debe ingresar un número valido.")

    def set_origen (self,nuevo_origen):
        if isinstance (nuevo_origen, str) and len(nuevo_origen) > 0:
            self.__origen = nuevo_origen
        

def main():
    print("====Bienvenido a la muebleria, la madera en tus manos====")

    mueble1 = mueble("Silla", "Madera", "Negro mate", 50000, "China")
    mueble2 = mueble("Cama", "Madera de bambú", "Plateado", 150000, "Rusia")
    mueble3 = mueble("Closet", "Madera refinada", "Café", 180000, "Argentina")
    mueble4 = mueble("Sala comedor", "Madera pesada", "Repisada con leopardo", 1500000, "Colombia")
    mueble5 = mueble("Mesa de noche", "Madera", "Azul oscuro", 70000, "Estados unidos")

    print("\n Información del primer mueble")
    print(f"El nombre es: {mueble1.get_nombre()}")
    print(f"El material es: {mueble1.get_material()}")
    print(f"El color es: {mueble1.get_color()}")
    print(f"El precio es: ${mueble1.get_precio()}")
    print(f"El origen es: {mueble1.get_origen()}")

    mueble1.mostrar_info()

    print("\n Actualización del material del primer mueble")
    nuevo_material = input("Ingrese el nuevo material: ")
    mueble1.set_material(nuevo_material)
    print("El nuevo material actualizado del mueble1 es: ")
    mueble1.get_material()

    print("\n Los datos actualizados son del mueble1 son: ")
    mueble1.mostrar_info()

    print("\n Información del segundo mueble")

    mueble2.mostrar_info()

    print("\n Información del tercer mueble")

    mueble3.mostrar_info()

    print("\n Información del cuarto mueble")

    mueble4.mostrar_info()

    print("\n Información del quinto mueble")

    mueble5.mostrar_info()

if __name__ == "__main__":
    main()