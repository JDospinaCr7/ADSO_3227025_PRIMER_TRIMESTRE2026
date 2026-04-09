from dataclasses import dataclass

@dataclass

class Usuario:

    def __init__(self, nombre_completo, rol, telefono, email, clave):
        self._nombre_completo = nombre_completo
        self._rol = rol
        self._telefono = telefono
        self._email = email
        self._clave = clave

    @property
    def clave(self) -> str:
        return self._clave
    
    @property
    def email(self) -> str:
        return self._email
    
    @property
    def telefono(self) -> float:
        return self._telefono
    
    @property
    def rol(self) -> str:
        return self._rol
    
    @property
    def nombre_completo(self) -> str:
        return self._nombre_completo
    

    @clave.setter
    def clave(self, nueva_clave: str) -> None:
        if isinstance(nueva_clave, str) and nueva_clave.strip():
            self._clave = nueva_clave
        else: raise ValueError("La clave debe ser un texto valido y no vacio \n")

    @email.setter
    def email(self, nuevo_email: str) -> None:
        if isinstance(nuevo_email, str) and nuevo_email.strip():
            self._email = nuevo_email
        else: raise ValueError("El correo debe ser un correo valido y no vacio \n")

    @telefono.setter
    def telefono(self, nuevo_telefono: float) -> None:
        if isinstance(nuevo_telefono, (int, float)) and nuevo_telefono >=0 :
            self._telefono = nuevo_telefono
        else: raise ValueError("El telefono debe ser un número valido \n")

    @rol.setter
    def rol(self, nuevo_rol: str) -> None:
        if isinstance(nuevo_rol, str) and nuevo_rol.strip():
            self._rol = nuevo_rol
        else: raise ValueError("El rol debe ser un texto valido y no vacio \n")

    @nombre_completo.setter
    def nombre_completo(self, nuevo_nombre: str) -> None:
        if isinstance(nuevo_nombre, str) and nuevo_nombre.strip():
            self._nombre_completo = nuevo_nombre
        else: raise ValueError("El nombre debe ser un texto valido y no vacio \n")

    def __repr__(self) -> str:
        return(
            f"El nombre del usuario es: {self._nombre_completo}\n"
            f"El rol del usuario es: {self._rol}\n"
            f"El telefono del usuario es: {self._telefono}\n"
            f"El correo del usuario es: {self._email}\n"
            f"La clave del usuario es: {self._clave}\n"
        )
def main():

    print("======Programa para Información del usuario======".center(50))

    usuario1 = Usuario ("Admin", "floristeria68@gmail.com", 3245689710, "Admin", "Juan Gabriel Marquez")
    usuario2 = Usuario ("pepito", "perez@gmail.com", 3215789420, "Cliente", "Hernesto Perez ")
    usuario3 = Usuario ("lacoste_69", "asistenciatecnicaflores@gmail.com", 321456789, "Tecnico", "Cristiano Ronaldo Dos Santos Aveiro")

    print("======Información del primer usuario======")
    print(usuario1)

    print("======Información del segundo usuario======")
    print(usuario2)

    print("======Información del tercer usuario======")
    print(usuario3)


    usuario1.nombre_completo = "Mezzi gordon"
    usuario1.email = "siemprelapampara@gmail.com"
    usuario1.telefono = 3254879520

    print("\n====== Datos Actualizados ======".center(50))
    print(usuario1)

if __name__ == "__main__":
    main()

    