# Ejercicio 3 – CSV:
# En este ejercicio, aprenderás a leer archivos CSV utilizando el módulo csv en Python.
# Explorarás dos métodos: usando csv.reader y csv.DictReader.

import csv

# 1. Lee el archivo “estudiantes.csv” con csv.reader
# 2. Extrae y muestra la cabecera.
# 3. Convierte cada fila en un diccionario usando la cabecera como claves y muestra el
# contenido.
with open('estudiantes.csv', newline="", encoding="utf-8") as fichero_csv:
    csv_reader = csv.reader(fichero_csv)
    cabecera = next(csv_reader)
    print("Cabecera:", cabecera)
    for fila in csv_reader:
        estudiante_dict = dict(zip(cabecera, fila))
        print(estudiante_dict)

# 4. Abre el mismo archivo CSV y utiliza csv.DictReader para leer el archivo.
# 5. Muestra la información de cada fila en un formato legible.

with open("estudiantes.csv", newline="", encoding="utf-8") as file:
    dict_reader = csv.DictReader(file)
    for estudiante in dict_reader:
        print(
            f'{estudiante["Nombre"]} estudia {estudiante["Carrera"]}, tiene {estudiante["Edad"]} años'
        )
