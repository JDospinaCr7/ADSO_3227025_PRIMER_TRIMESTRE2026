class Vehiculo: # Esta clase des la padre
    def mover(self):
        print("*****El vehicuulo se esta miviendo****\n")
        
class Carro(Vehiculo): #clase hija 
    def mover(self):
        print("*****El carro  rueda por la carretera****\n")
        

class Moto(Vehiculo):
     def mover(self):
        print("*****La moto va a mil por la autopista****\n")
        
class Avion(Vehiculo):
     def mover(self):
        print("*****El avion vuela por las nubes****\n")
        
class Submarino(Vehiculo):
     def mover(self):
        print("*****El submarino bucea el rio Bogota****\n")
        
def main():
    print("Ahora utilizaremos en metodo mover()pero desde hijo")
    print("Vamos a heredar este metodo  carro")
    carro1= Carro() 
    carro1.mover()  # Utilizaremos el metodo mover pero este esta en vehiculo
    moto1= Moto()
    print("Metodo mover reutilizado desde moto hijo")
    moto1.mover()
    avion1= Avion()
    avion1.mover()
    submrino1= Submarino()
    submrino1.mover()
if __name__ =="__main__":
    main()









