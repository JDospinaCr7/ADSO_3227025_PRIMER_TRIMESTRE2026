"""roles_usuario = ["administrador", "analista", "gerente", "auditor"]
# Ordenada: por orden de imgreso
print(roles_usuario[3])
for rol in roles_usuario:
    print(rol)


import random
nombres = ["Kelly", "Chistian", "Nelson", "Sra Paka", "Ñaño", "Sebastian"]

nombre_secreto = random.choice(nombres)

print("==== ADIVINA EL CHATO ====")
print("Tiene 3 intentos de vida...")
vidas = 3
while vidas > 0:
    intento = input("Ingrese el nombre del CHATO: ")
    if intento.lower() == nombre_secreto.lower():
        print("CHATO ganastte, adivinaste el nombre...")
        break
    else:
        vidas  -= 1
        print("ERROR CRITICO, El nombredel CHATO no es. Intentos restantes: ", vidas)
if vidas == 0:
    print("Pailas, PERDISTE EL NOMBRE ERA: ", nombre_secreto,"ahora consigna a mi nequi...")
    """
    
    
# Ejercicio de gestion dde clientes en una tienda
# Agregar nuevos clientes
# Recorrer la lista y mostrar todos los datos
# Modificar un nombre en caso de error 
# Eliminar un cliente

# Funciones que utilizaremos 
# Len() -> Cuenta las instacias dentro de la lista
# Append Añade datos a la lista
# Title Coloca el primer caracter en mayuscula ej, carlos - Carlos
# pop() Elimina un dato de la lista 

# Agregar nuevos clientes
def agregar_cliente(lista_clientes, nombre):
    # Verificamos el dato ingresado ssea una cadena y longitud valida entre 2 a 50 caracteres
    if isinstance(nombre, str) and 2 <= len(nombre) <= 50:
        # Si el nombre cumple
        lista_clientes.append(nombre.title()) 
        print(f"Cliente agregado: {nombre.title()}")
    else: # El nombre ingresado no cumple la validacion entonces
        print("Nombre del cliente invalido debe tener entre 2 a 50 caracteres")
        
def mostrar_clientes(lista_clientes):
    for cliente in lista_clientes:
        print(f"- {cliente}")
        
def modificar_cliente(lista_clientes, indice, nuevo_nombre):
    # Verificamos si el dato ingresado sea una cadena valida entre 2 a 50 caracteres
    if not isinstance(nuevo_nombre, str) and 2 <= len(nuevo_nombre) <= 50:
        print("Nombre del cliente invalido debe tener entre 2 a 50 caracteres")
        return
    if 0 <= indice <=len(lista_clientes):
        original = lista_clientes[indice]
        lista_clientes[indice] = nuevo_nombre.title()
        print(F"El cliene {original} fue  modificado por: {nuevo_nombre.title()}")
    else:
        print("No existe ese clientee la lista")

# Eliminar un cliente
# Vamos a eliminar un cliente
def eliminar_cliente(lista_clientes, indice):
    if 0 <= indice <=len(lista_clientes):
        eliminado = lista_clientes.pop(indice) # Elmina el cliente de acuerdo al numero indice
        # Mostramos el registro eliminado
        print(f"Cliente eliminado: {eliminado}")
    else:
        print("Ese cliente no existe en nuestro sistema.")
        
def main():
    clientes = ["Kelly", "Chistian", "Nelson", "Sra Paka", "Ñaño", "Sebastian"]  
    print("clientes activos")
    mostrar_clientes(clientes)
    agregar_cliente(clientes, "alejandro") 
    print("clientes activos más el nuevo")
    mostrar_clientes(clientes)
    modificar_cliente(clientes,4,"Gabriela")
    mostrar_clientes(clientes)
    eliminar_cliente(clientes, 3)
    mostrar_clientes(clientes)

    
    
if __name__ == "__main__":
    main()





