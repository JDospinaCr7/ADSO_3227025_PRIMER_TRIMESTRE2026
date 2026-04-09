class vehiculo: #Esta clase va a ser clase padre
   def mover(self): #Este metodo es el que vamos a heredar alos hijos
      print("El vehiculo se esta moviendo")

class carro(vehiculo):
    def mover(self):
        print("*****El carro rueda por la carretera*****\n")

class moto(vehiculo):  
    def mover(self):
        print("****la moto va a mil****\n")   

class avion(vehiculo):
     def mover(self):
         print("****El avion vuela sobre las nubes***\n")

class submarino(vehiculo):
    def mover(self):
        print("*******El submarino el bolivia****\n")

def main():
 print("Ahora utilizamos el metodo mover()pero desde el hijo")
 print("Vamos a heredar este metodo desde carro")
carro1 = carro()
carro1.mover()#Utilizamos el metodo mover pero este esta en el vehiculo
moto1 = moto()
print("metodo mover reutilizamos desde moto hijo")
moto1 = moto()

if __name__ =="__main__":   
     main()


