from dataclasses import dataclass
@dataclass
class Libro: 
    _titulo : str
    _autor : str
    _isbn : str
    _precio : float
    
    #ahora creamos los getter
    @property
    def titulo(self) -> str:
        return self._titulo
    @property
    def autor(self) -> str:
        return self._autor
    @property
    def isbn(self) -> str:
        return self._isbn
    @property
    def precio(self) -> float:
        return self._precio
    
    #ahora creamos los setters
    
    @titulo.setter
    def titulo(self, nuevo_titulo: str) -> None:
        if isinstance(nuevo_titulo, str) and nuevo_titulo != "" and nuevo_titulo.strip():
            self._titulo = nuevo_titulo
        else:
            raise ValueError("El titulo debe ser un texto valido y no vacio\n ")
    @autor.setter
    def autor(self, nuevo_autor: str) -> None:
        if isinstance(nuevo_autor, str) and nuevo_autor != "" and nuevo_autor.strip():
            self._autor = nuevo_autor
        else:
            raise ValueError("El autor debe de ser un texto valido y no vacio\n ")
    @isbn.setter
    def isbn(self, nuevo_isbn: str) -> None:
        if isinstance(nuevo_isbn, str) and nuevo_isbn != "" and nuevo_isbn.strip():
            self._autor = nuevo_isbn
        else:
            raise ValueError("El isbn debe de ser un texto valido y no vacio\n ")
    @precio.setter
    def precio(self, nuevo_precio: float) -> None:
        if isinstance(nuevo_precio, (int, float)) and nuevo_precio >= 0:
            self._precio = float(nuevo_precio)
        else:
            raise ValueError("El precio debe de ser un nùmero positivo\n ")
        
    def __repr__(self) -> str :
        return(
            f"Libro(titulo = '{self._titulo})'"
            f"Autor = '{self._autor}',"
            f"isbn = '{self._isbn})',"
            f"precio = {self._precio})")
        
  #programa principal - demostracion
def main():
    print("==== Programa Principal ====")
    libro1 = Libro("Pedro Paramo", "Pedrito Paramito", "JK-322-3", 50000)
    print("==== Informaciòn del Libro ====")
    print(libro1)
    libro1.precio= 115000
    libro1.titulo= "Aventuras"
    libro1.autor= "Pedrito Sanches"
    
    print("\n*** Datos actualizados ***")
    print(libro1)
if __name__ == "__main__":
        main()       