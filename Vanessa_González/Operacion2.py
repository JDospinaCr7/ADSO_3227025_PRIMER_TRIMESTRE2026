from logging import setLogRecordFactory
class Operacion():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def validar(self):
        if not isinstance(self.a,(int, float)) or not isinstance(self.b,(int, float)):
            raise ValueError("Los valores deben de ser numericos")
    def mostrar_datos(self):
        print(f"Valores recibidos: {self.a} y {self.b}")
    def calcular(self):
        print("Realizando operación matematica...")
        
class Suma(Operacion):
    def calcular(self):
        super().validar() # Realiza la verificacion de los valores desde el padre
        super().mostrar_datos() # Realiza el metodo para mostrar los datos desde pabre
        super().calcular() 
        resultado = self.a + self.b
        print(f"Resultado de la suma es: {resultado}")
        
class Resta(Operacion):
    def calcular(self):
        super().validar() 
        super().mostrar_datos() 
        super().calcular() 
        resultado = self.a - self.b
        print(f"Resultado de la resta es: {resultado}")
        
class Multiplicacion(Operacion):
    def calcular(self):
        super().validar() 
        super().mostrar_datos() 
        super().calcular() 
        resultado = self.a * self.b
        print(f"Resultado de la multiplicacion es: {resultado}")
        
class
        
def main():
    num1= float(input("Ingrese un número: "))
    num2= float(input("Ingrese un número: "))
    
    operacion_suma = Suma(num1, num2)
    operacion_suma.calcular()

    operacion_resta = Resta(num1, num2)
    operacion_resta.calcular()
    
    operacion_multiplicacion = Multiplicacion(num1, num2)
    operacion_multiplicacion.calcular()

if __name__ == "__main__":
    main()