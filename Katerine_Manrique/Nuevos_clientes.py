#Ejercicio de gestion de clientes en una tienda
# Agregar nuevos clientes
# Recorrer la lista y mostrar todos los datos 
# Modificar un nombre en caso de error
# Eliminar un cliente

#Funciones que utilizamos
# len() -> Cuenta las instancias dentro de la lista 
# append() Añade datos a la lista   
# title() Coloca el primer caracter en mayusculas ej, carlos -carlos
# pop() Elimina un dato de una lista



#Agregar nuevos clientes
def agregar_cliente(lista_clientes,nombre):
    #verificamos si el dato ingresado sea una cadena y la longitud valida entre 2 a 50 caracteres
    if isinstance(nombre,str) and 2  <= len(nombre) <= 50:
        #si el nombre cumple
        lista_clientes.append(nombre.title())
        print(f"Cliente agregado: {nombre.title()}")
    else: #El nombre ingresado no cumple la validacion entonces
        print("Nombre del cliente invalido debe tener entre 2 a 50 caracteres")
def mostrar_Clientes(Lista_Clientes):
    for  Cliente in Lista_Clientes:
         print:(f"- {Cliente}")
def modificar_Cliente(lista_clientes,indice,nuevo_nombre):      
    #verificamos si el dato ingresado sea una cadena y longitud valida entre 2 a 50 caracteres
    if not isinstance(nuevo_nombre,str)and 2 <= len(nuevo_nombre) <= 50:
        print("Nombre del cliente invalido debe tener entre 2 a 50 caracteres")
        return
    if 0 <= indice <=len(lista_clientes):
        original = lista_clientes[indice]
        lista_clientes[indice] = nuevo_nombre.title()
        print(f"El cliente {original} fue modificado por : {nuevo_nombre.title()}")
    else:
        print("No existe ese cliente en la lista")

#Eliminar cliente 
#vamos a eliminar un cliente de la lista por indice
def eliminar_cliente(lista_clientes,indice):
    if 0 <= indice <=len(lista_clientes):
        eliminado = lista_clientes.pop(indice)#Elimina el cliente de acuerdo al numero de indice
        #mostramos el registro eliminado
        print(f"cliente eliminado: {eliminado}")
    else:
        print("Ese cliente no existe en nuestro sistema")


def main():
    Clientes =["kelly","Cristian","Nelson","Sra Paka","ÑaÑo","Sebastian"]
    print("Clientes activos")
    mostrar_Clientes(Clientes,"alejandro")
    agregar_cliente(Clientes,"alejandro")
    print("clientes activos mas el nuevo")
    mostrar_Clientes(Clientes)
    modificar_Cliente(Clientes,4,"Gabriela")
    mostrar_Clientes(Clientes)
    eliminar_cliente(Clientes,3)
    mostrar_Clientes(Clientes)
if __name__ =="__main__":
    main()                 


