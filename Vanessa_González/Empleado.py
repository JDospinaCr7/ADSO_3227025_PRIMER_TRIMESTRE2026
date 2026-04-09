class Empleado():
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
        
class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Salario: {self.salario}")
        print(f"Departamento: {self.departamento}")
            
def main():
    gerente1 = Gerente("Chis", 5000, "Alta tacnologia de desarrollo")
    gerente1.mostrar_info()
    
if __name__ == "__main__":
    main()