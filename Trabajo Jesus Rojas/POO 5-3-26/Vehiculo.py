class Vehiculo: #Esta clave va a ser mi clase padre
    def mover(self): #Este metodo es el que vamos a heredar a los hijos
        print("El vehiculo se esta moviendo")

class Carro(Vehiculo):
    def mover(self):
        print("El carro rueda por la carretera")
    pass

class Moto(Vehiculo):
    def mover(self):
        print("La moto va a mil por la autopista")
    pass

class Avion(Vehiculo):
    def mover(self):
        print("El avion vuela sobre las nubes")
    pass

class Submarino(Vehiculo):
    def mover(self):
        print("El submarino fue hundido")
    pass

def main():
    print("Ahora utilizaremos el metodo mover() pero desde el hijo")
    print("vamos a heredar este metodo desde carro")

    carro1 = Carro()
    carro1.mover()

    moto1 = Moto()
    moto1.mover()

    Avion1 = Avion()
    Avion1.mover()

    Submarino1 = Submarino()
    Submarino1.mover()

if __name__ == "__main__":
    main()