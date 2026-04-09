from dataclasses import dataclass
@dataclass
class libro:
    _titulo: str
    _autor: str
    _isbn: str
    _precio: float
    #Ahora crearemos los GETTER
@property
def titulo(self) -> str:
    return self.__titulo

@property
def autor(self) -> str:
    return self.__Autor

@property
def isbn(self) ->str:
    return self.__isbn

@property
def precio(self) ->str:
    return self.__precio

#ahora creamos los SETTER
@titulo.setter
def titulo(self,Nuevo_titulo:str) -> None:
    if isinstance(Nuevo_titulo,str) and Nuevo_titulo !=""and Nuevo_titulo.strip():
        self.__titulo = Nuevo_titulo
    else:
        raise ValueError("El titulo debe ser un texto valido y no vacio\n")
@autor.setter
def autor(self,Nuevo_autor:str) -> None:
    if isinstance(Nuevo_autor,str) and Nuevo_autor !="".strip():
       self.__Autor = Nuevo_autor
    else:
        raise ValueError("El autor debe ser un texto valiso y no vacio\n")      

@isbn.setter
def isbn(self,Nuevo_isbn:str) -> None:
    if isinstance(Nuevo_isbn,str) and Nuevo_isbn !=""and Nuevo_isbn.strip():
        self.__isbn = Nuevo_isbn
    else:
        raise ValueError("El isbn debe ser un texto valido y no vacio\n")
    
@precio.setter
def precio(self,Nuevo_precio: float) -> None:
    if isinstance(Nuevo_precio,float,int) and Nuevo_precio !=""and Nuevo_precio.strip():
        self.__precio = Nuevo_precio
    else:
        raise ValueError("El precio debe ser un texto valido y no vacio\n")
    
def _repr_(self) -> str: 
    return(
      f"Libro(titulo='(self._titulo))',"
      f"Autor ='(self._autor)',"
      f"isbn(isbn ='(self._isbn))'," 
      f"precio = '(self.precio)',"

    )


  #programa principal - demostracion
def main():
      print("===========POGRAMA PRINCIPAL DEL LIBRO===========".center (50))
      libro1 = libro ("pedro paramo","Cristian valero","JK - 322 - 3 " , 50000)
      print(F"=====INFORMACION DEL LIBRO=====")
      print(libro1)
      libro1.titulo = "luisiño y sus travesuras"
      libro1._autor ="Andres Riaño"

      print("n\** DATOS ACTUALIZADOS**")
      print(libro1)

if __name__ =="_main_":
     main()