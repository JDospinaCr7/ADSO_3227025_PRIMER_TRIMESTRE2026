# Metodos comunes que utilizaremos 
# .append()
# .insert()
# .remove() / pop() - este ultimo elimina el ultimo campo de la lista
# sort() ordena la lista por el dato que ya le indique
# reverse() invertir los datos de la lista

# EJERCICIO INVENTARIO DE UNA FERRETERIA

"""
1. INGRESAR NUEVOS PRODUCTOS
2. INSERTAR PRODUCTOS
3. ELIMINAR PRODUCTOS AGOTADOS
4. ORDENA PRODUCTOS POR NOMBRE Y PRECIO
5. INVERTIR ORDEN DE PRESENTACION DE LOS PRODUCTOS

Requisistos del sistema
    -lista debe de tener nombre y Precio
    -validacion de entradas
"""
def mostrar_inventario(productos):
    print("INVENTARIO ACTUAL")
    if not productos:
        print("No hay productos registrados")
        return 
    for i, producto in enumerate(productos, start=1):
        print(f"{i}. {producto['nombre']} - ${producto['precio']:.2f}")
    

def main():
    inventario = [
        {"nombre": "Taladro", "precio":150000}
        {"nombre": "Martillo","precio":4000}
        {"nombre": "Destornillador","precio":15000}
    ]
    mostrar_inventario(inventario)
    if __name__ == "__main__":
        main()