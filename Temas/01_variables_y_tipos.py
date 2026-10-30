"""01 · Variables y tipos de datos

Una variable es un nombre que apunta a un valor. Se crea al asignarlo con =.
Python distingue mayúsculas: edad y Edad son nombres diferentes.
Usa nombres claros en snake_case, como precio_total.

Tipos básicos:
    int   → entero: 20
    float → número con decimales: 19.5
    str   → texto: "Hola"
    bool  → valor lógico: True o False
    None  → ausencia de un valor

El tipo pertenece al valor; una variable puede apuntar después a otro tipo.
Procura mantener un significado consistente para cada nombre.
"""

edad = 25
precio = 49.90  # En Python, el separador decimal es el punto.
nombre = "Ana"
es_estudiante = True
resultado = None  # No es lo mismo que 0, False ni una cadena vacía.

print(nombre, edad, precio, es_estudiante, resultado)
print(type(edad))  # <class 'int'>

# Conversión explícita: cambia la representación de un valor.
edad_desde_texto = int("25")
precio_desde_texto = float("49.90")
edad_como_texto = str(edad)
print(edad_desde_texto + 1, precio_desde_texto, edad_como_texto)

# int("hola") falla: el texto debe representar un entero válido.
# Reto: crea variables para un producto, su precio y si está disponible.
