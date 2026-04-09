mascotas = ["toby", "gruñon", "bety", "chiquitin", "pocho", "garrapata"]

def mostrar_mascotas(mascotas):
    for mascotas in mascotas:
        print(f"- {mascotas}")

def agregar_mascotas(lista_mascotas, nombre):
    if isinstance(nombre, str) and 2<= len(nombre) <= 50:
        lista_mascotas.append(nombre.title())
        print(f" Mascota agregada: {nombre.title()}")
    else:
        print("Nombre de la mascota invalida debe tener entre 2 a 50 caracteres")

def modificar_mascotas(lista_mascotas, indice, nuevo_nombre):
    if not isinstance(nuevo_nombre, str) and 2<= len(nuevo_nombre) <= 50:
        print(" Nombre de la mascota invalido debe tener entre 2 a 50 caracteres")
        return
    if 0 <= indice <= len(lista_mascotas[indice]):
        original = lista_mascotas[indice]
        lista_mascotas[indice] = nuevo_nombre.title()
        print(f"Mascota {original} fue modificado por: {nuevo_nombre.title()}")
    else: 
        print("No existe ese cliente en la lista")

def eliminar_mascota(lista_mascotas, indice):
    if 0 <= indice <= len(lista_mascotas):
        eliminado = lista_mascotas.pop(indice)
        print(f"Mascota eliminada: {eliminado}")
    else: 
        print("Esa mascota no existe en nuestro sistema")  

def main():
    print("==================================== BIENVENIDO AL S.I. DE MASCOTAS ====================================".center(50))
    print("\n============Mascotas registradas: ============".center(50))
    mostrar_mascotas(mascotas)
    print("\n============Mascotas que se eliminaran del registro: ============")
    eliminar_mascota(mascotas, 4)
    eliminar_mascota(mascotas, 1)
    print("\n============Mascotas que quedaron: ============".center(50))
    mostrar_mascotas(mascotas)
    print("\n============Mascotas que se agregaran del registro: ============".center(50))
    agregar_mascotas(mascotas, "tony")
    agregar_mascotas(mascotas, "mechas")
    agregar_mascotas(mascotas, "rapunsel")
    print("\n============Lista final de las mascotas: ============".center(50))
    mostrar_mascotas(mascotas)
    print("==================================== FIN AL S.I. DE MASCOTAS ====================================".center(50))



if __name__ == "__main__":
    main()