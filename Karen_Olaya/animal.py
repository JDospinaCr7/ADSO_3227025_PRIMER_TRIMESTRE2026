class Animal:
    def Sonindo(Self):
        print("El animal hace ruido")
class Perro(Animal):
    def Sonindo(Self):
        print("El perro ladra")
class Gato(Animal):
    def Sonindo(Self):
        print("El gato maulla")
class Tigre(Animal):
    def Sonindo(Self):
        print("El tigre resuple")
class Leon(Animal):
    def Sonindo(Self):
        print("El leon ruge")
class Delfin(Animal):
    def Sonindo(Self):
        print("El delfin silva")
def main():
    print ("Los animales")
    perro1 = Perro()
    perro1.Sonindo()
    gato1 = Gato()
    gato1.Sonindo()
    tigre1 = Tigre()
    tigre1.Sonindo()
    leon1 = Leon()
    leon1.Sonindo()
    delfin1 = Delfin()
    delfin1.Sonindo()

if __name__ == "__main__":
    main()