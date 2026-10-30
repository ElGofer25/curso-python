"""07 · Diccionarios (dict) y conjuntos (set)

dict relaciona claves únicas con valores: busca por clave, no por posición.
set guarda elementos únicos y no ofrece índices ni un orden de recorrido
garantizado. Sirve para eliminar duplicados y comprobar pertenencia.
"""

persona = {"nombre": "Ana", "edad": 25}
print(persona["nombre"])       # Una clave ausente aquí causa KeyError.
print(persona.get("ciudad", "Sin registrar"))  # Alternativa si falta la clave.
persona["edad"] = 26           # Actualiza una clave existente.
persona["ciudad"] = "Puebla"   # Agrega una clave nueva.
print("edad" in persona)       # in comprueba las CLAVES.
print(persona.keys(), persona.values(), persona.items())
del persona["ciudad"]
print(persona)

colores = {"rojo", "azul", "rojo"}
colores.add("verde")
colores.discard("amarillo")  # No falla si el elemento no existe.
print(colores)  # Solo hay un "rojo"; no dependas del orden mostrado.

a = {1, 2, 3}
b = {3, 4}
print(a | b)  # Unión: elementos de cualquiera de los dos conjuntos.
print(a & b)  # Intersección: elementos comunes.
print(a - b)  # Diferencia: elementos de a que no están en b.

conjunto_vacio = set()  # {} crea un diccionario vacío.
# Las claves de dict y los elementos de set deben ser hashables.
# str e int sirven; las listas y los diccionarios no.
# Reto: crea un diccionario de producto y un conjunto de sus categorías.
