# Ejercicio 3:
# En este ejercicio, deberás implementar una clase Dni en Python que represente un
# Documento Nacional de Identidad (DNI) español. La clase debe validar el número del DNI y
# calcular su letra correspondiente:
# 1. Define la Clase Dni:
# 1.1. Implementa el metodo constructor __init__ para inicializar el número de DNI.
# 1.2. Implementa un metodo privado __calcular_letra para calcular la letra del DNI.
# 1.3. Utiliza propiedades para manejar el acceso y la validación del número de DNI.
# 2. Validación del número de DNI:
# 2.1. El número de DNI debe tener exactamente 8 dígitos y ser completamente numérico.
# 2.2. Si el número de DNI no es válido, asigna el valor '00000000' y una letra especial, por
# ejemplo, '#'.
# 3. Cálculo de la letra del DNI:  La letra del DNI se calcula utilizando el resto de la división del número entre 23.  Usa la cadena 'TRWAGMYFPDXBNJZSQVHLCKE' para obtener la letra
# correspondiente.

class DNI:
    def __init__(self, numero):
        self.numero = numero

    def  __calcular_letra(self):
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        return letras[int(self.numero) % 23]

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        if len(numero) == 8 and numero.isdigit():
            self._numero = numero
            self._letra = self.__calcular_letra()
        else:
            self._numero = "incorrecto"
            self._letra = "#"

    def __str__(self):
        return f"DNI: {self.numero}-{self._letra}"


if __name__ == "__main__":
    dni_valido = DNI("12345678")
    print(dni_valido)  # Salida esperada: DNI: 12345678-Z

    dni_invalido = DNI("1234ABC8")
    print(dni_invalido)  # Salida esperada: DNI: 00000000-#