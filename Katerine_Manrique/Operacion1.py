class Operacion:
    def __init__(self,numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
        print("****** ALERTA,BEEP BEEP ----- INICIALIZANDO LA OPERACION *******")
    def calcular(self):
        print("+++++ REALIZANDO OPERACIONES GENERICAS ++++++")
        
class Suma(Operacion):
    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2)        
        print("Preparando la operacion suma")
    def calcular(self):
        super().calcular()#Realizo el metodo calcular pero del padre
        resultado = self.numero1 + self.numero2
        print(f"El resultado de la suma es: {resultado}")


def main():
    num1 = float (input("Ingrese el primer numero"))
    num2 = float (input("Ingrese el segundo numero"))
    operacion1 = Suma(num1, num2)
    operacion1.calcular()
    print("***** Alerta de operacion ya sin peligro. termina la alerta*****")

if __name__ == "__main__":
    main()
        

