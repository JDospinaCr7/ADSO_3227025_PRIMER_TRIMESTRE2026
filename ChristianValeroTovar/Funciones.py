def agregar_cliente(lista_clientes, nombre):
    #Verificamos si el dato ingresado es un cadena y longitud valida entre 2 a 50 caracteres
    if isinstance(nombre, str) and 2 <= len(nombre) <=50:
        #Si el nombre cumple
        lista_clientes.append(nombre.title())
        print(f"Cliente agregado: {nombre.title()}")
    else:
        print("Nombre del cliente invalido debe tener entre 2 y 50 caracteres")

def mostrar_clientes(lista_clientes):
    for cliente in lista_clientes:
        print(f"- {cliente}")

def modificar_cliente(lista_clientes, indice, nuevo_nombre):
    #verificamos si el dato ingresado es una cadena y longitud valida
    if not isinstance(nuevo_nombre, str) and 2 <= len(nuevo_nombre) <=50:
        print(f"Nombre del cliente invalido, debe tener entre 2 a 50 caracteres")
        return
    if 0 <= indice <=len(lista_clientes):
        original = lista_clientes[indice]
        lista_clientes[indice] = nuevo_nombre.title()
        print(f"El cliente {original} fue modificado por: {nuevo_nombre.title()}")
    else:
        print(f"No existe ese cliente en la lista")

#Eliminar un cliente

def eliminar_cliente(lista_clientes, indice):
    if 0 <= indice <= len(lista_clientes):
        eliminado = lista_clientes.pop(indice)
        print(f"Cliente eliminado: {eliminado}")
    else:
        print("Ese cliente no existe")

def main():
    clientes = ["Kelly", "Cristian", "Nelson", "SRA paka", "Ñaño", "Sebastian"]    
    print("Clientes activos")
    mostrar_clientes(clientes)
    agregar_cliente(clientes, "Alejandro")
    print(f"Clientes activos mas el nuevo")
    mostrar_clientes(clientes)
    modificar_cliente(clientes,4,"Gabriela")
    mostrar_clientes(clientes)
    eliminar_cliente(clientes, 3)
    mostrar_clientes(clientes)

if __name__ == "__main__":
    main()