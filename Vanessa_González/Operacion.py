class Operacion():
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
        print("****ALERTA, BEEP BEEP --- INICIANDO LA OPERACIÓN****")
    def calcular(self):
        print("++++ REALIZANDO OPERACIONES GENERICAS ++++")
class Suma(Operacion):
    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2)
        print(f"Preparando la operacion suma")
class Resta(Operacion):
    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2)
        print(f"Preparando la operacion resta")
class Multiplicacion(Operacion):
    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2)
        print(f"Preparando la operacion multiplicacion")
    def calcular(self):
        super().calcular()
        resultado = self.numero1 + self.numero2
        print(f"El resultado de la suma es: {resultado}")
        
def main():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    
    Operacion1 = Suma(num1,num2)
    Operacion1.calcular()
    print("****Alerta de operación ya sin peligro, Terminada la operacion****")
if __name__ == "__main__":
    main()
        
        