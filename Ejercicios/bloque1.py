# Ejercicio C — Funciones

# Crea una función llamada calcular_descuento(precio, porcentaje). Debe calcular el precio final después de aplicar el descuento indicado como porcentaje (por ejemplo, 20 significa 20 %). 
# Devuelve el resultado con return. Compruébala con precio=500 y porcentaje=20.

# Salida esperada: 400.0
def calcular_descuento(precio, porcentaje):
    resultado = precio - (precio*porcentaje/100)
    return resultado

prueba = calcular_descuento(500, 20)
print(prueba)



# Ejercicio B — Iteraciones

# Escribe un ciclo for que imprima los números pares desde 2 hasta 12, ambos incluidos. 
# Utiliza range(). Salida esperada: 2, 4, 6, 8, 10, 12 (uno por línea)

for i in range(1, 13):
    if i % 2 == 0:
        print(i)
    



# Ejercicio A — Condicionales

# Declara una variable temperatura con el valor 27. Si es mayor o igual a 30, imprime "Alta"; 
# si está entre 15 y 29 inclusive, imprime "Moderada"; en cualquier otro caso, imprime "Baja".
# Mi intento
# temp = 27.7

# if temp >= 30:
#     print('Alta')
# elif temp >=15:
#     print('Moderada')
# elif temp <= 14:
#     print('Baja') 

#Correción
temp = 27.7

if temp >= 30:
    print("Alta")
elif temp >= 15:
    print("Moderada")
else:
    print("Baja")