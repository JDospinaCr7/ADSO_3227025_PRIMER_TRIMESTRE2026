def agregar_mascota(lista_mascotas, nombre):
    # Verificamos el dato ingresado ssea una cadena y longitud valida entre 2 a 50 caracteres
    if isinstance(nombre, str) and 2 <= len(nombre) <= 50:
        # Si el nombre cumple
        lista_mascotas.append(nombre.title()) 
        print(f"Mascota agregada: {nombre.title()}")
    else: # El nombre ingresado no cumple la validacion entonces
        print("Nombre de tu mascota es invalido, debe tener entre 2 a 50 caracteres")
        
def mostrar_mascota(lista_mascotas):
    for mascota in lista_mascotas:
        print(f"- {mascota}")
        
def modificar_mascota(lista_mascotas, indice, nuevo_nombre):
    # Verificamos si el dato ingresado sea una cadena valida entre 2 a 50 caracteres
    if not isinstance(nuevo_nombre, str) and 2 <= len(nuevo_nombre) <= 50:
        print("Nombre de tu mascota es invalido, debe tener entre 2 a 50 caracteres")
        return
    if 0 <= indice <=len(lista_mascotas):
        original = lista_mascotas[indice]
        lista_mascotas[indice] = nuevo_nombre.title()
        print(F"La mascota {original} fue  modificado por: {nuevo_nombre.title()}")
    else:
        print("No existe esa mascota en la lista")

# Eliminar una mascota
# Vamos a eliminar una mascota
def eliminar_mascota(lista_mascotas, indice):
    if 0 <= indice <=len(lista_mascotas):
        eliminado = lista_mascotas.pop(indice) # Elminar la mascota de acuerdo al numero indice
        # Mostramos el registro eliminado
        print(f"Mascota eliminada: {eliminado}")
    else:
        print("Esa mascota no existe en nuestro sistema.")
        
def main():
    mascotas = ["Toby", "Gruñon", "Beky", "Chiquitin", "Pancho", "Garrapata"]  
    print("Mascotas activos")
    mostrar_mascota(mascotas)
    agregar_mascota(mascotas, "Tony") 
    agregar_mascota(mascotas, "Mechas")
    agregar_mascota(mascotas, "Rapunsel")  
    print("Mascotas activas, más el nuevo")
    mostrar_mascota(mascotas)
    modificar_mascota(mascotas,4,"Lulu")
    mostrar_mascota(mascotas)
    eliminar_mascota(mascotas, 5)
    mostrar_mascota(mascotas)

    
    
if __name__ == "__main__":
    main()





