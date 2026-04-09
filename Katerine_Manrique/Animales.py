class Animal: 
   def mover(self):("***hacer_sonido**\n")
print("El animal hace un sonido")

class perro(Animal):
    def mover(self):
        print("*****El perro ladra*****\n")

class gato(Animal):  
    def mover(self):
        print("****El gato maulla****\n")   

class tigre(Animal):
     def mover(self):
         print("****El tigre corre 90 km/h***\n")

class leon(Animal):
    def mover(self):
        print("*******El leon asecha a su presa****\n")

class leon(Animal):
    def mover(self):
        print("*******El delfin silba en el acuario****\n")       


def main():
 print("Ahora utilizamos el metodo mover()pero desde el hijo")
 print("Vamos a heredar este metodo desde perro")
perro1 = perro()
perro1.mover()#Utilizamos el metodo mover pero este esta en el Animal
gato1 = gato()
print("metodo mover reutilizamos desde gato hijo")
gato1 = gato()
tigre1 = tigre()
tigre1.mover()
 
if __name__ =="__main__":   
     main()