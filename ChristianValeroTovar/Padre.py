class Padre():
    def __init__(self, mensaje):
        self.mensaje = mensaje

class Hijo(Padre):
    def __init__(self, mensaje, nombre):
        super().__init__(mensaje)
        self.nombre = nombre


def main():
    objeto1 = Hijo("Este mensaje desde la clase padre", "Este mensaje desde la clase hijo")
    print(f"{objeto1.mensaje}, {objeto1.nombre}")
    print(f"{objeto1.mensaje}")
    print(f"{objeto1.nombre}")

if __name__ == "__main__":
    main()