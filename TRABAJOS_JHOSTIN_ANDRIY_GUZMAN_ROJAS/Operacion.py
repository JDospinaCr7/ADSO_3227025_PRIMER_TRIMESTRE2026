class Operacion():
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2 
        print("****** ALERTA; BEEP BEEP ---      INICIALIZACNDO LA OPERACION ******".center(50))
    def calcular(self):
        print("+++ REALIZANDO OPERACIONES GENERICAS +++")

class Suma(Operacion):
    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2)
        print("Preparando la operación SUMA.")

    def calcular(self):
        super().calcular() # reutilizo el metodo calcular pero del padre 
        resultado = self.numero1 + self.numero2
        print(f"El resultado de la suma es: {resultado}")
        print("=====================================================================")

class Resta(Operacion):
    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2)
        print("Preparando la operación RESTA.")

    def calcular(self):
        super().calcular()  
        resultado = self.numero1 - self.numero2
        print(f"El resultado de la resta es: {resultado}")
        print("=====================================================================")

class Multiplicacion(Operacion):
    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2)
        print("Preparando la operación MULTIPLICACION. ")
    def calcular(self):
        super().calcular()
        resultado = self.numero1 * self.numero2
        print(f"El resultado de la multiplicación es: {resultado}")
        print("=====================================================================")

class Division(Operacion):
    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2)
        print("Preparando la operación DIVISION. ")
    def calcular(self):
        super().calcular()
        resultado = self.numero1 / self.numero2

        if self.numero2 == 0:
            print("No se puede dividir por cero. ")
        else: resultado = self.numero1 / self.numero2
        print(f"El resultado de la división es: {resultado}")
        print("=====================================================================")

class Potencia(Operacion):
    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2)
        print("Preparando la operación POTENCIA. ")
    def calcular(self):
        super().calcular()
        resultado = self.numero1 ** self.numero2 
        print(f"El resultado de la potencia es: {resultado}")

def main():

    numero1 = float(input("Ingrese el primer numero: "))

    numero2 = float(input("Ingrese el segundo numero: "))

    while numero2 == 0:
        print("El segundo numero no puede ser 0 para la division")
        numero2 = float(input("Ingrese nuevamente el segundo numero: "))

    Operacion1= Suma(numero1, numero2)
    Operacion1.calcular()

    Operacion1= Resta(numero1, numero2)
    Operacion1.calcular()

    Operacion1= Multiplicacion(numero1, numero2)
    Operacion1.calcular()

    Operacion1= Division(numero1, numero2)
    Operacion1.calcular()

    Operacion1= Potencia(numero1, numero2)
    Operacion1.calcular()

    print("**** Alerta de operación ya sin peligro. Terminada la Alerta ****")
if __name__ == "__main__":
    main()