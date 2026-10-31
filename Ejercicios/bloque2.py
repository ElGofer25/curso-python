# D — Conjuntos

# Crea los conjuntos a = {1, 2, 3, 4} y b = {3, 4, 5, 6}. Obtén e imprime la unión, intersección y diferencia a - b, utilizando los operadores de conjuntos.
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
union = a | b
print(union)

interseccion = a & b
print(interseccion)




# C — Diccionarios

# Crea un diccionario llamado inventario con las claves 'lapices' y 'cuadernos', asociadas a las cantidades 10 y 5. Actualiza cuadernos a 8, agrega la clave 'borradores' con cantidad 3 e imprime las tres cantidades.
my_dict = {'lapices': 10, 'cuadernos': 5}
my_dict['cuadernos'] = 8
my_dict['borradores'] = 3
print(my_dict['lapices'], my_dict['cuadernos'], my_dict['borradores'])

# B — Tuplas

# Crea una tupla llamada dimensiones con los valores (1920, 1080). 
# Extrae ambos valores a dos variables llamadas ancho y alto, e imprímelas.
size = (1920, 1080)
height, width = size
print(height, width)

# A — Listas

# Crea una lista llamada productos con tres nombres de productos. Agrega un cuarto mediante append(), cambia el segundo mediante su índice y elimina el último mediante pop(). Finalmente imprime la lista y el elemento eliminado.

mylist = ["manzanas", "bananas", "naranjas"]

mylist.append('Uvas')
mylist.pop()
print(mylist)