# Ejercicio 1
## 2. ¿Cuál es la diferencia entre `os.path.join()` y `os.path.abspath`?

* `os.path.join()`:

Se usa para concatenar rutas de manera portátil en diferentes sistemas operativos.
Maneja automáticamente los separadores (`/` en Unix y `\` en Windows).

* `os.path.abspath()`:

Convierte una ruta relativa en una ruta absoluta.
Devuelve el camino completo desde la raíz del sistema de archivos.

## 2. ¿Cuál es el propósito del módulo `os`? Da ejemplos de su uso.

El módulo `os` proporciona interacción con el sistema operativo, permitiendo:

* Manejo de archivos y directorios
* Obtención de información del sistema
* Ejecución de comandos del sistema

📌 Ejemplos de uso:

✅ Obtener el directorio actual:

`import os
 print(os.getcwd())  # Muestra el directorio de trabajo actual`

✅ Listar archivos en un directorio:

`print(os.listdir("."))  # Lista archivos en el directorio actual`

✅ Crear y eliminar directorios:

`os.mkdir("nueva_carpeta")  # Crea una carpeta`
`os.rmdir("nueva_carpeta")  # Elimina la carpeta`

✅ Eliminar un archivo:

`os.remove("archivo.txt")  # Elimina un archivo`

✅ Ejecutar un comando del sistema:

`os.system("ls")  # En Linux/macOS`
`os.system("dir")  # En Windows`

## 3. ¿Cuál es el propósito del módulo `logging`? ¿Cómo se usa?

El módulo `logging` se usa para registrar eventos y mensajes en 
la ejecución del programa, útil para depuración y monitoreo.