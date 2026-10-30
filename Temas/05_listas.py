"""05 · Listas (list)

Una lista guarda varios elementos en orden y permite modificarlos.
Se escribe con corchetes []. Puede contener repetidos y distintos tipos,
aunque agrupar elementos del mismo tipo suele facilitar su uso.

El índice empieza en 0. Acceder a una posición inexistente causa IndexError.
len(lista) cuenta elementos; el último índice positivo es len(lista) - 1.
"""

frutas = ["manzana", "pera", "uva"]
print(frutas[0])    # manzana
print(frutas[-1])   # uva
print(frutas[:2])   # ['manzana', 'pera']: el límite final no se incluye.

# Modificar, agregar y eliminar son operaciones diferentes.
frutas[1] = "mango"         # Reemplaza el elemento de índice 1.
frutas.append("fresa")      # Agrega UN elemento al final.
frutas.extend(["kiwi", "melón"])  # Agrega los elementos de otra colección.
frutas.insert(1, "plátano")  # Inserta antes del elemento de índice 1.
frutas.remove("uva")        # Borra la primera coincidencia; falla si no existe.
ultima = frutas.pop()       # Borra y devuelve el último elemento.
del frutas[0]               # Borra por índice, sin devolver el elemento.
print(frutas, ultima)
print("kiwi" in frutas, len(frutas))

# Atención: asignar una lista a otro nombre NO la copia.
original = [3, 1, 2]
alias = original
alias.append(4)
print(original)  # [3, 1, 2, 4]: ambos nombres apuntan a la misma lista.

copia = original.copy()  # Copia superficial: basta aquí porque contiene enteros.
copia.append(5)
print(original, copia)  # Las listas exteriores ahora son independientes.
# Si hubiera listas internas, copy() seguiría compartiendo esas listas internas.

ordenados = sorted(original)  # Devuelve una lista nueva ordenada.
print(ordenados, original)
original.sort()               # Ordena la propia lista y devuelve None.
print(original)
# Evita original = original.sort(): perderías la lista al asignar None.
# Reto: crea una lista de tareas, agrega una y elimina una ya terminada.
