"""10 · Ciclo while

while repite un bloque MIENTRAS su condición sea verdadera.
Revisa la condición antes de cada vuelta: puede no ejecutar ninguna.
Úsalo cuando la repetición dependa de un estado, como intentos o saldo.

Identifica tres partes: estado inicial, condición y actualización.
Si nada vuelve falsa la condición y no hay break, el ciclo no termina.
"""

contador = 1                 # 1. Estado inicial
while contador <= 3:         # 2. Condición
    print(contador)
    contador += 1           # 3. Actualización: permite llegar al final
print(f"Terminó con contador={contador}")  # 4

# La condición se vuelve a evaluar con el estado actualizado.
saldo = 25
costo = 10
viajes = 0
while saldo >= costo:
    saldo -= costo
    viajes += 1
print(f"Viajes: {viajes}; saldo: {saldo}")  # 2 y 5

# while True necesita una salida explícita. Aquí el límite es de 3 intentos.
intentos = 0
while True:
    intentos += 1
    print(f"Intento {intentos}")
    if intentos == 3:
        break  # Sale del ciclo más cercano.

# Con continue, actualiza el estado ANTES de saltar la vuelta.
numero = 0
while numero < 5:
    numero += 1
    if numero == 3:
        continue
    print(numero)  # 1, 2, 4, 5

# for: "recorre estos elementos". while: "repite mientras esto se cumpla".
# Reto: parte de 10 y cuenta hacia atrás hasta 1 usando while.
