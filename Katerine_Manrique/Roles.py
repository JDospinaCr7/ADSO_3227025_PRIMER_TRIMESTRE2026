roles_usuario = ["administrador","analista","gerente","auditor"]
#ordenada: por orden de ingreso
print(roles_usuario[3])
for rol in roles_usuario:
    print(rol)

""""""
import random
nombres = ["Kelly","Cristian","Nelson","Sr paka","ñaño","Sebastian"]

mombre_secreto = random.choice(nombres)

print(" ======= ADIVINA EL CHATO========")
print("Tiene tres intestos de vida...")
vidas = 3
while vidas > 0:
    intento = input("Ingrese el nombre del CHATO:")
    if intento.lower () == nombre_secreto.lower():
      print("CHATO ganaste,Adivinaste el nombre...")
      break
    else:
        vidas -=1
        print("ERROR CRITICO, El nombre del CHATO no es.Intentos restaurante:",vidas)
    if vidas == 0:
       print("PAILAS,PERDISTE EL NOMBRE ERA:", mombre_secreto,"ahora consigna a mi nequi...")
       """""" 

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



   












































































































