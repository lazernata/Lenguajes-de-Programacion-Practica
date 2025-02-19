# Ejercicio 1:
## 1. Explica el propósito de la declaración with. 

La declaración `with` en Python se usa para manejar contextos 
de manera segura y garantizar la correcta liberación de recursos, 
como archivos o conexiones. Se usa principalmente para manejar 
archivos y asegurar que se cierren automáticamente, incluso si 
ocurre una excepción.

## 2. ¿Cómo puedes realizar operaciones de entrada/salida de archivos en modo binario?

Para leer y escribir archivos en modo binario, se usa la letra 
`'b'` en el modo de apertura `(rb, wb, ab)`

## 3. ¿Cómo serializas y deserializas objetos en Python?

La serialización convierte un objeto en una secuencia de bytes para almacenarlo o enviarlo.
La deserialización recupera el objeto original a partir de los bytes serializados.