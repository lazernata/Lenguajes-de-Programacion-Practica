# Ejercicio 2

line1 = 'Es mi primera línea.'
line2 = 'Es mi segunda línea.'
line3 = 'Es mi tercera línea.'
line4 = '¡Es el final del fichero!'

# 1. Crea un fichero vacío llamado primerfichero.txt sin usar with.
file1 = open("primerfichero.txt", "w")
file1.close()

# 2. Crea un segundo fichero vacío llamado segundofichero.txt usando with.
with open ('segundofichero.txt', 'w') as fichero:
    pass

# 3. Escribe line1 en primerfichero.txt
file1 = open("primerfichero.txt", "w", encoding="utf-8")
file1.write(line1)
file1.close()

# 4. Escribe line2, line3 y line4 en segundofichero.txt cada uno en una línea.
with open ('segundofichero.txt', 'w', encoding="utf-8") as fichero2:
    fichero2.write(line2 + '\n')
    fichero2.write(line3 + "\n")
    fichero2.write(line4 + "\n")

# 5. Lee primerfichero.txt y añade su contenido al final de segundofichero.txt.
with open("primerfichero.txt", "r", encoding="utf-8") as file1:
    content1 = file1.read()
with open("segundofichero.txt", "a", encoding="utf-8") as file2:
    file2.write(content1)