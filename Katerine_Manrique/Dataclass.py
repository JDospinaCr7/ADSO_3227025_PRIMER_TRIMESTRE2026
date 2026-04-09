from dataclasses import dataclass

@dataclass
class Usuario:
    nombre: str
    email: str
    telefono: str
    clave: str
    rol: str


@dataclass
class Catalogo:
    nombre_producto: str
    descripcion: str
    precio: float
    cantidad: int
    categoria: str



def main():

    usuario1 = Usuario(
        "Camila Torres",
        "Cami15@gmail.com",
        "3004567890",
        "12345",
        "cliente"
    )

    producto1 = Catalogo(
        "Libro Python",
        "Libro para aprender Python",
        80000,
        20,
        "Programación"
    )

    print("===== USUARIO =====")
    print(usuario1)

    print("\n===== PRODUCTO CATALOGO =====")
    print(producto1)


if __name__== "_main_":
    main()