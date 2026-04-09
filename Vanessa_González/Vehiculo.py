class Vehiculo: # Esta es la clase padre
    def mover(self): 
        print("****El vehiculo se esta moviendo****\n")
        
class Carro(Vehiculo): #clase hijo
   def mover(self): 
        print("****El carro rueda por la carretera****\n")
        
        
class Moto(Vehiculo):
    def mover(self): 
        print("****La moto va a mil por la autopista****\n")
        
class Avion(Vehiculo):
    def mover(self): 
        print("****El avion vuuela por las nubes****\n")
        
class Submarino(Vehiculo):
    def mover(self): 
        print("****El submariono busca el rio de Bogotá****\n")
        
def main():
    print("Ahora utilizaremos en metodo mover() pero desde el hijo\n")
    print("Vamos a heredar este metodo desde carro\n")
    carro1= Carro()
    carro1.mover()
    moto1= Moto()
    print("Metodo mover reutilizando desde moto hijo\n")
    moto1.mover()
    avion1= Avion()
    avion1.mover()
    submarino1= Submarino()
    submarino1.mover()
if __name__ =="__main__":
    main()


