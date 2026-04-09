class Operacion:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def validar(self):
        if not isinstance(self.a, (int, float)) or not isinstance(self.b, (int, float)):
            raise ValueError("Los valores deben ser numéricos")

    def mostrar_datos(self):
        print(f"Valores recibidos: {self.a} y {self.b}")

    def calcular(self):
        print("Realizando operación matemática...")


class Resta(Operacion):
    def calcular(self):
        super().validar()
        super().mostrar_datos()
        super().calcular()

        resultado = self.a - self.b
        print("Resultado de la resta:", resultado)


def main():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    operacion = Resta(num1, num2)
    operacion.calcular()


if __name__ == "__main__":
    main()