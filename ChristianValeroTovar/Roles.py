import random

nombres = ["Kelly", "Cristian", "Nelson", "Señora Paka", "ñaño", "Sebastian"]

nombre_secreto = random.choice(nombres)

print("Adivina el chato")
print("Tiene 3 intentos de vida...")
vidas = 3

while vidas > 0:
    intento = input("Ingrese el nombre del chato: ")
    if intento.lower() == nombre_secreto.lower():
        print("Chato ganaste, adivinaste el nombre")
        break
    else:
        vidas -= 1
        print("Error critico, el nombre del chato no es, intentos restantes ", vidas)

if vidas == 0:
    print("Pailas, perdiste, el nombre era: ", nombre_secreto," ahora consigna a mi nequi")