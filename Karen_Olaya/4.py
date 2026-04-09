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
    def calcular(self):
        super().calcular()
        resultado = self.numero1 + self.numero2
        print(f"El resultado de la suma es: {resultado}")
        
def main():
    num1 = float(input{"ingrese el primer numero:"})
    num2 = float(input{"ingrese el segundo  numero:"})
    Operacion1 = Suma(32, 12)
    Operacion1.calcular()
    print("****Alerta de operación ya sin peligro, Terminada la operacion****")
if __name__ == "__main__":
    main()
        