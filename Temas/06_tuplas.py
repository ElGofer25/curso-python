"""06 · Tuplas (tuple)

Una tupla es una secuencia ordenada que no permite reemplazar, agregar
ni eliminar sus elementos. Es útil para agrupar datos con estructura fija,
como una coordenada (x, y). Admite índices, cortes y valores repetidos.

Lista: colección que necesitas modificar, como un carrito de compras.
Tupla: grupo cuya estructura quieres mantener, como ancho y alto.
"""

punto = (10, 20)
print(punto[0], punto[-1], len(punto))

# Desempaquetar asigna cada elemento a un nombre.
x, y = punto  # Debe haber tantos nombres como elementos.
print(f"x={x}, y={y}")

una_tupla = (7,)  # La coma crea la tupla de un elemento.
un_entero = (7)   # Los paréntesis solos no crean una tupla.
vacia = ()
print(type(una_tupla), type(un_entero), vacia)

valores = (1, 2, 2, 3)
print(valores.count(2))  # 2: cantidad de apariciones
print(valores.index(3))  # 3: índice de la primera aparición; falla si no existe.

# punto[0] = 99 daría TypeError: la tupla es inmutable.
# Puedes construir otra tupla y asignarla al mismo nombre.
punto = (99, punto[1])
print(punto)

# Matiz: si contiene una lista, esa lista sí puede cambiar.
registro = ("Ana", [8, 9])
registro[1].append(10)  # No reemplazamos el elemento: modificamos su lista.
print(registro)
# Reto: guarda nombre y edad en una tupla y desempaquétala en dos variables.
