def mostrar_menu():
    print("\n## Bienvenido al Sistema de Inventario")
    print("\n1. Agregar productos al inventario")
    print("2. Eliminar producto del inventario")
    print("3. Mostrar inventario")
    print("4. Consultar producto")
    print("5. Salir")

def mostrar_inventario(inventario):
    if not inventario:
        print("Por favor, introduce un producto")
    for product in inventario:
        print(f"Nombre del producto: {product['nombre']} | "
              f"Precio: {product['precio']} | "
              f"Cantidad: {product['cantidad']}")

def eliminar_inventario(inventario, nombre):
    for product in inventario:
        if product["nombre"] == nombre:
            inventario.remove(product)
            print(f"Producto {'nombre'} eliminado")
            return

if __name__ == "__main__":
    inventario = []

    while True:
        mostrar_menu()
        opcion = input("Elige una opcion: ")

        if opcion == "1":
            nombre = input("Introduce el nombre del producto: ")
            precio = float(input("Introduce el precio del producto: "))
            cantidad = int(input("Introduce la cantidad de la producto: "))

            producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
            inventario.append(producto)

            mostrar_inventario(inventario)

        elif opcion == "2":
            nombre_producto = input("Introduce el nombre del producto: ")
            eliminar_inventario(inventario, nombre_producto)

        elif opcion == "3":
            mostrar_inventario(inventario)
        # elif opcion == "4":
        #     #todo
        elif opcion == "5":
            print("Finalizando la ejecución del programa...")
            break
        else:
            print("Opción no válida")