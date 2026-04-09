
class Usuario:

    def _init_(self, nombre, email, telefono, clave, rol):
        self.__nombre = nombre
        self.__email = email
        self.__telefono = telefono
        self.__clave = clave
        self.__rol = rol

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, nuevo_email):
        if "@" in nuevo_email:
            self.__email = nuevo_email
        else:
            print("Email inválido")

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, nuevo_telefono):
        if nuevo_telefono.isdigit():
            self.__telefono = nuevo_telefono
        else:
            print("Teléfono inválido")

    @property
    def clave(self):
        return self.__clave

    @clave.setter
    def clave(self, nueva_clave):
        if len(nueva_clave) >= 4:
            self.__clave = nueva_clave
        else:
            print("La clave debe tener al menos 4 caracteres")

    def mostrar_info(self):
        print("Nombre:", self.__nombre)
        print("Email:", self.__email)
        print("Telefono:", self.__telefono)
        print("Rol:", self.__rol)



class Catalogo:

    def _init_(self, nombre_producto, descripcion, precio, cantidad, categoria):
        self.__nombre_producto = nombre_producto
        self.__descripcion = descripcion
        self.__precio = precio
        self.__cantidad = cantidad
        self.__categoria = categoria

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("Precio inválido")

    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, nueva_descripcion):
        if nueva_descripcion.strip() != "":
            self.__descripcion = nueva_descripcion
        else:
            print("Descripción inválida")

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, nueva_cantidad):
        if nueva_cantidad >= 0:
            self.__cantidad = nueva_cantidad
        else:
            print("Cantidad inválida")

    def mostrar_producto(self):
        print("Producto:", self.__nombre_producto)
        print("Descripción:", self.__descripcion)
        print("Precio:", self.__precio)
        print("Cantidad:", self.__cantidad)
        print("Categoria:", self.__categoria)



def main():

    usuario1 = Usuario("Camila", "cami15@gmail.com", "3004567890", "12345", "cliente")

    producto1 = Catalogo(
        "Libro Python",
        "Libro de programación",
        80000,
        5,
        "Educación"
    )

    print("===== USUARIO =====")
    usuario1.mostrar_info()

    print("\n===== PRODUCTO =====")
    producto1.mostrar_producto()

    
    usuario1.email = "nuevo@gmail.com"
    producto1.precio = 90000
    producto1.cantidad = 8

    print("\n===== DATOS ACTUALIZADOS =====")
    usuario1.mostrar_info()
    producto1.mostrar_producto()


if __name__ == "_main_":
    main()
