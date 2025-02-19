# Ejercicio 4 – JSON:

import json

# 1. Carga los datos de los productos existentes desde el archivo “productos.json”.

with open('productos.json', 'r', encoding="utf-8") as file:
    datos = json.load(file)

print(datos)

# 2. Implementa la función agregar_producto que agregue un producto al inventario.
inventory = []
def agregar_producto(nombre: str, cantidad: int, precio: float, inventario: list):
    producto = {'nombre': nombre,
                'cantidad': cantidad,
                'precio': precio,}
    inventario.append(producto)
    return inventario

agregar_producto(nombre='lalla', cantidad=1, precio=5.0, inventario=inventory)

# 3. Implementa la función escribir_fichero. Esta función toma el inventario como argumento
# y lo escribe en un archivo JSON llamado ‘inventario.json’. Formatéalo con una
# indentación de 4 espacios para que sea más legible.

# noinspection PyTypeChecker
def escribir_fichero(inventario: list):
    with open('inventario.json', 'w', encoding="utf-8") as file1:
        # noinspection PyTypeChecker
        json.dump(inventario, file1, indent=4)
    return 'Archivo JSON creado con exito.'

escribir_fichero(inventory)