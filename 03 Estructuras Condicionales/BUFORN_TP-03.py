# 1)

edad = int(input("Ingrese la edad:"))
if (edad >= 18):
    print("Es mayor de edad")

# 2)

nota = int(input("Ingrese la nota:"))
if (nota >= 6):
    print("Aprobado")
else:
    print("Desaprobado")

# 3)

numero = int(input("Ingrese un número par:"))
if (numero%2 == 0):
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# 4)

edad = int(input("Ingrese la edad:"))

if edad < 12:
    print("Niño/a")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# 5)

contraseña = input("Ingrese una contraseña: ")

if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6)

import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

if media > mediana > moda:
    print("Sesgo positivo")
elif media < mediana < moda:
    print("Sesgo negativo")
else:
    print("Sin sesgo")

# 7)

frase = input("Ingrese una frase o palabra:")

if (frase[-1] in "aeiouAEIOUáéíóúÁÉÍÓÚ"):
    frase += "!"

print(frase)

# 8)

nombre = input("Ingrese su nombre:")
opcion = input("Elija una opción (1: mayúsculas, 2: minúsculas, 3: primera letra mayúscula):")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción inválida")

# 9)

magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

# 10)

hemisferio = input("Ingrese el hemisferio (N/S):")
mes = int(input("Ingrese el número del mes (1-12):"))
dia = int(input("Ingrese el día del mes:"))

if hemisferio not in ("N", "S"):
    print("Hemisferio inválido")
else:
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        estacion_norte = "Invierno"
        estacion_sur = "Verano"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        estacion_norte = "Primavera"
        estacion_sur = "Otoño"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
        estacion_norte = "Verano"
        estacion_sur = "Invierno"
    else:
        estacion_norte = "Otoño"
        estacion_sur = "Primavera"

    estacion = estacion_norte if hemisferio == "N" else estacion_sur
    print("Está en", estacion)
