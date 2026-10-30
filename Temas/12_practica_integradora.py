"""12 · Práctica integradora: carrito de compras

Lee primero los archivos 01 a 11. Aquí se combinan listas, diccionarios,
for, if, while y funciones con datos fijos, sin pedir entrada.

Sigue el flujo: definir funciones → crear datos → calcular → mostrar.
"""


def calcular_total(carrito):
    """Suma precio por cantidad para cada producto del carrito."""
    total = 0
    for producto in carrito:
        total += producto["precio"] * producto["cantidad"]
    return total


def aplicar_descuento(total):
    """Aplica 10 % de descuento a compras de al menos 100."""
    if total >= 100:
        return total * 0.90
    return total


carrito = [
    {"nombre": "Cuaderno", "precio": 40, "cantidad": 2},
    {"nombre": "Lápiz", "precio": 10, "cantidad": 3},
]

for producto in carrito:
    print(f"{producto['nombre']}: {producto['cantidad']} unidades")

subtotal = calcular_total(carrito)
total = aplicar_descuento(subtotal)
print(f"Subtotal: ${subtotal:.2f}")  # 110.00
print(f"Total: ${total:.2f}")        # 99.00

# Simula pagos de hasta 40 hasta completar el total.
pendiente = total
pagos = 0
while pendiente > 0:
    abono = min(40, pendiente)  # Toma el menor: no paga de más.
    pendiente -= abono
    pagos += 1
    print(f"Abono: ${abono:.2f}; pendiente: ${pendiente:.2f}")
print(f"Pagos realizados: {pagos}")

# Reto: agrega un producto, cambia el descuento y predice el nuevo resultado.
# Después ejecuta el archivo para comprobarlo.
# Nota: para dinero en aplicaciones reales se suele usar decimal.Decimal;
# aquí los números mantienen el foco en el flujo del programa.
