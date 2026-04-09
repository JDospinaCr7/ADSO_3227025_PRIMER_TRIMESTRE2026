from dataclasses import dataclass

@dataclass
class Libro:
    _titulo: str
    _autor: str
    _isbn: str
    _precio: float
    
    
    @property
    #Ahora crearemos los getter
    def titulo(self) -> str:
        return self.titulo
    
    @property
    def autor(self) -> str:
        return self.autor
    
    @property
    def isbn(self) -> str:
        return self.isbn
    
    @property
    def precio(self) -> str:
        return self.precio
    
    #Ahora crearemos lo setter
    
    @titulo.setter
    def titulo(self, nuevo_titulo: str) -> None:
        if isinstance(nuevo_titulo, str) and nuevo_titulo != nuevo_titulo.strip():
            self._titulo = nuevo_titulo
        else:
            raise ValueError("El titulo debe ser un texto valido y no vacio")
        
    @autor.setter
    def autor(self, nuevo_autor: str) -> None:
        if isinstance(nuevo_autor, str) and nuevo_autor != nuevo_autor.strip():
            self._autor = nuevo_autor
        else:
            raise ValueError("El autor debe ser un texto valido y no vacio")
        
    @isbn.setter
    def isbn(self, nuevo_isbn: str) -> None:
        if isinstance(nuevo_isbn, str) and nuevo_isbn != nuevo_isbn.strip():
            self._isbn = nuevo_isbn
        else:
            raise ValueError("El isbn debe ser un texto valido y no vacio")
        
    @precio.setter
    def precio(self, nuevo_precio: float, int) -> None:
        if isinstance(nuevo_precio, (float, int)) and nuevo_precio >= nuevo_precio.strip():
            self._precio = nuevo_precio
        else:
            raise ValueError("Ingrese un precio valido")
        
    def __repr__(self) ->str:
        return(
            f"Libro = {self._titulo} \n"
            f"Autor = {self._autor} \n"
            f"isbn = {self._isbn} \n"
            f"precio = {self._precio} \n"
        )
        
    #Programa principal
def main():
    print("====== Programa principal ======")
    Libro1 = Libro("Pedro Paramo", "Cristan Valero", "JK-322-3", 50000)
    print(f"****** Informacion del libro ******")
    print(Libro1)
    
    
if __name__ == "__main__":
        main()