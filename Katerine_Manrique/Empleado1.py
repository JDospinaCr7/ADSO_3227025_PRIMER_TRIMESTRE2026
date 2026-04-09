class empleado:

    def __init__(self,nombre,salario):
        self.nombre = nombre
        self.salario = salario

class gerente(empleado):
    def __init__(self, nombre, salario, departamento):
      super().__init__(nombre, salario) #Heredo estos atributos del padre
      self.departamento = departamento 

def mostrar_info(self):     
        print(f"nombre: {self.nombre}")
        print(f"salario: {self.salario}")  
        print(f"Departamento: {self.departamento}")

def  main():
         gerente1 = gerente("Cristian Valero",5000,"Alta tecnologia de desarrollo IA")
         gerente1.mostrar_info()


if __name__ == "__main__":
    main()    


