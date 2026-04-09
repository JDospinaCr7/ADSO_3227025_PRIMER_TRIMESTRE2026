class libro:

  def __init__(self,titulo,precio):
      self .__titulo = titulo
      self .__precio = precio

  def getter_titulo(self):
      return self.__titulo
  
  def getter_precio(self):
      return self.__precio
  def set_titulo(self,nuevo_titulo):
      if isinstance(nuevo_titulo,str) and nuevo_titulo.strip() !="":
         self.__titulo = nuevo_titulo
      else:
        print("Titulo invalido")

  def set_precio(self, nuevo_precio):   
      if isinstance(nuevo_precio, (int,float)) and nuevo_precio > 0:
         self.__precio = nuevo_precio
      else:
        print("Precio invalido")

  def mostrar_info(self):
       print("Titulo:",self.__titulo)
       print("precio:",self.__precio)

def main():

   libro1 =libro("Camila Torres", 80000)
   print("Titulo actual:",libro1.get_titulo())

   libro1.set_precio(90000)
   print("Nuevo precio:",libro1.get_precio())

if __name__=="__main__":   
    main()



