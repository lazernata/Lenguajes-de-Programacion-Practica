# Ejercicio 2:
# 1. Cree una clase `Vehicle` que reciba el nombre, velocidad máxima y el kilometraje.
# 2. Cree una clase `Bus` que herede todos los métodos y variables de `Vehicle`.
# 3. Cree un metodo a `Vehicle` que, recibiendo la capacidad, imprima por pantalla
# `“La capacidad de (nombre) es de (capacidad).`
# 4. Cree el mismo metodo para `Bus` en el que por defecto la capacidad sea de 50.
# 5. Defina la variable `owner` que tenga el valor `“NWorld”` para todos los objetos de la clase.

class Vehicle:
    owner = 'NWorld'

    def __init__(self, nombre, velocidad, km):
        self.nombre = nombre
        self.velocidad = velocidad
        self.km = km

    def mostrar_capacidad(self, capacidad):
        """
        Imprime la capacidad del vehículo.

        Args:
            capacidad (int): La capacidad del vehículo.
        """

        print(f'La capacidad de {self.nombre} es de {capacidad}')


class Bus(Vehicle):
    def mostrar_capacidad(self, capacidad = 50):
        """
        Imprime la capacidad del vehículo.

        Args:
            capacidad (int): La capacidad del vehículo.
        """
        print(f'La capacidad de {self.nombre} es de {capacidad}')

# Crear una instancia de la clase Vehicle
vehiculo = Vehicle("Coche", 180, 15000)
vehiculo.mostrar_capacidad(5)  # Salida esperada: La capacidad de Coche es de 5.

# Crear una instancia de la clase Bus
bus = Bus("Autobús Escolar", 120, 30000)
bus.mostrar_capacidad()  # Salida esperada: La capacidad de Autobús Escolar es de 50.
bus.mostrar_capacidad(75)  # Salida esperada: La capacidad de Autobús Escolar es de 75.

# Verificar la variable owner
print(Vehicle.owner)  # Salida esperada: NWorld
print(Bus.owner)  # Salida esperada: NWorld
print(vehiculo.owner)  # Salida esperada: NWorld
print(bus.owner)  # Salida esperada: NWorld
