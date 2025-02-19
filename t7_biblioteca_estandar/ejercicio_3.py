# Ejercicio 3:
# En este ejercicio, utilizarás los módulos os y re de Python para buscar un patrón de
# expresiones regulares (regex) en todos los archivos TXT de un directorio específico. El
# objetivo es encontrar todas las palabras que terminan en un signo de exclamación (!) y
# mostrarlas en la consola.
# 1. Usa os.listdir para obtener todos los archivos en el directorio actual.
# 2. Filtra los archivos para obtener solo los archivos con extensión .txt.
# 3. Define una expresión regular que coincida con todas las palabras que terminan en !.
# 4. Abre cada archivo TXT y lee su contenido.
# 5. Busca coincidencias del patrón regex en el contenido del archivo.
# 6. Imprime las coincidencias encontradas en la consola

import re
import os

# Listar todos los archivos en el directorio actual y filtrar aquellos que sean archivos TXT
files = os.listdir(os.getcwd())
txt_files = [file for file in files if file.endswith(".txt")]

# Definir un patrón regex para buscar palabras que terminan en '!'
search_regex = re.compile(
    r"¡?\s?\w*\!"
)  # Coincide con todas las palabras que terminan en '!'

# Abrir cada archivo TXT y buscar el patrón regex
for doc in txt_files:
    with open(doc, "r", encoding="utf-8") as opened_file:
        contents = opened_file.read()
        found = search_regex.findall(contents)
        if found:
            found_str = " ".join(found)
            print(
                f"En el archivo '{doc}', se encontraron las siguientes coincidencias: {found_str}"
            )
        else:
            print(f"En el archivo '{doc}', no se encontraron coincidencias.")