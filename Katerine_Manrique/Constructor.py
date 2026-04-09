class libro:

 def __init__(self,titulo,precio):
    self.__titulo = titulo
    self.__precio = precio

 def mostrar_info(self):
    print("titulo:",self.__titulo)
    print("precio:",self.__precio) 

 def  main():
   
   libro1 = libro("Natalia Marquéz",80000)

   print("=====Informacion del libro=====")
   libro1.mostrar_info()

 if __name__=="__main__":
     main()