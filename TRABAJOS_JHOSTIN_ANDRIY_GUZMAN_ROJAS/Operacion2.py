class Operacion:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def validar(self):
        if not isinstance(self.a, (int, float)) or not isinstance(self.b, (int, float)):
            raise ValueError("Los valores deben ser numericos")
    def mostrar_datos(self):
        print(f"valores recibidos: {self.a} y {self.b}")
    def calcular(self):
        print("Realizando operacion matematica....\n")

class Suma(Operacion):

    def calcular(self):
        super().validar() # Realiza la verificacion de los valores desde el padre 
        super().mostrar_datos() # Realiza el metodo para mostrar los datos desde padre
        super().calcular() 
        resultado = self.a + self.b
        print(f"Resultado de la suma es: {resultado}\n")

class Resta(Operacion):
    
    def calcular(self):
        super().validar()
        super().mostrar_datos()
        super().calcular()
        resultado = self.a - self.b
        print(f"Resultado de la resta es: {resultado}\n")

class Multiplicacion(Operacion):
    
    def calcular(self):
        super().validar()
        super().mostrar_datos()
        super().calcular()
        resultado = self.a * self.b
        print(f"Resultado de la multiplicacion es: {resultado}\n")

class Divison(Operacion):
    
    def calcular(self):
        super().validar()
        super().mostrar_datos()
        super().calcular()
        

        if self.b == 0:
            print("No se puede dividir por cero.\n")
        else: resultado = self.a / self.b
        print(f"Resultado de la division es: {resultado}\n")

class Potencia(Operacion):
    
    def calcular(self):
        super().validar()
        super().mostrar_datos()
        super().calcular()
        resultado = self.a ** self.b
        print(f"Resultado de la potencia es: {resultado}\n")

def main():
    
    a = float(input("Ingrese el primer numero: \n"))

    b = float(input("Ingrese el segundo numero: \n"))

    while b == 0:
        print("El segundo numero no se puede ser 0 para la division\n")
        b = float(input("Ingrese nuevamente el segundo numero: \n"))

    operacion1 = Suma(a,b)
    operacion1.calcular()

    operacion1 = Resta(a,b)
    operacion1.calcular()

    operacion1 = Multiplicacion(a,b)
    operacion1.calcular()

    operacion1 = Divison(a,b)
    operacion1.calcular()

    operacion1 = Potencia(a,b)
    operacion1.calcular()

if __name__ == "__main__":
    main()