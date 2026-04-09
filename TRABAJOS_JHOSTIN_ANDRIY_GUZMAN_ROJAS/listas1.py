""""
persona = ["Cristiano", 180, 20, "Ciudad bolivar"]
#ordenada: por orden de ingreso
print(persona[1])
for persona in persona:
    print(persona) 
    """

""""
import random
nombres = ["Cristiano","neymar","James","Westcol","Leandro","Diddy"]

nombre_secreto = random.choice(nombres)

print("=== ADIVINA EL CHATO ===".center(50))
print("Tienes 3 intentos")
intentos = 3
while intentos > 0:
    for nombre in nombres:
         print(nombre)
    intento = input("Ingrese el nombre del CHATO: ")
    if intento.lower() == nombre_secreto.lower():
        print("CHATO ganaste, Adivinaste el nombre...")
    else:
            intentos -= 1
            print("ERROR CRITICO, El nombre CHATO no es. Te quedan: ", intentos)

    if intentos == 0:
         print("Perdiste el nombre era:", nombre_secreto)
         """

# Ejercicio de gestion de clientes en una tienda
# Agragar nuevos clientes
# Recorrer la lista y mostrar todos los datos 
# Modificar un nombre en caso de error
# Eliminar un cliente 

# Funciones que utilizaremos 
# lent() -> cuenta las instancias dentro de la lista
# append() añade datos a la lista
# tittle() coloca el primer caracter en mayuscula ej: carlos -> Carlos 
# pop() Elimina un dato de la lista 


# Agregar nuevos clientes
"""
def agregar_cliente(lista_clientes, nombre):
    # verificamos si el dato ingresado sea una cadena y longitud valida entre 2 a 50 caracteres
    if isinstance(nombre, str) and 2 <= len(nombre) <= 50:
        # si el nombre cumple
        lista_clientes.append(nombre.title())
        print(f" Cliente agregado: {nombre.title()}")
    else: # El nombre ingresado no cumple la validacion entonces 
        print("Nombre del cliente invalido debe tener entre 2 a 50 caracteres ")

# Recorrer la lista y mostrar todos los datos 
def mostrar_clientes(lista_clientes):
    for cliente in lista_clientes:
        print(f"- {cliente}")


def modificar_clientes(lista_clientes, indice, nuevo_nombre):
    # verificamos si el dato ingresado sea una cadena y longitud valida entre 2 a 50 caracteres
    if not isinstance(nuevo_nombre, str) and 2 <= len(nuevo_nombre) <= 50:
        print(" Nombre del cliente invalido debe tener entre 2 a 50 caracteres")
        return
    if 0 <= indice <= len(lista_clientes):
        original = lista_clientes[indice]
        lista_clientes[indice] = nuevo_nombre.title()
        print(f"Cliente {original} fue modificado por: {nuevo_nombre.title()}")

    else: 
        print("No existe ese cliente en la lista")  

# Eliminar un cliente
# Vamos a eliminar un cliente de la lista por indice
def eliminar_cliente(lista_clientes, indice):
    if 0 <= indice <= len(lista_clientes):
        eliminado = lista_clientes.pop(indice) # elimina el cliente de acuerdo al numero de indice 
        # mostraremos el registro eliminado
        print(f"Cliente eliminado: {eliminado}")
    else:
        print("Ese cliente no existe en nuestro sistema") 


def main():

    clientes = ["Cristiano","neymar","James","Westcol","Leandro","Diddy"]
    print("Clientes activos")
    mostrar_clientes(clientes)
    agregar_cliente (clientes, "petro")
    print("Clientes activos mas el nuevo")
    mostrar_clientes(clientes)
    modificar_clientes(clientes, 4, "hitler")
    eliminar_cliente(clientes, 3)
    mostrar_clientes(clientes)
if __name__ == "__main__":
    main()
    """

# METODOS COMUNES QUE UTILIZAREMOS
# .append()
# .remove() / pop()
# sort() ordena la lista por el dato que yo le indique
# reverse() invertir los datos de la lista
# Ejercicio INVENTARIO DE UNA FERRETERIA

"""
1. AGREGAR NUEVOS PRODUCTOS
2. INSERTAR PRODUCTOS EN UNA POSICION ESPECIFICA
3. ELIMINAR PRODUCTOS AGOTADOS
4. ORDENAR PRODUCTOS POR NOMBRE Y PRECIO
5. INVERTIR ORDEN DE PRESENTACION DE LOS PRODUCTOS
requisitos del Sistema:
    -lista debe tener, nombre y precio
    -validacion de entradas
"""
def mostrar_inventario(productos):
    print("INVENTARIO ACTUAL")
    if not productos:
        print("No hay productos registrados")
        return
    for i, productos in enumerate(productos, start = 1):
        print(f"{i}. {productos["nombre"]} - $(producto ['Precio']:.2f)")

def main():
    inventario = [
        {"nombre": "Taladro", "Precio:": 15000"},
        {"nombre": "Martillo", "Precio:": 4000"},
        {"nombre": "Destornillador", "Precio:": 15000"}
    ]
    mostrar_inventario(inventario)

if __name__ == "__main__":
    main()