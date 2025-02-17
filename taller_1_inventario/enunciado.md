# Simulador de Inventario de una Tienda

## Descripción General
Crearás un programa que simule la gestión de inventario de una pequeña tienda. Este programa permitirá al usuario agregar productos al inventario, eliminarlos cuando sea necesario y consultar el inventario actual.

---

## Objetivos de Aprendizaje:
- Uso de funciones para organizar el código de manera modular.
- Implementación de estructuras de control de flujo para manejar la lógica del programa.
- Manejo de listas y diccionarios para almacenar los datos del inventario.

---

## Funcionalidades a Implementar:

### 1. Función para Consultar un Producto
Crea una función que permita al usuario consultar un producto por su nombre y muestre su cantidad y precio.

### 2. Función para Agregar Productos al Inventario
Deberás crear una función que permita al usuario introducir un nuevo producto al inventario. Cada producto estará representado como un diccionario con las claves `nombre`, `cantidad` y `precio`. El inventario será una lista de estos diccionarios.

### 3. Función para Eliminar Productos del Inventario
Implementa una función que permita al usuario eliminar un producto del inventario por su nombre.

### 4. Función para Mostrar el Inventario Actual
Desarrolla una función que imprima todos los productos en el inventario, incluyendo su nombre, cantidad y precio.

---

## Interfaz de Usuario en la Consola
Usa un bucle `while` con una estructura de control de flujo (`if`, `elif`, `else`) para permitir al usuario elegir entre agregar, eliminar, consultar un producto o mostrar todo el inventario. El programa se ejecutará hasta que el usuario decida salir.

---

## Antes de Comenzar
- **Librerías**: Para este ejercicio, no es necesario instalar librerías adicionales. Utilizarás las que ya vienen incluidas con Python.
- **Script Principal**: El punto de entrada para este ejercicio es un script llamado `inventario.py`.

---

## Ampliación: Persistencia de Datos

### Archivo de Persistencia
Debes crear un archivo llamado `inventario.json` donde se guardarán los datos de los productos.

### Carga Inicial del Inventario
Al iniciar el programa, este debe intentar leer el archivo `inventario.json` si existe, para cargar los datos de productos previamente almacenados.

### Actualización del Archivo
Cada vez que se añade o elimina un producto, el archivo `inventario.json` debe actualizarse para reflejar los cambios.

---

