"""08 · Condicionales: if, elif, else

Un condicional decide qué bloque ejecutar según una condición.
if evalúa primero; elif prueba alternativas; else cubre lo restante.
En una misma cadena se ejecuta SOLO el primer bloque cuya condición sea
verdadera. elif y else son opcionales.

Cada encabezado termina en : y su bloque lleva sangría de cuatro espacios.
La sangría forma parte del programa: determina qué pertenece al bloque.
"""

edad = 17
if edad < 13:
    print("Tarifa infantil")
elif edad < 18:
    print("Tarifa adolescente")
else:
    print("Tarifa de adulto")
print("Consulta terminada")  # Sin sangría: se ejecuta después de la decisión.

# Usa if separados cuando las decisiones sean independientes.
temperatura = 30
hay_sol = True
if temperatura >= 28:
    print("Lleva agua")
if hay_sol:
    print("Usa protector solar")  # Pueden ejecutarse ambos bloques.

tiene_boleto = True
esta_abierto = False
if tiene_boleto and esta_abierto:
    print("Puedes entrar")
else:
    print("No puedes entrar todavía")

# Python también evalúa valores como condiciones:
# False, None, ceros y colecciones vacías se consideran falsos.
pendientes = []
if pendientes:
    print("Hay tareas por hacer")
else:
    print("No hay tareas pendientes")

nota = 85
if 0 <= nota <= 100:  # Comparación encadenada: dentro del intervalo.
    print("Nota válida")

# Error común: confundir = (asignación) con == (comparación).
# Reto: clasifica una nota como aprobada (>= 60) o reprobada.
# Primero verifica que esté entre 0 y 100.
