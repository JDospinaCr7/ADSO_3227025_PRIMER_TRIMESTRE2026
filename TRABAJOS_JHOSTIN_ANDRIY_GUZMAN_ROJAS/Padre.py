class Padre():
    def __init__(self, mensaje):
        self.mensaje = mensaje 

class Hijo (Padre):
    def __init__(self, mensaje, nombre):
       super().__init__(mensaje)      # Reutilizamos el contructor del padre  
       self.nombre = nombre

def main():
    
    objeto1 = Hijo("Este mensjae desde la clase padre", "Este mensaje desde clase hijo ")
    print(f"{objeto1}, {objeto1.nombre}")
    print(objeto1.mensaje)
    print(objeto1.nombre)
if __name__ == "__main__":
    main()