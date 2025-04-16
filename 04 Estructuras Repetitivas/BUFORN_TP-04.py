#1

for i in range(101):
    print(i)

#2

num = input("Ingresá un número entero: ")
print("Cantidad de dígitos:", len(num))

#3

inicio = int(input("Primer número: "))
fin = int(input("Segundo número: "))

suma = 0
for i in range(inicio + 1, fin):
    suma += i

print("Suma de los números entre ellos:", suma)

#4

total = 0
while True:
    n = int(input("Ingresá un número (0 para salir): "))
    if n == 0:
        break
    total += n

print("Suma total:", total)

#5

import random

secreto = random.randint(0, 9)
intentos = 0

while True:
    intento = int(input("Adiviná el número (0-9): "))
    intentos += 1
    if intento == secreto:
        break

print(f"¡Correcto! Lo lograste en {intentos} intento(s).")

#6

for i in range(100, -1, -2):
    print(i)

#7

n = int(input("Ingresá un número entero positivo: "))
suma = 0

for i in range(n + 1):
    suma += i

print("La suma es:", suma)

#8

pares = impares = positivos = negativos = 0
cantidad = 100

for i in range(cantidad):
    n = int(input("Ingresá un número: "))
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1
    if n > 0:
        positivos += 1
    elif n < 0:
        negativos += 1

print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)

#9

cantidad = 100 
suma = 0

for i in range(cantidad):
    n = int(input("Ingresá un número: "))
    suma += n

media = suma / cantidad
print("Media:", media)

#10

num = input("Ingresá un número: ")
invertido = num[::-1]
print("Número invertido:", invertido)
