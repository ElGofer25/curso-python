"""09 · Ciclo for

for recorre los elementos de un iterable, como una lista, un texto o range.
En cada vuelta, la variable recibe el siguiente elemento y ejecuta el bloque.
El ciclo termina al agotar los elementos; una colección vacía da cero vueltas.

Usa for para recorrer datos o repetir una cantidad conocida de veces.
No necesitas incrementar manualmente la variable del recorrido.
"""

frutas = ["manzana", "pera", "uva"]
for fruta in frutas:
    print(fruta)

# range(inicio, fin, paso): incluye inicio y excluye fin.
for numero in range(1, 4):
    print(numero)  # 1, 2, 3
for numero in range(0, 6, 2):
    print(numero)  # 0, 2, 4
# range(3) produce 0, 1, 2. Un paso negativo permite descender.

# Un acumulador conserva el resultado entre vueltas.
total = 0
for precio in [10, 20, 5]:
    total += precio
print(f"Total: {total}")  # 35; imprime después de terminar el ciclo.

# enumerate aporta posición y elemento sin llevar un contador manual.
for posicion, fruta in enumerate(frutas, start=1):
    print(f"{posicion}. {fruta}")

persona = {"nombre": "Ana", "edad": 25}
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# continue salta a la siguiente vuelta; break termina el ciclo completo.
for numero in range(1, 8):
    if numero == 3:
        continue
    if numero == 6:
        break
    print(numero)  # 1, 2, 4, 5

# Evita agregar o quitar elementos de la misma lista que estás recorriendo.
# Reto: recorre [4, 7, 10, 13] y suma únicamente los números pares.
