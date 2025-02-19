# Ejercicio 1:
## 1. ¿Cuál es el propósito de la declaración `if __name__ == "__main__":`?

Esta declaración se usa para asegurarse de que un bloque de código 
solo se ejecute cuando el script se ejecuta directamente y no
cuando se importa como módulo en otro script.
## 2. ¿Para qué sirve la función `super()` en Python?

La función `super()` se usa para llamar métodos de una clase 
padre (superclase) dentro de una subclase. Es útil en la herencia, 
especialmente cuando se quiere extender o modificar el 
comportamiento de una clase base sin reescribir completamente 
su implementación.

## 3. Describe el uso del decorador `@staticmethod`

El decorador `@staticmethod` se usa para definir un método dentro 
de una clase que no necesita acceso a los atributos ni métodos 
de la instancia (self) o de la clase (cls). Se comporta como 
una función normal dentro del contexto de la clase.