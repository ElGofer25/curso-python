"""04 · Entrada y salida

print() muestra información. input() lee lo que escribe la persona y
SIEMPRE devuelve str, aunque se escriban números.

Este ejemplo pide datos solo al ejecutar el archivo directamente.
La condición de abajo evita pedirlos si otro archivo importa este módulo.
"""

if __name__ == "__main__":
    nombre = input("¿Cómo te llamas? ").strip()
    edad_texto = input("¿Cuántos años tienes? ")
    edad = int(edad_texto)  # Supone un entero válido, como 25.

    print(f"Hola, {nombre}. El próximo año tendrás {edad + 1} años.")
    print("Python", "es", "claro", sep=" | ")

# Si escribes "veinte", int() lanza ValueError y el programa se detiene.
# En este ejemplo se espera una entrada válida; validar es un paso posterior.
# Nunca uses eval() para convertir la entrada del usuario en un número.
# Reto: pide dos números con float() y muestra su suma.
