# Ejercicio 4:
# Define la clase Empleado utilizando el decorador @dataclass:
# 1. La clase debe tener los atributos nombre, edad, ciudad y empresa. La variable empresa
# debe tener un valor por defecto.
# 2. Añade un metodo estático ‘calcular_salario’. Este metodo debe calcular el salario de un
# empleado basado en el salario base, el número de horas extras y el coste de la hora
# extra.
# 3. Añade un metodo de clase ‘obtener_nombre_empresa’:
# 4. Utiliza el metodo de clase para obtener y mostrar el nombre de la empresa.
# 5. Utiliza el metodo estático para calcular el salario de un empleado y muestra el resultado.
# 6. Crea una instancia de la clase Empleado y muestra su representación.

from dataclasses import dataclass

@dataclass
class Empleado:
    nombre: str
    edad: int
    ciudad: str
    empresa: str = 'NWorld'

    def __str__(self):
        return (f"El empleado {self.nombre} tiene {self.edad} es de {self.ciudad} y "
                f"trabaja en {self.empresa}")

    @classmethod
    def obtener_nombre_empresa(cls):
        return f'La empresa es {cls.empresa}'

    @staticmethod
    def calcular_salario(base: float, horas_extra: int, coste_horas_extra: float) -> float:
        return base + (horas_extra * coste_horas_extra)


if __name__ == "__main__":
    empleado = Empleado("Juan", 30, "Madrid")
    print(empleado)  # Representación del objeto

    print(Empleado.obtener_nombre_empresa())  # Obtener nombre de la empresa

    salario = Empleado.calcular_salario(1500, 10, 20)  # Cálculo del salario
    print(f"El salario calculado es: {salario}")