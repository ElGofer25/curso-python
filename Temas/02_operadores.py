"""02 · Operadores

Los operadores permiten calcular, comparar y combinar condiciones.
= asigna un valor; == pregunta si dos valores son iguales.
"""

a = 10
b = 3
print(a + b)   # 13: suma
print(a - b)   # 7: resta
print(a * b)   # 30: multiplicación
print(a / b)   # División: devuelve float, incluso en 10 / 2.
print(a // b)  # 3: división redondeada hacia abajo; -10 // 3 es -4.
print(a % b)   # 1: residuo; sirve para detectar pares con numero % 2 == 0.
print(a ** b)  # 1000: potencia

# Comparaciones: producen True o False.
print(a == b, a != b, a > b, a < b, a >= b, a <= b)

edad = 20
tiene_boleto = True
print(edad >= 18 and tiene_boleto)  # and: ambas condiciones deben cumplirse.
print(edad < 18 or tiene_boleto)   # or: basta con que se cumpla una.
print(not tiene_boleto)           # not: invierte el valor lógico.

puntos = 10
puntos += 5  # Equivale a puntos = puntos + 5.
print(puntos)

# Los paréntesis hacen explícito el orden del cálculo.
print((2 + 3) * 4)  # 20; sin paréntesis, 2 + 3 * 4 da 14.
# Reto: comprueba si un número es par y mayor que 10.
