class Libro:
    def __init__(self, titulo, precio):
        self.__titulo = titulo
        self.__precio = precio
        
        #vamos a crear los getters, permite acceder al valor de el atributo de forma segura
    def get_titulo(self):
        return self.__titulo
    def get_precio(self):
        return self.__precio
       
        #vamos a controlar, valoidar los valores antes de ser modificados
    def set_titulo(self, nuevo_titulo):
        if isinstance(nuevo_titulo, str) and nuevo_titulo != "":
            self.__titulo = nuevo_titulo
        else: 
            print("Error en el titulo ingresado, debe de ser un titulo valido")
    def set_precio(self, nuevo_precio):
        if isinstance(nuevo_precio,(int, float)) and nuevo_precio >=0:
            self.__precio = nuevo_precio 
        else:
            print("Error en el precio ingresado, debe de ser un nùmero valido")
            
def main():
    if __name__ == "__main__":
        main()