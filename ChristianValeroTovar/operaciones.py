class operacion:
    def __init__(self, a, b):
        self.a = b
        self.b = a

    def validar(self):

        if not isinstance(self.a, (int,float)) or not isinstance(self.b, (int, float)):
            raise ValueError("Los valores deben ser numericos")
        
    def mostrar_datos(self):
        print(f"Valores recibidos: {self.a} y {self.b}\n")

    def calcular(self):
        print("Realizando la operacion matematica")

class Suma(operacion):
    def __init__(self, a, b):
        super().__init__(a,b)
        super().validar() #realiza la verificacion de los valores desde el padre
        super().mostrar_datos()
        super().calcular()
        resultado = self.a + self.b
        print(f"Resultado de la suma es: {resultado}\n")

class Resta(operacion):
    def __init__(self, a, b):
        super().__init__(a,b)
        super().validar() #realiza la verificacion de los valores desde el padre
        resultado = self.a - self.b
        print(f"Resultado de la resta es: {resultado}\n")

class Multiplicacion(operacion):
    def __init__(self, a, b):
        super().__init__(a,b)
        super().validar() #realiza la verificacion de los valores desde el padre
        resultado = self.a * self.b
        print(f"Resultado de la multiplicacion es: {resultado}\n")

class Division(operacion):
    def __init__(self, a, b):
        super().__init__(a,b)
        super().validar() #realiza la verificacion de los valores desde el padre
        resultado = self.a / self.b
        if b == 0:
            print("No se puede dividir por 0\n")
            quit
        else:
            print(f"Resultado de la division es: {resultado}\n")


class Potencia(operacion):
    def __init__(self, a, b):
        super().__init__(a, b)
        super().validar() #realiza la verificacion de los valores desde el padre
        resultado = self.a ** self.b
        print(f"Resultado de la potencia es: {resultado}\n")

def main():
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))

    operacion1 = Suma(num1,num2)

    operacion1 = Resta(num1,num2)

    operacion1 = Multiplicacion(num1,num2)

    operacion1 = Division(num1,num2)

    operacion1 = Potencia(num1, num2)


if __name__ == "__main__":
    main()