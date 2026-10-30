"""03 · Cadenas de texto (str)

Una cadena es una secuencia ordenada de caracteres.
Sus posiciones, llamadas índices, empiezan en 0. -1 indica el último.
Las cadenas son inmutables: sus caracteres no se cambian en el mismo objeto.
Los métodos que transforman texto devuelven una cadena nueva.
"""

lenguaje = "Python"
print(lenguaje[0])     # P
print(lenguaje[-1])    # n
print(lenguaje[0:3])   # Pyt: incluye el inicio y excluye el final.
print(lenguaje[:2])    # Py
print(lenguaje[2:])    # thon
print(len(lenguaje))   # 6: cantidad de caracteres

texto = "  Hola, Ana  "
limpio = texto.strip()  # Quita espacios de los extremos.
print(limpio.upper())
print(limpio.lower())
print(limpio.replace("Ana", "Luis"))
print("Ana" in limpio)  # True: comprueba si aparece ese texto.

nombre = "Ana"
precio = 19.5
print(f"Hola, {nombre}. El precio es ${precio:.2f}.")
# Una f-string inserta expresiones entre llaves; :.2f muestra dos decimales.

palabras = "pan leche fruta".split()  # Convierte el texto en una lista.
print(palabras)
print(", ".join(palabras))  # Une textos con un separador.
# Reto: limpia un nombre con espacios y úsalo en un saludo con f-string.
