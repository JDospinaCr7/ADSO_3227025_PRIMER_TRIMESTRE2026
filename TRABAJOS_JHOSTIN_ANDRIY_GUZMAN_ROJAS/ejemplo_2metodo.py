from dataclasses import dataclass

@dataclass
class Libro:
    _titulo: str
    _autor: str
    _isbn: str
    _precio: float

# Ahora creamos los GETTER
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
    
    
# ahora creamos los SETTER
    @titulo.setter
    def titulo(self, nuevo_titulo: str) -> None:
        if isinstance(nuevo_titulo, str) and nuevo_titulo.strip():
            self._titulo = nuevo_titulo
        else: 
            raise ValueError("El titulo debe ser un texto valido y no vacio \n")
        
    @autor.setter
    def autor(self, nuevo_autor: str) -> None:
        if isinstance(nuevo_autor, str) and nuevo_autor.strip():
            self._autor = nuevo_autor
        else: 
            raise ValueError("El autor debe ser un texto valido y no vacio \n")
        
    @isbn.setter
    def isbn(self, nuevo_isbn: str) -> None:
        if isinstance(nuevo_isbn, str)  and nuevo_isbn.strip():
            self._isbn = nuevo_isbn
        else: 
            raise ValueError("El isbn debe ser un texto valido y no vacio \n")
        
    @precio.setter
    def precio(self, nuevo_precio: float) -> None:
        if isinstance(nuevo_precio, (int, float)) and nuevo_precio >= 0:
            self._precio = float(nuevo_precio)
        else: 
            raise ValueError("El precio debe ser un número valido\n")
        
    def __repr__(self) -> str: 
        return(
            f"Titulo: {self._titulo}\n" 
            f"Autor: {self._autor}\n"
            f"Isbn: {self._isbn}\n"
            f"Precio: {self._precio}" 
        )
    
# PROGRAMA PRINCIPAL - DEMOSTRACIÓN 
def main():

    print("====== PRGRAMA PRINCIPAL DE LIBRO ======".center(50))

    libro1 = Libro ("Pedro Paramo", "Cristian Valero", "JK-3223", 50000)

    print("====== INFORMACIÓN DEL LIBRO======".center(50))
    print(libro1)
    libro1.precio = 115000
    libro1.titulo = "Luisiño y sus travesuras"
    libro1.autor = "Andres Riaño"

    print("\n====== Datos Actualizados ======".center(50))
    print(libro1)
    



if __name__ == "__main__":
    main()

