"""11 · Funciones

Una función agrupa una tarea con un nombre para poder reutilizarla.
def la define; escribir su nombre con paréntesis la llama.
Los parámetros son nombres en la definición; los argumentos son los valores
que entregas al llamar. return devuelve un resultado y termina la llamada.
"""


def sumar(a, b):
    """Devuelve la suma de dos valores compatibles."""
    return a + b


resultado = sumar(3, 4)  # a recibe 3 y b recibe 4.
print(resultado * 2)    # 14: el valor devuelto se puede seguir usando.


def saludar(nombre, saludo="Hola"):
    """Construye un saludo; usa 'Hola' si no se indica otro."""
    return f"{saludo}, {nombre}"


print(saludar("Ana"))
print(saludar(nombre="Luis", saludo="Buen día"))  # Argumentos por nombre.


def es_par(numero):
    """Indica si un entero es divisible entre dos."""
    return numero % 2 == 0


if es_par(8):
    print("8 es par")

# print muestra; return entrega un valor a quien llamó la función.
# Una función sin return explícito devuelve None.
def mostrar_aviso():
    print("Operación terminada")


valor = mostrar_aviso()
print(valor)  # None

# Las variables creadas dentro de una función son locales a esa llamada.
def calcular_total(precio, cantidad):
    subtotal = precio * cantidad
    return subtotal


print(calcular_total(15, 3))
# subtotal no está disponible fuera de calcular_total.
# Prefiere recibir datos y devolver resultados a depender de variables globales.
# Evita valores por defecto mutables, como lista=[]: se comparten entre llamadas.
# Reto: define calcular_area(base, altura) y devuelve el área de un triángulo.
