num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

class operacion():
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
        print("Alerta Beep Beep Iniciando la operacion")

    def calcular(self):
        print("Realizando operacion genericas")

class Suma(operacion):

    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2)
        print("Preparando la operacion suma")

    def calcular(self):
        super().calcular()
        resultado = self.numero1 + self.numero2
        print(f"El resultado de la suma es: {resultado}")

def main():
    Operacion1 = Suma(num1,num2)
    Operacion1.calcular()
    print(f"Alera de operacion ya sin peligro. Terminando la alerta")

if __name__ == "__main__":
    main()