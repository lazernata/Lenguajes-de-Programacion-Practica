# Ejercicio 2
# Implementa un programa que solicite al usuario que ingrese un número entero. Debes
# asegurar que el usuario ingresa un valor válido. Si el usuario ingresa un valor no numérico,
# se mostrará un mensaje de error y se le pedirá que lo intente nuevamente

while True:
    try:
        num = int(input("Introduce un numero: "))
        break
    except ValueError:
        print('Introduce un número entero!')