class Animal:
    def sonido(self):
        print("El animal esta haciendo ruido")

class Perro(Animal):
    def sonido(self):
        print("El perro dice Guau Guau")

    pass

class Gato(Animal):
    def sonido(self):
        print("El gato dice Miau Miau")
    pass

class Tigre(Animal):
    def sonido(self):
        print("El tigre hace GRRRRRR")
    pass

class Leon(Animal):
    def sonido(self):
        print("El leon hace Guuuuuu")

class Delfin(Animal):
    def sonido(self):
        print("El delfin hace UiUiUiUiUiUi")

#Sonidos de animales
def main():

    perro1 = Perro()
    perro1.sonido()

    gato1 = Gato()
    gato1.sonido()

    tigre1 = Tigre()
    tigre1.sonido()

    leon1 = Leon()
    leon1.sonido()

    delfin1 = Delfin()
    delfin1.sonido()


if __name__ == "__main__":
    main()