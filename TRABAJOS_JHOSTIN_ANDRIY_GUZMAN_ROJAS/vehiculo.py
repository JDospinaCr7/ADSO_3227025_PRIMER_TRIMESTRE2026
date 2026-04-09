class Vehiculo: #Esta clase va a ser mi clase padre
    def mover(self): # Este metodo es el que vamos a heredar a los hijos
        print("****** El Vehiculo se esta moviendo. ******\n")

class Carro(Vehiculo):
    def mover(self):
        print("****** El Carro rueda por la carretera. ******\n")

class Moto(Vehiculo):
    def mover(self):
        print("****** La moto va a mil por la autopista. ******\n")

class Avion(Vehiculo):
    def mover(self):
        print("****** El Avion vuela sobre las nubes. ******\n")
        
class Submarino(Vehiculo):
    def mover(self):
        print("****** El Submarino buvea el rio Bogotá. ******\n")

def main():
    vehiculo = Vehiculo()
    vehiculo.mover()
    print("Ahora utilizaremos en metodo mover() pero desde el hijo\n")

    print("Vamos a heredar este metodo desde carro\n")
    carro1 = Carro()
    carro1.mover() #Utilizaremos el metodo mover pero este esta en vehiculo

    moto1 = Moto()
    print(" Metodo mover reutilizado desde moto hijo\n")
    moto1.mover()

    avion1 = Avion()
    avion1.mover()

    submarino1 = Submarino()
    submarino1.mover()

if __name__ == "__main__":
    main()
