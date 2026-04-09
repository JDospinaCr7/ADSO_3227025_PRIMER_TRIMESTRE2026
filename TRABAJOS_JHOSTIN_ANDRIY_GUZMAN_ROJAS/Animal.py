class Animal:
    def hacer_sonido(self):
        print("****** El animal hace un sonido ******\n")

class Perro(Animal):
    def hacer_sonido(self):
        print("****** El Perro Ladra ******\n")

class Gato(Animal):
    def hacer_sonido(self):
        print("****** El Gato Maulla ******\n")

class Tigre(Animal):
    def hacer_sonido(self):
        print("****** El Tigre Falcao ******\n")

class Leon(Animal):
    def hacer_sonido(self):
        print("****** El Leon Ruge ******\n")

class Delfin(Animal):
    def hacer_sonido(self): 
        print("****** El Delfin Silba ******\n")

def main():
    animal1 = Animal()
    animal1.hacer_sonido() 
    print("Ahora utilizaremos en metodo hacer_sonido() pero desde el hijo\n")

    perro1 = Perro()
    perro1.hacer_sonido()

    gato1 = Gato()
    gato1.hacer_sonido()

    tigre1 = Tigre()
    tigre1.hacer_sonido()

    leon1 = Leon()
    leon1.hacer_sonido()

    delfin1 = Delfin()
    delfin1.hacer_sonido()

if __name__ == "__main__":
    main()